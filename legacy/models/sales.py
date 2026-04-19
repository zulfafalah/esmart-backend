from django.db import models


class Qrypindahanstok(models.Model):
    urut = models.CharField(max_length=1, blank=True, null=True)
    keterangan = models.CharField(max_length=538, blank=True, null=True)
    rcvid = models.IntegerField(blank=True, null=True)
    rcvno = models.CharField(max_length=100, blank=True, null=True)
    tgl = models.CharField(max_length=10, blank=True, null=True)
    productid = models.IntegerField(blank=True, null=True)
    namabarang = models.CharField(max_length=200, blank=True, null=True)
    qtyin = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    qtyout = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    status = models.CharField(max_length=15, blank=True, null=True)
    rcvwhs = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'qrypindahanstok'


class Txinvoice(models.Model):
    invoiceid = models.AutoField(primary_key=True)
    soid = models.IntegerField(blank=True, null=True)
    invoiceno = models.CharField(max_length=30)
    invoicedate = models.DateField(blank=True, null=True)
    customerid = models.IntegerField()
    currinvid = models.CharField(max_length=10)
    deliveryno = models.CharField(max_length=30, blank=True, null=True)
    deliverydate = models.DateField(blank=True, null=True)
    isfacturestd = models.SmallIntegerField(blank=True, null=True)
    islunas = models.SmallIntegerField(blank=True, null=True)
    totalpayment = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    totalretur = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    bunitid = models.IntegerField()
    beamaterai = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    bealain = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    bealaintext = models.CharField(max_length=100, blank=True, null=True)
    sinvoiceno = models.CharField(max_length=100, blank=True, null=True)
    sinvoicedate = models.DateField(blank=True, null=True)
    scustomer = models.CharField(max_length=100, blank=True, null=True)
    invwhsid = models.IntegerField()
    salesid = models.IntegerField(blank=True, null=True)
    kursjual = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    kurseval = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    kursbl = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    iscancel = models.SmallIntegerField(blank=True, null=True)
    canceldate = models.DateTimeField(blank=True, null=True)
    canceluser = models.CharField(max_length=100, blank=True, null=True)
    duedateinv = models.IntegerField(blank=True, null=True)
    invdeladdrs = models.CharField(max_length=510, blank=True, null=True)
    totalhpp = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    ispaidkom = models.SmallIntegerField(blank=True, null=True)
    komamount = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    komdateambil = models.DateTimeField(blank=True, null=True)
    totalsales = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    dsct = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    disctvalue = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    inv_subtotal_after_disc = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    ppn = models.SmallIntegerField(blank=True, null=True)
    ppnpctval = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    ppnvalue = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    grandtotal = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    tkonversijual = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    issppl = models.SmallIntegerField(blank=True, null=True)
    coa26 = models.IntegerField(blank=True, null=True)
    iskys = models.SmallIntegerField(blank=True, null=True)
    pcinv1 = models.SmallIntegerField(blank=True, null=True)
    pcinv2 = models.SmallIntegerField(blank=True, null=True)
    statusinv = models.SmallIntegerField(blank=True, null=True)
    iskontrabon = models.SmallIntegerField(blank=True, null=True)
    iscashinv = models.SmallIntegerField(blank=True, null=True)
    invnote = models.CharField(max_length=510, blank=True, null=True)
    payamount = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    printedby = models.CharField(max_length=100, blank=True, null=True)
    printed = models.DateTimeField(blank=True, null=True)
    fpajakno = models.CharField(max_length=100, blank=True, null=True)
    totalinvq = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    ketresi = models.CharField(max_length=100, blank=True, null=True)
    ekspedisiid = models.IntegerField()
    paramst_sls = models.IntegerField()
    coa_inv = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    createdby = models.CharField(max_length=100, blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    modifiedby = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'txinvoice'
        unique_together = (('invoiceno', 'invoicedate'),)


class Txinvoicec(models.Model):
    invoicecid = models.AutoField(primary_key=True)
    invoiceid = models.IntegerField()
    paymentid = models.IntegerField()
    productid = models.IntegerField()
    ekspedisi_idf = models.IntegerField()
    totalused = models.DecimalField(max_digits=19, decimal_places=4)
    coa27 = models.IntegerField()
    invoicekey = models.CharField(max_length=100, blank=True, null=True)
    addremarks = models.CharField(max_length=400)
    namaalias = models.CharField(max_length=100)
    containerno = models.CharField(max_length=100)
    sealno = models.CharField(max_length=100)
    printed = models.DateTimeField(blank=True, null=True)
    printedby = models.CharField(max_length=50, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    createdby = models.CharField(max_length=100)
    modified = models.DateTimeField(blank=True, null=True)
    modifiedby = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'txinvoicec'
        unique_together = (('invoiceid', 'paymentid', 'productid'),)


class Txinvoiced(models.Model):
    invoicedid = models.AutoField(primary_key=True)
    sod_idf = models.IntegerField()
    invoiceid = models.CharField(max_length=64, blank=True, null=True)
    productid = models.IntegerField()
    qtyinvoice = models.DecimalField(max_digits=19, decimal_places=4)
    uom_idf = models.IntegerField()
    produnit = models.CharField(max_length=100, blank=True, null=True)
    discvalued = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    discpctd = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    qtycoli = models.CharField(max_length=20, blank=True, null=True)
    qtyinvoicek = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    invslsprice = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    proddesc = models.CharField(max_length=8000, blank=True, null=True)
    coa28 = models.IntegerField(blank=True, null=True)
    qtyb = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    qtybuom = models.CharField(max_length=20, blank=True, null=True)
    qtybprice = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    skuid = models.CharField(max_length=200, blank=True, null=True)
    komisiperqty = models.DecimalField(max_digits=19, decimal_places=4)
    hrgawalinv = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    invd_disc_pct_1 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    invd_disc_val_1 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    invd_price_after_disc_1 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    invd_disc_pct_2 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    invd_disc_val_2 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    invd_price_after_disc_2 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    invd_disc_pct_3 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    invd_disc_val_3 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    invd_price_after_disc_3 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    invd_disc_pct_4 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    invd_disc_val_4 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    invd_price_after_disc_4 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    invd_disc_pct_5 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    invd_disc_val_5 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    invd_price_after_disc_5 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    invd_disc_pct_6 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    invd_disc_val_6 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    invd_price_after_disc_6 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    invd_ppn_pct = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    invd_ppn_val = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    invprice = models.DecimalField(max_digits=19, decimal_places=4)
    created = models.DateTimeField(blank=True, null=True)
    createdby = models.CharField(max_length=100, blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    modifiedby = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'txinvoiced'
        unique_together = (('invoiceid', 'productid'),)


class Txreceivable(models.Model):
    detail_pk = models.AutoField(primary_key=True)
    custid = models.IntegerField()
    invoiceid = models.IntegerField()
    returid = models.IntegerField()
    ispaid = models.SmallIntegerField(blank=True, null=True)
    totalpiutang = models.DecimalField(max_digits=19, decimal_places=4)
    totalretur = models.DecimalField(max_digits=19, decimal_places=4)
    totaldiscount = models.DecimalField(max_digits=19, decimal_places=4)
    totalbealain = models.DecimalField(max_digits=19, decimal_places=4)
    totalbayar = models.DecimalField(max_digits=19, decimal_places=4)
    isap = models.SmallIntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    createdby = models.CharField(max_length=50)
    modified = models.DateTimeField(blank=True, null=True)
    modifiedby = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'txreceivable'
        unique_together = (('invoiceid', 'custid'),)


class Txsaldopiutang(models.Model):
    periode = models.DateTimeField(blank=True, null=True)
    customerid = models.IntegerField()
    saldopiutang = models.DecimalField(max_digits=19, decimal_places=4)
    isap = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'txsaldopiutang'
        unique_together = (('customerid', 'periode'),)


class Txsn(models.Model):
    detailguid = models.CharField(primary_key=True, max_length=64)
    headerid = models.CharField(unique=True, max_length=64)
    productid = models.IntegerField()
    serialnumber = models.CharField(max_length=100)
    flagtrx = models.IntegerField()
    qtysn = models.IntegerField()
    qtysnused = models.SmallIntegerField(blank=True, null=True)
    noindex = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    createdby = models.CharField(max_length=30, blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    modifiedby = models.CharField(max_length=30, blank=True, null=True)
    refguid = models.CharField(unique=True, max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'txsn'


class Txso(models.Model):
    soid = models.BigAutoField(primary_key=True)
    sono = models.CharField(max_length=45)
    sodate = models.DateField(blank=True, null=True)
    issolokal = models.SmallIntegerField(blank=True, null=True, db_comment='0;Lokal;1;Ekspor;2;Sample Lokal;3;Sample Ekspor ')
    isreject = models.SmallIntegerField(blank=True, null=True)
    customerid = models.IntegerField(blank=True, null=True)
    customeralias_so = models.CharField(max_length=100)
    salesid_so = models.IntegerField()
    socurr = models.CharField(max_length=45, blank=True, null=True)
    sorate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    sotop = models.IntegerField(blank=True, null=True)
    soket1 = models.CharField(max_length=255, blank=True, null=True)
    soket2 = models.CharField(max_length=255, blank=True, null=True)
    sokontrakno = models.CharField(max_length=45, blank=True, null=True)
    tipebiaya = models.IntegerField(blank=True, null=True)
    subtotalso = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    discpct = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    discval = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    so_subtotal_after_disc = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    ppnpct = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    ppnval = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    gtotalso = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    totalkonversiso = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    totalbayarso = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    totaldpso = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    totalbiaya = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    totalkarton = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    totalvolume = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    totalberat = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    statusso = models.IntegerField(blank=True, null=True)
    bunitid = models.IntegerField(blank=True, null=True)
    printed = models.DateTimeField(blank=True, null=True)
    printedby = models.CharField(max_length=45, blank=True, null=True)
    totalapprove = models.IntegerField()
    approved = models.DateTimeField(blank=True, null=True)
    approvedby = models.CharField(max_length=45, blank=True, null=True)
    viewed = models.DateTimeField(blank=True, null=True)
    viewedby = models.CharField(max_length=45, blank=True, null=True)
    isrejected = models.SmallIntegerField(blank=True, null=True)
    rejected = models.DateTimeField(blank=True, null=True)
    rejectedby = models.CharField(max_length=50, blank=True, null=True)
    rejectedreason = models.CharField(max_length=255, blank=True, null=True)
    iscancel = models.SmallIntegerField(blank=True, null=True)
    cancelled = models.DateTimeField(blank=True, null=True)
    cancelledby = models.CharField(max_length=45, blank=True, null=True)
    isclosed = models.SmallIntegerField(blank=True, null=True)
    closed = models.DateTimeField(blank=True, null=True)
    closedby = models.CharField(max_length=45, blank=True, null=True)
    sendemailnotif = models.IntegerField()
    tinvoiced_val = models.DecimalField(max_digits=19, decimal_places=4)
    tdelivered_val = models.DecimalField(max_digits=19, decimal_places=4)
    totalcogs = models.DecimalField(max_digits=19, decimal_places=4)
    created = models.DateTimeField(blank=True, null=True)
    createdby = models.CharField(max_length=45, blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    modifiedby = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'txso'


class Txsod(models.Model):
    sodid = models.AutoField(primary_key=True)
    soidh = models.IntegerField(blank=True, null=True)
    productid = models.IntegerField(blank=True, null=True)
    ketbarang = models.CharField(max_length=255, blank=True, null=True)
    kettambahan = models.CharField(max_length=255, blank=True, null=True)
    unitprodsod = models.CharField(max_length=45, blank=True, null=True)
    qtysod = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    qtysodr = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, db_comment='qty yang diterima berdasarkan podid')
    biayaratesod = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    biaya2 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    biayacurrsod = models.CharField(max_length=45, blank=True, null=True)
    kartonsod = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    volsodm3 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    beratsodkg = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    estsod = models.DateTimeField(blank=True, null=True)
    uomid = models.IntegerField()
    pricesod = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    discpctsod = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    discvalsod = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    sod_price_after_disc_1 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    sod_disc_pct_2 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    sod_disc_val_2 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    sod_price_after_disc_2 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    sod_disc_pct_3 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    sod_disc_val_3 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    sod_price_after_disc_3 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    sod_disc_pct_4 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    sod_disc_val_4 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    sod_price_after_disc_4 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    sod_disc_pct_5 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    sod_disc_val_5 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    sod_price_after_disc_5 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    sod_disc_pct_6 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    sod_disc_val_6 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    sod_price_after_disc_6 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    sod_ppn_pct = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    sod_ppn_val = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    pricesoda = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    harga_cogs = models.DecimalField(max_digits=19, decimal_places=4)
    tgl_cogs = models.DateField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    createdby = models.CharField(max_length=45, blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    modifiedby = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'txsod'
        unique_together = (('soidh', 'productid'),)


class Txstockadj(models.Model):
    adj_pk = models.AutoField(primary_key=True)
    adj_no = models.CharField(unique=True, max_length=50)
    adj_date = models.DateField(blank=True, null=True)
    adj_status = models.CharField(max_length=15)
    whs_idf = models.IntegerField()
    whsto_idf = models.IntegerField()
    istransfer_idf = models.IntegerField()
    istransfer_in = models.SmallIntegerField(blank=True, null=True)
    ref_transfer_idf = models.IntegerField()
    adj_reasonid = models.IntegerField()
    adj_remarks = models.CharField(max_length=100)
    adj_qty_val = models.DecimalField(max_digits=10, decimal_places=2)
    adj_total_val = models.DecimalField(max_digits=19, decimal_places=4)
    adj_refno = models.CharField(max_length=100)
    paramst_inv = models.SmallIntegerField(blank=True, null=True)
    status_trx = models.SmallIntegerField(blank=True, null=True)
    is_exc_biaya = models.SmallIntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    createdby = models.CharField(max_length=50)
    modified = models.DateTimeField(blank=True, null=True)
    modifiedby = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'txstockadj'


class TxstockadjDetail(models.Model):
    adj_d_pk = models.AutoField(primary_key=True)
    adj_idh = models.IntegerField()
    product_idh = models.IntegerField()
    product_desc = models.CharField(max_length=100)
    uom_idh = models.IntegerField()
    qty_fisik = models.IntegerField(db_comment='qty fisik digudang ybs')
    adj_qty = models.DecimalField(max_digits=10, decimal_places=0, db_comment='qty yg mau diadjust')
    adj_price = models.DecimalField(max_digits=19, decimal_places=4)
    created = models.DateTimeField(blank=True, null=True)
    createdby = models.CharField(max_length=50)
    modified = models.DateTimeField(blank=True, null=True)
    modifiedby = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'txstockadj_detail'
        unique_together = (('adj_idh', 'product_idh'),)


class Txstok(models.Model):
    whsid = models.IntegerField(blank=True, null=True)
    productid = models.IntegerField()
    periode = models.DateTimeField(blank=True, null=True)
    qtyawal = models.DecimalField(max_digits=19, decimal_places=4)
    qtybeli = models.DecimalField(max_digits=19, decimal_places=4)
    qtyjual = models.DecimalField(max_digits=19, decimal_places=4)
    qtyretur = models.DecimalField(max_digits=19, decimal_places=4)
    qtyadjplus = models.DecimalField(max_digits=19, decimal_places=4)
    qtyadjmin = models.DecimalField(max_digits=19, decimal_places=4)
    jadjplus = models.DecimalField(max_digits=19, decimal_places=4)
    jadjmin = models.DecimalField(max_digits=19, decimal_places=4)
    qtytout = models.DecimalField(max_digits=19, decimal_places=4)
    jtout = models.DecimalField(max_digits=19, decimal_places=4)
    qtytin = models.DecimalField(max_digits=19, decimal_places=4)
    jtin = models.DecimalField(max_digits=19, decimal_places=4)
    qtyakhir = models.DecimalField(max_digits=19, decimal_places=4)
    hpp = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    createdby = models.CharField(max_length=30, blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    modifiedby = models.CharField(max_length=30, blank=True, null=True)
    bunitid = models.IntegerField(blank=True, null=True)
    qtyreturbeli = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    jawal = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    jbeli = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    jreturjual = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    jjual = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    jreturbeli = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    jakhir = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'txstok'
        unique_together = (('productid', 'periode'),)


class Txtransfer(models.Model):
    transferid = models.AutoField(primary_key=True)
    transferdate = models.DateTimeField(blank=True, null=True)
    transferno = models.CharField(max_length=20)
    trffrom = models.IntegerField()
    trfto = models.IntegerField()
    productid = models.IntegerField()
    qtytrf = models.IntegerField()
    bunitid = models.IntegerField()
    refrcvid = models.IntegerField()
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    uom = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'txtransfer'
        unique_together = (('transferdate', 'trffrom', 'trfto', 'transferno'),)
