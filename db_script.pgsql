--
-- PostgreSQL database dump
--

-- Dumped from database version 12.6
-- Dumped by pg_dump version 12.6

-- Started on 2022-05-21 23:59:59

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
-- TOC entry 2870 (class 0 OID 57842)
-- Dependencies: 210
-- Data for Name: full_requests_info; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.full_requests_info (request_id, info, first_approval, second_approval) FROM stdin;
\.


--
-- TOC entry 2866 (class 0 OID 49470)
-- Dependencies: 205
-- Data for Name: requests; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.requests (id, product, description, amount, created_at, status, customer) FROM stdin;
\.


--
-- TOC entry 2867 (class 0 OID 49485)
-- Dependencies: 206
-- Data for Name: requests_history; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.requests_history (request_id, action, date, approver) FROM stdin;
\.


--
-- TOC entry 2868 (class 0 OID 49707)
-- Dependencies: 208
-- Data for Name: user_rol_history; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.user_rol_history ("user", new_rol, old_rol, admin, date) FROM stdin;
\.


--
-- TOC entry 2864 (class 0 OID 49457)
-- Dependencies: 203
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users (username, first_name, last_name, birth_date, rol, email, password, status) FROM stdin;
admin	Elias	Mena	2022-06-21	1	elias@gmail.com	pbkdf2:sha256:260000$WbZxDPwf4I3EfQxI$de87f9fc7b7f048cf879981167838e3be9ec631de82ba78fede4a95fc843679a	A
financial1	Mikael	Partlett	2022-08-16	4	emenas453@ulacit.ed.cr	pbkdf2:sha256:260000$pqO9QCuAxIg1KrkL$90c2676a3090028620a639ab77da22a56481268a7861e26f8e41ab7fd4fa2cc4	A
financial2	Max	Esbrook	2022-06-22	5	eli1199@hotmail.es	pbkdf2:sha256:260000$72oNEViQfbxs51vr$16f151fc5fa18ccffa0dc3338cbba73ae5bb120d8bbd4c94ce6691ac30aec83e	A
financial3	Steve	Kirvell	2022-03-25	6	eliasms2911@gmail.com	pbkdf2:sha256:260000$2UVGyF0ALNwoV26z$ad01ce04d785615e0f6176ae65802624a7a06a69f5232a93624dad39e4893c3f	A
customer	Regen	Hoopper	2022-03-24	2	eliasmena.2911@gmail.com	pbkdf2:sha256:260000$jsOtE0aZovcJNtTS$5bcdec8bd051ff04fb71264bc999f25e1da62673d755855013583e2ccd2d633b	A
chief	Francis	Malyon	2022-01-19	3	eliasmena.2911@gmail.com	pbkdf2:sha256:260000$MLQ8s4LOow7BaqK5$3b7fe2e32d507c6ee4450fadf665f8323563c48feb57c083b7c561be474134d5	A
\.


--
-- TOC entry 2863 (class 0 OID 49449)
-- Dependencies: 202
-- Data for Name: users_rols; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users_rols (rol_id, name, description) FROM stdin;
1	Administrador	The user who can add, update, activate and inactivate users
2	Comprador	The user who can generate the requests for buy a product
3	Aprobador Jefe	First level of approver, this user is  the customer´s direct boss
4	Aprobador Fianciero 1	This user approves orders between ₡1 and ₡100,000
5	Aprobador Fianciero 2	This user approves orders between ₡100,000 and ₡1,000,000
6	Aprobador Fianciero 3	This user approves orders between ₡1,000,000 and ₡10,000,000
\.


--
-- TOC entry 2877 (class 0 OID 0)
-- Dependencies: 209
-- Name: full_request_info_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.full_request_info_id_seq', 8, true);


--
-- TOC entry 2878 (class 0 OID 0)
-- Dependencies: 204
-- Name: requests_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.requests_id_seq', 82, true);


-- Completed on 2022-05-22 00:00:00

--
-- PostgreSQL database dump complete
--

