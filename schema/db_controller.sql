--
-- PostgreSQL database dump
--

\restrict peoEPnCxt1oiWrdhdcNAafnoqwtjcVKKEPr8DCCxLs4WPC4rxJeEP0kEzWhqzN4

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


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: tr_control; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.tr_control (
    db_code character varying(100) NOT NULL,
    showtext character varying(255)
);


--
-- Name: tr_control idx_37690_primary; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.tr_control
    ADD CONSTRAINT idx_37690_primary PRIMARY KEY (db_code);


--
-- PostgreSQL database dump complete
--

\unrestrict peoEPnCxt1oiWrdhdcNAafnoqwtjcVKKEPr8DCCxLs4WPC4rxJeEP0kEzWhqzN4

