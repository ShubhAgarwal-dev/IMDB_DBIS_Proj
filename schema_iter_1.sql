-- CreateEnum
CREATE TYPE "title_types" AS ENUM ('alternative', 'dvd', 'festival', 'television', 'video', 'working', 'original_title', 'imdbDisplay');

-- CreateTable
CREATE TABLE "Basic" (
    "tconst" VARCHAR(9) NOT NULL,
    "title_type" TEXT NOT NULL,
    "original_title" VARCHAR(256) NOT NULL,
    "promotion_title" VARCHAR(256) NOT NULL,
    "is_adult" BOOLEAN NOT NULL,
    "start_year" SMALLINT NOT NULL,
    "end_year" SMALLINT,

    CONSTRAINT "Basic_pkey" PRIMARY KEY ("tconst")
);

-- CreateTable
CREATE TABLE "Person" (
    "nconst" VARCHAR(9) NOT NULL,
    "name" VARCHAR(32) NOT NULL,
    "birty_year" SMALLINT NOT NULL,
    "death_year" SMALLINT,
    "primary_profession" VARCHAR(16)[],

    CONSTRAINT "Person_pkey" PRIMARY KEY ("nconst")
);

-- CreateTable
CREATE TABLE "Linker" (
    "nconst" VARCHAR(9) NOT NULL,
    "tconst" VARCHAR(9) NOT NULL,
    "rank" SMALLINT NOT NULL,

    CONSTRAINT "Linker_pkey" PRIMARY KEY ("nconst","tconst")
);

-- CreateTable
CREATE TABLE "Principal" (
    "tconst" VARCHAR(9) NOT NULL,
    "ordering" SMALLINT NOT NULL,
    "nconst" VARCHAR(9) NOT NULL,
    "category" VARCHAR(16) NOT NULL,
    "job" TEXT,
    "role" TEXT,

    CONSTRAINT "Principal_pkey" PRIMARY KEY ("tconst","ordering")
);

-- CreateTable
CREATE TABLE "Director" (
    "tconst" VARCHAR(9) NOT NULL,
    "nconst" VARCHAR(9) NOT NULL,

    CONSTRAINT "Director_pkey" PRIMARY KEY ("tconst","nconst")
);

-- CreateTable
CREATE TABLE "Writer" (
    "tconst" VARCHAR(9) NOT NULL,
    "nconst" VARCHAR(9) NOT NULL,

    CONSTRAINT "Writer_pkey" PRIMARY KEY ("tconst","nconst")
);

-- CreateTable
CREATE TABLE "Episode" (
    "tconst" VARCHAR(9) NOT NULL,
    "parent_tconst" VARCHAR(9) NOT NULL,
    "season_number" SMALLINT,
    "episode_number" SMALLINT,

    CONSTRAINT "Episode_pkey" PRIMARY KEY ("tconst")
);

-- CreateTable
CREATE TABLE "Akas" (
    "tconst" VARCHAR(9) NOT NULL,
    "ordering" SMALLINT NOT NULL,
    "local_title" VARCHAR(256) NOT NULL,
    "region" VARCHAR(32) NOT NULL,
    "language" VARCHAR(16),
    "types" "title_types" NOT NULL,
    "attributes" VARCHAR(16)[],
    "is_original_title" BOOLEAN NOT NULL,

    CONSTRAINT "Akas_pkey" PRIMARY KEY ("tconst","ordering")
);

-- AddForeignKey
ALTER TABLE "Linker" ADD CONSTRAINT "Linker_nconst_fkey" FOREIGN KEY ("nconst") REFERENCES "Person"("nconst") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Linker" ADD CONSTRAINT "Linker_tconst_fkey" FOREIGN KEY ("tconst") REFERENCES "Basic"("tconst") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Principal" ADD CONSTRAINT "Principal_tconst_fkey" FOREIGN KEY ("tconst") REFERENCES "Basic"("tconst") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Principal" ADD CONSTRAINT "Principal_nconst_fkey" FOREIGN KEY ("nconst") REFERENCES "Person"("nconst") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Director" ADD CONSTRAINT "Director_tconst_fkey" FOREIGN KEY ("tconst") REFERENCES "Basic"("tconst") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Director" ADD CONSTRAINT "Director_nconst_fkey" FOREIGN KEY ("nconst") REFERENCES "Person"("nconst") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Writer" ADD CONSTRAINT "Writer_tconst_fkey" FOREIGN KEY ("tconst") REFERENCES "Basic"("tconst") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Writer" ADD CONSTRAINT "Writer_nconst_fkey" FOREIGN KEY ("nconst") REFERENCES "Person"("nconst") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Episode" ADD CONSTRAINT "Episode_tconst_fkey" FOREIGN KEY ("tconst") REFERENCES "Basic"("tconst") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Episode" ADD CONSTRAINT "Episode_parent_tconst_fkey" FOREIGN KEY ("parent_tconst") REFERENCES "Basic"("tconst") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Akas" ADD CONSTRAINT "Akas_tconst_fkey" FOREIGN KEY ("tconst") REFERENCES "Basic"("tconst") ON DELETE RESTRICT ON UPDATE CASCADE;
