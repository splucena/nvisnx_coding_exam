-- Table: public.jobs

-- DROP TABLE IF EXISTS public.jobs;

CREATE TABLE IF NOT EXISTS public.jobs
(
    job_id integer NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    job_name text COLLATE pg_catalog."default" NOT NULL,
    job_summary text COLLATE pg_catalog."default",
    CONSTRAINT job_id PRIMARY KEY (job_id)
)