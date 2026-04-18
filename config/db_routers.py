class DatabaseRouter:
    """
    Routes database operations for multi-database setup:
      - 'legacy' app  → 'esmart' database
      - 'db_controller' app → 'db_controller' database
      - everything else    → 'default' database
    """

    route_app_labels = {"legacy"}
    db_controller_app_labels = {"db_controller"}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return "esmart"
        if model._meta.app_label in self.db_controller_app_labels:
            return "db_controller"
        return "default"

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return "esmart"
        if model._meta.app_label in self.db_controller_app_labels:
            return "db_controller"
        return "default"

    def allow_relation(self, obj1, obj2, **hints):
        db_set = {obj1._state.db, obj2._state.db}
        # Allow relations within the same database
        if len(db_set) == 1:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == "esmart"
        if app_label in self.db_controller_app_labels:
            return db == "db_controller"
        return db == "default"
