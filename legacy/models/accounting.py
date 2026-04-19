from django.db import models


class Exno(models.Model):
    primarykey = models.AutoField(primary_key=True)
    trxtype = models.CharField(max_length=6)
    trxno = models.IntegerField()
    trxsuffix = models.CharField(max_length=75, blank=True, null=True)
    trxprefix = models.CharField(max_length=40, blank=True, null=True)
    trxdigit = models.IntegerField()
    coa1 = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'exno'
        unique_together = (('trxtype', 'trxno'),)


class Gninit(models.Model):
    pk = models.CompositePrimaryKey('initname', 'coa2')
    initname = models.CharField(max_length=40)
    coa2 = models.IntegerField()
    description = models.CharField(max_length=100, blank=True, null=True)
    valtext = models.CharField(max_length=255)
    created = models.DateTimeField(blank=True, null=True)
    createdby = models.CharField(max_length=30, blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    modifiedby = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gninit'


class Journal(models.Model):
    primarykey = models.AutoField(primary_key=True)
    code = models.CharField(unique=True, max_length=40)
    journaldate = models.DateField(blank=True, null=True)
    descriptions = models.CharField(max_length=510, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    currencyid = models.CharField(max_length=10, blank=True, null=True)
    kursjurnal = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    tkonversijurnal = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    bunitid = models.IntegerField(blank=True, null=True)
    debetval = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    creditval = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    debetvalf = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    creditvalf = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    pcjournal1 = models.CharField(max_length=20)
    ishide = models.SmallIntegerField(blank=True, null=True)
    coa3 = models.IntegerField(blank=True, null=True)
    idtrx = models.CharField(max_length=5)
    created = models.DateTimeField(blank=True, null=True)
    createdby = models.CharField(max_length=100, blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    modifiedby = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'journal'


class Journalentry(models.Model):
    primarykey = models.AutoField(primary_key=True)
    journalkey = models.IntegerField()
    sequence = models.IntegerField(blank=True, null=True)
    descriptions = models.CharField(max_length=510, blank=True, null=True)
    voucher = models.CharField(max_length=40, blank=True, null=True)
    accountkey = models.IntegerField(blank=True, null=True)
    debetcredit = models.IntegerField(blank=True, null=True)
    amount = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    amountf = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    voucherno1 = models.CharField(max_length=510, blank=True, null=True)
    journalkey1 = models.CharField(max_length=64, blank=True, null=True)
    coa4 = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    createdby = models.CharField(max_length=100, blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    modifiedby = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'journalentry'
        unique_together = (('journalkey', 'sequence', 'accountkey', 'debetcredit', 'descriptions'),)


class Txbiaya(models.Model):
    biayaid = models.AutoField(primary_key=True)
    keterangan = models.CharField(max_length=255)
    tglbiaya = models.DateTimeField(blank=True, null=True)
    accountkey_idf = models.IntegerField()
    currency_idf = models.IntegerField()
    kurs_val = models.DecimalField(max_digits=19, decimal_places=4)
    saldo_awal = models.DecimalField(max_digits=19, decimal_places=4)
    debet_val_local = models.DecimalField(max_digits=19, decimal_places=4)
    credit_val_local = models.DecimalField(max_digits=19, decimal_places=4)
    debet_val_foreign = models.DecimalField(max_digits=19, decimal_places=4)
    credit_val_foreign = models.DecimalField(max_digits=19, decimal_places=4)
    saldo_akhir = models.DecimalField(max_digits=19, decimal_places=4)
    biayalain = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    nilaipenjualan = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    nilaipembelian = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    nilailabakotor = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    biayabatch = models.CharField(max_length=30, blank=True, null=True)
    bunitid = models.IntegerField(blank=True, null=True)
    coa25 = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    createdby = models.CharField(max_length=30, blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    modifiedby = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'txbiaya'
        unique_together = (('tglbiaya', 'accountkey_idf', 'bunitid', 'currency_idf'),)


class TxreqJournal(models.Model):
    req_journal_pk = models.AutoField(primary_key=True)
    req_journal_no = models.CharField(unique=True, max_length=50)
    req_journal_date = models.DateField(blank=True, null=True)
    req_journal_status = models.SmallIntegerField(blank=True, null=True)
    req_journal_keterangan = models.CharField(max_length=100)
    req_journal_accountkey = models.IntegerField()
    req_isstat = models.SmallIntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    createdby = models.CharField(max_length=50)
    modified = models.DateTimeField(blank=True, null=True)
    modifiedby = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'txreq_journal'


class TxreqJournalDetail(models.Model):
    req_journal_d_pk = models.AutoField(primary_key=True)
    req_journal_idh = models.IntegerField()
    journal_idh = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    createdby = models.CharField(max_length=50)
    modified = models.DateTimeField(blank=True, null=True)
    modifiedby = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'txreq_journal_detail'
        unique_together = (('req_journal_idh', 'journal_idh'),)
