--
-- PostgreSQL database dump
--

\restrict O8kGVwrX6z71XI64OfHDIhrJ6kxJg9JsfZICCfQ5X5KTuLoVA3q3D2ruPBCkPg9

-- Dumped from database version 14.5 (Debian 14.5-2.pgdg110+2)
-- Dumped by pg_dump version 18.3

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: public; Type: SCHEMA; Schema: -; Owner: -
--

-- *not* creating schema, since initdb creates it


--
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: -
--

COMMENT ON SCHEMA public IS '';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: accounts; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.accounts (
    primarykey integer NOT NULL,
    code character varying(40) NOT NULL,
    name character varying(100),
    groupkey integer,
    parentkey integer,
    accounttypekey integer,
    acpos integer DEFAULT 0 NOT NULL,
    coa0 integer DEFAULT 0 NOT NULL,
    currac_idf integer DEFAULT 0 NOT NULL,
    isbank integer DEFAULT 0,
    isrl integer DEFAULT 0,
    isgl integer DEFAULT 0,
    isneraca integer DEFAULT 0,
    isneracap integer DEFAULT 0,
    limit_saldo_val numeric(19,4) DEFAULT 0.0000 NOT NULL,
    created timestamp without time zone,
    createdby character varying(100),
    modified timestamp without time zone,
    modifiedby character varying(100)
);


--
-- Name: accounts_primarykey_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.accounts_primarykey_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: accounts_primarykey_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.accounts_primarykey_seq OWNED BY public.accounts.primarykey;


--
-- Name: dtproperties; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.dtproperties (
    id integer NOT NULL,
    objectid integer,
    property character varying(64) NOT NULL,
    value character varying(255),
    uvalue character varying(510),
    lvalue bytea,
    version integer DEFAULT 0 NOT NULL
);


--
-- Name: dtproperties_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.dtproperties_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: dtproperties_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.dtproperties_id_seq OWNED BY public.dtproperties.id;


--
-- Name: exno; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.exno (
    primarykey integer NOT NULL,
    trxtype character varying(6) NOT NULL,
    trxno integer NOT NULL,
    trxsuffix character varying(75),
    trxprefix character varying(40),
    trxdigit integer NOT NULL,
    coa1 integer,
    created timestamp without time zone
);


--
-- Name: exno_primarykey_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.exno_primarykey_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: exno_primarykey_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.exno_primarykey_seq OWNED BY public.exno.primarykey;


--
-- Name: gninit; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.gninit (
    initname character varying(40) NOT NULL,
    coa2 integer DEFAULT 0 NOT NULL,
    description character varying(100),
    valtext character varying(255) NOT NULL,
    created timestamp without time zone,
    createdby character varying(30),
    modified timestamp without time zone,
    modifiedby character varying(30)
);


--
-- Name: journal; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.journal (
    primarykey integer NOT NULL,
    code character varying(40) NOT NULL,
    journaldate date,
    descriptions character varying(510),
    status integer,
    currencyid character varying(10),
    kursjurnal numeric(19,4),
    tkonversijurnal numeric(19,4),
    bunitid integer,
    debetval numeric(19,4) DEFAULT 0.0000,
    creditval numeric(19,4) DEFAULT 0.0000,
    debetvalf numeric(19,4) DEFAULT 0.0000,
    creditvalf numeric(19,4) DEFAULT 0.0000,
    pcjournal1 character varying(20) DEFAULT '1'::character varying NOT NULL,
    ishide smallint,
    coa3 integer,
    idtrx character varying(5) NOT NULL,
    created timestamp without time zone,
    createdby character varying(100),
    modified timestamp without time zone,
    modifiedby character varying(100)
);


--
-- Name: journal_primarykey_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.journal_primarykey_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: journal_primarykey_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.journal_primarykey_seq OWNED BY public.journal.primarykey;


--
-- Name: journalentry; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.journalentry (
    primarykey integer NOT NULL,
    journalkey integer DEFAULT 0 NOT NULL,
    sequence integer,
    descriptions character varying(510),
    voucher character varying(40),
    accountkey integer,
    debetcredit integer,
    amount numeric(19,4),
    amountf numeric(19,4),
    voucherno1 character varying(510),
    journalkey1 character varying(64),
    coa4 integer,
    created timestamp without time zone,
    createdby character varying(100),
    modified timestamp without time zone,
    modifiedby character varying(100)
);


--
-- Name: journalentry_primarykey_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.journalentry_primarykey_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: journalentry_primarykey_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.journalentry_primarykey_seq OWNED BY public.journalentry.primarykey;


--
-- Name: moaccs; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.moaccs (
    accessid integer NOT NULL,
    levelid integer NOT NULL,
    formid integer NOT NULL,
    allowsave smallint,
    allowopen smallint,
    allowedit smallint,
    allowdelete smallint,
    allowfilter smallint,
    allowapprove smallint,
    allowunapprove smallint,
    created timestamp without time zone,
    createdby character varying(50) NOT NULL,
    modified timestamp without time zone,
    modifiedby character varying(50) NOT NULL
);


--
-- Name: moaccs_accessid_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.moaccs_accessid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: moaccs_accessid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.moaccs_accessid_seq OWNED BY public.moaccs.accessid;


--
-- Name: mocomp; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.mocomp (
    companyid integer NOT NULL,
    companyname character varying(25) DEFAULT '0'::character varying,
    companyinitial character varying(100) NOT NULL,
    companylogin character varying(50) NOT NULL,
    address1 character varying(100) DEFAULT '0'::character varying,
    phone1 character varying(15) DEFAULT '0'::character varying,
    fax1 character varying(15) DEFAULT '0'::character varying,
    email1 character varying(25) DEFAULT '0'::character varying,
    address2 character varying(100),
    phone2 character varying(15),
    fax2 character varying(15),
    email2 character varying(25),
    address3 character varying(100),
    phone3 character varying(15),
    fax3 character varying(15),
    email3 character varying(25),
    updateddate timestamp without time zone,
    updatedby character varying(25),
    createddate timestamp without time zone,
    createdby character varying(25)
);


--
-- Name: mocomp_companyid_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.mocomp_companyid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: mocomp_companyid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.mocomp_companyid_seq OWNED BY public.mocomp.companyid;


--
-- Name: moctgr; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.moctgr (
    categoryid integer NOT NULL,
    categoryname character varying(50) NOT NULL,
    createddate timestamp without time zone,
    createdby character varying(50) NOT NULL,
    updateddate timestamp without time zone,
    updatedby character varying(50) NOT NULL
);


--
-- Name: moctgr_categoryid_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.moctgr_categoryid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: moctgr_categoryid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.moctgr_categoryid_seq OWNED BY public.moctgr.categoryid;


--
-- Name: modept; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.modept (
    deptid integer NOT NULL,
    deptname text NOT NULL,
    createddate timestamp without time zone,
    createdby character varying(50) NOT NULL,
    updateddate timestamp without time zone,
    updatedby character varying(50) NOT NULL
);


--
-- Name: modept_deptid_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.modept_deptid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: modept_deptid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.modept_deptid_seq OWNED BY public.modept.deptid;


--
-- Name: modivn; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.modivn (
    divisionid integer NOT NULL,
    divisionname character varying(50) NOT NULL,
    createddate timestamp without time zone,
    createdby character varying(50) NOT NULL,
    updateddate timestamp without time zone,
    updatedby character varying(50)
);


--
-- Name: modivn_divisionid_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.modivn_divisionid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: modivn_divisionid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.modivn_divisionid_seq OWNED BY public.modivn.divisionid;


--
-- Name: moform; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.moform (
    formid integer NOT NULL,
    formname character varying(50) NOT NULL,
    formdescription character varying(100),
    formdescriptionen character varying(255),
    headerid integer DEFAULT 0 NOT NULL,
    url_text character varying(1000) NOT NULL,
    stmenu integer DEFAULT 0 NOT NULL,
    ismenu smallint,
    created timestamp without time zone,
    createdby character varying(50) NOT NULL,
    modified timestamp without time zone,
    modifiedby character varying(50) NOT NULL,
    url_group_id character varying(50),
    url_seq_menu integer,
    url_table_id character varying(50),
    url_where_id character varying(50),
    url_modacc_id character varying(50),
    icon_menu character varying(50),
    form_name_ext character varying(50)
);


--
-- Name: moform_formid_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.moform_formid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: moform_formid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.moform_formid_seq OWNED BY public.moform.formid;


--
-- Name: molevl; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.molevl (
    levelid integer NOT NULL,
    levelname character varying(50) NOT NULL,
    isactive smallint,
    created timestamp without time zone,
    createdby character varying(50) NOT NULL,
    modified timestamp without time zone,
    modifiedby character varying(50)
);


--
-- Name: molevl_levelid_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.molevl_levelid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: molevl_levelid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.molevl_levelid_seq OWNED BY public.molevl.levelid;


--
-- Name: moloca; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.moloca (
    locationid integer NOT NULL,
    locationname character varying(50) NOT NULL,
    companyname character varying(100) NOT NULL,
    companyinitial character varying(100) NOT NULL,
    companylogin character varying(100) NOT NULL,
    address1 character varying(100) NOT NULL,
    address2 character varying(100) NOT NULL,
    address3 character varying(100) NOT NULL,
    phone1 character varying(100) NOT NULL,
    phone2 character varying(100) NOT NULL,
    phone3 character varying(100) NOT NULL,
    fax1 character varying(100) NOT NULL,
    fax2 character varying(100) NOT NULL,
    fax3 character varying(100) NOT NULL,
    email1 character varying(100) NOT NULL,
    email2 character varying(100) NOT NULL,
    email3 character varying(100) NOT NULL,
    created timestamp without time zone,
    createdby character varying(50) NOT NULL,
    modifiedby character varying(50) NOT NULL,
    modified timestamp without time zone
);


--
-- Name: moloca_locationid_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.moloca_locationid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: moloca_locationid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.moloca_locationid_seq OWNED BY public.moloca.locationid;


--
-- Name: monmbr; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.monmbr (
    numberid integer NOT NULL,
    divisionid integer NOT NULL,
    descr character varying(5),
    startno integer DEFAULT 0 NOT NULL,
    endno integer DEFAULT 9999 NOT NULL,
    lastno integer DEFAULT 0 NOT NULL,
    tagseparator character varying(5),
    digit smallint,
    createddate timestamp without time zone,
    createdby character varying(20),
    updateddate timestamp without time zone,
    updatedby character varying(20)
);


--
-- Name: monmbr_numberid_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.monmbr_numberid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: monmbr_numberid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.monmbr_numberid_seq OWNED BY public.monmbr.numberid;


--
-- Name: mostat; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.mostat (
    statid integer NOT NULL,
    statusid integer NOT NULL,
    statusname character varying(50) NOT NULL,
    createddate timestamp without time zone,
    createdby character varying(50),
    updateddate timestamp without time zone,
    updatedby character varying(50)
);


--
-- Name: mostat_statid_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.mostat_statid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: mostat_statid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.mostat_statid_seq OWNED BY public.mostat.statid;


--
-- Name: mosupp; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.mosupp (
    supplierid integer NOT NULL,
    suppliername character varying(50),
    supplieraddress character varying(50),
    suppliertelp1 character varying(15),
    suppliertelp2 character varying(15),
    createddate timestamp without time zone,
    createdby character varying(20),
    updateddate timestamp without time zone,
    updatedby character varying(20)
);


--
-- Name: mosupp_supplierid_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.mosupp_supplierid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: mosupp_supplierid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.mosupp_supplierid_seq OWNED BY public.mosupp.supplierid;


--
-- Name: mouser; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.mouser (
    user_pk integer NOT NULL,
    userid character varying(50) NOT NULL,
    username character varying(50) NOT NULL,
    password character varying(50) NOT NULL,
    divisionid integer NOT NULL,
    deptidf integer NOT NULL,
    levelid integer NOT NULL,
    upperlevelid integer NOT NULL,
    creditlimit integer DEFAULT 0 NOT NULL,
    email character varying(50),
    email2 character varying(50),
    phone character varying(20),
    handphone character varying(20),
    signatureid character varying(50),
    photoid character varying(50),
    isactive smallint,
    whsid_locked character varying(11) DEFAULT '0'::character varying NOT NULL,
    istopuser integer DEFAULT 0 NOT NULL,
    created timestamp without time zone,
    createdby character varying(50),
    modified timestamp without time zone,
    modifiedby character varying(50)
);


--
-- Name: mouser_user_pk_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.mouser_user_pk_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: mouser_user_pk_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.mouser_user_pk_seq OWNED BY public.mouser.user_pk;


--
-- Name: mouserloca; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.mouserloca (
    userlocationid integer NOT NULL,
    userid character varying(50) NOT NULL,
    locationid integer NOT NULL,
    created timestamp without time zone,
    createdby character varying(50),
    modified timestamp without time zone,
    modifiedby character varying(50)
);


--
-- Name: mouserloca_userlocationid_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.mouserloca_userlocationid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: mouserloca_userlocationid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.mouserloca_userlocationid_seq OWNED BY public.mouserloca.userlocationid;


--
-- Name: mtbagian; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.mtbagian (
    bagianid integer NOT NULL,
    divisiid integer NOT NULL,
    bagianname character varying(100) NOT NULL,
    created timestamp without time zone,
    createdby character varying(30),
    modified timestamp without time zone,
    modifiedby character varying(30),
    coa6 integer
);


--
-- Name: mtbagian_bagianid_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.mtbagian_bagianid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: mtbagian_bagianid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.mtbagian_bagianid_seq OWNED BY public.mtbagian.bagianid;


--
-- Name: mtbahasa; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.mtbahasa (
    kodebhs character varying(6) NOT NULL,
    namabhs character varying(4) NOT NULL,
    ketbhs character varying(100) NOT NULL
);


--
-- Name: mtbankaccount; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.mtbankaccount (
    accountid integer NOT NULL,
    accountname character varying(100) NOT NULL,
    accountbankname character varying(100) NOT NULL,
    accountno character varying(100) NOT NULL,
    accountcurrency character varying(100) NOT NULL,
    accountbranch character varying(100),
    accountbranchtelp character varying(40),
    accountbranchfax character varying(40),
    accountbranchemail character varying(100),
    deptid integer NOT NULL,
    created timestamp without time zone,
    createdby character varying(30),
    modified timestamp without time zone,
    modifiedby character varying(30),
    coa7 integer
);


--
-- Name: mtbankaccount_accountid_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.mtbankaccount_accountid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: mtbankaccount_accountid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.mtbankaccount_accountid_seq OWNED BY public.mtbankaccount.accountid;


--
-- Name: mtbussinessunit; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.mtbussinessunit (
    bunitid integer NOT NULL,
    bunitname character varying(100) NOT NULL,
    buinit character varying(10) NOT NULL,
    created timestamp without time zone,
    createdby character varying(30),
    modified timestamp without time zone,
    modifiedby character varying(30),
    coa8 integer
);


--
-- Name: mtbussinessunit_bunitid_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.mtbussinessunit_bunitid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: mtbussinessunit_bunitid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.mtbussinessunit_bunitid_seq OWNED BY public.mtbussinessunit.bunitid;


--
-- Name: mtcategorycustomer; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.mtcategorycustomer (
    categoryid integer NOT NULL,
    categoryname character varying(50) NOT NULL,
    created timestamp without time zone,
    createdby character varying(30),
    modified timestamp without time zone,
    modifiedby character varying(30),
    bunitid integer,
    coa9 integer
);


--
-- Name: mtcategorycustomer_categoryid_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.mtcategorycustomer_categoryid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: mtcategorycustomer_categoryid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.mtcategorycustomer_categoryid_seq OWNED BY public.mtcategorycustomer.categoryid;


--
-- Name: mtcity; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.mtcity (
    cityid integer NOT NULL,
    cityname character varying(40) NOT NULL,
    citycountry character varying(40) NOT NULL,
    created timestamp without time zone,
    createdby character varying(30),
    modified timestamp without time zone,
    modifiedby character varying(30),
    bunitid integer,
    coa10 integer,
    isdeleted smallint,
    kodetelp character varying(5) NOT NULL,
    bahasa character varying(10) NOT NULL,
    ibukota character varying(20) NOT NULL,
    presiden character varying(35) NOT NULL
);


--
-- Name: mtcity_cityid_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.mtcity_cityid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: mtcity_cityid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.mtcity_cityid_seq OWNED BY public.mtcity.cityid;


--
-- Name: mtcurrency; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.mtcurrency (
    currency_pk integer NOT NULL,
    currencycode character varying(5) NOT NULL,
    currencyid character varying(6) NOT NULL,
    currencyname character varying(20) NOT NULL,
    digit integer NOT NULL,
    created timestamp without time zone,
    createdby character varying(30),
    modified timestamp without time zone,
    modifiedby character varying(30),
    bunitid integer,
    coa11 integer
);


--
-- Name: mtcurrency_currency_pk_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.mtcurrency_currency_pk_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: mtcurrency_currency_pk_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.mtcurrency_currency_pk_seq OWNED BY public.mtcurrency.currency_pk;


--
-- Name: mtcurrencyd; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.mtcurrencyd (
    currencydid integer NOT NULL,
    currency_idf integer DEFAULT 0 NOT NULL,
    currencyid character varying(6) NOT NULL,
    currencydate timestamp without time zone,
    conversion numeric(19,4) NOT NULL,
    kurs1 numeric(19,4),
    kurs2 numeric(19,4),
    kurs3 numeric(19,4),
    created timestamp without time zone,
    createdby character varying(30),
    modified timestamp without time zone,
    modifiedby character varying(30),
    coa12 integer
);


--
-- Name: mtcurrencyd_currencydid_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.mtcurrencyd_currencydid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: mtcurrencyd_currencydid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.mtcurrencyd_currencydid_seq OWNED BY public.mtcurrencyd.currencydid;


--
-- Name: mtcustomer; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.mtcustomer (
    customerid integer NOT NULL,
    customerinitial character varying(20) NOT NULL,
    customername character varying(100) NOT NULL,
    gelar character varying(45) NOT NULL,
    customeralias character varying(100) NOT NULL,
    contactperson character varying(100) NOT NULL,
    addressresidence character varying(510),
    addressbilling character varying(510),
    addressdelivery character varying(510),
    npwpno character varying(50),
    npwpname character varying(100),
    npwpaddress character varying(510),
    terms integer DEFAULT 0,
    toplimit integer DEFAULT 0 NOT NULL,
    phone1 character varying(40),
    phone2 character varying(30),
    fax character varying(30),
    email character varying(100),
    custcatid integer NOT NULL,
    ppnvaluecustomer double precision DEFAULT '0'::double precision,
    salesid integer NOT NULL,
    bunitid integer NOT NULL,
    custregion integer NOT NULL,
    custcurr character varying(100) NOT NULL,
    custgolongan character varying(10),
    custbahasa character varying(40),
    creditlimit numeric(19,4) DEFAULT 0.0000,
    sisapiutang numeric(19,4) DEFAULT 0.0000,
    memberdate timestamp without time zone,
    lastinvoice character varying(100),
    saldopiutanglalu numeric(19,4) DEFAULT 0.0000,
    whsid integer,
    idsppl integer DEFAULT 0,
    coa13 integer,
    approve smallint,
    isaktif integer DEFAULT 0,
    birthdate date,
    jeniskelamin character varying(1) NOT NULL,
    pinbb character varying(20) NOT NULL,
    idcardno character varying(50) NOT NULL,
    idcardtype character varying(20) NOT NULL,
    jbb character varying(10) DEFAULT '-'::character varying NOT NULL,
    versi character varying(10),
    islocal smallint,
    customer_countryid integer DEFAULT 0 NOT NULL,
    customer_zipcode character varying(10) DEFAULT '000000'::character varying NOT NULL,
    created timestamp without time zone,
    createdby character varying(30),
    modified timestamp without time zone,
    modifiedby character varying(30)
);


--
-- Name: COLUMN mtcustomer.islocal; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.mtcustomer.islocal IS '1;Ekspor;0;Lokal';


--
-- Name: mtcustomer_customerid_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.mtcustomer_customerid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: mtcustomer_customerid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.mtcustomer_customerid_seq OWNED BY public.mtcustomer.customerid;


--
-- Name: mtdivisi; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.mtdivisi (
    divisiid integer NOT NULL,
    divisiname character varying(100) NOT NULL,
    created timestamp without time zone,
    createdby character varying(30),
    modified timestamp without time zone,
    modifiedby character varying(30),
    bunitid integer,
    coa14 integer
);


--
-- Name: mtdivisi_divisiid_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.mtdivisi_divisiid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: mtdivisi_divisiid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.mtdivisi_divisiid_seq OWNED BY public.mtdivisi.divisiid;


--
-- Name: mtfamilyprod; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.mtfamilyprod (
    familyid integer NOT NULL,
    famno character varying(100),
    productfamily character varying(100) NOT NULL,
    bunitid integer,
    coa15 integer,
    created timestamp without time zone,
    createdby character varying(30),
    modified timestamp without time zone,
    modifiedby character varying(30)
);


--
-- Name: mtfamilyprod_familyid_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.mtfamilyprod_familyid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: mtfamilyprod_familyid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.mtfamilyprod_familyid_seq OWNED BY public.mtfamilyprod.familyid;


--
-- Name: mtformcontrol; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.mtformcontrol (
    formname character varying(100) NOT NULL,
    controlname character varying(100) NOT NULL,
    controltype character varying(100) NOT NULL,
    kodebahasa character varying(100) NOT NULL,
    judulctrl character varying(100) NOT NULL,
    ukfont integer,
    beratfont integer,
    coa16 integer
);


--
-- Name: mtgrupcoa; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.mtgrupcoa (
    primarykey integer NOT NULL,
    groupname character varying(50) NOT NULL,
    saldonormal smallint,
    saldominus smallint,
    created timestamp without time zone,
    createdby character varying(50) NOT NULL,
    modified timestamp without time zone,
    modifiedby character varying(50) NOT NULL
);


--
-- Name: mtgrupcoa_primarykey_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.mtgrupcoa_primarykey_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: mtgrupcoa_primarykey_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.mtgrupcoa_primarykey_seq OWNED BY public.mtgrupcoa.primarykey;


--
-- Name: mtlevel; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.mtlevel (
    levelid integer NOT NULL,
    levelname character varying(100) NOT NULL,
    created timestamp without time zone,
    createdby character varying(30),
    modified timestamp without time zone,
    modifiedby character varying(30),
    bunitid integer,
    coa17 integer
);


--
-- Name: mtlevel_levelid_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.mtlevel_levelid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: mtlevel_levelid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.mtlevel_levelid_seq OWNED BY public.mtlevel.levelid;


--
-- Name: mtproduct; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.mtproduct (
    productid integer NOT NULL,
    familyid integer NOT NULL,
    productcode character varying(200) NOT NULL,
    productname character varying(200) NOT NULL,
    productname2 character varying(200) NOT NULL,
    productname3 character varying(200) NOT NULL,
    ketprod character varying(510),
    barcodeno character varying(510),
    barcodeno2 character varying(100),
    prodcur character varying(100) NOT NULL,
    iscontinue smallint,
    sizeprod smallint,
    ikatan character varying(20),
    produnit character varying(20),
    uom_id_prod integer DEFAULT 20 NOT NULL,
    prodtype character varying(20),
    limitstok integer DEFAULT 0,
    maxprice numeric(19,4) DEFAULT 0.0000,
    minprice numeric(19,4) DEFAULT 0.0000,
    hpp numeric(19,4) DEFAULT 0.0000,
    prodwhs integer NOT NULL,
    supplierid integer,
    periodeharga timestamp without time zone,
    kodekonversi character varying(10),
    oldid integer,
    coa18 integer,
    isusebarcode smallint,
    picture character varying(200),
    minorder numeric(10,0) DEFAULT '0'::numeric NOT NULL,
    curstok numeric(10,0) DEFAULT '0'::numeric NOT NULL,
    beratprod double precision DEFAULT '0'::double precision NOT NULL,
    picmobile character varying(255),
    prod_p numeric(5,2) DEFAULT 0.00 NOT NULL,
    prod_l numeric(5,2) DEFAULT 0.00 NOT NULL,
    prod_t numeric(5,2) DEFAULT 0.00 NOT NULL,
    uom_plt integer DEFAULT 0 NOT NULL,
    prod_nw numeric(10,2) DEFAULT 0.00 NOT NULL,
    prod_gw numeric(10,2) DEFAULT 0.00 NOT NULL,
    qty_inner numeric(10,2) DEFAULT 0.00 NOT NULL,
    qty_outer numeric(10,2) DEFAULT 0.00 NOT NULL,
    uom_inner_outer integer DEFAULT 0 NOT NULL,
    qty_gram numeric(10,2) DEFAULT 0.00 NOT NULL,
    uom_berat integer DEFAULT 0 NOT NULL,
    created timestamp without time zone,
    createdby character varying(30),
    modified timestamp without time zone,
    modifiedby character varying(30)
);


--
-- Name: mtproduct_price; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.mtproduct_price (
    priceid integer NOT NULL,
    productid integer DEFAULT 0 NOT NULL,
    regionid integer DEFAULT 0 NOT NULL,
    jeniskirim smallint,
    custcatid integer DEFAULT 0 NOT NULL,
    qty_start integer DEFAULT 0 NOT NULL,
    qty_end integer DEFAULT 0 NOT NULL,
    diskon_1 numeric(3,2) DEFAULT 0.00 NOT NULL,
    diskon_2 numeric(3,2) DEFAULT 0.00 NOT NULL,
    diskon_3 numeric(3,2) DEFAULT 0.00 NOT NULL,
    diskon_4 numeric(3,2) DEFAULT 0.00 NOT NULL,
    price_val numeric(19,2) DEFAULT 0.00 NOT NULL,
    created timestamp without time zone,
    createdby character varying(50) NOT NULL,
    modified timestamp without time zone,
    modifiedby character varying(50) NOT NULL
);


--
-- Name: mtproduct_price_priceid_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.mtproduct_price_priceid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: mtproduct_price_priceid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.mtproduct_price_priceid_seq OWNED BY public.mtproduct_price.priceid;


--
-- Name: mtproduct_productid_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.mtproduct_productid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: mtproduct_productid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.mtproduct_productid_seq OWNED BY public.mtproduct.productid;


--
-- Name: mtprovince; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.mtprovince (
    province_id integer NOT NULL,
    province_code character varying(50) NOT NULL,
    province_name character varying(50) NOT NULL,
    province_capital character varying(50) NOT NULL,
    province_inactive smallint,
    province_governor character varying(50) NOT NULL,
    province_zipcode_start character varying(10) NOT NULL,
    province_zipcode_end character varying(10) NOT NULL,
    province_country_id integer NOT NULL,
    created timestamp without time zone,
    createdby character varying(50) NOT NULL,
    modified timestamp without time zone,
    modifiedby character varying(50) NOT NULL
);


--
-- Name: COLUMN mtprovince.province_country_id; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.mtprovince.province_country_id IS 'konek ke mtcity where coa10=0';


--
-- Name: mtprovince_province_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.mtprovince_province_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: mtprovince_province_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.mtprovince_province_id_seq OWNED BY public.mtprovince.province_id;


--
-- Name: mtregion; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.mtregion (
    regionid integer NOT NULL,
    cityid integer NOT NULL,
    regionname character varying(100) NOT NULL,
    regioncode character varying(100),
    bunitid integer,
    coa19 integer,
    created timestamp without time zone,
    createdby character varying(30),
    modified timestamp without time zone,
    modifiedby character varying(30)
);


--
-- Name: mtregion_regionid_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.mtregion_regionid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: mtregion_regionid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.mtregion_regionid_seq OWNED BY public.mtregion.regionid;


--
-- Name: mtsalesprice; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.mtsalesprice (
    idprice character varying(20),
    slsprice integer NOT NULL,
    utility1 integer,
    utility2 integer,
    customerid integer,
    productid integer NOT NULL,
    periodeharga timestamp without time zone,
    periode character varying(20),
    harga numeric(19,4) DEFAULT 0.0000 NOT NULL,
    flag1 smallint,
    flag2 smallint,
    flag3 smallint,
    bunitid integer,
    coa20 integer,
    jumlah numeric(19,4) DEFAULT 0.0000,
    keterangan character varying(510),
    trxid integer DEFAULT 0,
    trxidout integer DEFAULT 0,
    utilityid integer NOT NULL,
    keterangan2 character varying(510),
    ongkir numeric(10,0) DEFAULT '0'::numeric NOT NULL,
    linkfilepath character varying(500),
    created timestamp without time zone,
    createdby character varying(30),
    modified timestamp without time zone,
    modifiedby character varying(30)
);


--
-- Name: mtsalesprice_utilityid_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.mtsalesprice_utilityid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: mtsalesprice_utilityid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.mtsalesprice_utilityid_seq OWNED BY public.mtsalesprice.utilityid;


--
-- Name: mtsupplier; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.mtsupplier (
    supplierid integer NOT NULL,
    suppcode character varying(100),
    companyname character varying(510) NOT NULL,
    contactname character varying(100) NOT NULL,
    contacttitle character varying(20),
    address character varying(510),
    addressbilling character varying(510),
    addressdelivery character varying(510),
    npwpno character varying(50),
    npwpname character varying(100),
    npwpaddress character varying(510),
    city character varying(50),
    region character varying(50),
    postalcode character varying(20),
    country character varying(50),
    phone character varying(100),
    fax character varying(100),
    homepage character varying(100),
    bunitid integer,
    email character varying(100),
    tempobyr integer DEFAULT 0,
    sisahutang numeric(19,4) DEFAULT 0.0000,
    sisahutangjln numeric(19,4),
    iswhs smallint,
    currencyid character varying(20),
    whsid integer,
    idshpl integer DEFAULT 0,
    coa21 integer DEFAULT 18,
    idshpl1 character varying(64),
    islocal smallint,
    isactive smallint,
    created timestamp without time zone,
    createdby character varying(30),
    modified timestamp without time zone,
    modifiedby character varying(30)
);


--
-- Name: mtsupplier_supplierid_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.mtsupplier_supplierid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: mtsupplier_supplierid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.mtsupplier_supplierid_seq OWNED BY public.mtsupplier.supplierid;


--
-- Name: mtunit; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.mtunit (
    unitid integer NOT NULL,
    tipekonversi character varying(10) NOT NULL,
    satuan integer,
    isi integer,
    unit character varying(10) NOT NULL,
    unitname character varying(100) NOT NULL,
    isplat smallint,
    isctl smallint,
    isprodtype smallint,
    isukuran smallint,
    issatuan smallint,
    uppct double precision,
    created timestamp without time zone,
    createdby character varying(30),
    modified timestamp without time zone,
    modifiedby character varying(30),
    bunitid integer,
    coa22 integer
);


--
-- Name: mtunit_unitid_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.mtunit_unitid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: mtunit_unitid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.mtunit_unitid_seq OWNED BY public.mtunit.unitid;


--
-- Name: mtuser; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.mtuser (
    userid integer NOT NULL,
    deptid integer NOT NULL,
    usercode character varying(14) NOT NULL,
    username character varying(50) NOT NULL,
    email character varying(255) NOT NULL,
    email2 character varying(255) NOT NULL,
    upperlevelid integer NOT NULL,
    password character varying(40) NOT NULL,
    levelsecurity integer NOT NULL,
    deleted smallint,
    issales smallint,
    pegawaidivisi integer,
    pegawaibagian integer,
    ugapok numeric(19,4),
    uumakan numeric(19,4),
    utransport numeric(19,4),
    upph numeric(19,4),
    ustatus character varying(100),
    uidno character varying(100),
    uidtype character varying(100),
    utelp1 character varying(100),
    utelp2 character varying(100),
    umtelp character varying(100),
    commission double precision,
    coa23 integer DEFAULT 1,
    signatureid character varying(255) NOT NULL,
    photoid character varying(255) NOT NULL,
    creditlimit numeric(10,0) DEFAULT '0'::numeric NOT NULL,
    created timestamp without time zone,
    createdby character varying(30),
    modified timestamp without time zone,
    modifiedby character varying(30)
);


--
-- Name: mtuser_userid_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.mtuser_userid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: mtuser_userid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.mtuser_userid_seq OWNED BY public.mtuser.userid;


--
-- Name: mtutility; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.mtutility (
    utilityid integer NOT NULL,
    utilityname character varying(255) NOT NULL,
    utilitydesc character varying(255) NOT NULL,
    statusid integer DEFAULT 0 NOT NULL,
    created timestamp without time zone,
    createdby character varying(50) NOT NULL,
    modified timestamp without time zone,
    modifiedby character varying(50) NOT NULL
);


--
-- Name: mtutility_utilityid_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.mtutility_utilityid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: mtutility_utilityid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.mtutility_utilityid_seq OWNED BY public.mtutility.utilityid;


--
-- Name: mtwhs; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.mtwhs (
    whsid integer NOT NULL,
    whscode character varying(12) NOT NULL,
    whsname character varying(100) NOT NULL,
    whsloc character varying(255),
    whstelp character varying(100),
    whsman character varying(100),
    bunitid integer NOT NULL,
    splid integer,
    coa24 integer,
    ishead smallint,
    groupid smallint,
    is_virtual smallint,
    created timestamp without time zone,
    createdby character varying(30),
    modified timestamp without time zone,
    modifiedby character varying(30)
);


--
-- Name: mtwhs_whsid_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.mtwhs_whsid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: mtwhs_whsid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.mtwhs_whsid_seq OWNED BY public.mtwhs.whsid;


--
-- Name: qrypindahanpiutang; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.qrypindahanpiutang (
    invoiceid integer,
    invoiceno character varying(100),
    tgltrx character varying(10),
    paydatemoney timestamp without time zone,
    customerid integer,
    customerinitial character varying(20),
    customername character varying(100),
    jumlah numeric(39,8),
    ket character varying(631),
    tanda character varying(1),
    validpayment integer,
    lunas integer,
    invwhsid integer,
    bunitid integer
);


--
-- Name: qrypindahanstok; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.qrypindahanstok (
    urut character varying(1),
    keterangan character varying(538),
    rcvid integer,
    rcvno character varying(100),
    tgl character varying(10),
    productid integer,
    namabarang character varying(200),
    qtyin numeric(19,4),
    qtyout numeric(19,4),
    status character varying(15),
    rcvwhs integer
);


--
-- Name: qrypiutangperinvoice; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.qrypiutangperinvoice (
    trxid numeric(10,0),
    invoiceid integer,
    invoiceno character varying(100),
    tgltrx character varying(10),
    paydatemoney timestamp without time zone,
    customerid integer,
    customerinitial character varying(20),
    customername character varying(100),
    jumlah numeric(39,8),
    ket character varying(631),
    tanda character varying(1),
    validpayment integer,
    lunas integer,
    invwhsid integer,
    bunitid integer
);


--
-- Name: qrytmphpp; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.qrytmphpp (
    productid integer,
    whsid integer,
    nhpp numeric(65,12),
    stokakhir numeric(41,4)
);


--
-- Name: rt_bilyet; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.rt_bilyet (
    bilyet_pk integer NOT NULL,
    bilyet_no character varying(20) NOT NULL,
    bilyet_date date,
    bilyet_status character varying(5) NOT NULL,
    bilyet_type_id smallint,
    bilyet_person_idf integer NOT NULL,
    bilyet_currency_idf numeric(10,0) NOT NULL,
    bilyet_rate_val numeric(10,0) NOT NULL,
    bilyet_remarks character varying(100) NOT NULL,
    bilyet_total_local_val numeric(10,0) NOT NULL,
    bilyet_total_foreign_val numeric(10,0) NOT NULL,
    created timestamp without time zone,
    createdby character varying(50) NOT NULL,
    modified timestamp without time zone,
    modifiedby character varying(50) NOT NULL
);


--
-- Name: COLUMN rt_bilyet.bilyet_type_id; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.rt_bilyet.bilyet_type_id IS '0;customer;1;supplier';


--
-- Name: rt_bilyet_bilyet_pk_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.rt_bilyet_bilyet_pk_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: rt_bilyet_bilyet_pk_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.rt_bilyet_bilyet_pk_seq OWNED BY public.rt_bilyet.bilyet_pk;


--
-- Name: rt_txrcv; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.rt_txrcv (
    rtid integer NOT NULL,
    rcvidf integer NOT NULL,
    biayabm numeric(10,8) DEFAULT 0.00000000 NOT NULL,
    biayacukai numeric(10,8) DEFAULT 0.00000000 NOT NULL,
    biayappn numeric(10,8) DEFAULT 0.00000000 NOT NULL,
    biayappnbm numeric(10,8) DEFAULT 0.00000000 NOT NULL,
    biayapph numeric(10,8) DEFAULT 0.00000000 NOT NULL,
    biayalain numeric(10,8) DEFAULT 0.00000000 NOT NULL,
    total numeric(10,8) DEFAULT 0.00000000 NOT NULL
);


--
-- Name: TABLE rt_txrcv; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON TABLE public.rt_txrcv IS 'table tengah antara txrcv dengan segala biayanya, mempengaruhi HPP';


--
-- Name: rt_txrcv_rtid_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.rt_txrcv_rtid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: rt_txrcv_rtid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.rt_txrcv_rtid_seq OWNED BY public.rt_txrcv.rtid;


--
-- Name: rt_utility; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.rt_utility (
    rt_utility_pk integer NOT NULL,
    rt_id_h integer DEFAULT 0 NOT NULL,
    rt_id_f integer DEFAULT 0 NOT NULL,
    rt_utility_option smallint,
    rt_utility_status integer DEFAULT 0 NOT NULL,
    rt_utility_val numeric(19,4) DEFAULT 0.0000 NOT NULL,
    created timestamp without time zone,
    createdby character varying(50) NOT NULL,
    modified timestamp without time zone,
    modifiedby character varying(50) NOT NULL
);


--
-- Name: rt_utility_rt_utility_pk_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.rt_utility_rt_utility_pk_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: rt_utility_rt_utility_pk_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.rt_utility_rt_utility_pk_seq OWNED BY public.rt_utility.rt_utility_pk;


--
-- Name: sys_version; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.sys_version (
    daterel timestamp without time zone,
    version character varying(100) NOT NULL,
    aktif smallint,
    rowguid character varying(64) NOT NULL
);


--
-- Name: tmppindahanstok; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.tmppindahanstok (
    urut character varying(1) DEFAULT ''::character varying NOT NULL,
    keterangan character varying(25) DEFAULT ''::character varying NOT NULL,
    rcvid bytea,
    rcvno character varying(1) DEFAULT ''::character varying NOT NULL,
    rcvdate character varying(10),
    productid integer DEFAULT 0 NOT NULL,
    namabarang character varying(200) DEFAULT ''::character varying NOT NULL,
    qtyin numeric(41,4),
    qtyout numeric(45,4),
    status character varying(1) DEFAULT ''::character varying NOT NULL,
    rcvwhs integer DEFAULT 0 NOT NULL
);


--
-- Name: topord; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.topord (
    purchaseid integer NOT NULL,
    purchaseno character varying(4),
    requestid integer,
    purchasedate timestamp without time zone,
    paymentterm integer,
    supplierid integer NOT NULL,
    receivedno character varying(10),
    receiveddate timestamp without time zone
);


--
-- Name: topord_purchaseid_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.topord_purchaseid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: topord_purchaseid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.topord_purchaseid_seq OWNED BY public.topord.purchaseid;


--
-- Name: toreqs; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.toreqs (
    requestid integer NOT NULL,
    requestno character varying(50) NOT NULL,
    requestref character varying(50) NOT NULL,
    requestdate timestamp without time zone,
    userid character varying(50) NOT NULL,
    categoryid integer NOT NULL,
    requestto character varying(50),
    totalqty numeric(10,0) NOT NULL,
    totalamount numeric(10,0) NOT NULL,
    statusid integer NOT NULL,
    finalstatus integer NOT NULL,
    requestnote character varying(50) NOT NULL,
    requestpriority integer NOT NULL,
    locationid integer,
    createddate timestamp without time zone,
    createdby character varying(50) NOT NULL,
    updateddate timestamp without time zone,
    updatedby character varying(50) NOT NULL,
    approvedesc1 character varying(50),
    approvedesc2 character varying(50),
    spvapprovedate timestamp without time zone,
    approvedate1 timestamp without time zone,
    approvedate2 timestamp without time zone,
    reason1 character varying(200),
    reason2 character varying(200) NOT NULL
);


--
-- Name: toreqs_requestid_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.toreqs_requestid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: toreqs_requestid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.toreqs_requestid_seq OWNED BY public.toreqs.requestid;


--
-- Name: toreqsdetl; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.toreqsdetl (
    requestdetailid integer NOT NULL,
    requestid integer NOT NULL,
    itemgroupid integer NOT NULL,
    itemid integer NOT NULL,
    qty integer NOT NULL,
    price numeric(10,0) NOT NULL,
    amount numeric(10,0),
    supplierid integer,
    brandname character varying(50),
    unit character varying(10),
    useddate timestamp without time zone,
    usedfor character varying(50),
    itemtype character varying(50),
    itemnote character varying(100),
    statusid integer NOT NULL,
    approveddate timestamp without time zone,
    approvedby character varying(50) NOT NULL,
    createddate timestamp without time zone,
    createdby character varying(50) NOT NULL,
    updateddate timestamp without time zone,
    updatedby character varying(50) NOT NULL
);


--
-- Name: toreqsdetl_requestdetailid_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.toreqsdetl_requestdetailid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: toreqsdetl_requestdetailid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.toreqsdetl_requestdetailid_seq OWNED BY public.toreqsdetl.requestdetailid;


--
-- Name: tr_logfile; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.tr_logfile (
    log_pk integer NOT NULL,
    log_desc character varying(255) NOT NULL,
    log_comp character varying(50) NOT NULL,
    log_user character varying(25) NOT NULL,
    log_curdate timestamp without time zone,
    log_module character varying(50) NOT NULL,
    log_event character varying(50) NOT NULL
);


--
-- Name: tr_logfile_log_pk_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.tr_logfile_log_pk_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: tr_logfile_log_pk_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.tr_logfile_log_pk_seq OWNED BY public.tr_logfile.log_pk;


--
-- Name: txbiaya; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.txbiaya (
    biayaid integer NOT NULL,
    keterangan character varying(255) NOT NULL,
    tglbiaya timestamp without time zone,
    accountkey_idf integer NOT NULL,
    currency_idf integer DEFAULT 0 NOT NULL,
    kurs_val numeric(19,4) DEFAULT 0.0000 NOT NULL,
    saldo_awal numeric(19,4) DEFAULT 0.0000 NOT NULL,
    debet_val_local numeric(19,4) DEFAULT 0.0000 NOT NULL,
    credit_val_local numeric(19,4) DEFAULT 0.0000 NOT NULL,
    debet_val_foreign numeric(19,4) DEFAULT 0.0000 NOT NULL,
    credit_val_foreign numeric(19,4) DEFAULT 0.0000 NOT NULL,
    saldo_akhir numeric(19,4) DEFAULT 0.0000 NOT NULL,
    biayalain numeric(19,4),
    nilaipenjualan numeric(19,4),
    nilaipembelian numeric(19,4),
    nilailabakotor numeric(19,4),
    biayabatch character varying(30),
    bunitid integer,
    coa25 integer DEFAULT 0 NOT NULL,
    created timestamp without time zone,
    createdby character varying(30),
    modified timestamp without time zone,
    modifiedby character varying(30)
);


--
-- Name: txbiaya_biayaid_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.txbiaya_biayaid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: txbiaya_biayaid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.txbiaya_biayaid_seq OWNED BY public.txbiaya.biayaid;


--
-- Name: txbilyet_detail; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.txbilyet_detail (
    bilyet_d_pk integer NOT NULL,
    bilyet_no character varying(25) NOT NULL,
    bilyet_type smallint,
    currency_idf integer NOT NULL,
    bilyet_bank_idf integer DEFAULT 0 NOT NULL,
    currency_rate numeric(19,4) DEFAULT 0.0000 NOT NULL,
    original_val numeric(19,4) DEFAULT 0.0000 NOT NULL,
    original_allocation_val numeric(19,4) DEFAULT 0.0000 NOT NULL,
    local_val numeric(19,4) DEFAULT 0.0000 NOT NULL,
    local_allocation_val numeric(19,4) DEFAULT 0.0000 NOT NULL,
    bilyet_jenis integer NOT NULL,
    bilyet_remarks character varying(100) NOT NULL,
    bilyet_receive_date date,
    bilyet_person_idf integer NOT NULL,
    bilyet_due_date date,
    bilyet_setor_date date,
    bilyet_cair_date date,
    bilyet_cair smallint,
    bilyet_status integer DEFAULT 0 NOT NULL,
    created timestamp without time zone,
    createdby character varying(50) NOT NULL,
    modified timestamp without time zone,
    modifiedby character varying(50) NOT NULL
);


--
-- Name: COLUMN txbilyet_detail.bilyet_type; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.txbilyet_detail.bilyet_type IS '1;supplier;0;customer';


--
-- Name: txbilyet_detail_bilyet_d_pk_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.txbilyet_detail_bilyet_d_pk_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: txbilyet_detail_bilyet_d_pk_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.txbilyet_detail_bilyet_d_pk_seq OWNED BY public.txbilyet_detail.bilyet_d_pk;


--
-- Name: txinvoice; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.txinvoice (
    invoiceid integer NOT NULL,
    soid integer DEFAULT 0,
    invoiceno character varying(30) NOT NULL,
    invoicedate date,
    customerid integer NOT NULL,
    currinvid character varying(10) NOT NULL,
    deliveryno character varying(30),
    deliverydate date,
    isfacturestd smallint,
    islunas smallint,
    totalpayment numeric(19,4) DEFAULT 0.0000,
    totalretur numeric(19,4) DEFAULT 0.0000,
    bunitid integer NOT NULL,
    beamaterai numeric(19,4) DEFAULT 0.0000,
    bealain numeric(19,4) DEFAULT 0.0000,
    bealaintext character varying(100) DEFAULT 'Potongan Harga'::character varying,
    sinvoiceno character varying(100),
    sinvoicedate date,
    scustomer character varying(100),
    invwhsid integer NOT NULL,
    salesid integer,
    kursjual numeric(19,4) DEFAULT 0.0000,
    kurseval numeric(19,4) DEFAULT 0.0000,
    kursbl numeric(19,4) DEFAULT 0.0000,
    iscancel smallint,
    canceldate timestamp without time zone,
    canceluser character varying(100),
    duedateinv integer DEFAULT 0,
    invdeladdrs character varying(510),
    totalhpp numeric(19,4) DEFAULT 0.0000,
    ispaidkom smallint,
    komamount numeric(19,4) DEFAULT 0.0000,
    komdateambil timestamp without time zone,
    totalsales numeric(19,4) DEFAULT 0.0000,
    dsct numeric(19,4) DEFAULT 0.0000,
    disctvalue numeric(19,4) DEFAULT 0.0000,
    inv_subtotal_after_disc numeric(19,4) DEFAULT 0.0000,
    ppn smallint,
    ppnpctval numeric(19,4) DEFAULT 0.0000,
    ppnvalue numeric(19,4) DEFAULT 0.0000,
    grandtotal numeric(19,4) DEFAULT 0.0000,
    tkonversijual numeric(19,4) DEFAULT 0.0000,
    issppl smallint,
    coa26 integer DEFAULT 0,
    iskys smallint,
    pcinv1 smallint,
    pcinv2 smallint,
    statusinv smallint,
    iskontrabon smallint,
    iscashinv smallint,
    invnote character varying(510),
    payamount numeric(19,4) DEFAULT 0.0000,
    printedby character varying(100),
    printed timestamp without time zone,
    fpajakno character varying(100),
    totalinvq numeric(19,4) DEFAULT 0.0000,
    ketresi character varying(100),
    ekspedisiid integer DEFAULT 0 NOT NULL,
    paramst_sls integer DEFAULT 0 NOT NULL,
    coa_inv integer DEFAULT 0 NOT NULL,
    created timestamp without time zone,
    createdby character varying(100),
    modified timestamp without time zone,
    modifiedby character varying(100)
);


--
-- Name: txinvoice_invoiceid_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.txinvoice_invoiceid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: txinvoice_invoiceid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.txinvoice_invoiceid_seq OWNED BY public.txinvoice.invoiceid;


--
-- Name: txinvoicec; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.txinvoicec (
    invoicecid integer NOT NULL,
    invoiceid integer NOT NULL,
    paymentid integer NOT NULL,
    productid integer DEFAULT 0 NOT NULL,
    ekspedisi_idf integer DEFAULT 0 NOT NULL,
    totalused numeric(19,4) DEFAULT 0.0000 NOT NULL,
    coa27 integer DEFAULT 0 NOT NULL,
    invoicekey character varying(100),
    addremarks character varying(400) NOT NULL,
    namaalias character varying(100) NOT NULL,
    containerno character varying(100) NOT NULL,
    sealno character varying(100) NOT NULL,
    printed timestamp without time zone,
    printedby character varying(50),
    created timestamp without time zone,
    createdby character varying(100) NOT NULL,
    modified timestamp without time zone,
    modifiedby character varying(100) NOT NULL
);


--
-- Name: txinvoicec_invoicecid_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.txinvoicec_invoicecid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: txinvoicec_invoicecid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.txinvoicec_invoicecid_seq OWNED BY public.txinvoicec.invoicecid;


--
-- Name: txinvoiced; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.txinvoiced (
    invoicedid integer NOT NULL,
    sod_idf integer DEFAULT 0 NOT NULL,
    invoiceid character varying(64),
    productid integer NOT NULL,
    qtyinvoice numeric(19,4) DEFAULT 0.0000 NOT NULL,
    uom_idf integer DEFAULT 0 NOT NULL,
    produnit character varying(100),
    discvalued numeric(19,4) DEFAULT 0.0000,
    discpctd numeric(19,4) DEFAULT 0.0000,
    qtycoli character varying(20),
    qtyinvoicek numeric(19,4) DEFAULT 0.0000,
    invslsprice numeric(19,4) DEFAULT 0.0000,
    proddesc character varying(8000),
    coa28 integer DEFAULT 0,
    qtyb numeric(19,4) DEFAULT 0.0000,
    qtybuom character varying(20),
    qtybprice numeric(19,4) DEFAULT 0.0000,
    skuid character varying(200),
    komisiperqty numeric(19,4) DEFAULT 0.0000 NOT NULL,
    hrgawalinv numeric(19,4) DEFAULT 0.0000,
    invd_disc_pct_1 numeric(19,4) DEFAULT 0.0000,
    invd_disc_val_1 numeric(19,4) DEFAULT 0.0000,
    invd_price_after_disc_1 numeric(19,4) DEFAULT 0.0000,
    invd_disc_pct_2 numeric(19,4) DEFAULT 0.0000,
    invd_disc_val_2 numeric(19,4) DEFAULT 0.0000,
    invd_price_after_disc_2 numeric(19,4) DEFAULT 0.0000,
    invd_disc_pct_3 numeric(19,4) DEFAULT 0.0000,
    invd_disc_val_3 numeric(19,4) DEFAULT 0.0000,
    invd_price_after_disc_3 numeric(19,4) DEFAULT 0.0000,
    invd_disc_pct_4 numeric(19,4) DEFAULT 0.0000,
    invd_disc_val_4 numeric(19,4) DEFAULT 0.0000,
    invd_price_after_disc_4 numeric(19,4) DEFAULT 0.0000,
    invd_disc_pct_5 numeric(19,4) DEFAULT 0.0000,
    invd_disc_val_5 numeric(19,4) DEFAULT 0.0000,
    invd_price_after_disc_5 numeric(19,4) DEFAULT 0.0000,
    invd_disc_pct_6 numeric(19,4) DEFAULT 0.0000,
    invd_disc_val_6 numeric(19,4) DEFAULT 0.0000,
    invd_price_after_disc_6 numeric(19,4) DEFAULT 0.0000,
    invd_ppn_pct numeric(19,4) DEFAULT 0.0000,
    invd_ppn_val numeric(19,4) DEFAULT 0.0000,
    invprice numeric(19,4) DEFAULT 0.0000 NOT NULL,
    created timestamp without time zone,
    createdby character varying(100),
    modified timestamp without time zone,
    modifiedby character varying(100)
);


--
-- Name: txinvoiced_invoicedid_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.txinvoiced_invoicedid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: txinvoiced_invoicedid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.txinvoiced_invoicedid_seq OWNED BY public.txinvoiced.invoicedid;


--
-- Name: txpayable; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.txpayable (
    paymentdid integer NOT NULL,
    paymentid integer,
    rcvid integer,
    bilyetguid integer DEFAULT 0 NOT NULL,
    paymentid1 character varying(64),
    rcvid1 character varying(64),
    jenisbayar character varying(510) NOT NULL,
    kurstrx numeric(19,4),
    totalbayar numeric(19,4) DEFAULT 0.0000 NOT NULL,
    oriamount numeric(19,4),
    tkonversibayar numeric(19,4),
    tgljt timestamp without time zone,
    islunaslalu smallint,
    currencyid character varying(10),
    kursbayar numeric(19,4) DEFAULT 0.0000,
    kursharian numeric(19,4),
    kursbayar2 numeric(19,4) DEFAULT 0.0000,
    coa29 integer,
    iscair smallint,
    created timestamp without time zone,
    paytype character varying(20),
    createdby character varying(30),
    modified timestamp without time zone,
    modifiedby character varying(30)
);


--
-- Name: txpayable_paymentdid_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.txpayable_paymentdid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: txpayable_paymentdid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.txpayable_paymentdid_seq OWNED BY public.txpayable.paymentdid;


--
-- Name: txpayment; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.txpayment (
    paymentid integer NOT NULL,
    customerid integer NOT NULL,
    totalpaid numeric(19,4) NOT NULL,
    balancepayment numeric(19,4),
    paymentdate timestamp without time zone,
    paymentno character varying(510) NOT NULL,
    descbank character varying(510) NOT NULL,
    validpayment smallint,
    bunitid integer NOT NULL,
    paymentdatercv timestamp without time zone,
    accountbankid integer,
    ispelunasan smallint,
    islunaslalu smallint,
    nogiro character varying(510),
    created timestamp without time zone,
    createdby character varying(30),
    modified timestamp without time zone,
    modifiedby character varying(30),
    paymentbatch character varying(30),
    whsid integer,
    coa30 integer
);


--
-- Name: txpayment_paymentid_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.txpayment_paymentid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: txpayment_paymentid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.txpayment_paymentid_seq OWNED BY public.txpayment.paymentid;


--
-- Name: txpaymenth; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.txpaymenth (
    paymentid integer NOT NULL,
    paymentno character varying(100) NOT NULL,
    paymentdate date,
    customerid integer NOT NULL,
    kursbayarh numeric(19,4) DEFAULT 0.0000,
    totalpayment numeric(19,4) DEFAULT 0.0000,
    totalpaymentf numeric(19,4) DEFAULT 0.0000,
    isap smallint,
    bunitid integer,
    currencyid character varying(20),
    whsid integer,
    coa31 integer,
    status integer DEFAULT 0,
    pcpay1 smallint,
    created timestamp without time zone,
    paynote character varying(510),
    createdby character varying(30),
    modified timestamp without time zone,
    modifiedby character varying(30)
);


--
-- Name: txpaymenth_paymentid_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.txpaymenth_paymentid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: txpaymenth_paymentid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.txpaymenth_paymentid_seq OWNED BY public.txpaymenth.paymentid;


--
-- Name: txpo; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.txpo (
    poid bigint NOT NULL,
    pono character varying(45),
    podate date,
    ispolokal smallint,
    isprq smallint,
    supplierid integer,
    pocurr character varying(45),
    porate numeric(10,2) DEFAULT 1.00,
    potop integer DEFAULT 0,
    poket1 character varying(255),
    poket2 character varying(255),
    pokontrakno character varying(45),
    pokontrakdate date,
    tipebiaya integer DEFAULT 0,
    po_gross_val numeric(19,4) DEFAULT 0.0000 NOT NULL,
    subtotalpo numeric(19,4) DEFAULT 0.0000,
    discpct numeric(19,4) DEFAULT 0.0000,
    discval numeric(19,4) DEFAULT 0.0000,
    po_subtotal_after_disc numeric(19,4) DEFAULT 0.0000,
    ppnpct numeric(19,4) DEFAULT 0.0000,
    ppnval numeric(19,4) DEFAULT 0.0000,
    gtotalpo numeric(19,4) DEFAULT 0.0000,
    totalkonversipo numeric(19,4) DEFAULT 0.0000,
    local_po_subtotal numeric(19,4) DEFAULT 0.0000 NOT NULL,
    local_po_tax numeric(19,4) DEFAULT 0.0000 NOT NULL,
    local_po_total numeric(19,4) DEFAULT 0.0000 NOT NULL,
    totalbayarpo numeric(19,4) DEFAULT 0.0000,
    totaldppo numeric(19,4) DEFAULT 0.0000,
    totalbiaya numeric(19,4) DEFAULT 0.0000,
    totalkarton numeric(19,4) DEFAULT 0.0000,
    totalvolume numeric(19,4) DEFAULT 0.0000,
    totalberat numeric(19,4) DEFAULT 0.0000,
    statuspo integer DEFAULT 0,
    statuspodel integer DEFAULT 0 NOT NULL,
    bunitid integer DEFAULT 0,
    printed timestamp without time zone,
    printedby character varying(45),
    totalapprove integer DEFAULT 0 NOT NULL,
    approved timestamp without time zone,
    approvedby character varying(45),
    viewed timestamp without time zone,
    viewedby character varying(45),
    isrejected smallint,
    rejected timestamp without time zone,
    rejectedby character varying(50),
    rejectedreason character varying(255),
    requested timestamp without time zone,
    requestedby character varying(255) NOT NULL,
    iscancel smallint,
    cancelled timestamp without time zone,
    cancelledby character varying(45),
    isclosed smallint,
    closed timestamp without time zone,
    closedby character varying(45),
    sendemailnotif integer DEFAULT 0 NOT NULL,
    deliverydate date,
    po_fpajaknorcv character varying(500),
    po_inv_no_supplier character varying(255),
    po_sj_no_supplier character varying(255),
    po_fpajaktglrcv date,
    treceived_val numeric(19,4) DEFAULT 0.0000 NOT NULL,
    tinvoiced_val numeric(19,4) DEFAULT 0.0000 NOT NULL,
    created timestamp without time zone,
    createdby character varying(45),
    modified timestamp without time zone,
    modifiedby character varying(45)
);


--
-- Name: COLUMN txpo.ispolokal; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.txpo.ispolokal IS '1;Impor;0;Lokal';


--
-- Name: txpo_poid_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.txpo_poid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: txpo_poid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.txpo_poid_seq OWNED BY public.txpo.poid;


--
-- Name: txpod; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.txpod (
    podid integer NOT NULL,
    poidh integer,
    productid integer,
    ketbarang character varying(255),
    kettambahan character varying(255),
    unitprodpod integer DEFAULT 0 NOT NULL,
    qtypod numeric(10,2) DEFAULT 0.00,
    qtypodr numeric(10,2) DEFAULT 0.00,
    qtypodi numeric(10,2) DEFAULT 0.00 NOT NULL,
    biayaratepod numeric(19,4) DEFAULT 0.0000,
    biaya2 numeric(19,4) DEFAULT 0.0000,
    biayacurrpod character varying(45),
    kartonpod numeric(19,4) DEFAULT 0.0000,
    volpodm3 numeric(19,4) DEFAULT 0.0000,
    beratpodkg numeric(19,4) DEFAULT 0.0000,
    estpod timestamp without time zone,
    uomid integer DEFAULT 0 NOT NULL,
    stprod integer DEFAULT 0 NOT NULL,
    pricepod numeric(19,4) DEFAULT 0.0000,
    discpctpod numeric(19,4) DEFAULT 0.0000,
    discvalpod numeric(19,4) DEFAULT 0.0000,
    pod_price_after_disc_1 numeric(19,4) DEFAULT 0.0000,
    pod_disc_pct_2 numeric(19,4) DEFAULT 0.0000,
    pod_disc_val_2 numeric(19,4) DEFAULT 0.0000,
    pod_price_after_disc_2 numeric(19,4) DEFAULT 0.0000,
    pod_disc_pct_3 numeric(19,4) DEFAULT 0.0000,
    pod_disc_val_3 numeric(19,4) DEFAULT 0.0000,
    pod_price_after_disc_3 numeric(19,4) DEFAULT 0.0000,
    pod_disc_pct_4 numeric(19,4) DEFAULT 0.0000,
    pod_disc_val_4 numeric(19,4) DEFAULT 0.0000,
    pod_price_after_disc_4 numeric(19,4) DEFAULT 0.0000,
    pod_disc_pct_5 numeric(19,4) DEFAULT 0.0000,
    pod_disc_val_5 numeric(19,4) DEFAULT 0.0000,
    pod_price_after_disc_5 numeric(19,4) DEFAULT 0.0000,
    pod_disc_pct_6 numeric(19,4) DEFAULT 0.0000,
    pod_disc_val_6 numeric(19,4) DEFAULT 0.0000,
    pod_price_after_disc_6 numeric(19,4) DEFAULT 0.0000,
    pod_ppn_pct numeric(19,4) DEFAULT 0.0000,
    pod_ppn_val numeric(19,4) DEFAULT 0.0000,
    pricepoda numeric(19,4) DEFAULT 0.0000,
    created timestamp without time zone,
    createdby character varying(45),
    modified timestamp without time zone,
    modifiedby character varying(45)
);


--
-- Name: COLUMN txpod.qtypodr; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.txpod.qtypodr IS 'qty yang diterima berdasarkan podid';


--
-- Name: txpod_podid_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.txpod_podid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: txpod_podid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.txpod_podid_seq OWNED BY public.txpod.podid;


--
-- Name: txrcv; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.txrcv (
    rcvid integer NOT NULL,
    isretur smallint,
    isreturpo smallint,
    isstockawal smallint,
    istransfer smallint,
    isinvoice smallint,
    trfrefid integer DEFAULT 0 NOT NULL,
    bdp_refid integer DEFAULT 0 NOT NULL,
    rcvno character varying(100) NOT NULL,
    rcvdate date,
    supplierid integer,
    poidh integer DEFAULT 0 NOT NULL,
    currencyid character varying(10) NOT NULL,
    containerid integer,
    rcvwhs integer NOT NULL,
    rcvnote character varying(510),
    customerid integer,
    rcvcurr character varying(10),
    bunitid integer DEFAULT 1 NOT NULL,
    rcvwhsto integer DEFAULT 0 NOT NULL,
    totalrcvq numeric(19,4) DEFAULT 0.0000 NOT NULL,
    iscancel smallint,
    canceluser integer,
    canceldate timestamp without time zone,
    isold smallint,
    apod integer DEFAULT 0,
    islunas smallint,
    totalbayar numeric(19,4) DEFAULT 0.0000,
    kursbeli numeric(19,4) DEFAULT 1.0000,
    kurseval numeric(19,4) DEFAULT 1.0000,
    kursbl numeric(19,4) DEFAULT 1.0000,
    isshpl smallint,
    coa32 integer,
    totalretur numeric(19,4),
    iskys smallint,
    reftrxid character varying(64) DEFAULT '0'::character varying,
    pcrcv1 bigint DEFAULT '0'::bigint NOT NULL,
    pcrcv2 bigint DEFAULT '0'::bigint NOT NULL,
    statusrcv smallint,
    iskontrabon smallint,
    iscashrcv smallint,
    printedby character varying(100),
    printed timestamp without time zone,
    ppnvalrcvh numeric(19,4) DEFAULT 0.0000,
    discvalrcvh numeric(19,4) DEFAULT 0.0000,
    subtotalrcv numeric(19,4) DEFAULT 0.0000,
    totalpotongan numeric(19,4) DEFAULT 0.0000,
    rcv_subtotal_after_disc numeric(19,4) DEFAULT 0.0000,
    ppnvalue numeric(19,4),
    totalrcvm numeric(19,4) DEFAULT 0.0000 NOT NULL,
    grandtotalrcv numeric(19,4) DEFAULT 0.0000,
    tkonversibeli numeric(19,4) DEFAULT 0.0000,
    fpajaknorcv character varying(500),
    fpajaktglrcv date,
    inv_no_supplier character varying(255) NOT NULL,
    sj_no_supplier character varying(255) NOT NULL,
    paramst_pch integer DEFAULT 0 NOT NULL,
    tinvoiced_qty_val numeric(19,4) DEFAULT 0.0000 NOT NULL,
    tinvoiced_jml_val numeric(19,4) DEFAULT 0.0000 NOT NULL,
    created timestamp without time zone,
    createdby character varying(30),
    modified timestamp without time zone,
    modifiedby character varying(30)
);


--
-- Name: COLUMN txrcv.reftrxid; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.txrcv.reftrxid IS 'invoiceid';


--
-- Name: txrcv_rcvid_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.txrcv_rcvid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: txrcv_rcvid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.txrcv_rcvid_seq OWNED BY public.txrcv.rcvid;


--
-- Name: txrcvd; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.txrcvd (
    rcvdid integer NOT NULL,
    poid_d_idf integer DEFAULT 0 NOT NULL,
    rcvid integer NOT NULL,
    rinvoiceid integer DEFAULT 0,
    rinvoicedid integer DEFAULT 0,
    rcvidref integer DEFAULT 0,
    productid integer NOT NULL,
    noteline character varying(8000),
    ketrcv character varying(100),
    uom_idf integer DEFAULT 20 NOT NULL,
    qtyrcv numeric(19,4) DEFAULT 0.0000 NOT NULL,
    qtydus numeric(19,4) DEFAULT 0.0000,
    qtyunitdus numeric(19,4) DEFAULT 0.0000,
    discvalrcv numeric(19,4) DEFAULT 0.0000,
    produnit character varying(100),
    konversircv character varying(10),
    coa33 integer,
    discvalrcvd numeric(19,4) DEFAULT 0.0000,
    skuid character varying(200),
    kursbelid numeric(19,4) DEFAULT 0.0000,
    ongkos numeric(19,4) DEFAULT 0.0000,
    ongkosf numeric(19,4) DEFAULT 0.0000,
    expireddate date,
    hrgawalrcv numeric(19,4) DEFAULT 0.0000,
    hargadasar numeric(19,4) DEFAULT 0.0000,
    rcvd_disc_pct_1 numeric(19,4) DEFAULT 0.0000,
    rcvd_disc_val_1 numeric(19,4) DEFAULT 0.0000,
    rcvd_price_after_disc_1 numeric(19,4) DEFAULT 0.0000,
    rcvd_disc_pct_2 numeric(19,4) DEFAULT 0.0000,
    rcvd_disc_val_2 numeric(19,4) DEFAULT 0.0000,
    rcvd_price_after_disc_2 numeric(19,4) DEFAULT 0.0000,
    rcvd_disc_pct_3 numeric(19,4) DEFAULT 0.0000,
    rcvd_disc_val_3 numeric(19,4) DEFAULT 0.0000,
    rcvd_price_after_disc_3 numeric(19,4) DEFAULT 0.0000,
    rcvd_disc_pct_4 numeric(19,4) DEFAULT 0.0000,
    rcvd_disc_val_4 numeric(19,4) DEFAULT 0.0000,
    rcvd_price_after_disc_4 numeric(19,4) DEFAULT 0.0000,
    rcvd_disc_pct_5 numeric(19,4) DEFAULT 0.0000,
    rcvd_disc_val_5 numeric(19,4) DEFAULT 0.0000,
    rcvd_price_after_disc_5 numeric(19,4) DEFAULT 0.0000,
    rcvd_disc_pct_6 numeric(19,4) DEFAULT 0.0000,
    rcvd_disc_val_6 numeric(19,4) DEFAULT 0.0000,
    rcvd_price_after_disc_6 numeric(19,4) DEFAULT 0.0000,
    rcvd_ppn_pct numeric(19,4) DEFAULT 0.0000,
    rcvd_ppn_val numeric(19,4) DEFAULT 0.0000,
    pricercv numeric(19,4) DEFAULT 0.0000,
    hrgmodal numeric(19,4) DEFAULT 0.0000,
    invprcprice numeric(19,4) DEFAULT 0.0000 NOT NULL,
    invoiced_qty_val numeric(10,2) DEFAULT 0.00 NOT NULL,
    invoiced_val numeric(19,4) DEFAULT 0.0000 NOT NULL,
    created timestamp without time zone,
    createdby character varying(100) DEFAULT 'user'::character varying,
    modified timestamp without time zone,
    modifiedby character varying(100) DEFAULT 'user'::character varying
);


--
-- Name: txrcvd_rcvdid_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.txrcvd_rcvdid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: txrcvd_rcvdid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.txrcvd_rcvdid_seq OWNED BY public.txrcvd.rcvdid;


--
-- Name: txreceivable; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.txreceivable (
    detail_pk integer NOT NULL,
    custid integer NOT NULL,
    invoiceid integer NOT NULL,
    returid integer DEFAULT 0 NOT NULL,
    ispaid smallint,
    totalpiutang numeric(19,4) DEFAULT 0.0000 NOT NULL,
    totalretur numeric(19,4) DEFAULT 0.0000 NOT NULL,
    totaldiscount numeric(19,4) DEFAULT 0.0000 NOT NULL,
    totalbealain numeric(19,4) DEFAULT 0.0000 NOT NULL,
    totalbayar numeric(19,4) DEFAULT 0.0000 NOT NULL,
    isap smallint,
    created timestamp without time zone,
    createdby character varying(50) NOT NULL,
    modified timestamp without time zone,
    modifiedby character varying(50) NOT NULL
);


--
-- Name: txreceivable_detail_pk_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.txreceivable_detail_pk_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: txreceivable_detail_pk_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.txreceivable_detail_pk_seq OWNED BY public.txreceivable.detail_pk;


--
-- Name: txreq_journal; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.txreq_journal (
    req_journal_pk integer NOT NULL,
    req_journal_no character varying(50) NOT NULL,
    req_journal_date date,
    req_journal_status smallint,
    req_journal_keterangan character varying(100) NOT NULL,
    req_journal_accountkey integer DEFAULT 0 NOT NULL,
    req_isstat smallint,
    created timestamp without time zone,
    createdby character varying(50) NOT NULL,
    modified timestamp without time zone,
    modifiedby character varying(50) NOT NULL
);


--
-- Name: txreq_journal_detail; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.txreq_journal_detail (
    req_journal_d_pk integer NOT NULL,
    req_journal_idh integer NOT NULL,
    journal_idh integer NOT NULL,
    created timestamp without time zone,
    createdby character varying(50) NOT NULL,
    modified timestamp without time zone,
    modifiedby character varying(50) NOT NULL
);


--
-- Name: txreq_journal_detail_req_journal_d_pk_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.txreq_journal_detail_req_journal_d_pk_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: txreq_journal_detail_req_journal_d_pk_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.txreq_journal_detail_req_journal_d_pk_seq OWNED BY public.txreq_journal_detail.req_journal_d_pk;


--
-- Name: txreq_journal_req_journal_pk_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.txreq_journal_req_journal_pk_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: txreq_journal_req_journal_pk_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.txreq_journal_req_journal_pk_seq OWNED BY public.txreq_journal.req_journal_pk;


--
-- Name: txsaldopiutang; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.txsaldopiutang (
    periode timestamp without time zone,
    customerid integer NOT NULL,
    saldopiutang numeric(19,4) DEFAULT 0.0000 NOT NULL,
    isap smallint
);


--
-- Name: txsn; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.txsn (
    detailguid character varying(64) NOT NULL,
    headerid character varying(64) NOT NULL,
    productid integer NOT NULL,
    serialnumber character varying(100) NOT NULL,
    flagtrx integer DEFAULT 0 NOT NULL,
    qtysn integer DEFAULT 1 NOT NULL,
    qtysnused smallint DEFAULT '0'::smallint,
    noindex integer DEFAULT 1,
    created timestamp without time zone,
    createdby character varying(30),
    modified timestamp without time zone,
    modifiedby character varying(30),
    refguid character varying(64)
);


--
-- Name: txso; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.txso (
    soid bigint NOT NULL,
    sono character varying(45) NOT NULL,
    sodate date,
    issolokal smallint,
    isreject smallint,
    customerid integer,
    customeralias_so character varying(100) NOT NULL,
    salesid_so integer DEFAULT 0 NOT NULL,
    socurr character varying(45),
    sorate numeric(10,2) DEFAULT 1.00,
    sotop integer DEFAULT 0,
    soket1 character varying(255),
    soket2 character varying(255),
    sokontrakno character varying(45),
    tipebiaya integer DEFAULT 0,
    subtotalso numeric(19,4) DEFAULT 0.0000,
    discpct numeric(19,4) DEFAULT 0.0000,
    discval numeric(19,4) DEFAULT 0.0000,
    so_subtotal_after_disc numeric(19,4) DEFAULT 0.0000,
    ppnpct numeric(19,4) DEFAULT 0.0000,
    ppnval numeric(19,4) DEFAULT 0.0000,
    gtotalso numeric(19,4) DEFAULT 0.0000,
    totalkonversiso numeric(19,4) DEFAULT 0.0000,
    totalbayarso numeric(19,4) DEFAULT 0.0000,
    totaldpso numeric(19,4) DEFAULT 0.0000,
    totalbiaya numeric(19,4) DEFAULT 0.0000,
    totalkarton numeric(19,4) DEFAULT 0.0000,
    totalvolume numeric(19,4) DEFAULT 0.0000,
    totalberat numeric(19,4) DEFAULT 0.0000,
    statusso integer DEFAULT 0,
    bunitid integer DEFAULT 0,
    printed timestamp without time zone,
    printedby character varying(45),
    totalapprove integer DEFAULT 0 NOT NULL,
    approved timestamp without time zone,
    approvedby character varying(45),
    viewed timestamp without time zone,
    viewedby character varying(45),
    isrejected smallint,
    rejected timestamp without time zone,
    rejectedby character varying(50),
    rejectedreason character varying(255),
    iscancel smallint,
    cancelled timestamp without time zone,
    cancelledby character varying(45),
    isclosed smallint,
    closed timestamp without time zone,
    closedby character varying(45),
    sendemailnotif integer DEFAULT 0 NOT NULL,
    tinvoiced_val numeric(19,4) DEFAULT 0.0000 NOT NULL,
    tdelivered_val numeric(19,4) DEFAULT 0.0000 NOT NULL,
    totalcogs numeric(19,4) DEFAULT 0.0000 NOT NULL,
    created timestamp without time zone,
    createdby character varying(45),
    modified timestamp without time zone,
    modifiedby character varying(45)
);


--
-- Name: COLUMN txso.issolokal; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.txso.issolokal IS '0;Lokal;1;Ekspor;2;Sample Lokal;3;Sample Ekspor ';


--
-- Name: txso_soid_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.txso_soid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: txso_soid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.txso_soid_seq OWNED BY public.txso.soid;


--
-- Name: txsod; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.txsod (
    sodid integer NOT NULL,
    soidh integer,
    productid integer,
    ketbarang character varying(255),
    kettambahan character varying(255),
    unitprodsod character varying(45),
    qtysod numeric(10,2) DEFAULT 0.00,
    qtysodr numeric(10,2) DEFAULT 0.00,
    biayaratesod numeric(19,4) DEFAULT 0.0000,
    biaya2 numeric(19,4) DEFAULT 0.0000,
    biayacurrsod character varying(45),
    kartonsod numeric(19,4) DEFAULT 0.0000,
    volsodm3 numeric(19,4) DEFAULT 0.0000,
    beratsodkg numeric(19,4) DEFAULT 0.0000,
    estsod timestamp without time zone,
    uomid integer DEFAULT 0 NOT NULL,
    pricesod numeric(19,4) DEFAULT 0.0000,
    discpctsod numeric(19,4) DEFAULT 0.0000,
    discvalsod numeric(19,4) DEFAULT 0.0000,
    sod_price_after_disc_1 numeric(19,4) DEFAULT 0.0000,
    sod_disc_pct_2 numeric(19,4) DEFAULT 0.0000,
    sod_disc_val_2 numeric(19,4) DEFAULT 0.0000,
    sod_price_after_disc_2 numeric(19,4) DEFAULT 0.0000,
    sod_disc_pct_3 numeric(19,4) DEFAULT 0.0000,
    sod_disc_val_3 numeric(19,4) DEFAULT 0.0000,
    sod_price_after_disc_3 numeric(19,4) DEFAULT 0.0000,
    sod_disc_pct_4 numeric(19,4) DEFAULT 0.0000,
    sod_disc_val_4 numeric(19,4) DEFAULT 0.0000,
    sod_price_after_disc_4 numeric(19,4) DEFAULT 0.0000,
    sod_disc_pct_5 numeric(19,4) DEFAULT 0.0000,
    sod_disc_val_5 numeric(19,4) DEFAULT 0.0000,
    sod_price_after_disc_5 numeric(19,4) DEFAULT 0.0000,
    sod_disc_pct_6 numeric(19,4) DEFAULT 0.0000,
    sod_disc_val_6 numeric(19,4) DEFAULT 0.0000,
    sod_price_after_disc_6 numeric(19,4) DEFAULT 0.0000,
    sod_ppn_pct numeric(19,4) DEFAULT 0.0000,
    sod_ppn_val numeric(19,4) DEFAULT 0.0000,
    pricesoda numeric(19,4) DEFAULT 0.0000,
    harga_cogs numeric(19,4) DEFAULT 0.0000 NOT NULL,
    tgl_cogs date,
    created timestamp without time zone,
    createdby character varying(45),
    modified timestamp without time zone,
    modifiedby character varying(45)
);


--
-- Name: COLUMN txsod.qtysodr; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.txsod.qtysodr IS 'qty yang diterima berdasarkan podid';


--
-- Name: txsod_sodid_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.txsod_sodid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: txsod_sodid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.txsod_sodid_seq OWNED BY public.txsod.sodid;


--
-- Name: txstockadj; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.txstockadj (
    adj_pk integer NOT NULL,
    adj_no character varying(50) NOT NULL,
    adj_date date,
    adj_status character varying(15) NOT NULL,
    whs_idf integer NOT NULL,
    whsto_idf integer DEFAULT 0 NOT NULL,
    istransfer_idf integer DEFAULT 0 NOT NULL,
    istransfer_in smallint,
    ref_transfer_idf integer DEFAULT 0 NOT NULL,
    adj_reasonid integer NOT NULL,
    adj_remarks character varying(100) NOT NULL,
    adj_qty_val numeric(10,2) DEFAULT 0.00 NOT NULL,
    adj_total_val numeric(19,4) DEFAULT 0.0000 NOT NULL,
    adj_refno character varying(100) NOT NULL,
    paramst_inv smallint,
    status_trx smallint,
    is_exc_biaya smallint,
    created timestamp without time zone,
    createdby character varying(50) NOT NULL,
    modified timestamp without time zone,
    modifiedby character varying(50) NOT NULL
);


--
-- Name: txstockadj_adj_pk_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.txstockadj_adj_pk_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: txstockadj_adj_pk_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.txstockadj_adj_pk_seq OWNED BY public.txstockadj.adj_pk;


--
-- Name: txstockadj_detail; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.txstockadj_detail (
    adj_d_pk integer NOT NULL,
    adj_idh integer NOT NULL,
    product_idh integer NOT NULL,
    product_desc character varying(100) NOT NULL,
    uom_idh integer NOT NULL,
    qty_fisik integer DEFAULT 0 NOT NULL,
    adj_qty numeric(10,0) DEFAULT '0'::numeric NOT NULL,
    adj_price numeric(19,4) NOT NULL,
    created timestamp without time zone,
    createdby character varying(50) NOT NULL,
    modified timestamp without time zone,
    modifiedby character varying(50) NOT NULL
);


--
-- Name: COLUMN txstockadj_detail.qty_fisik; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.txstockadj_detail.qty_fisik IS 'qty fisik digudang ybs';


--
-- Name: COLUMN txstockadj_detail.adj_qty; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.txstockadj_detail.adj_qty IS 'qty yg mau diadjust';


--
-- Name: txstockadj_detail_adj_d_pk_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.txstockadj_detail_adj_d_pk_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: txstockadj_detail_adj_d_pk_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.txstockadj_detail_adj_d_pk_seq OWNED BY public.txstockadj_detail.adj_d_pk;


--
-- Name: txstok; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.txstok (
    whsid integer DEFAULT 0,
    productid integer NOT NULL,
    periode timestamp without time zone,
    qtyawal numeric(19,4) NOT NULL,
    qtybeli numeric(19,4) NOT NULL,
    qtyjual numeric(19,4) NOT NULL,
    qtyretur numeric(19,4) NOT NULL,
    qtyadjplus numeric(19,4) DEFAULT 0.0000 NOT NULL,
    qtyadjmin numeric(19,4) DEFAULT 0.0000 NOT NULL,
    jadjplus numeric(19,4) DEFAULT 0.0000 NOT NULL,
    jadjmin numeric(19,4) DEFAULT 0.0000 NOT NULL,
    qtytout numeric(19,4) DEFAULT 0.0000 NOT NULL,
    jtout numeric(19,4) DEFAULT 0.0000 NOT NULL,
    qtytin numeric(19,4) DEFAULT 0.0000 NOT NULL,
    jtin numeric(19,4) DEFAULT 0.0000 NOT NULL,
    qtyakhir numeric(19,4) NOT NULL,
    hpp numeric(19,4),
    created timestamp without time zone,
    createdby character varying(30),
    modified timestamp without time zone,
    modifiedby character varying(30),
    bunitid integer,
    qtyreturbeli numeric(19,4) DEFAULT 0.0000,
    jawal numeric(19,4) DEFAULT 0.0000,
    jbeli numeric(19,4) DEFAULT 0.0000,
    jreturjual numeric(19,4) DEFAULT 0.0000,
    jjual numeric(19,4) DEFAULT 0.0000,
    jreturbeli numeric(19,4) DEFAULT 0.0000,
    jakhir numeric(19,4) DEFAULT 0.0000
);


--
-- Name: txtransfer; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.txtransfer (
    transferid integer NOT NULL,
    transferdate timestamp without time zone,
    transferno character varying(20) NOT NULL,
    trffrom integer NOT NULL,
    trfto integer NOT NULL,
    productid integer NOT NULL,
    qtytrf integer NOT NULL,
    bunitid integer NOT NULL,
    refrcvid integer NOT NULL,
    harga numeric(10,2) DEFAULT 0.00 NOT NULL,
    uom character varying(5) DEFAULT 'PCS'::character varying NOT NULL
);


--
-- Name: txtransfer_transferid_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.txtransfer_transferid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: txtransfer_transferid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.txtransfer_transferid_seq OWNED BY public.txtransfer.transferid;


--
-- Name: accounts primarykey; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.accounts ALTER COLUMN primarykey SET DEFAULT nextval('public.accounts_primarykey_seq'::regclass);


--
-- Name: dtproperties id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.dtproperties ALTER COLUMN id SET DEFAULT nextval('public.dtproperties_id_seq'::regclass);


--
-- Name: exno primarykey; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.exno ALTER COLUMN primarykey SET DEFAULT nextval('public.exno_primarykey_seq'::regclass);


--
-- Name: journal primarykey; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.journal ALTER COLUMN primarykey SET DEFAULT nextval('public.journal_primarykey_seq'::regclass);


--
-- Name: journalentry primarykey; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.journalentry ALTER COLUMN primarykey SET DEFAULT nextval('public.journalentry_primarykey_seq'::regclass);


--
-- Name: moaccs accessid; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.moaccs ALTER COLUMN accessid SET DEFAULT nextval('public.moaccs_accessid_seq'::regclass);


--
-- Name: mocomp companyid; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.mocomp ALTER COLUMN companyid SET DEFAULT nextval('public.mocomp_companyid_seq'::regclass);


--
-- Name: moctgr categoryid; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.moctgr ALTER COLUMN categoryid SET DEFAULT nextval('public.moctgr_categoryid_seq'::regclass);


--
-- Name: modept deptid; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.modept ALTER COLUMN deptid SET DEFAULT nextval('public.modept_deptid_seq'::regclass);


--
-- Name: modivn divisionid; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.modivn ALTER COLUMN divisionid SET DEFAULT nextval('public.modivn_divisionid_seq'::regclass);


--
-- Name: moform formid; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.moform ALTER COLUMN formid SET DEFAULT nextval('public.moform_formid_seq'::regclass);


--
-- Name: molevl levelid; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.molevl ALTER COLUMN levelid SET DEFAULT nextval('public.molevl_levelid_seq'::regclass);


--
-- Name: moloca locationid; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.moloca ALTER COLUMN locationid SET DEFAULT nextval('public.moloca_locationid_seq'::regclass);


--
-- Name: monmbr numberid; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.monmbr ALTER COLUMN numberid SET DEFAULT nextval('public.monmbr_numberid_seq'::regclass);


--
-- Name: mostat statid; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.mostat ALTER COLUMN statid SET DEFAULT nextval('public.mostat_statid_seq'::regclass);


--
-- Name: mosupp supplierid; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.mosupp ALTER COLUMN supplierid SET DEFAULT nextval('public.mosupp_supplierid_seq'::regclass);


--
-- Name: mouser user_pk; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.mouser ALTER COLUMN user_pk SET DEFAULT nextval('public.mouser_user_pk_seq'::regclass);


--
-- Name: mouserloca userlocationid; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.mouserloca ALTER COLUMN userlocationid SET DEFAULT nextval('public.mouserloca_userlocationid_seq'::regclass);


--
-- Name: mtbagian bagianid; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.mtbagian ALTER COLUMN bagianid SET DEFAULT nextval('public.mtbagian_bagianid_seq'::regclass);


--
-- Name: mtbankaccount accountid; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.mtbankaccount ALTER COLUMN accountid SET DEFAULT nextval('public.mtbankaccount_accountid_seq'::regclass);


--
-- Name: mtbussinessunit bunitid; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.mtbussinessunit ALTER COLUMN bunitid SET DEFAULT nextval('public.mtbussinessunit_bunitid_seq'::regclass);


--
-- Name: mtcategorycustomer categoryid; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.mtcategorycustomer ALTER COLUMN categoryid SET DEFAULT nextval('public.mtcategorycustomer_categoryid_seq'::regclass);


--
-- Name: mtcity cityid; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.mtcity ALTER COLUMN cityid SET DEFAULT nextval('public.mtcity_cityid_seq'::regclass);


--
-- Name: mtcurrency currency_pk; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.mtcurrency ALTER COLUMN currency_pk SET DEFAULT nextval('public.mtcurrency_currency_pk_seq'::regclass);


--
-- Name: mtcurrencyd currencydid; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.mtcurrencyd ALTER COLUMN currencydid SET DEFAULT nextval('public.mtcurrencyd_currencydid_seq'::regclass);


--
-- Name: mtcustomer customerid; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.mtcustomer ALTER COLUMN customerid SET DEFAULT nextval('public.mtcustomer_customerid_seq'::regclass);


--
-- Name: mtdivisi divisiid; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.mtdivisi ALTER COLUMN divisiid SET DEFAULT nextval('public.mtdivisi_divisiid_seq'::regclass);


--
-- Name: mtfamilyprod familyid; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.mtfamilyprod ALTER COLUMN familyid SET DEFAULT nextval('public.mtfamilyprod_familyid_seq'::regclass);


--
-- Name: mtgrupcoa primarykey; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.mtgrupcoa ALTER COLUMN primarykey SET DEFAULT nextval('public.mtgrupcoa_primarykey_seq'::regclass);


--
-- Name: mtlevel levelid; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.mtlevel ALTER COLUMN levelid SET DEFAULT nextval('public.mtlevel_levelid_seq'::regclass);


--
-- Name: mtproduct productid; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.mtproduct ALTER COLUMN productid SET DEFAULT nextval('public.mtproduct_productid_seq'::regclass);


--
-- Name: mtproduct_price priceid; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.mtproduct_price ALTER COLUMN priceid SET DEFAULT nextval('public.mtproduct_price_priceid_seq'::regclass);


--
-- Name: mtprovince province_id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.mtprovince ALTER COLUMN province_id SET DEFAULT nextval('public.mtprovince_province_id_seq'::regclass);


--
-- Name: mtregion regionid; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.mtregion ALTER COLUMN regionid SET DEFAULT nextval('public.mtregion_regionid_seq'::regclass);


--
-- Name: mtsalesprice utilityid; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.mtsalesprice ALTER COLUMN utilityid SET DEFAULT nextval('public.mtsalesprice_utilityid_seq'::regclass);


--
-- Name: mtsupplier supplierid; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.mtsupplier ALTER COLUMN supplierid SET DEFAULT nextval('public.mtsupplier_supplierid_seq'::regclass);


--
-- Name: mtunit unitid; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.mtunit ALTER COLUMN unitid SET DEFAULT nextval('public.mtunit_unitid_seq'::regclass);


--
-- Name: mtuser userid; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.mtuser ALTER COLUMN userid SET DEFAULT nextval('public.mtuser_userid_seq'::regclass);


--
-- Name: mtutility utilityid; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.mtutility ALTER COLUMN utilityid SET DEFAULT nextval('public.mtutility_utilityid_seq'::regclass);


--
-- Name: mtwhs whsid; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.mtwhs ALTER COLUMN whsid SET DEFAULT nextval('public.mtwhs_whsid_seq'::regclass);


--
-- Name: rt_bilyet bilyet_pk; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.rt_bilyet ALTER COLUMN bilyet_pk SET DEFAULT nextval('public.rt_bilyet_bilyet_pk_seq'::regclass);


--
-- Name: rt_txrcv rtid; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.rt_txrcv ALTER COLUMN rtid SET DEFAULT nextval('public.rt_txrcv_rtid_seq'::regclass);


--
-- Name: rt_utility rt_utility_pk; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.rt_utility ALTER COLUMN rt_utility_pk SET DEFAULT nextval('public.rt_utility_rt_utility_pk_seq'::regclass);


--
-- Name: topord purchaseid; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.topord ALTER COLUMN purchaseid SET DEFAULT nextval('public.topord_purchaseid_seq'::regclass);


--
-- Name: toreqs requestid; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.toreqs ALTER COLUMN requestid SET DEFAULT nextval('public.toreqs_requestid_seq'::regclass);


--
-- Name: toreqsdetl requestdetailid; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.toreqsdetl ALTER COLUMN requestdetailid SET DEFAULT nextval('public.toreqsdetl_requestdetailid_seq'::regclass);


--
-- Name: tr_logfile log_pk; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.tr_logfile ALTER COLUMN log_pk SET DEFAULT nextval('public.tr_logfile_log_pk_seq'::regclass);


--
-- Name: txbiaya biayaid; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.txbiaya ALTER COLUMN biayaid SET DEFAULT nextval('public.txbiaya_biayaid_seq'::regclass);


--
-- Name: txbilyet_detail bilyet_d_pk; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.txbilyet_detail ALTER COLUMN bilyet_d_pk SET DEFAULT nextval('public.txbilyet_detail_bilyet_d_pk_seq'::regclass);


--
-- Name: txinvoice invoiceid; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.txinvoice ALTER COLUMN invoiceid SET DEFAULT nextval('public.txinvoice_invoiceid_seq'::regclass);


--
-- Name: txinvoicec invoicecid; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.txinvoicec ALTER COLUMN invoicecid SET DEFAULT nextval('public.txinvoicec_invoicecid_seq'::regclass);


--
-- Name: txinvoiced invoicedid; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.txinvoiced ALTER COLUMN invoicedid SET DEFAULT nextval('public.txinvoiced_invoicedid_seq'::regclass);


--
-- Name: txpayable paymentdid; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.txpayable ALTER COLUMN paymentdid SET DEFAULT nextval('public.txpayable_paymentdid_seq'::regclass);


--
-- Name: txpayment paymentid; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.txpayment ALTER COLUMN paymentid SET DEFAULT nextval('public.txpayment_paymentid_seq'::regclass);


--
-- Name: txpaymenth paymentid; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.txpaymenth ALTER COLUMN paymentid SET DEFAULT nextval('public.txpaymenth_paymentid_seq'::regclass);


--
-- Name: txpo poid; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.txpo ALTER COLUMN poid SET DEFAULT nextval('public.txpo_poid_seq'::regclass);


--
-- Name: txpod podid; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.txpod ALTER COLUMN podid SET DEFAULT nextval('public.txpod_podid_seq'::regclass);


--
-- Name: txrcv rcvid; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.txrcv ALTER COLUMN rcvid SET DEFAULT nextval('public.txrcv_rcvid_seq'::regclass);


--
-- Name: txrcvd rcvdid; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.txrcvd ALTER COLUMN rcvdid SET DEFAULT nextval('public.txrcvd_rcvdid_seq'::regclass);


--
-- Name: txreceivable detail_pk; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.txreceivable ALTER COLUMN detail_pk SET DEFAULT nextval('public.txreceivable_detail_pk_seq'::regclass);


--
-- Name: txreq_journal req_journal_pk; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.txreq_journal ALTER COLUMN req_journal_pk SET DEFAULT nextval('public.txreq_journal_req_journal_pk_seq'::regclass);


--
-- Name: txreq_journal_detail req_journal_d_pk; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.txreq_journal_detail ALTER COLUMN req_journal_d_pk SET DEFAULT nextval('public.txreq_journal_detail_req_journal_d_pk_seq'::regclass);


--
-- Name: txso soid; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.txso ALTER COLUMN soid SET DEFAULT nextval('public.txso_soid_seq'::regclass);


--
-- Name: txsod sodid; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.txsod ALTER COLUMN sodid SET DEFAULT nextval('public.txsod_sodid_seq'::regclass);


--
-- Name: txstockadj adj_pk; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.txstockadj ALTER COLUMN adj_pk SET DEFAULT nextval('public.txstockadj_adj_pk_seq'::regclass);


--
-- Name: txstockadj_detail adj_d_pk; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.txstockadj_detail ALTER COLUMN adj_d_pk SET DEFAULT nextval('public.txstockadj_detail_adj_d_pk_seq'::regclass);


--
-- Name: txtransfer transferid; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.txtransfer ALTER COLUMN transferid SET DEFAULT nextval('public.txtransfer_transferid_seq'::regclass);


--
-- Name: accounts idx_36635_primary; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.accounts
    ADD CONSTRAINT idx_36635_primary PRIMARY KEY (primarykey);


--
-- Name: dtproperties idx_36649_primary; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.dtproperties
    ADD CONSTRAINT idx_36649_primary PRIMARY KEY (id, property);


--
-- Name: exno idx_36657_primary; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.exno
    ADD CONSTRAINT idx_36657_primary PRIMARY KEY (primarykey);


--
-- Name: gninit idx_36661_primary; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.gninit
    ADD CONSTRAINT idx_36661_primary PRIMARY KEY (initname, coa2);


--
-- Name: journal idx_36666_primary; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.journal
    ADD CONSTRAINT idx_36666_primary PRIMARY KEY (primarykey);


--
-- Name: journalentry idx_36678_primary; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.journalentry
    ADD CONSTRAINT idx_36678_primary PRIMARY KEY (primarykey);


--
-- Name: moaccs idx_36686_primary; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.moaccs
    ADD CONSTRAINT idx_36686_primary PRIMARY KEY (accessid);


--
-- Name: mocomp idx_36691_primary; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.mocomp
    ADD CONSTRAINT idx_36691_primary PRIMARY KEY (companyid);


--
-- Name: moctgr idx_36703_primary; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.moctgr
    ADD CONSTRAINT idx_36703_primary PRIMARY KEY (categoryid);


--
-- Name: modept idx_36708_primary; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.modept
    ADD CONSTRAINT idx_36708_primary PRIMARY KEY (deptid);


--
-- Name: modivn idx_36715_primary; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.modivn
    ADD CONSTRAINT idx_36715_primary PRIMARY KEY (divisionid);


--
-- Name: moform idx_36720_primary; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.moform
    ADD CONSTRAINT idx_36720_primary PRIMARY KEY (formid);


--
-- Name: molevl idx_36729_primary; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.molevl
    ADD CONSTRAINT idx_36729_primary PRIMARY KEY (levelid);


--
-- Name: moloca idx_36734_primary; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.moloca
    ADD CONSTRAINT idx_36734_primary PRIMARY KEY (locationid);


--
-- Name: monmbr idx_36741_primary; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.monmbr
    ADD CONSTRAINT idx_36741_primary PRIMARY KEY (numberid);


--
-- Name: mostat idx_36749_primary; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.mostat
    ADD CONSTRAINT idx_36749_primary PRIMARY KEY (statid);


--
-- Name: mosupp idx_36754_primary; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.mosupp
    ADD CONSTRAINT idx_36754_primary PRIMARY KEY (supplierid);


--
-- Name: mouser idx_36759_primary; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.mouser
    ADD CONSTRAINT idx_36759_primary PRIMARY KEY (user_pk);


--
-- Name: mouserloca idx_36769_primary; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.mouserloca
    ADD CONSTRAINT idx_36769_primary PRIMARY KEY (userlocationid);


--
-- Name: mtbagian idx_36774_primary; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.mtbagian
    ADD CONSTRAINT idx_36774_primary PRIMARY KEY (bagianid);


--
-- Name: mtbankaccount idx_36782_primary; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.mtbankaccount
    ADD CONSTRAINT idx_36782_primary PRIMARY KEY (accountid);


--
-- Name: mtbussinessunit idx_36789_primary; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.mtbussinessunit
    ADD CONSTRAINT idx_36789_primary PRIMARY KEY (bunitid);


--
-- Name: mtcategorycustomer idx_36794_primary; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.mtcategorycustomer
    ADD CONSTRAINT idx_36794_primary PRIMARY KEY (categoryid);


--
-- Name: mtcity idx_36799_primary; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.mtcity
    ADD CONSTRAINT idx_36799_primary PRIMARY KEY (cityid);


--
-- Name: mtcurrency idx_36804_primary; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.mtcurrency
    ADD CONSTRAINT idx_36804_primary PRIMARY KEY (currency_pk);


--
-- Name: mtcurrencyd idx_36809_primary; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.mtcurrencyd
    ADD CONSTRAINT idx_36809_primary PRIMARY KEY (currencydid);


--
-- Name: mtcustomer idx_36815_primary; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.mtcustomer
    ADD CONSTRAINT idx_36815_primary PRIMARY KEY (customerid);


--
-- Name: mtdivisi idx_36833_primary; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.mtdivisi
    ADD CONSTRAINT idx_36833_primary PRIMARY KEY (divisiid);


--
-- Name: mtfamilyprod idx_36838_primary; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.mtfamilyprod
    ADD CONSTRAINT idx_36838_primary PRIMARY KEY (familyid);


--
-- Name: mtgrupcoa idx_36848_primary; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.mtgrupcoa
    ADD CONSTRAINT idx_36848_primary PRIMARY KEY (primarykey);


--
-- Name: mtlevel idx_36853_primary; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.mtlevel
    ADD CONSTRAINT idx_36853_primary PRIMARY KEY (levelid);


--
-- Name: mtproduct idx_36858_primary; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.mtproduct
    ADD CONSTRAINT idx_36858_primary PRIMARY KEY (productid);


--
-- Name: mtproduct_price idx_36884_primary; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.mtproduct_price
    ADD CONSTRAINT idx_36884_primary PRIMARY KEY (priceid);


--
-- Name: mtprovince idx_36899_primary; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.mtprovince
    ADD CONSTRAINT idx_36899_primary PRIMARY KEY (province_id);


--
-- Name: mtregion idx_36904_primary; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.mtregion
    ADD CONSTRAINT idx_36904_primary PRIMARY KEY (regionid);


--
-- Name: mtsalesprice idx_36909_primary; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.mtsalesprice
    ADD CONSTRAINT idx_36909_primary PRIMARY KEY (utilityid);


--
-- Name: mtsupplier idx_36921_primary; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.mtsupplier
    ADD CONSTRAINT idx_36921_primary PRIMARY KEY (supplierid);


--
-- Name: mtunit idx_36932_primary; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.mtunit
    ADD CONSTRAINT idx_36932_primary PRIMARY KEY (unitid);


--
-- Name: mtuser idx_36937_primary; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.mtuser
    ADD CONSTRAINT idx_36937_primary PRIMARY KEY (userid);


--
-- Name: mtutility idx_36946_primary; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.mtutility
    ADD CONSTRAINT idx_36946_primary PRIMARY KEY (utilityid);


--
-- Name: mtwhs idx_36954_primary; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.mtwhs
    ADD CONSTRAINT idx_36954_primary PRIMARY KEY (whsid);


--
-- Name: rt_bilyet idx_36979_primary; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.rt_bilyet
    ADD CONSTRAINT idx_36979_primary PRIMARY KEY (bilyet_pk);


--
-- Name: rt_txrcv idx_36984_primary; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.rt_txrcv
    ADD CONSTRAINT idx_36984_primary PRIMARY KEY (rtid);


--
-- Name: rt_utility idx_36996_primary; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.rt_utility
    ADD CONSTRAINT idx_36996_primary PRIMARY KEY (rt_utility_pk);


--
-- Name: topord idx_37020_primary; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.topord
    ADD CONSTRAINT idx_37020_primary PRIMARY KEY (purchaseid);


--
-- Name: toreqs idx_37025_primary; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.toreqs
    ADD CONSTRAINT idx_37025_primary PRIMARY KEY (requestid);


--
-- Name: toreqsdetl idx_37032_primary; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.toreqsdetl
    ADD CONSTRAINT idx_37032_primary PRIMARY KEY (requestdetailid);


--
-- Name: tr_logfile idx_37037_primary; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.tr_logfile
    ADD CONSTRAINT idx_37037_primary PRIMARY KEY (log_pk);


--
-- Name: txbiaya idx_37042_primary; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.txbiaya
    ADD CONSTRAINT idx_37042_primary PRIMARY KEY (biayaid);


--
-- Name: txbilyet_detail idx_37056_primary; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.txbilyet_detail
    ADD CONSTRAINT idx_37056_primary PRIMARY KEY (bilyet_d_pk);


--
-- Name: txinvoice idx_37068_primary; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.txinvoice
    ADD CONSTRAINT idx_37068_primary PRIMARY KEY (invoiceid);


--
-- Name: txinvoicec idx_37101_primary; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.txinvoicec
    ADD CONSTRAINT idx_37101_primary PRIMARY KEY (invoicecid);


--
-- Name: txinvoiced idx_37112_primary; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.txinvoiced
    ADD CONSTRAINT idx_37112_primary PRIMARY KEY (invoicedid);


--
-- Name: txpayable idx_37152_primary; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.txpayable
    ADD CONSTRAINT idx_37152_primary PRIMARY KEY (paymentdid);


--
-- Name: txpayment idx_37163_primary; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.txpayment
    ADD CONSTRAINT idx_37163_primary PRIMARY KEY (paymentid);


--
-- Name: txpaymenth idx_37170_primary; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.txpaymenth
    ADD CONSTRAINT idx_37170_primary PRIMARY KEY (paymentid);


--
-- Name: txpo idx_37181_primary; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.txpo
    ADD CONSTRAINT idx_37181_primary PRIMARY KEY (poid);


--
-- Name: txpod idx_37216_primary; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.txpod
    ADD CONSTRAINT idx_37216_primary PRIMARY KEY (podid);


--
-- Name: txrcv idx_37256_primary; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.txrcv
    ADD CONSTRAINT idx_37256_primary PRIMARY KEY (rcvid);


--
-- Name: txrcvd idx_37288_primary; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.txrcvd
    ADD CONSTRAINT idx_37288_primary PRIMARY KEY (rcvdid);


--
-- Name: txreceivable idx_37337_primary; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.txreceivable
    ADD CONSTRAINT idx_37337_primary PRIMARY KEY (detail_pk);


--
-- Name: txreq_journal idx_37348_primary; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.txreq_journal
    ADD CONSTRAINT idx_37348_primary PRIMARY KEY (req_journal_pk);


--
-- Name: txreq_journal_detail idx_37354_primary; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.txreq_journal_detail
    ADD CONSTRAINT idx_37354_primary PRIMARY KEY (req_journal_d_pk);


--
-- Name: txsn idx_37362_primary; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.txsn
    ADD CONSTRAINT idx_37362_primary PRIMARY KEY (detailguid);


--
-- Name: txso idx_37370_primary; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.txso
    ADD CONSTRAINT idx_37370_primary PRIMARY KEY (soid);


--
-- Name: txsod idx_37402_primary; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.txsod
    ADD CONSTRAINT idx_37402_primary PRIMARY KEY (sodid);


--
-- Name: txstockadj idx_37440_primary; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.txstockadj
    ADD CONSTRAINT idx_37440_primary PRIMARY KEY (adj_pk);


--
-- Name: txstockadj_detail idx_37450_primary; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.txstockadj_detail
    ADD CONSTRAINT idx_37450_primary PRIMARY KEY (adj_d_pk);


--
-- Name: txtransfer idx_37476_primary; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.txtransfer
    ADD CONSTRAINT idx_37476_primary PRIMARY KEY (transferid);


--
-- Name: idx_36635_ix_accounts; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX idx_36635_ix_accounts ON public.accounts USING btree (code);


--
-- Name: idx_36657_ix_exno; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX idx_36657_ix_exno ON public.exno USING btree (trxtype, trxno);


--
-- Name: idx_36666_ix_journal; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX idx_36666_ix_journal ON public.journal USING btree (code);


--
-- Name: idx_36678_journalkey; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX idx_36678_journalkey ON public.journalentry USING btree (journalkey, sequence, accountkey, debetcredit, descriptions);


--
-- Name: idx_36686_x1; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX idx_36686_x1 ON public.moaccs USING btree (formid, levelid);


--
-- Name: idx_36703_categoryname; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX idx_36703_categoryname ON public.moctgr USING btree (categoryname);


--
-- Name: idx_36708_x1; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX idx_36708_x1 ON public.modept USING btree (deptname);


--
-- Name: idx_36715_divisionname; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX idx_36715_divisionname ON public.modivn USING btree (divisionname);


--
-- Name: idx_36720_x1; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX idx_36720_x1 ON public.moform USING btree (formname);


--
-- Name: idx_36729_levelname; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX idx_36729_levelname ON public.molevl USING btree (levelname);


--
-- Name: idx_36734_locationname; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX idx_36734_locationname ON public.moloca USING btree (locationname);


--
-- Name: idx_36749_statusname; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX idx_36749_statusname ON public.mostat USING btree (statusname);


--
-- Name: idx_36759_x1; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX idx_36759_x1 ON public.mouser USING btree (userid);


--
-- Name: idx_36769_x1; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX idx_36769_x1 ON public.mouserloca USING btree (userid, locationid);


--
-- Name: idx_36774_ix_mtbagian; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX idx_36774_ix_mtbagian ON public.mtbagian USING btree (divisiid, bagianname);


--
-- Name: idx_36778_ix_mtbahasa; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX idx_36778_ix_mtbahasa ON public.mtbahasa USING btree (kodebhs, namabhs, ketbhs);


--
-- Name: idx_36782_ix_mtaccount; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX idx_36782_ix_mtaccount ON public.mtbankaccount USING btree (accountname, accountbankname, accountcurrency);


--
-- Name: idx_36789_ix_mtbussinessunit; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX idx_36789_ix_mtbussinessunit ON public.mtbussinessunit USING btree (bunitname, buinit);


--
-- Name: idx_36794_ix_mtcategorycustomer; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX idx_36794_ix_mtcategorycustomer ON public.mtcategorycustomer USING btree (categoryname);


--
-- Name: idx_36799_ix_mtcity; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX idx_36799_ix_mtcity ON public.mtcity USING btree (cityname, citycountry);


--
-- Name: idx_36804_x1; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX idx_36804_x1 ON public.mtcurrency USING btree (currencyid);


--
-- Name: idx_36809_x1; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX idx_36809_x1 ON public.mtcurrencyd USING btree (currency_idf, currencydate);


--
-- Name: idx_36815_ix_mtcustomer; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX idx_36815_ix_mtcustomer ON public.mtcustomer USING btree (customername);


--
-- Name: idx_36833_ix_mtdivisi; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX idx_36833_ix_mtdivisi ON public.mtdivisi USING btree (divisiname);


--
-- Name: idx_36838_x1; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX idx_36838_x1 ON public.mtfamilyprod USING btree (productfamily);


--
-- Name: idx_36842_ix_mtformcontrol; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX idx_36842_ix_mtformcontrol ON public.mtformcontrol USING btree (formname, controlname, controltype, kodebahasa, judulctrl);


--
-- Name: idx_36848_x1; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX idx_36848_x1 ON public.mtgrupcoa USING btree (groupname);


--
-- Name: idx_36858_ix_mtproduct; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX idx_36858_ix_mtproduct ON public.mtproduct USING btree (productname);


--
-- Name: idx_36884_x1; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX idx_36884_x1 ON public.mtproduct_price USING btree (productid, regionid, jeniskirim);


--
-- Name: idx_36904_ix_mtregion; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX idx_36904_ix_mtregion ON public.mtregion USING btree (cityid, regionname);


--
-- Name: idx_36909_ix_mtsalesprice; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX idx_36909_ix_mtsalesprice ON public.mtsalesprice USING btree (productid, periode, harga, idprice, utility1, utility2, customerid, trxid, trxidout);


--
-- Name: idx_36921_ix_mtsupplier; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX idx_36921_ix_mtsupplier ON public.mtsupplier USING btree (companyname, bunitid);


--
-- Name: idx_36932_ix_mtunit; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX idx_36932_ix_mtunit ON public.mtunit USING btree (unit, tipekonversi, satuan, isi, unitname);


--
-- Name: idx_36937_x1; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX idx_36937_x1 ON public.mtuser USING btree (usercode);


--
-- Name: idx_36946_x1; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX idx_36946_x1 ON public.mtutility USING btree (utilityname);


--
-- Name: idx_36954_ix_mtwhs; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX idx_36954_ix_mtwhs ON public.mtwhs USING btree (whsname);


--
-- Name: idx_36996_x1; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX idx_36996_x1 ON public.rt_utility USING btree (rt_id_h, rt_id_f, rt_utility_status);


--
-- Name: idx_37004_index_1060198827; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX idx_37004_index_1060198827 ON public.sys_version USING btree (rowguid);


--
-- Name: idx_37004_ix_sys_version; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX idx_37004_ix_sys_version ON public.sys_version USING btree (daterel, version);


--
-- Name: idx_37004_rowguid; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX idx_37004_rowguid ON public.sys_version USING btree (rowguid);


--
-- Name: idx_37042_ix_txbiaya; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX idx_37042_ix_txbiaya ON public.txbiaya USING btree (tglbiaya, accountkey_idf, bunitid, currency_idf);


--
-- Name: idx_37068_ix_txinvoice_1; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX idx_37068_ix_txinvoice_1 ON public.txinvoice USING btree (invoiceno, invoicedate);


--
-- Name: idx_37101_ix_txinvoicec; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX idx_37101_ix_txinvoicec ON public.txinvoicec USING btree (invoiceid, paymentid, productid);


--
-- Name: idx_37112_ixinvd; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX idx_37112_ixinvd ON public.txinvoiced USING btree (invoiceid, productid);


--
-- Name: idx_37152_ix_txpayable; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX idx_37152_ix_txpayable ON public.txpayable USING btree (jenisbayar, rcvid, paymentid);


--
-- Name: idx_37170_ix_txpaymenth; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX idx_37170_ix_txpaymenth ON public.txpaymenth USING btree (paymentno, paymentdate, customerid);


--
-- Name: idx_37216_podid_unique; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX idx_37216_podid_unique ON public.txpod USING btree (podid);


--
-- Name: idx_37216_x1; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX idx_37216_x1 ON public.txpod USING btree (poidh, productid);


--
-- Name: idx_37256_ix_txrcv; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX idx_37256_ix_txrcv ON public.txrcv USING btree (rcvno, rcvdate, rcvwhs, customerid, rcvcurr, supplierid);


--
-- Name: idx_37288_ix_txrcvd; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX idx_37288_ix_txrcvd ON public.txrcvd USING btree (rcvid, productid, rinvoiceid, rinvoicedid, rcvidref);


--
-- Name: idx_37337_x1; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX idx_37337_x1 ON public.txreceivable USING btree (invoiceid, custid);


--
-- Name: idx_37348_x1; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX idx_37348_x1 ON public.txreq_journal USING btree (req_journal_no);


--
-- Name: idx_37354_x1; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX idx_37354_x1 ON public.txreq_journal_detail USING btree (req_journal_idh, journal_idh);


--
-- Name: idx_37358_ix_txsaldopiutang; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX idx_37358_ix_txsaldopiutang ON public.txsaldopiutang USING btree (customerid, periode);


--
-- Name: idx_37362_detailguid; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX idx_37362_detailguid ON public.txsn USING btree (detailguid);


--
-- Name: idx_37362_headerid; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX idx_37362_headerid ON public.txsn USING btree (headerid);


--
-- Name: idx_37362_refguid; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX idx_37362_refguid ON public.txsn USING btree (refguid);


--
-- Name: idx_37402_podid_unique; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX idx_37402_podid_unique ON public.txsod USING btree (sodid);


--
-- Name: idx_37402_x1; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX idx_37402_x1 ON public.txsod USING btree (soidh, productid);


--
-- Name: idx_37440_x1; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX idx_37440_x1 ON public.txstockadj USING btree (adj_no);


--
-- Name: idx_37450_x1; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX idx_37450_x1 ON public.txstockadj_detail USING btree (adj_idh, product_idh);


--
-- Name: idx_37456_ix_txstok; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX idx_37456_ix_txstok ON public.txstok USING btree (productid, periode);


--
-- Name: idx_37476_ix_txtransfer; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX idx_37476_ix_txtransfer ON public.txtransfer USING btree (transferdate, trffrom, trfto, transferno);


--
-- PostgreSQL database dump complete
--

\unrestrict O8kGVwrX6z71XI64OfHDIhrJ6kxJg9JsfZICCfQ5X5KTuLoVA3q3D2ruPBCkPg9

