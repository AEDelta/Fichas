--
-- PostgreSQL database dump
--

\restrict DuhdOYbe3QtGBwugsZjCYdb4fgYhgQ1CAJrYErPK6Eu8uAZCWuk2VAyqtUNz7w5

-- Dumped from database version 16.10
-- Dumped by pg_dump version 16.10

-- Started on 2025-08-25 12:40:06

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

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 224 (class 1259 OID 16609)
-- Name: clientes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.clientes (
    id integer NOT NULL,
    nome character varying(100) NOT NULL,
    email character varying(100),
    telefone character varying(20)
);


ALTER TABLE public.clientes OWNER TO postgres;

--
-- TOC entry 223 (class 1259 OID 16608)
-- Name: clientes_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.clientes_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.clientes_id_seq OWNER TO postgres;

--
-- TOC entry 4840 (class 0 OID 0)
-- Dependencies: 223
-- Name: clientes_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.clientes_id_seq OWNED BY public.clientes.id;


--
-- TOC entry 226 (class 1259 OID 16616)
-- Name: fichas; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.fichas (
    id integer NOT NULL,
    descricao character varying(255) NOT NULL,
    data date NOT NULL,
    valor numeric(10,2),
    responsavel character varying(100)
);


ALTER TABLE public.fichas OWNER TO postgres;

--
-- TOC entry 225 (class 1259 OID 16615)
-- Name: fichas_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.fichas_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.fichas_id_seq OWNER TO postgres;

--
-- TOC entry 4841 (class 0 OID 0)
-- Dependencies: 225
-- Name: fichas_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.fichas_id_seq OWNED BY public.fichas.id;


--
-- TOC entry 222 (class 1259 OID 16597)
-- Name: financeiro; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.financeiro (
    id integer NOT NULL,
    descricao text,
    valor numeric(10,2),
    tipo character varying(10),
    data date
);


ALTER TABLE public.financeiro OWNER TO postgres;

--
-- TOC entry 221 (class 1259 OID 16596)
-- Name: financeiro_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.financeiro_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.financeiro_id_seq OWNER TO postgres;

--
-- TOC entry 4842 (class 0 OID 0)
-- Dependencies: 221
-- Name: financeiro_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.financeiro_id_seq OWNED BY public.financeiro.id;


--
-- TOC entry 218 (class 1259 OID 16576)
-- Name: funcionarios; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.funcionarios (
    id integer NOT NULL,
    nome character varying(100) NOT NULL,
    cargo character varying(100),
    telefone character varying(20)
);


ALTER TABLE public.funcionarios OWNER TO postgres;

--
-- TOC entry 217 (class 1259 OID 16575)
-- Name: funcionarios_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.funcionarios_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.funcionarios_id_seq OWNER TO postgres;

--
-- TOC entry 4843 (class 0 OID 0)
-- Dependencies: 217
-- Name: funcionarios_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.funcionarios_id_seq OWNED BY public.funcionarios.id;


--
-- TOC entry 216 (class 1259 OID 16565)
-- Name: usuarios; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.usuarios (
    id integer NOT NULL,
    nome character varying(100) NOT NULL,
    email character varying(100) NOT NULL,
    senha character varying(255) NOT NULL,
    funcao character varying(50) NOT NULL
);


ALTER TABLE public.usuarios OWNER TO postgres;

--
-- TOC entry 215 (class 1259 OID 16564)
-- Name: usuarios_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.usuarios_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.usuarios_id_seq OWNER TO postgres;

--
-- TOC entry 4844 (class 0 OID 0)
-- Dependencies: 215
-- Name: usuarios_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.usuarios_id_seq OWNED BY public.usuarios.id;


--
-- TOC entry 220 (class 1259 OID 16583)
-- Name: vistorias; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.vistorias (
    id integer NOT NULL,
    data date NOT NULL,
    descricao text,
    funcionario_id integer,
    status character varying(50)
);


ALTER TABLE public.vistorias OWNER TO postgres;

--
-- TOC entry 219 (class 1259 OID 16582)
-- Name: vistorias_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.vistorias_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.vistorias_id_seq OWNER TO postgres;

--
-- TOC entry 4845 (class 0 OID 0)
-- Dependencies: 219
-- Name: vistorias_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.vistorias_id_seq OWNED BY public.vistorias.id;


--
-- TOC entry 4663 (class 2604 OID 16612)
-- Name: clientes id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.clientes ALTER COLUMN id SET DEFAULT nextval('public.clientes_id_seq'::regclass);


--
-- TOC entry 4664 (class 2604 OID 16619)
-- Name: fichas id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fichas ALTER COLUMN id SET DEFAULT nextval('public.fichas_id_seq'::regclass);


--
-- TOC entry 4662 (class 2604 OID 16600)
-- Name: financeiro id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.financeiro ALTER COLUMN id SET DEFAULT nextval('public.financeiro_id_seq'::regclass);


--
-- TOC entry 4660 (class 2604 OID 16579)
-- Name: funcionarios id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.funcionarios ALTER COLUMN id SET DEFAULT nextval('public.funcionarios_id_seq'::regclass);


--
-- TOC entry 4659 (class 2604 OID 16568)
-- Name: usuarios id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.usuarios ALTER COLUMN id SET DEFAULT nextval('public.usuarios_id_seq'::regclass);


--
-- TOC entry 4661 (class 2604 OID 16586)
-- Name: vistorias id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.vistorias ALTER COLUMN id SET DEFAULT nextval('public.vistorias_id_seq'::regclass);


--
-- TOC entry 4832 (class 0 OID 16609)
-- Dependencies: 224
-- Data for Name: clientes; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.clientes (id, nome, email, telefone) FROM stdin;
2	Maria Souza	maria@email.com	11988888888
3	João Silva	joao@email.com	11999999999
4	Maria Souza	maria@email.com	11988888888
5	João Silva	joao@email.com	11999999999
6	Maria Souza	maria@email.com	11988888888
7	João Silva	joao@email.com	11999999999
8	Maria Souza	maria@email.com	11988888888
9	João Silva	joao@email.com	11999999999
10	Maria Souza	maria@email.com	11988888888
1	João Silva	joao@email.com	11977777777
\.


--
-- TOC entry 4834 (class 0 OID 16616)
-- Dependencies: 226
-- Data for Name: fichas; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.fichas (id, descricao, data, valor, responsavel) FROM stdin;
\.


--
-- TOC entry 4830 (class 0 OID 16597)
-- Dependencies: 222
-- Data for Name: financeiro; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.financeiro (id, descricao, valor, tipo, data) FROM stdin;
\.


--
-- TOC entry 4826 (class 0 OID 16576)
-- Dependencies: 218
-- Data for Name: funcionarios; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.funcionarios (id, nome, cargo, telefone) FROM stdin;
\.


--
-- TOC entry 4824 (class 0 OID 16565)
-- Dependencies: 216
-- Data for Name: usuarios; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.usuarios (id, nome, email, senha, funcao) FROM stdin;
\.


--
-- TOC entry 4828 (class 0 OID 16583)
-- Dependencies: 220
-- Data for Name: vistorias; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.vistorias (id, data, descricao, funcionario_id, status) FROM stdin;
\.


--
-- TOC entry 4846 (class 0 OID 0)
-- Dependencies: 223
-- Name: clientes_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.clientes_id_seq', 10, true);


--
-- TOC entry 4847 (class 0 OID 0)
-- Dependencies: 225
-- Name: fichas_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.fichas_id_seq', 1, false);


--
-- TOC entry 4848 (class 0 OID 0)
-- Dependencies: 221
-- Name: financeiro_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.financeiro_id_seq', 1, false);


--
-- TOC entry 4849 (class 0 OID 0)
-- Dependencies: 217
-- Name: funcionarios_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.funcionarios_id_seq', 1, false);


--
-- TOC entry 4850 (class 0 OID 0)
-- Dependencies: 215
-- Name: usuarios_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.usuarios_id_seq', 1, false);


--
-- TOC entry 4851 (class 0 OID 0)
-- Dependencies: 219
-- Name: vistorias_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.vistorias_id_seq', 1, false);


--
-- TOC entry 4676 (class 2606 OID 16614)
-- Name: clientes clientes_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.clientes
    ADD CONSTRAINT clientes_pkey PRIMARY KEY (id);


--
-- TOC entry 4678 (class 2606 OID 16621)
-- Name: fichas fichas_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fichas
    ADD CONSTRAINT fichas_pkey PRIMARY KEY (id);


--
-- TOC entry 4674 (class 2606 OID 16604)
-- Name: financeiro financeiro_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.financeiro
    ADD CONSTRAINT financeiro_pkey PRIMARY KEY (id);


--
-- TOC entry 4670 (class 2606 OID 16581)
-- Name: funcionarios funcionarios_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.funcionarios
    ADD CONSTRAINT funcionarios_pkey PRIMARY KEY (id);


--
-- TOC entry 4666 (class 2606 OID 16574)
-- Name: usuarios usuarios_email_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.usuarios
    ADD CONSTRAINT usuarios_email_key UNIQUE (email);


--
-- TOC entry 4668 (class 2606 OID 16572)
-- Name: usuarios usuarios_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.usuarios
    ADD CONSTRAINT usuarios_pkey PRIMARY KEY (id);


--
-- TOC entry 4672 (class 2606 OID 16590)
-- Name: vistorias vistorias_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.vistorias
    ADD CONSTRAINT vistorias_pkey PRIMARY KEY (id);


--
-- TOC entry 4679 (class 2606 OID 16591)
-- Name: vistorias vistorias_funcionario_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.vistorias
    ADD CONSTRAINT vistorias_funcionario_id_fkey FOREIGN KEY (funcionario_id) REFERENCES public.funcionarios(id);


-- Completed on 2025-08-25 12:40:06

--
-- PostgreSQL database dump complete
--

\unrestrict DuhdOYbe3QtGBwugsZjCYdb4fgYhgQ1CAJrYErPK6Eu8uAZCWuk2VAyqtUNz7w5

