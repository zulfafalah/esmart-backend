from django.db import models


class Qrypindahanpiutang(models.Model):
    invoiceid = models.IntegerField(blank=True, null=True)
    invoiceno = models.CharField(max_length=100, blank=True, null=True)
    tgltrx = models.CharField(max_length=10, blank=True, null=True)
    paydatemoney = models.DateTimeField(blank=True, null=True)
    customerid = models.IntegerField(blank=True, null=True)
    customerinitial = models.CharField(max_length=20, blank=True, null=True)
    customername = models.CharField(max_length=100, blank=True, null=True)
    jumlah = models.DecimalField(max_digits=39, decimal_places=8, blank=True, null=True)
    ket = models.CharField(max_length=631, blank=True, null=True)
    tanda = models.CharField(max_length=1, blank=True, null=True)
    validpayment = models.IntegerField(blank=True, null=True)
    lunas = models.IntegerField(blank=True, null=True)
    invwhsid = models.IntegerField(blank=True, null=True)
    bunitid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'qrypindahanpiutang'


class Qrypiutangperinvoice(models.Model):
    trxid = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    invoiceid = models.IntegerField(blank=True, null=True)
    invoiceno = models.CharField(max_length=100, blank=True, null=True)
    tgltrx = models.CharField(max_length=10, blank=True, null=True)
    paydatemoney = models.DateTimeField(blank=True, null=True)
    customerid = models.IntegerField(blank=True, null=True)
    customerinitial = models.CharField(max_length=20, blank=True, null=True)
    customername = models.CharField(max_length=100, blank=True, null=True)
    jumlah = models.DecimalField(max_digits=39, decimal_places=8, blank=True, null=True)
    ket = models.CharField(max_length=631, blank=True, null=True)
    tanda = models.CharField(max_length=1, blank=True, null=True)
    validpayment = models.IntegerField(blank=True, null=True)
    lunas = models.IntegerField(blank=True, null=True)
    invwhsid = models.IntegerField(blank=True, null=True)
    bunitid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'qrypiutangperinvoice'


class RtBilyet(models.Model):
    bilyet_pk = models.AutoField(primary_key=True)
    bilyet_no = models.CharField(max_length=20)
    bilyet_date = models.DateField(blank=True, null=True)
    bilyet_status = models.CharField(max_length=5)
    bilyet_type_id = models.SmallIntegerField(blank=True, null=True, db_comment='0;customer;1;supplier')
    bilyet_person_idf = models.IntegerField()
    bilyet_currency_idf = models.DecimalField(max_digits=10, decimal_places=0)
    bilyet_rate_val = models.DecimalField(max_digits=10, decimal_places=0)
    bilyet_remarks = models.CharField(max_length=100)
    bilyet_total_local_val = models.DecimalField(max_digits=10, decimal_places=0)
    bilyet_total_foreign_val = models.DecimalField(max_digits=10, decimal_places=0)
    created = models.DateTimeField(blank=True, null=True)
    createdby = models.CharField(max_length=50)
    modified = models.DateTimeField(blank=True, null=True)
    modifiedby = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'rt_bilyet'


class RtUtility(models.Model):
    rt_utility_pk = models.AutoField(primary_key=True)
    rt_id_h = models.IntegerField()
    rt_id_f = models.IntegerField()
    rt_utility_option = models.SmallIntegerField(blank=True, null=True)
    rt_utility_status = models.IntegerField()
    rt_utility_val = models.DecimalField(max_digits=19, decimal_places=4)
    created = models.DateTimeField(blank=True, null=True)
    createdby = models.CharField(max_length=50)
    modified = models.DateTimeField(blank=True, null=True)
    modifiedby = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'rt_utility'
        unique_together = (('rt_id_h', 'rt_id_f', 'rt_utility_status'),)


class TxbilyetDetail(models.Model):
    bilyet_d_pk = models.AutoField(primary_key=True)
    bilyet_no = models.CharField(max_length=25)
    bilyet_type = models.SmallIntegerField(blank=True, null=True, db_comment='1;supplier;0;customer')
    currency_idf = models.IntegerField()
    bilyet_bank_idf = models.IntegerField()
    currency_rate = models.DecimalField(max_digits=19, decimal_places=4)
    original_val = models.DecimalField(max_digits=19, decimal_places=4)
    original_allocation_val = models.DecimalField(max_digits=19, decimal_places=4)
    local_val = models.DecimalField(max_digits=19, decimal_places=4)
    local_allocation_val = models.DecimalField(max_digits=19, decimal_places=4)
    bilyet_jenis = models.IntegerField()
    bilyet_remarks = models.CharField(max_length=100)
    bilyet_receive_date = models.DateField(blank=True, null=True)
    bilyet_person_idf = models.IntegerField()
    bilyet_due_date = models.DateField(blank=True, null=True)
    bilyet_setor_date = models.DateField(blank=True, null=True)
    bilyet_cair_date = models.DateField(blank=True, null=True)
    bilyet_cair = models.SmallIntegerField(blank=True, null=True)
    bilyet_status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    createdby = models.CharField(max_length=50)
    modified = models.DateTimeField(blank=True, null=True)
    modifiedby = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'txbilyet_detail'


class Txpayment(models.Model):
    paymentid = models.AutoField(primary_key=True)
    customerid = models.IntegerField()
    totalpaid = models.DecimalField(max_digits=19, decimal_places=4)
    balancepayment = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    paymentdate = models.DateTimeField(blank=True, null=True)
    paymentno = models.CharField(max_length=510)
    descbank = models.CharField(max_length=510)
    validpayment = models.SmallIntegerField(blank=True, null=True)
    bunitid = models.IntegerField()
    paymentdatercv = models.DateTimeField(blank=True, null=True)
    accountbankid = models.IntegerField(blank=True, null=True)
    ispelunasan = models.SmallIntegerField(blank=True, null=True)
    islunaslalu = models.SmallIntegerField(blank=True, null=True)
    nogiro = models.CharField(max_length=510, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    createdby = models.CharField(max_length=30, blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    modifiedby = models.CharField(max_length=30, blank=True, null=True)
    paymentbatch = models.CharField(max_length=30, blank=True, null=True)
    whsid = models.IntegerField(blank=True, null=True)
    coa30 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'txpayment'
