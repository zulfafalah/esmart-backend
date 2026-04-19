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


class SysVersion(models.Model):
    daterel = models.DateTimeField(blank=True, null=True)
    version = models.CharField(max_length=100)
    aktif = models.SmallIntegerField(blank=True, null=True)
    rowguid = models.CharField(unique=True, max_length=64)

    class Meta:
        managed = False
        db_table = 'sys_version'
        unique_together = (('daterel', 'version'),)


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
