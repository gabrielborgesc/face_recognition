CREATE TABLE public.passwords (
	user_id int4 NOT NULL,
	"password" varchar NOT NULL,
	description varchar NULL
);

CREATE TABLE public.users (
	id serial NOT NULL,
	"name" varchar NULL,
	encoded_array jsonb NULL
);
