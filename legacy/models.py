# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Accounts(models.Model):
    primarykey = models.AutoField(primary_key=True)
    code = models.CharField(unique=True, max_length=40)
    name = models.CharField(max_length=100, blank=True, null=True)
    groupkey = models.IntegerField(blank=True, null=True)
    parentkey = models.IntegerField(blank=True, null=True)
    accounttypekey = models.IntegerField(blank=True, null=True)
    acpos = models.IntegerField()
    coa0 = models.IntegerField()
    currac_idf = models.IntegerField()
    isbank = models.IntegerField(blank=True, null=True)
    isrl = models.IntegerField(blank=True, null=True)
    isgl = models.IntegerField(blank=True, null=True)
    isneraca = models.IntegerField(blank=True, null=True)
    isneracap = models.IntegerField(blank=True, null=True)
    limit_saldo_val = models.DecimalField(max_digits=19, decimal_places=4)
    created = models.DateTimeField(blank=True, null=True)
    createdby = models.CharField(max_length=100, blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    modifiedby = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accounts'


class Dtproperties(models.Model):
    pk = models.CompositePrimaryKey('id', 'property')
    id = models.IntegerField()
    objectid = models.IntegerField(blank=True, null=True)
    property = models.CharField(max_length=64)
    value = models.CharField(max_length=255, blank=True, null=True)
    uvalue = models.CharField(max_length=510, blank=True, null=True)
    lvalue = models.BinaryField(blank=True, null=True)
    version = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dtproperties'


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


class Moaccs(models.Model):
    accessid = models.AutoField(primary_key=True)
    levelid = models.IntegerField()
    formid = models.IntegerField()
    allowsave = models.SmallIntegerField(blank=True, null=True)
    allowopen = models.SmallIntegerField(blank=True, null=True)
    allowedit = models.SmallIntegerField(blank=True, null=True)
    allowdelete = models.SmallIntegerField(blank=True, null=True)
    allowfilter = models.SmallIntegerField(blank=True, null=True)
    allowapprove = models.SmallIntegerField(blank=True, null=True)
    allowunapprove = models.SmallIntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    createdby = models.CharField(max_length=50)
    modified = models.DateTimeField(blank=True, null=True)
    modifiedby = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'moaccs'
        unique_together = (('formid', 'levelid'),)


class Mocomp(models.Model):
    companyid = models.AutoField(primary_key=True)
    companyname = models.CharField(max_length=25, blank=True, null=True)
    companyinitial = models.CharField(max_length=100)
    companylogin = models.CharField(max_length=50)
    address1 = models.CharField(max_length=100, blank=True, null=True)
    phone1 = models.CharField(max_length=15, blank=True, null=True)
    fax1 = models.CharField(max_length=15, blank=True, null=True)
    email1 = models.CharField(max_length=25, blank=True, null=True)
    address2 = models.CharField(max_length=100, blank=True, null=True)
    phone2 = models.CharField(max_length=15, blank=True, null=True)
    fax2 = models.CharField(max_length=15, blank=True, null=True)
    email2 = models.CharField(max_length=25, blank=True, null=True)
    address3 = models.CharField(max_length=100, blank=True, null=True)
    phone3 = models.CharField(max_length=15, blank=True, null=True)
    fax3 = models.CharField(max_length=15, blank=True, null=True)
    email3 = models.CharField(max_length=25, blank=True, null=True)
    updateddate = models.DateTimeField(blank=True, null=True)
    updatedby = models.CharField(max_length=25, blank=True, null=True)
    createddate = models.DateTimeField(blank=True, null=True)
    createdby = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mocomp'


class Moctgr(models.Model):
    categoryid = models.AutoField(primary_key=True)
    categoryname = models.CharField(max_length=50)
    createddate = models.DateTimeField(blank=True, null=True)
    createdby = models.CharField(max_length=50)
    updateddate = models.DateTimeField(blank=True, null=True)
    updatedby = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'moctgr'


class Modept(models.Model):
    deptid = models.AutoField(primary_key=True)
    deptname = models.TextField(unique=True)
    createddate = models.DateTimeField(blank=True, null=True)
    createdby = models.CharField(max_length=50)
    updateddate = models.DateTimeField(blank=True, null=True)
    updatedby = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'modept'


class Modivn(models.Model):
    divisionid = models.AutoField(primary_key=True)
    divisionname = models.CharField(unique=True, max_length=50)
    createddate = models.DateTimeField(blank=True, null=True)
    createdby = models.CharField(max_length=50)
    updateddate = models.DateTimeField(blank=True, null=True)
    updatedby = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'modivn'


class Moform(models.Model):
    formid = models.AutoField(primary_key=True)
    formname = models.CharField(unique=True, max_length=50)
    formdescription = models.CharField(max_length=100, blank=True, null=True)
    formdescriptionen = models.CharField(max_length=255, blank=True, null=True)
    headerid = models.IntegerField()
    url_text = models.CharField(max_length=1000)
    stmenu = models.IntegerField()
    ismenu = models.SmallIntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    createdby = models.CharField(max_length=50)
    modified = models.DateTimeField(blank=True, null=True)
    modifiedby = models.CharField(max_length=50)
    url_group_id = models.CharField(max_length=50, blank=True, null=True)
    url_seq_menu = models.IntegerField(blank=True, null=True)
    url_table_id = models.CharField(max_length=50, blank=True, null=True)
    url_where_id = models.CharField(max_length=50, blank=True, null=True)
    url_modacc_id = models.CharField(max_length=50, blank=True, null=True)
    icon_menu = models.CharField(max_length=50, blank=True, null=True)
    form_name_ext = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'moform'


class Molevl(models.Model):
    levelid = models.AutoField(primary_key=True)
    levelname = models.CharField(unique=True, max_length=50)
    isactive = models.SmallIntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    createdby = models.CharField(max_length=50)
    modified = models.DateTimeField(blank=True, null=True)
    modifiedby = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'molevl'


class Moloca(models.Model):
    locationid = models.AutoField(primary_key=True)
    locationname = models.CharField(unique=True, max_length=50)
    companyname = models.CharField(max_length=100)
    companyinitial = models.CharField(max_length=100)
    companylogin = models.CharField(max_length=100)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    address3 = models.CharField(max_length=100)
    phone1 = models.CharField(max_length=100)
    phone2 = models.CharField(max_length=100)
    phone3 = models.CharField(max_length=100)
    fax1 = models.CharField(max_length=100)
    fax2 = models.CharField(max_length=100)
    fax3 = models.CharField(max_length=100)
    email1 = models.CharField(max_length=100)
    email2 = models.CharField(max_length=100)
    email3 = models.CharField(max_length=100)
    created = models.DateTimeField(blank=True, null=True)
    createdby = models.CharField(max_length=50)
    modifiedby = models.CharField(max_length=50)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'moloca'


class Monmbr(models.Model):
    numberid = models.AutoField(primary_key=True)
    divisionid = models.IntegerField()
    descr = models.CharField(max_length=5, blank=True, null=True)
    startno = models.IntegerField()
    endno = models.IntegerField()
    lastno = models.IntegerField()
    tagseparator = models.CharField(max_length=5, blank=True, null=True)
    digit = models.SmallIntegerField(blank=True, null=True)
    createddate = models.DateTimeField(blank=True, null=True)
    createdby = models.CharField(max_length=20, blank=True, null=True)
    updateddate = models.DateTimeField(blank=True, null=True)
    updatedby = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'monmbr'


class Mostat(models.Model):
    statid = models.AutoField(primary_key=True)
    statusid = models.IntegerField()
    statusname = models.CharField(unique=True, max_length=50)
    createddate = models.DateTimeField(blank=True, null=True)
    createdby = models.CharField(max_length=50, blank=True, null=True)
    updateddate = models.DateTimeField(blank=True, null=True)
    updatedby = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mostat'


class Mosupp(models.Model):
    supplierid = models.AutoField(primary_key=True)
    suppliername = models.CharField(max_length=50, blank=True, null=True)
    supplieraddress = models.CharField(max_length=50, blank=True, null=True)
    suppliertelp1 = models.CharField(max_length=15, blank=True, null=True)
    suppliertelp2 = models.CharField(max_length=15, blank=True, null=True)
    createddate = models.DateTimeField(blank=True, null=True)
    createdby = models.CharField(max_length=20, blank=True, null=True)
    updateddate = models.DateTimeField(blank=True, null=True)
    updatedby = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mosupp'


class Mouser(models.Model):
    user_pk = models.AutoField(primary_key=True)
    userid = models.CharField(unique=True, max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    divisionid = models.IntegerField()
    deptidf = models.IntegerField()
    levelid = models.IntegerField()
    upperlevelid = models.IntegerField()
    creditlimit = models.IntegerField()
    email = models.CharField(max_length=50, blank=True, null=True)
    email2 = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    handphone = models.CharField(max_length=20, blank=True, null=True)
    signatureid = models.CharField(max_length=50, blank=True, null=True)
    photoid = models.CharField(max_length=50, blank=True, null=True)
    isactive = models.SmallIntegerField(blank=True, null=True)
    whsid_locked = models.CharField(max_length=11)
    istopuser = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    createdby = models.CharField(max_length=50, blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    modifiedby = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mouser'


class Mouserloca(models.Model):
    userlocationid = models.AutoField(primary_key=True)
    userid = models.CharField(max_length=50)
    locationid = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    createdby = models.CharField(max_length=50, blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    modifiedby = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mouserloca'
        unique_together = (('userid', 'locationid'),)


class Mtbagian(models.Model):
    bagianid = models.AutoField(primary_key=True)
    divisiid = models.IntegerField()
    bagianname = models.CharField(max_length=100)
    created = models.DateTimeField(blank=True, null=True)
    createdby = models.CharField(max_length=30, blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    modifiedby = models.CharField(max_length=30, blank=True, null=True)
    coa6 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mtbagian'
        unique_together = (('divisiid', 'bagianname'),)


class Mtbahasa(models.Model):
    kodebhs = models.CharField(max_length=6)
    namabhs = models.CharField(max_length=4)
    ketbhs = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'mtbahasa'
        unique_together = (('kodebhs', 'namabhs', 'ketbhs'),)


class Mtbankaccount(models.Model):
    accountid = models.AutoField(primary_key=True)
    accountname = models.CharField(max_length=100)
    accountbankname = models.CharField(max_length=100)
    accountno = models.CharField(max_length=100)
    accountcurrency = models.CharField(max_length=100)
    accountbranch = models.CharField(max_length=100, blank=True, null=True)
    accountbranchtelp = models.CharField(max_length=40, blank=True, null=True)
    accountbranchfax = models.CharField(max_length=40, blank=True, null=True)
    accountbranchemail = models.CharField(max_length=100, blank=True, null=True)
    deptid = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    createdby = models.CharField(max_length=30, blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    modifiedby = models.CharField(max_length=30, blank=True, null=True)
    coa7 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mtbankaccount'
        unique_together = (('accountname', 'accountbankname', 'accountcurrency'),)


class Mtbussinessunit(models.Model):
    bunitid = models.AutoField(primary_key=True)
    bunitname = models.CharField(max_length=100)
    buinit = models.CharField(max_length=10)
    created = models.DateTimeField(blank=True, null=True)
    createdby = models.CharField(max_length=30, blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    modifiedby = models.CharField(max_length=30, blank=True, null=True)
    coa8 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mtbussinessunit'
        unique_together = (('bunitname', 'buinit'),)


class Mtcategorycustomer(models.Model):
    categoryid = models.AutoField(primary_key=True)
    categoryname = models.CharField(unique=True, max_length=50)
    created = models.DateTimeField(blank=True, null=True)
    createdby = models.CharField(max_length=30, blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    modifiedby = models.CharField(max_length=30, blank=True, null=True)
    bunitid = models.IntegerField(blank=True, null=True)
    coa9 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mtcategorycustomer'


class Mtcity(models.Model):
    cityid = models.AutoField(primary_key=True)
    cityname = models.CharField(max_length=40)
    citycountry = models.CharField(max_length=40)
    created = models.DateTimeField(blank=True, null=True)
    createdby = models.CharField(max_length=30, blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    modifiedby = models.CharField(max_length=30, blank=True, null=True)
    bunitid = models.IntegerField(blank=True, null=True)
    coa10 = models.IntegerField(blank=True, null=True)
    isdeleted = models.SmallIntegerField(blank=True, null=True)
    kodetelp = models.CharField(max_length=5)
    bahasa = models.CharField(max_length=10)
    ibukota = models.CharField(max_length=20)
    presiden = models.CharField(max_length=35)

    class Meta:
        managed = False
        db_table = 'mtcity'
        unique_together = (('cityname', 'citycountry'),)


class Mtcurrency(models.Model):
    currency_pk = models.AutoField(primary_key=True)
    currencycode = models.CharField(max_length=5)
    currencyid = models.CharField(unique=True, max_length=6)
    currencyname = models.CharField(max_length=20)
    digit = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    createdby = models.CharField(max_length=30, blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    modifiedby = models.CharField(max_length=30, blank=True, null=True)
    bunitid = models.IntegerField(blank=True, null=True)
    coa11 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mtcurrency'


class Mtcurrencyd(models.Model):
    currencydid = models.AutoField(primary_key=True)
    currency_idf = models.IntegerField()
    currencyid = models.CharField(max_length=6)
    currencydate = models.DateTimeField(blank=True, null=True)
    conversion = models.DecimalField(max_digits=19, decimal_places=4)
    kurs1 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    kurs2 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    kurs3 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    createdby = models.CharField(max_length=30, blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    modifiedby = models.CharField(max_length=30, blank=True, null=True)
    coa12 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mtcurrencyd'
        unique_together = (('currency_idf', 'currencydate'),)


class Mtcustomer(models.Model):
    customerid = models.AutoField(primary_key=True)
    customerinitial = models.CharField(max_length=20)
    customername = models.CharField(unique=True, max_length=100)
    gelar = models.CharField(max_length=45)
    customeralias = models.CharField(max_length=100)
    contactperson = models.CharField(max_length=100)
    addressresidence = models.CharField(max_length=510, blank=True, null=True)
    addressbilling = models.CharField(max_length=510, blank=True, null=True)
    addressdelivery = models.CharField(max_length=510, blank=True, null=True)
    npwpno = models.CharField(max_length=50, blank=True, null=True)
    npwpname = models.CharField(max_length=100, blank=True, null=True)
    npwpaddress = models.CharField(max_length=510, blank=True, null=True)
    terms = models.IntegerField(blank=True, null=True)
    toplimit = models.IntegerField()
    phone1 = models.CharField(max_length=40, blank=True, null=True)
    phone2 = models.CharField(max_length=30, blank=True, null=True)
    fax = models.CharField(max_length=30, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    custcatid = models.IntegerField()
    ppnvaluecustomer = models.FloatField(blank=True, null=True)
    salesid = models.IntegerField()
    bunitid = models.IntegerField()
    custregion = models.IntegerField()
    custcurr = models.CharField(max_length=100)
    custgolongan = models.CharField(max_length=10, blank=True, null=True)
    custbahasa = models.CharField(max_length=40, blank=True, null=True)
    creditlimit = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    sisapiutang = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    memberdate = models.DateTimeField(blank=True, null=True)
    lastinvoice = models.CharField(max_length=100, blank=True, null=True)
    saldopiutanglalu = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    whsid = models.IntegerField(blank=True, null=True)
    idsppl = models.IntegerField(blank=True, null=True)
    coa13 = models.IntegerField(blank=True, null=True)
    approve = models.SmallIntegerField(blank=True, null=True)
    isaktif = models.IntegerField(blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    jeniskelamin = models.CharField(max_length=1)
    pinbb = models.CharField(max_length=20)
    idcardno = models.CharField(max_length=50)
    idcardtype = models.CharField(max_length=20)
    jbb = models.CharField(max_length=10)
    versi = models.CharField(max_length=10, blank=True, null=True)
    islocal = models.SmallIntegerField(blank=True, null=True, db_comment='1;Ekspor;0;Lokal')
    customer_countryid = models.IntegerField()
    customer_zipcode = models.CharField(max_length=10)
    created = models.DateTimeField(blank=True, null=True)
    createdby = models.CharField(max_length=30, blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    modifiedby = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mtcustomer'


class Mtdivisi(models.Model):
    divisiid = models.AutoField(primary_key=True)
    divisiname = models.CharField(unique=True, max_length=100)
    created = models.DateTimeField(blank=True, null=True)
    createdby = models.CharField(max_length=30, blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    modifiedby = models.CharField(max_length=30, blank=True, null=True)
    bunitid = models.IntegerField(blank=True, null=True)
    coa14 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mtdivisi'


class Mtfamilyprod(models.Model):
    familyid = models.AutoField(primary_key=True)
    famno = models.CharField(max_length=100, blank=True, null=True)
    productfamily = models.CharField(unique=True, max_length=100)
    bunitid = models.IntegerField(blank=True, null=True)
    coa15 = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    createdby = models.CharField(max_length=30, blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    modifiedby = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mtfamilyprod'


class Mtformcontrol(models.Model):
    formname = models.CharField(max_length=100)
    controlname = models.CharField(max_length=100)
    controltype = models.CharField(max_length=100)
    kodebahasa = models.CharField(max_length=100)
    judulctrl = models.CharField(max_length=100)
    ukfont = models.IntegerField(blank=True, null=True)
    beratfont = models.IntegerField(blank=True, null=True)
    coa16 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mtformcontrol'
        unique_together = (('formname', 'controlname', 'controltype', 'kodebahasa', 'judulctrl'),)


class Mtgrupcoa(models.Model):
    primarykey = models.AutoField(primary_key=True)
    groupname = models.CharField(unique=True, max_length=50)
    saldonormal = models.SmallIntegerField(blank=True, null=True)
    saldominus = models.SmallIntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    createdby = models.CharField(max_length=50)
    modified = models.DateTimeField(blank=True, null=True)
    modifiedby = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'mtgrupcoa'


class Mtlevel(models.Model):
    levelid = models.AutoField(primary_key=True)
    levelname = models.CharField(max_length=100)
    created = models.DateTimeField(blank=True, null=True)
    createdby = models.CharField(max_length=30, blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    modifiedby = models.CharField(max_length=30, blank=True, null=True)
    bunitid = models.IntegerField(blank=True, null=True)
    coa17 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mtlevel'


class Mtproduct(models.Model):
    productid = models.AutoField(primary_key=True)
    familyid = models.IntegerField()
    productcode = models.CharField(max_length=200)
    productname = models.CharField(unique=True, max_length=200)
    productname2 = models.CharField(max_length=200)
    productname3 = models.CharField(max_length=200)
    ketprod = models.CharField(max_length=510, blank=True, null=True)
    barcodeno = models.CharField(max_length=510, blank=True, null=True)
    barcodeno2 = models.CharField(max_length=100, blank=True, null=True)
    prodcur = models.CharField(max_length=100)
    iscontinue = models.SmallIntegerField(blank=True, null=True)
    sizeprod = models.SmallIntegerField(blank=True, null=True)
    ikatan = models.CharField(max_length=20, blank=True, null=True)
    produnit = models.CharField(max_length=20, blank=True, null=True)
    uom_id_prod = models.IntegerField()
    prodtype = models.CharField(max_length=20, blank=True, null=True)
    limitstok = models.IntegerField(blank=True, null=True)
    maxprice = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    minprice = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    hpp = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    prodwhs = models.IntegerField()
    supplierid = models.IntegerField(blank=True, null=True)
    periodeharga = models.DateTimeField(blank=True, null=True)
    kodekonversi = models.CharField(max_length=10, blank=True, null=True)
    oldid = models.IntegerField(blank=True, null=True)
    coa18 = models.IntegerField(blank=True, null=True)
    isusebarcode = models.SmallIntegerField(blank=True, null=True)
    picture = models.CharField(max_length=200, blank=True, null=True)
    minorder = models.DecimalField(max_digits=10, decimal_places=0)
    curstok = models.DecimalField(max_digits=10, decimal_places=0)
    beratprod = models.FloatField()
    picmobile = models.CharField(max_length=255, blank=True, null=True)
    prod_p = models.DecimalField(max_digits=5, decimal_places=2)
    prod_l = models.DecimalField(max_digits=5, decimal_places=2)
    prod_t = models.DecimalField(max_digits=5, decimal_places=2)
    uom_plt = models.IntegerField()
    prod_nw = models.DecimalField(max_digits=10, decimal_places=2)
    prod_gw = models.DecimalField(max_digits=10, decimal_places=2)
    qty_inner = models.DecimalField(max_digits=10, decimal_places=2)
    qty_outer = models.DecimalField(max_digits=10, decimal_places=2)
    uom_inner_outer = models.IntegerField()
    qty_gram = models.DecimalField(max_digits=10, decimal_places=2)
    uom_berat = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    createdby = models.CharField(max_length=30, blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    modifiedby = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mtproduct'


class MtproductPrice(models.Model):
    priceid = models.AutoField(primary_key=True)
    productid = models.IntegerField()
    regionid = models.IntegerField()
    jeniskirim = models.SmallIntegerField(blank=True, null=True)
    custcatid = models.IntegerField()
    qty_start = models.IntegerField()
    qty_end = models.IntegerField()
    diskon_1 = models.DecimalField(max_digits=3, decimal_places=2)
    diskon_2 = models.DecimalField(max_digits=3, decimal_places=2)
    diskon_3 = models.DecimalField(max_digits=3, decimal_places=2)
    diskon_4 = models.DecimalField(max_digits=3, decimal_places=2)
    price_val = models.DecimalField(max_digits=19, decimal_places=2)
    created = models.DateTimeField(blank=True, null=True)
    createdby = models.CharField(max_length=50)
    modified = models.DateTimeField(blank=True, null=True)
    modifiedby = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'mtproduct_price'
        unique_together = (('productid', 'regionid', 'jeniskirim'),)


class Mtprovince(models.Model):
    province_id = models.AutoField(primary_key=True)
    province_code = models.CharField(max_length=50)
    province_name = models.CharField(max_length=50)
    province_capital = models.CharField(max_length=50)
    province_inactive = models.SmallIntegerField(blank=True, null=True)
    province_governor = models.CharField(max_length=50)
    province_zipcode_start = models.CharField(max_length=10)
    province_zipcode_end = models.CharField(max_length=10)
    province_country_id = models.IntegerField(db_comment='konek ke mtcity where coa10=0')
    created = models.DateTimeField(blank=True, null=True)
    createdby = models.CharField(max_length=50)
    modified = models.DateTimeField(blank=True, null=True)
    modifiedby = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'mtprovince'


class Mtregion(models.Model):
    regionid = models.AutoField(primary_key=True)
    cityid = models.IntegerField()
    regionname = models.CharField(max_length=100)
    regioncode = models.CharField(max_length=100, blank=True, null=True)
    bunitid = models.IntegerField(blank=True, null=True)
    coa19 = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    createdby = models.CharField(max_length=30, blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    modifiedby = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mtregion'
        unique_together = (('cityid', 'regionname'),)


class Mtsalesprice(models.Model):
    idprice = models.CharField(max_length=20, blank=True, null=True)
    slsprice = models.IntegerField()
    utility1 = models.IntegerField(blank=True, null=True)
    utility2 = models.IntegerField(blank=True, null=True)
    customerid = models.IntegerField(blank=True, null=True)
    productid = models.IntegerField()
    periodeharga = models.DateTimeField(blank=True, null=True)
    periode = models.CharField(max_length=20, blank=True, null=True)
    harga = models.DecimalField(max_digits=19, decimal_places=4)
    flag1 = models.SmallIntegerField(blank=True, null=True)
    flag2 = models.SmallIntegerField(blank=True, null=True)
    flag3 = models.SmallIntegerField(blank=True, null=True)
    bunitid = models.IntegerField(blank=True, null=True)
    coa20 = models.IntegerField(blank=True, null=True)
    jumlah = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    keterangan = models.CharField(max_length=510, blank=True, null=True)
    trxid = models.IntegerField(blank=True, null=True)
    trxidout = models.IntegerField(blank=True, null=True)
    utilityid = models.AutoField(primary_key=True)
    keterangan2 = models.CharField(max_length=510, blank=True, null=True)
    ongkir = models.DecimalField(max_digits=10, decimal_places=0)
    linkfilepath = models.CharField(max_length=500, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    createdby = models.CharField(max_length=30, blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    modifiedby = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mtsalesprice'
        unique_together = (('productid', 'periode', 'harga', 'idprice', 'utility1', 'utility2', 'customerid', 'trxid', 'trxidout'),)


class Mtsupplier(models.Model):
    supplierid = models.AutoField(primary_key=True)
    suppcode = models.CharField(max_length=100, blank=True, null=True)
    companyname = models.CharField(max_length=510)
    contactname = models.CharField(max_length=100)
    contacttitle = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=510, blank=True, null=True)
    addressbilling = models.CharField(max_length=510, blank=True, null=True)
    addressdelivery = models.CharField(max_length=510, blank=True, null=True)
    npwpno = models.CharField(max_length=50, blank=True, null=True)
    npwpname = models.CharField(max_length=100, blank=True, null=True)
    npwpaddress = models.CharField(max_length=510, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    region = models.CharField(max_length=50, blank=True, null=True)
    postalcode = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    fax = models.CharField(max_length=100, blank=True, null=True)
    homepage = models.CharField(max_length=100, blank=True, null=True)
    bunitid = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    tempobyr = models.IntegerField(blank=True, null=True)
    sisahutang = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    sisahutangjln = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    iswhs = models.SmallIntegerField(blank=True, null=True)
    currencyid = models.CharField(max_length=20, blank=True, null=True)
    whsid = models.IntegerField(blank=True, null=True)
    idshpl = models.IntegerField(blank=True, null=True)
    coa21 = models.IntegerField(blank=True, null=True)
    idshpl1 = models.CharField(max_length=64, blank=True, null=True)
    islocal = models.SmallIntegerField(blank=True, null=True)
    isactive = models.SmallIntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    createdby = models.CharField(max_length=30, blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    modifiedby = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mtsupplier'
        unique_together = (('companyname', 'bunitid'),)


class Mtunit(models.Model):
    unitid = models.AutoField(primary_key=True)
    tipekonversi = models.CharField(max_length=10)
    satuan = models.IntegerField(blank=True, null=True)
    isi = models.IntegerField(blank=True, null=True)
    unit = models.CharField(max_length=10)
    unitname = models.CharField(max_length=100)
    isplat = models.SmallIntegerField(blank=True, null=True)
    isctl = models.SmallIntegerField(blank=True, null=True)
    isprodtype = models.SmallIntegerField(blank=True, null=True)
    isukuran = models.SmallIntegerField(blank=True, null=True)
    issatuan = models.SmallIntegerField(blank=True, null=True)
    uppct = models.FloatField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    createdby = models.CharField(max_length=30, blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    modifiedby = models.CharField(max_length=30, blank=True, null=True)
    bunitid = models.IntegerField(blank=True, null=True)
    coa22 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mtunit'
        unique_together = (('unit', 'tipekonversi', 'satuan', 'isi', 'unitname'),)


class Mtuser(models.Model):
    userid = models.AutoField(primary_key=True)
    deptid = models.IntegerField()
    usercode = models.CharField(unique=True, max_length=14)
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=255)
    email2 = models.CharField(max_length=255)
    upperlevelid = models.IntegerField()
    password = models.CharField(max_length=40)
    levelsecurity = models.IntegerField()
    deleted = models.SmallIntegerField(blank=True, null=True)
    issales = models.SmallIntegerField(blank=True, null=True)
    pegawaidivisi = models.IntegerField(blank=True, null=True)
    pegawaibagian = models.IntegerField(blank=True, null=True)
    ugapok = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    uumakan = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    utransport = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    upph = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    ustatus = models.CharField(max_length=100, blank=True, null=True)
    uidno = models.CharField(max_length=100, blank=True, null=True)
    uidtype = models.CharField(max_length=100, blank=True, null=True)
    utelp1 = models.CharField(max_length=100, blank=True, null=True)
    utelp2 = models.CharField(max_length=100, blank=True, null=True)
    umtelp = models.CharField(max_length=100, blank=True, null=True)
    commission = models.FloatField(blank=True, null=True)
    coa23 = models.IntegerField(blank=True, null=True)
    signatureid = models.CharField(max_length=255)
    photoid = models.CharField(max_length=255)
    creditlimit = models.DecimalField(max_digits=10, decimal_places=0)
    created = models.DateTimeField(blank=True, null=True)
    createdby = models.CharField(max_length=30, blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    modifiedby = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mtuser'


class Mtutility(models.Model):
    utilityid = models.AutoField(primary_key=True)
    utilityname = models.CharField(unique=True, max_length=255)
    utilitydesc = models.CharField(max_length=255)
    statusid = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    createdby = models.CharField(max_length=50)
    modified = models.DateTimeField(blank=True, null=True)
    modifiedby = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'mtutility'


class Mtwhs(models.Model):
    whsid = models.AutoField(primary_key=True)
    whscode = models.CharField(max_length=12)
    whsname = models.CharField(unique=True, max_length=100)
    whsloc = models.CharField(max_length=255, blank=True, null=True)
    whstelp = models.CharField(max_length=100, blank=True, null=True)
    whsman = models.CharField(max_length=100, blank=True, null=True)
    bunitid = models.IntegerField()
    splid = models.IntegerField(blank=True, null=True)
    coa24 = models.IntegerField(blank=True, null=True)
    ishead = models.SmallIntegerField(blank=True, null=True)
    groupid = models.SmallIntegerField(blank=True, null=True)
    is_virtual = models.SmallIntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    createdby = models.CharField(max_length=30, blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    modifiedby = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mtwhs'


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


class Qrytmphpp(models.Model):
    productid = models.IntegerField(blank=True, null=True)
    whsid = models.IntegerField(blank=True, null=True)
    nhpp = models.DecimalField(max_digits=65, decimal_places=12, blank=True, null=True)
    stokakhir = models.DecimalField(max_digits=41, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'qrytmphpp'


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


class RtTxrcv(models.Model):
    rtid = models.AutoField(primary_key=True)
    rcvidf = models.IntegerField()
    biayabm = models.DecimalField(max_digits=10, decimal_places=8)
    biayacukai = models.DecimalField(max_digits=10, decimal_places=8)
    biayappn = models.DecimalField(max_digits=10, decimal_places=8)
    biayappnbm = models.DecimalField(max_digits=10, decimal_places=8)
    biayapph = models.DecimalField(max_digits=10, decimal_places=8)
    biayalain = models.DecimalField(max_digits=10, decimal_places=8)
    total = models.DecimalField(max_digits=10, decimal_places=8)

    class Meta:
        managed = False
        db_table = 'rt_txrcv'
        db_table_comment = 'table tengah antara txrcv dengan segala biayanya, mempengaruhi HPP'


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


class SysVersion(models.Model):
    daterel = models.DateTimeField(blank=True, null=True)
    version = models.CharField(max_length=100)
    aktif = models.SmallIntegerField(blank=True, null=True)
    rowguid = models.CharField(unique=True, max_length=64)

    class Meta:
        managed = False
        db_table = 'sys_version'
        unique_together = (('daterel', 'version'),)


class Tmppindahanstok(models.Model):
    urut = models.CharField(max_length=1)
    keterangan = models.CharField(max_length=25)
    rcvid = models.BinaryField(blank=True, null=True)
    rcvno = models.CharField(max_length=1)
    rcvdate = models.CharField(max_length=10, blank=True, null=True)
    productid = models.IntegerField()
    namabarang = models.CharField(max_length=200)
    qtyin = models.DecimalField(max_digits=41, decimal_places=4, blank=True, null=True)
    qtyout = models.DecimalField(max_digits=45, decimal_places=4, blank=True, null=True)
    status = models.CharField(max_length=1)
    rcvwhs = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tmppindahanstok'


class Topord(models.Model):
    purchaseid = models.AutoField(primary_key=True)
    purchaseno = models.CharField(max_length=4, blank=True, null=True)
    requestid = models.IntegerField(blank=True, null=True)
    purchasedate = models.DateTimeField(blank=True, null=True)
    paymentterm = models.IntegerField(blank=True, null=True)
    supplierid = models.IntegerField()
    receivedno = models.CharField(max_length=10, blank=True, null=True)
    receiveddate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'topord'


class Toreqs(models.Model):
    requestid = models.AutoField(primary_key=True)
    requestno = models.CharField(max_length=50)
    requestref = models.CharField(max_length=50)
    requestdate = models.DateTimeField(blank=True, null=True)
    userid = models.CharField(max_length=50)
    categoryid = models.IntegerField()
    requestto = models.CharField(max_length=50, blank=True, null=True)
    totalqty = models.DecimalField(max_digits=10, decimal_places=0)
    totalamount = models.DecimalField(max_digits=10, decimal_places=0)
    statusid = models.IntegerField()
    finalstatus = models.IntegerField()
    requestnote = models.CharField(max_length=50)
    requestpriority = models.IntegerField()
    locationid = models.IntegerField(blank=True, null=True)
    createddate = models.DateTimeField(blank=True, null=True)
    createdby = models.CharField(max_length=50)
    updateddate = models.DateTimeField(blank=True, null=True)
    updatedby = models.CharField(max_length=50)
    approvedesc1 = models.CharField(max_length=50, blank=True, null=True)
    approvedesc2 = models.CharField(max_length=50, blank=True, null=True)
    spvapprovedate = models.DateTimeField(blank=True, null=True)
    approvedate1 = models.DateTimeField(blank=True, null=True)
    approvedate2 = models.DateTimeField(blank=True, null=True)
    reason1 = models.CharField(max_length=200, blank=True, null=True)
    reason2 = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'toreqs'


class Toreqsdetl(models.Model):
    requestdetailid = models.AutoField(primary_key=True)
    requestid = models.IntegerField()
    itemgroupid = models.IntegerField()
    itemid = models.IntegerField()
    qty = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=0)
    amount = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    supplierid = models.IntegerField(blank=True, null=True)
    brandname = models.CharField(max_length=50, blank=True, null=True)
    unit = models.CharField(max_length=10, blank=True, null=True)
    useddate = models.DateTimeField(blank=True, null=True)
    usedfor = models.CharField(max_length=50, blank=True, null=True)
    itemtype = models.CharField(max_length=50, blank=True, null=True)
    itemnote = models.CharField(max_length=100, blank=True, null=True)
    statusid = models.IntegerField()
    approveddate = models.DateTimeField(blank=True, null=True)
    approvedby = models.CharField(max_length=50)
    createddate = models.DateTimeField(blank=True, null=True)
    createdby = models.CharField(max_length=50)
    updateddate = models.DateTimeField(blank=True, null=True)
    updatedby = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'toreqsdetl'


class TrLogfile(models.Model):
    log_pk = models.AutoField(primary_key=True)
    log_desc = models.CharField(max_length=255)
    log_comp = models.CharField(max_length=50)
    log_user = models.CharField(max_length=25)
    log_curdate = models.DateTimeField(blank=True, null=True)
    log_module = models.CharField(max_length=50)
    log_event = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'tr_logfile'


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


class Txpayable(models.Model):
    paymentdid = models.AutoField(primary_key=True)
    paymentid = models.IntegerField(blank=True, null=True)
    rcvid = models.IntegerField(blank=True, null=True)
    bilyetguid = models.IntegerField()
    paymentid1 = models.CharField(max_length=64, blank=True, null=True)
    rcvid1 = models.CharField(max_length=64, blank=True, null=True)
    jenisbayar = models.CharField(max_length=510)
    kurstrx = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    totalbayar = models.DecimalField(max_digits=19, decimal_places=4)
    oriamount = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    tkonversibayar = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    tgljt = models.DateTimeField(blank=True, null=True)
    islunaslalu = models.SmallIntegerField(blank=True, null=True)
    currencyid = models.CharField(max_length=10, blank=True, null=True)
    kursbayar = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    kursharian = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    kursbayar2 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    coa29 = models.IntegerField(blank=True, null=True)
    iscair = models.SmallIntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    paytype = models.CharField(max_length=20, blank=True, null=True)
    createdby = models.CharField(max_length=30, blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    modifiedby = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'txpayable'
        unique_together = (('jenisbayar', 'rcvid', 'paymentid'),)


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


class Txpaymenth(models.Model):
    paymentid = models.AutoField(primary_key=True)
    paymentno = models.CharField(max_length=100)
    paymentdate = models.DateField(blank=True, null=True)
    customerid = models.IntegerField()
    kursbayarh = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    totalpayment = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    totalpaymentf = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    isap = models.SmallIntegerField(blank=True, null=True)
    bunitid = models.IntegerField(blank=True, null=True)
    currencyid = models.CharField(max_length=20, blank=True, null=True)
    whsid = models.IntegerField(blank=True, null=True)
    coa31 = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    pcpay1 = models.SmallIntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    paynote = models.CharField(max_length=510, blank=True, null=True)
    createdby = models.CharField(max_length=30, blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    modifiedby = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'txpaymenth'
        unique_together = (('paymentno', 'paymentdate', 'customerid'),)


class Txpo(models.Model):
    poid = models.BigAutoField(primary_key=True)
    pono = models.CharField(max_length=45, blank=True, null=True)
    podate = models.DateField(blank=True, null=True)
    ispolokal = models.SmallIntegerField(blank=True, null=True, db_comment='1;Impor;0;Lokal')
    isprq = models.SmallIntegerField(blank=True, null=True)
    supplierid = models.IntegerField(blank=True, null=True)
    pocurr = models.CharField(max_length=45, blank=True, null=True)
    porate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    potop = models.IntegerField(blank=True, null=True)
    poket1 = models.CharField(max_length=255, blank=True, null=True)
    poket2 = models.CharField(max_length=255, blank=True, null=True)
    pokontrakno = models.CharField(max_length=45, blank=True, null=True)
    pokontrakdate = models.DateField(blank=True, null=True)
    tipebiaya = models.IntegerField(blank=True, null=True)
    po_gross_val = models.DecimalField(max_digits=19, decimal_places=4)
    subtotalpo = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    discpct = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    discval = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    po_subtotal_after_disc = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    ppnpct = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    ppnval = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    gtotalpo = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    totalkonversipo = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    local_po_subtotal = models.DecimalField(max_digits=19, decimal_places=4)
    local_po_tax = models.DecimalField(max_digits=19, decimal_places=4)
    local_po_total = models.DecimalField(max_digits=19, decimal_places=4)
    totalbayarpo = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    totaldppo = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    totalbiaya = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    totalkarton = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    totalvolume = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    totalberat = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    statuspo = models.IntegerField(blank=True, null=True)
    statuspodel = models.IntegerField()
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
    requested = models.DateTimeField(blank=True, null=True)
    requestedby = models.CharField(max_length=255)
    iscancel = models.SmallIntegerField(blank=True, null=True)
    cancelled = models.DateTimeField(blank=True, null=True)
    cancelledby = models.CharField(max_length=45, blank=True, null=True)
    isclosed = models.SmallIntegerField(blank=True, null=True)
    closed = models.DateTimeField(blank=True, null=True)
    closedby = models.CharField(max_length=45, blank=True, null=True)
    sendemailnotif = models.IntegerField()
    deliverydate = models.DateField(blank=True, null=True)
    po_fpajaknorcv = models.CharField(max_length=500, blank=True, null=True)
    po_inv_no_supplier = models.CharField(max_length=255, blank=True, null=True)
    po_sj_no_supplier = models.CharField(max_length=255, blank=True, null=True)
    po_fpajaktglrcv = models.DateField(blank=True, null=True)
    treceived_val = models.DecimalField(max_digits=19, decimal_places=4)
    tinvoiced_val = models.DecimalField(max_digits=19, decimal_places=4)
    created = models.DateTimeField(blank=True, null=True)
    createdby = models.CharField(max_length=45, blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    modifiedby = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'txpo'


class Txpod(models.Model):
    podid = models.AutoField(primary_key=True)
    poidh = models.IntegerField(blank=True, null=True)
    productid = models.IntegerField(blank=True, null=True)
    ketbarang = models.CharField(max_length=255, blank=True, null=True)
    kettambahan = models.CharField(max_length=255, blank=True, null=True)
    unitprodpod = models.IntegerField()
    qtypod = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    qtypodr = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, db_comment='qty yang diterima berdasarkan podid')
    qtypodi = models.DecimalField(max_digits=10, decimal_places=2)
    biayaratepod = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    biaya2 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    biayacurrpod = models.CharField(max_length=45, blank=True, null=True)
    kartonpod = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    volpodm3 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    beratpodkg = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    estpod = models.DateTimeField(blank=True, null=True)
    uomid = models.IntegerField()
    stprod = models.IntegerField()
    pricepod = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    discpctpod = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    discvalpod = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    pod_price_after_disc_1 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    pod_disc_pct_2 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    pod_disc_val_2 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    pod_price_after_disc_2 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    pod_disc_pct_3 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    pod_disc_val_3 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    pod_price_after_disc_3 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    pod_disc_pct_4 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    pod_disc_val_4 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    pod_price_after_disc_4 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    pod_disc_pct_5 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    pod_disc_val_5 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    pod_price_after_disc_5 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    pod_disc_pct_6 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    pod_disc_val_6 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    pod_price_after_disc_6 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    pod_ppn_pct = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    pod_ppn_val = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    pricepoda = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    createdby = models.CharField(max_length=45, blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    modifiedby = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'txpod'
        unique_together = (('poidh', 'productid'),)


class Txrcv(models.Model):
    rcvid = models.AutoField(primary_key=True)
    isretur = models.SmallIntegerField(blank=True, null=True)
    isreturpo = models.SmallIntegerField(blank=True, null=True)
    isstockawal = models.SmallIntegerField(blank=True, null=True)
    istransfer = models.SmallIntegerField(blank=True, null=True)
    isinvoice = models.SmallIntegerField(blank=True, null=True)
    trfrefid = models.IntegerField()
    bdp_refid = models.IntegerField()
    rcvno = models.CharField(max_length=100)
    rcvdate = models.DateField(blank=True, null=True)
    supplierid = models.IntegerField(blank=True, null=True)
    poidh = models.IntegerField()
    currencyid = models.CharField(max_length=10)
    containerid = models.IntegerField(blank=True, null=True)
    rcvwhs = models.IntegerField()
    rcvnote = models.CharField(max_length=510, blank=True, null=True)
    customerid = models.IntegerField(blank=True, null=True)
    rcvcurr = models.CharField(max_length=10, blank=True, null=True)
    bunitid = models.IntegerField()
    rcvwhsto = models.IntegerField()
    totalrcvq = models.DecimalField(max_digits=19, decimal_places=4)
    iscancel = models.SmallIntegerField(blank=True, null=True)
    canceluser = models.IntegerField(blank=True, null=True)
    canceldate = models.DateTimeField(blank=True, null=True)
    isold = models.SmallIntegerField(blank=True, null=True)
    apod = models.IntegerField(blank=True, null=True)
    islunas = models.SmallIntegerField(blank=True, null=True)
    totalbayar = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    kursbeli = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    kurseval = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    kursbl = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    isshpl = models.SmallIntegerField(blank=True, null=True)
    coa32 = models.IntegerField(blank=True, null=True)
    totalretur = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    iskys = models.SmallIntegerField(blank=True, null=True)
    reftrxid = models.CharField(max_length=64, blank=True, null=True, db_comment='invoiceid')
    pcrcv1 = models.BigIntegerField()
    pcrcv2 = models.BigIntegerField()
    statusrcv = models.SmallIntegerField(blank=True, null=True)
    iskontrabon = models.SmallIntegerField(blank=True, null=True)
    iscashrcv = models.SmallIntegerField(blank=True, null=True)
    printedby = models.CharField(max_length=100, blank=True, null=True)
    printed = models.DateTimeField(blank=True, null=True)
    ppnvalrcvh = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    discvalrcvh = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    subtotalrcv = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    totalpotongan = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    rcv_subtotal_after_disc = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    ppnvalue = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    totalrcvm = models.DecimalField(max_digits=19, decimal_places=4)
    grandtotalrcv = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    tkonversibeli = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    fpajaknorcv = models.CharField(max_length=500, blank=True, null=True)
    fpajaktglrcv = models.DateField(blank=True, null=True)
    inv_no_supplier = models.CharField(max_length=255)
    sj_no_supplier = models.CharField(max_length=255)
    paramst_pch = models.IntegerField()
    tinvoiced_qty_val = models.DecimalField(max_digits=19, decimal_places=4)
    tinvoiced_jml_val = models.DecimalField(max_digits=19, decimal_places=4)
    created = models.DateTimeField(blank=True, null=True)
    createdby = models.CharField(max_length=30, blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    modifiedby = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'txrcv'
        unique_together = (('rcvno', 'rcvdate', 'rcvwhs', 'customerid', 'rcvcurr', 'supplierid'),)


class Txrcvd(models.Model):
    rcvdid = models.AutoField(primary_key=True)
    poid_d_idf = models.IntegerField()
    rcvid = models.IntegerField()
    rinvoiceid = models.IntegerField(blank=True, null=True)
    rinvoicedid = models.IntegerField(blank=True, null=True)
    rcvidref = models.IntegerField(blank=True, null=True)
    productid = models.IntegerField()
    noteline = models.CharField(max_length=8000, blank=True, null=True)
    ketrcv = models.CharField(max_length=100, blank=True, null=True)
    uom_idf = models.IntegerField()
    qtyrcv = models.DecimalField(max_digits=19, decimal_places=4)
    qtydus = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    qtyunitdus = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    discvalrcv = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    produnit = models.CharField(max_length=100, blank=True, null=True)
    konversircv = models.CharField(max_length=10, blank=True, null=True)
    coa33 = models.IntegerField(blank=True, null=True)
    discvalrcvd = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    skuid = models.CharField(max_length=200, blank=True, null=True)
    kursbelid = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    ongkos = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    ongkosf = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    expireddate = models.DateField(blank=True, null=True)
    hrgawalrcv = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    hargadasar = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    rcvd_disc_pct_1 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    rcvd_disc_val_1 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    rcvd_price_after_disc_1 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    rcvd_disc_pct_2 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    rcvd_disc_val_2 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    rcvd_price_after_disc_2 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    rcvd_disc_pct_3 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    rcvd_disc_val_3 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    rcvd_price_after_disc_3 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    rcvd_disc_pct_4 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    rcvd_disc_val_4 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    rcvd_price_after_disc_4 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    rcvd_disc_pct_5 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    rcvd_disc_val_5 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    rcvd_price_after_disc_5 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    rcvd_disc_pct_6 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    rcvd_disc_val_6 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    rcvd_price_after_disc_6 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    rcvd_ppn_pct = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    rcvd_ppn_val = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    pricercv = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    hrgmodal = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    invprcprice = models.DecimalField(max_digits=19, decimal_places=4)
    invoiced_qty_val = models.DecimalField(max_digits=10, decimal_places=2)
    invoiced_val = models.DecimalField(max_digits=19, decimal_places=4)
    created = models.DateTimeField(blank=True, null=True)
    createdby = models.CharField(max_length=100, blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    modifiedby = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'txrcvd'
        unique_together = (('rcvid', 'productid', 'rinvoiceid', 'rinvoicedid', 'rcvidref'),)


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
