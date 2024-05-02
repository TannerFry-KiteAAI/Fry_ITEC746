--
-- PostgreSQL database dump
--

-- Dumped from database version 16.1
-- Dumped by pg_dump version 16.1

-- Started on 2024-05-01 20:10:41

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 7 (class 2615 OID 24627)
-- Name: fry; Type: SCHEMA; Schema: -; Owner: -
--

DROP SCHEMA IF EXISTS fry CASCADE;
CREATE SCHEMA fry;


--
-- TOC entry 4898 (class 0 OID 0)
-- Dependencies: 7
-- Name: SCHEMA fry; Type: COMMENT; Schema: -; Owner: -
--

COMMENT ON SCHEMA fry IS 'Potential improvements to this schema: Create an order style checkout table. Functions for handling checkouts by item types. Default due date for media that does not have a set type';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 222 (class 1259 OID 24660)
-- Name: client; Type: TABLE; Schema: fry; Owner: -
--

CREATE TABLE fry.client (
    cid uuid NOT NULL,
    first_name character varying NOT NULL,
    last_name character varying NOT NULL,
    street_address character varying NOT NULL,
    postal integer,
    phone character varying,
    email character varying NOT NULL,
    pswd character varying NOT NULL
);


--
-- TOC entry 4899 (class 0 OID 0)
-- Dependencies: 222
-- Name: TABLE client; Type: COMMENT; Schema: fry; Owner: -
--

COMMENT ON TABLE fry.client IS 'This table stores client content information. Phone number and email is used to login for online account management.';


--
-- TOC entry 224 (class 1259 OID 24688)
-- Name: holds; Type: TABLE; Schema: fry; Owner: -
--

CREATE TABLE fry.holds (
    holdid uuid NOT NULL,
    mediaid uuid,
    clientid uuid,
    holddate date NOT NULL,
    holdqueue integer NOT NULL
);


--
-- TOC entry 4900 (class 0 OID 0)
-- Dependencies: 224
-- Name: TABLE holds; Type: COMMENT; Schema: fry; Owner: -
--

COMMENT ON TABLE fry.holds IS 'A joining table to store a record of what media is on hold and to whom. Multiple people can place a hold on a piece of media';


--
-- TOC entry 223 (class 1259 OID 24671)
-- Name: loans; Type: TABLE; Schema: fry; Owner: -
--

CREATE TABLE fry.loans (
    checkid uuid NOT NULL,
    mediaid uuid,
    clientid uuid,
    dateout date NOT NULL,
    datedue date NOT NULL
);


--
-- TOC entry 4901 (class 0 OID 0)
-- Dependencies: 223
-- Name: TABLE loans; Type: COMMENT; Schema: fry; Owner: -
--

COMMENT ON TABLE fry.loans IS 'A joining table to store a record of what media has been checked out to whom. Each media can only be checked out to a single client.';


--
-- TOC entry 219 (class 1259 OID 24628)
-- Name: location; Type: TABLE; Schema: fry; Owner: -
--

CREATE TABLE fry.location (
    locid integer NOT NULL,
    location_name character varying NOT NULL
);


--
-- TOC entry 4902 (class 0 OID 0)
-- Dependencies: 219
-- Name: TABLE location; Type: COMMENT; Schema: fry; Owner: -
--

COMMENT ON TABLE fry.location IS 'A simple table to store location identifiers for cataloging';


--
-- TOC entry 221 (class 1259 OID 24642)
-- Name: media; Type: TABLE; Schema: fry; Owner: -
--

CREATE TABLE fry.media (
    mid uuid NOT NULL,
    title character varying NOT NULL,
    dewey double precision NOT NULL,
    loc integer NOT NULL,
    medtype integer,
    cancheckout boolean DEFAULT true
);


--
-- TOC entry 4903 (class 0 OID 0)
-- Dependencies: 221
-- Name: TABLE media; Type: COMMENT; Schema: fry; Owner: -
--

COMMENT ON TABLE fry.media IS 'This table stores media items for the library. Dewey and Location are required for cataloging. Type is not';


--
-- TOC entry 220 (class 1259 OID 24635)
-- Name: type; Type: TABLE; Schema: fry; Owner: -
--

CREATE TABLE fry.type (
    typeid integer NOT NULL,
    media_type character varying NOT NULL,
    checkout_time integer NOT NULL
);


--
-- TOC entry 4904 (class 0 OID 0)
-- Dependencies: 220
-- Name: TABLE type; Type: COMMENT; Schema: fry; Owner: -
--

COMMENT ON TABLE fry.type IS 'A simple table to store media type identifiers. Identifies length of checkout time.';


--
-- TOC entry 4890 (class 0 OID 24660)
-- Dependencies: 222
-- Data for Name: client; Type: TABLE DATA; Schema: fry; Owner: -
--

INSERT INTO fry.client VALUES ('7c3a9469-2fef-43d2-a9f4-262458a5fa37', 'Fox', 'Mulder', '1313 Spooky Drive', 66045, '785-542-7892', 'ibelieve92@hotmail.com', 'aliens');
INSERT INTO fry.client VALUES ('aa4309bc-1cb8-4d12-8091-05c85ffd2ee2', 'Billy', 'Mays', '2450 Eagle Road', 66047, '456-937-7830', 'oxi.clean@mail.com', 'K@B00m');
INSERT INTO fry.client VALUES ('64034eb2-2e79-4a91-9946-a91b45e57b0f', 'Tanner', 'Fry', '1122 Maple Lane', 66049, '984-125-5432', 'tannermail@mail.com', 'sqlpass1234');


--
-- TOC entry 4892 (class 0 OID 24688)
-- Dependencies: 224
-- Data for Name: holds; Type: TABLE DATA; Schema: fry; Owner: -
--

INSERT INTO fry.holds VALUES ('4fb6b9cd-3e11-4e8a-ab13-50004b279cb3', 'ccb3a386-f36b-44d2-8940-74f7b6c52ad9', 'aa4309bc-1cb8-4d12-8091-05c85ffd2ee2', '2024-05-01', 0);


--
-- TOC entry 4891 (class 0 OID 24671)
-- Dependencies: 223
-- Data for Name: loans; Type: TABLE DATA; Schema: fry; Owner: -
--

INSERT INTO fry.loans VALUES ('b2ef042c-d9ba-4bab-a3b6-99247731dadd', '8fab3b14-44b0-4dd1-9f9d-c6eec493de91', '64034eb2-2e79-4a91-9946-a91b45e57b0f', '2024-05-01', '2024-05-15');
INSERT INTO fry.loans VALUES ('0dc345f1-4408-43f8-9b89-e5796c59e43d', '7efa111b-e3b6-447d-9b40-3fd770aeb26b', '64034eb2-2e79-4a91-9946-a91b45e57b0f', '2024-05-01', '2024-05-15');


--
-- TOC entry 4887 (class 0 OID 24628)
-- Dependencies: 219
-- Data for Name: location; Type: TABLE DATA; Schema: fry; Owner: -
--

INSERT INTO fry.location VALUES (1, 'Adult Nonfiction');
INSERT INTO fry.location VALUES (2, 'Adult Fiction');
INSERT INTO fry.location VALUES (3, 'Children Fiction');
INSERT INTO fry.location VALUES (4, 'Children Non-Fiction');
INSERT INTO fry.location VALUES (5, 'Movies');
INSERT INTO fry.location VALUES (6, 'Teen Zone');


--
-- TOC entry 4889 (class 0 OID 24642)
-- Dependencies: 221
-- Data for Name: media; Type: TABLE DATA; Schema: fry; Owner: -
--

INSERT INTO fry.media VALUES ('9c048931-ef90-41e0-bf13-e39707c6d46e', 'Reaper Man', 306.9, 1, 1, true);
INSERT INTO fry.media VALUES ('7efa111b-e3b6-447d-9b40-3fd770aeb26b', 'The Encyclopedia', 1, 1, 1, true);
INSERT INTO fry.media VALUES ('8fab3b14-44b0-4dd1-9f9d-c6eec493de91', 'Walking with Chickens', 636.5, 1, 1, true);
INSERT INTO fry.media VALUES ('ccb3a386-f36b-44d2-8940-74f7b6c52ad9', 'Chinese For Dummies', 495.13, 1, 1, true);


--
-- TOC entry 4888 (class 0 OID 24635)
-- Dependencies: 220
-- Data for Name: type; Type: TABLE DATA; Schema: fry; Owner: -
--

INSERT INTO fry.type VALUES (1, 'Book', 2);
INSERT INTO fry.type VALUES (3, 'Game', 1);
INSERT INTO fry.type VALUES (4, 'Music', 2);
INSERT INTO fry.type VALUES (5, 'Periodical', 1);
INSERT INTO fry.type VALUES (2, 'Film', 2);


--
-- TOC entry 4725 (class 2606 OID 24670)
-- Name: client client_email_key; Type: CONSTRAINT; Schema: fry; Owner: -
--

ALTER TABLE ONLY fry.client
    ADD CONSTRAINT client_email_key UNIQUE (email);


--
-- TOC entry 4727 (class 2606 OID 24668)
-- Name: client client_phone_key; Type: CONSTRAINT; Schema: fry; Owner: -
--

ALTER TABLE ONLY fry.client
    ADD CONSTRAINT client_phone_key UNIQUE (phone);


--
-- TOC entry 4729 (class 2606 OID 24666)
-- Name: client client_pkey; Type: CONSTRAINT; Schema: fry; Owner: -
--

ALTER TABLE ONLY fry.client
    ADD CONSTRAINT client_pkey PRIMARY KEY (cid);


--
-- TOC entry 4737 (class 2606 OID 24692)
-- Name: holds holds_pkey; Type: CONSTRAINT; Schema: fry; Owner: -
--

ALTER TABLE ONLY fry.holds
    ADD CONSTRAINT holds_pkey PRIMARY KEY (holdid);


--
-- TOC entry 4733 (class 2606 OID 24677)
-- Name: loans loans_mediaid_key; Type: CONSTRAINT; Schema: fry; Owner: -
--

ALTER TABLE ONLY fry.loans
    ADD CONSTRAINT loans_mediaid_key UNIQUE (mediaid);


--
-- TOC entry 4735 (class 2606 OID 24675)
-- Name: loans loans_pkey; Type: CONSTRAINT; Schema: fry; Owner: -
--

ALTER TABLE ONLY fry.loans
    ADD CONSTRAINT loans_pkey PRIMARY KEY (checkid);


--
-- TOC entry 4717 (class 2606 OID 24634)
-- Name: location location_pkey; Type: CONSTRAINT; Schema: fry; Owner: -
--

ALTER TABLE ONLY fry.location
    ADD CONSTRAINT location_pkey PRIMARY KEY (locid);


--
-- TOC entry 4723 (class 2606 OID 24649)
-- Name: media media_pkey; Type: CONSTRAINT; Schema: fry; Owner: -
--

ALTER TABLE ONLY fry.media
    ADD CONSTRAINT media_pkey PRIMARY KEY (mid);


--
-- TOC entry 4719 (class 2606 OID 24641)
-- Name: type type_pkey; Type: CONSTRAINT; Schema: fry; Owner: -
--

ALTER TABLE ONLY fry.type
    ADD CONSTRAINT type_pkey PRIMARY KEY (typeid);


--
-- TOC entry 4730 (class 1259 OID 24703)
-- Name: idx_client_name; Type: INDEX; Schema: fry; Owner: -
--

CREATE INDEX idx_client_name ON fry.client USING btree (last_name);


--
-- TOC entry 4720 (class 1259 OID 24705)
-- Name: idx_dewey_catalog; Type: INDEX; Schema: fry; Owner: -
--

CREATE INDEX idx_dewey_catalog ON fry.media USING btree (dewey);


--
-- TOC entry 4731 (class 1259 OID 24704)
-- Name: idx_due_dates; Type: INDEX; Schema: fry; Owner: -
--

CREATE INDEX idx_due_dates ON fry.loans USING btree (datedue);


--
-- TOC entry 4721 (class 1259 OID 24706)
-- Name: idx_media_title; Type: INDEX; Schema: fry; Owner: -
--

CREATE INDEX idx_media_title ON fry.media USING btree (title);


--
-- TOC entry 4742 (class 2606 OID 24698)
-- Name: holds holds_clientid_fkey; Type: FK CONSTRAINT; Schema: fry; Owner: -
--

ALTER TABLE ONLY fry.holds
    ADD CONSTRAINT holds_clientid_fkey FOREIGN KEY (clientid) REFERENCES fry.client(cid);


--
-- TOC entry 4743 (class 2606 OID 24693)
-- Name: holds holds_mediaid_fkey; Type: FK CONSTRAINT; Schema: fry; Owner: -
--

ALTER TABLE ONLY fry.holds
    ADD CONSTRAINT holds_mediaid_fkey FOREIGN KEY (mediaid) REFERENCES fry.media(mid);


--
-- TOC entry 4740 (class 2606 OID 24683)
-- Name: loans loans_clientid_fkey; Type: FK CONSTRAINT; Schema: fry; Owner: -
--

ALTER TABLE ONLY fry.loans
    ADD CONSTRAINT loans_clientid_fkey FOREIGN KEY (clientid) REFERENCES fry.client(cid);


--
-- TOC entry 4741 (class 2606 OID 24678)
-- Name: loans loans_mediaid_fkey; Type: FK CONSTRAINT; Schema: fry; Owner: -
--

ALTER TABLE ONLY fry.loans
    ADD CONSTRAINT loans_mediaid_fkey FOREIGN KEY (mediaid) REFERENCES fry.media(mid);


--
-- TOC entry 4738 (class 2606 OID 24650)
-- Name: media media_loc_fkey; Type: FK CONSTRAINT; Schema: fry; Owner: -
--

ALTER TABLE ONLY fry.media
    ADD CONSTRAINT media_loc_fkey FOREIGN KEY (loc) REFERENCES fry.location(locid);


--
-- TOC entry 4739 (class 2606 OID 24655)
-- Name: media media_medtype_fkey; Type: FK CONSTRAINT; Schema: fry; Owner: -
--

ALTER TABLE ONLY fry.media
    ADD CONSTRAINT media_medtype_fkey FOREIGN KEY (medtype) REFERENCES fry.type(typeid);


-- Completed on 2024-05-01 20:10:41

--
-- PostgreSQL database dump complete
--

