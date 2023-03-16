CREATE SEQUENCE bed_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 32767 CACHE 1;

CREATE TABLE "public"."bed" (
    "id" smallint DEFAULT nextval('bed_id_seq') NOT NULL,
    "size" smallint NOT NULL,
    "life_factor" smallint NOT NULL,
    "garden_id" smallint NOT NULL,
    CONSTRAINT "bed_pkey" PRIMARY KEY ("id")
) WITH (oids = false);


CREATE SEQUENCE garden_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 32767 CACHE 1;

CREATE TABLE "public"."garden" (
    "id" smallint DEFAULT nextval('garden_id_seq') NOT NULL,
    "name" text NOT NULL,
    CONSTRAINT "garden_pkey" PRIMARY KEY ("id")
) WITH (oids = false);



CREATE SEQUENCE plant_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1;

CREATE TABLE "public"."plant" (
    "id" smallint DEFAULT nextval('plant_id_seq') NOT NULL,
    "name" character(255) NOT NULL,
    "stage" smallint NOT NULL,
    "bed_id" smallint NOT NULL,
    CONSTRAINT "plant_pkey" PRIMARY KEY ("id")
) WITH (oids = false);


ALTER TABLE ONLY "public"."bed" ADD CONSTRAINT "bed_garden_id_fkey" FOREIGN KEY (garden_id) REFERENCES garden(id) NOT DEFERRABLE;

ALTER TABLE ONLY "public"."plant" ADD CONSTRAINT "plant_bed_id_fkey" FOREIGN KEY (bed_id) REFERENCES bed(id) NOT DEFERRABLE;