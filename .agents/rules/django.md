---
trigger: always_on
---


# Django Backend — Project Rules

Apply these rules whenever creating or modifying code in the esmart-backend project.

---

## 1. Tech Stack

- **Django 6.x** / Python 3.14 / uv (package manager)
- **DRF** + drf-spectacular (API + Swagger)
- **django-allauth** + TokenAuthentication
- **Celery** + Redis + django-celery-beat
- **PostgreSQL** (multi-database)
- **Ruff** (lint + format) / **mypy** (type check) / **pytest** (test)
- **Docker Compose** + Gunicorn/Uvicorn (deploy)

---

## 2. Project Structure

```
esmart-backend/
├── config/                  # Settings, URLs, routers — NO business logic
│   ├── settings/{base,local,production,test}.py
│   ├── api_router.py        # DRF router registrations
│   ├── db_routers.py        # Multi-database routing
│   ├── urls.py              # Root URL config
│   └── celery_app.py
├── core/                    # Main app directory (managed models, new features)
│   └── users/               # Custom User app (reference implementation)
├── legacy/                  # Legacy DB models (managed=False, no migrations)
│   └── models/{__init__, master_data, accounting, purchasing, sales, finance}.py
├── db_controller/           # Controller DB models (managed=False, no migrations)
├── master_data/             # New master data app (managed)
├── schema/                  # Raw SQL schema files
├── tests/                   # Project-level tests
├── compose/                 # Docker build files
├── .envs/                   # Env files per stage (.local/, .production/)
└── pyproject.toml           # All tool configs (ruff, pytest, mypy)
```

**Rules:**
- `config/` — configuration only, never business logic.
- `core/` — new features go here as sub-apps (e.g. `core/invoices/`).
- `legacy/` & `db_controller/` — always `managed = False`, never create migrations.

---

## 3. Multi-Database

| Alias          | Env Variable                | App Label        | Purpose              |
| -------------- | --------------------------- | ---------------- | -------------------- |
| `default`      | `DATABASE_URL`              | everything else  | Auth, users, celery  |
| `esmart`       | `ESMART_DATABASE_URL`       | `legacy`         | Legacy ERP database  |
| `db_controller`| `DB_CONTROLLER_DATABASE_URL`| `db_controller`  | Controller database  |

- Routing handled by `config/db_routers.py` (`DatabaseRouter`).
- Cross-database ForeignKeys are **forbidden** — use manual ID references.
- New databases require updates to both `DatabaseRouter` and `DATABASES` in `base.py`.

---

## 4. Models

**Managed (new apps):**
```python
class PurchaseOrder(models.Model):
    """Short description."""
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return self.name
```

**Unmanaged (legacy / db_controller):**
```python
class Txpayment(models.Model):
    paymentid = models.AutoField(primary_key=True)
    # ... fields matching existing schema

    class Meta:
        managed = False
        db_table = "txpayment"
```

**Rules:**
- Default PK is `BigAutoField` (via `DEFAULT_AUTO_FIELD`).
- Legacy models must always set `db_table` explicitly.
- When splitting models into `models/` directory, re-export everything from `__init__.py`.

---

## 5. API Creation (End-to-End)

Follow these steps whenever building a new API endpoint:

### Step 1 — Serializer (`app/api/serializers.py`)

```python
from rest_framework import serializers
from app.models import MyModel


class MyModelSerializer(serializers.ModelSerializer[MyModel]):
    class Meta:
        model = MyModel
        fields = ["id", "name", "created_at"]
        read_only_fields = ["id", "created_at"]
```

- Use `ModelSerializer[ModelType]` for type safety with django-stubs.
- Keep `fields` explicit — never use `"__all__"`.
- Use `read_only_fields` for auto-generated or computed fields.
- For nested relations, create a separate read serializer vs write serializer if needed.

### Step 2 — ViewSet (`app/api/views.py`)

```python
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from app.models import MyModel
from .serializers import MyModelSerializer


# Full CRUD
class MyModelViewSet(ModelViewSet):
    serializer_class = MyModelSerializer
    queryset = MyModel.objects.all()
    lookup_field = "pk"

    # Custom action example
    @action(detail=True, methods=["post"])
    def approve(self, request, pk=None):
        obj = self.get_object()
        obj.status = "approved"
        obj.save(update_fields=["status"])
        return Response(
            MyModelSerializer(obj).data,
            status=status.HTTP_200_OK,
        )


# Read-only (for legacy models)
class MyLegacyViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    serializer_class = MyModelSerializer
    queryset = MyModel.objects.all()
```

- Use `ModelViewSet` for full CRUD, or compose specific mixins for limited access.
- Legacy/unmanaged models should be **read-only** — use `ListModelMixin + RetrieveModelMixin` only.
- Always use `rest_framework.status` constants, never hardcode status codes.
- Filter/search: add `filterset_fields`, `search_fields`, `ordering_fields` as needed.

### Step 3 — Register Router (`config/api_router.py`)

```python
from app.api.views import MyModelViewSet

router.register("my-models", MyModelViewSet)
```

- URL prefix uses **kebab-case** (e.g. `purchase-orders`, not `purchase_orders`).
- This auto-generates: `GET /api/my-models/`, `POST /api/my-models/`, `GET /api/my-models/{id}/`, etc.
- Custom actions auto-generate: `POST /api/my-models/{id}/approve/`.

### Step 4 — Swagger / OpenAPI (drf-spectacular)

Swagger UI is available at `/api/docs/` (already configured).

**Add schema annotations when the auto-generated docs are insufficient:**

```python
from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiParameter


@extend_schema_view(
    list=extend_schema(
        summary="List all purchase orders",
        description="Returns paginated list of purchase orders.",
        tags=["Purchase Orders"],
    ),
    retrieve=extend_schema(
        summary="Get purchase order detail",
        tags=["Purchase Orders"],
    ),
)
class PurchaseOrderViewSet(ModelViewSet):
    ...

    @extend_schema(
        summary="Approve a purchase order",
        request=None,
        responses={200: PurchaseOrderSerializer},
        tags=["Purchase Orders"],
    )
    @action(detail=True, methods=["post"])
    def approve(self, request, pk=None):
        ...
```

**Rules:**
- Always add `tags` to group endpoints logically in Swagger.
- Add `summary` for every endpoint — keep it short and descriptive.
- Add `description` only when extra context is needed.
- Use `extend_schema(request=None)` for actions with no request body.
- Use `@extend_schema(responses={...})` to document non-standard responses.
- Spectacular global config is in `base.py` → `SPECTACULAR_SETTINGS`.

### Step 5 — App-level URLs (optional)

Only needed for non-ViewSet endpoints (e.g. custom `APIView`):

```python
# app/urls.py
from django.urls import path
from .api.views import CustomAPIView

app_name = "app"
urlpatterns = [
    path("custom-endpoint/", CustomAPIView.as_view(), name="custom-endpoint"),
]

# Then include in config/urls.py:
path("api/app/", include("app.urls", namespace="app")),
```

### API File Structure Summary

```
app_name/
├── api/
│   ├── __init__.py
│   ├── serializers.py
│   └── views.py
├── models.py
├── admin.py
├── apps.py
└── tests/
    ├── test_api.py
    └── factories.py
```

---

## 6. Celery Tasks

```python
from celery import shared_task

@shared_task()
def sync_inventory(warehouse_id: int) -> str:
    """Sync inventory for a specific warehouse."""
    ...
    return "done"
```

- Place in `tasks.py` per app. Always use `@shared_task()`.
- Tasks must be **idempotent**.
- Periodic tasks managed via `django-celery-beat` admin.

---

## 7. Testing

```python
import pytest
from rest_framework.test import APIClient
from .factories import MyModelFactory

class TestMyModelAPI:
    def test_list(self, db, user):
        MyModelFactory.create_batch(3)
        client = APIClient()
        client.force_authenticate(user=user)
        response = client.get("/api/my-models/")
        assert response.status_code == 200
        assert len(response.data) == 3
```

- Use **pytest** + **factory-boy** (never hardcode fixtures).
- Test settings: `config.settings.test`.
- Conftest at `core/conftest.py`.
- Coverage scope: `core/` directory only.

---

## 8. Code Style & Naming

| Thing        | Convention        | Example                    |
| ------------ | ----------------- | -------------------------- |
| Model        | PascalCase        | `PurchaseOrder`            |
| Field        | snake_case        | `created_at`               |
| Serializer   | Model + Serializer| `PurchaseOrderSerializer`  |
| ViewSet      | Model + ViewSet   | `PurchaseOrderViewSet`     |
| URL prefix   | kebab-case        | `purchase-orders`          |
| App name     | snake_case        | `purchase_order`           |
| Task func    | snake_case        | `sync_inventory_data`      |
| Test class   | Test + Model      | `TestPurchaseOrder`        |
| Factory      | Model + Factory   | `PurchaseOrderFactory`     |

- One import per line (`force-single-line = true`).
- Double-quotes for strings.
- Run `ruff check --fix && ruff format` before commit.
- Pre-commit hooks configured in `.pre-commit-config.yaml`.

---

## 9. Dependency & Environment

- **uv** for package management: `uv add <pkg>`, `uv add --group dev <pkg>`, `uv sync`.
- Lock file `uv.lock` — never edit manually.
- Env vars via `django-environ`: stored in `.envs/.local/` and `.envs/.production/`.
- Never commit secrets.

---

## 10. Docker

```bash
# Start all services
docker compose -f docker-compose.local.yml up --build

# Run management commands
docker compose -f docker-compose.local.yml run --rm django python manage.py <cmd>
```

Services: `django`, `postgres`, `redis`, `celeryworker`, `celerybeat`, `flower`.

---

## 11. Security

- `SECRET_KEY` hardcoded only in `local.py` — production reads from env.
- Password hashing: Argon2.
- CORS limited to `/api/*` paths only.
- Default permission: `IsAuthenticated`.
- `DEBUG = False` in production — never expose debug info.
