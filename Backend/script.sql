-- CreateEnum
CREATE TYPE "Genres" AS ENUM ('Fiction', 'Crime', 'Horror', 'Ghoul', 'Romance', 'Fantasy', 'Drama', 'Action', 'War', 'Historical', 'Erotic', 'Adventure', 'Mystery', 'Anime', 'Documentary', 'NOTA');

-- CreateEnum
CREATE TYPE "title_types" AS ENUM ('alternative', 'dvd', 'festival', 'television', 'video', 'working', 'original_title', 'imdbDisplay');


create table if not exists public."Basic"
(
    tconst          varchar(9)                    not null,
    title_type      text                          not null,
    original_title  varchar(256)                  not null,
    promotion_title varchar(256)                  not null,
    is_adult        boolean                       not null,
    start_year      smallint                      not null,
    end_year        smallint,
    genres          "Genres"[]       default ARRAY ['NOTA'::"Genres"],
    rating          double precision default 6.9  not null,
    image_link      text,
    urating         double precision default 7.00 not null
);

alter table public."Basic"
    add constraint "Basic_pkey"
        primary key (tconst);

create table if not exists public."Person"
(
    nconst             varchar(9)  not null,
    name               varchar(32) not null,
    birty_year         smallint    not null,
    death_year         smallint,
    primary_profession varchar(16)[]
);

alter table public."Person"
    add constraint "Person_pkey"
        primary key (nconst);

create table if not exists public."Linker"
(
    nconst varchar(9) not null,
    tconst varchar(9) not null,
    rank   smallint   not null
);

alter table public."Linker"
    add constraint "Linker_pkey"
        primary key (nconst, tconst);

alter table public."Linker"
    add constraint "Linker_nconst_fkey"
        foreign key (nconst) references public."Person"
            on update cascade on delete restrict;

alter table public."Linker"
    add constraint "Linker_tconst_fkey"
        foreign key (tconst) references public."Basic"
            on update cascade on delete restrict;

create table if not exists public."Principal"
(
    tconst   varchar(9)  not null,
    ordering smallint    not null,
    nconst   varchar(9)  not null,
    category varchar(16) not null,
    job      text,
    role     text
);

alter table public."Principal"
    add constraint "Principal_pkey"
        primary key (tconst, ordering);

alter table public."Principal"
    add constraint "Principal_tconst_fkey"
        foreign key (tconst) references public."Basic"
            on update cascade on delete restrict;

alter table public."Principal"
    add constraint "Principal_nconst_fkey"
        foreign key (nconst) references public."Person"
            on update cascade on delete restrict;

create table if not exists public."Director"
(
    tconst varchar(9) not null,
    nconst varchar(9) not null
);

alter table public."Director"
    add constraint "Director_pkey"
        primary key (tconst, nconst);

alter table public."Director"
    add constraint "Director_tconst_fkey"
        foreign key (tconst) references public."Basic"
            on update cascade on delete restrict;

alter table public."Director"
    add constraint "Director_nconst_fkey"
        foreign key (nconst) references public."Person"
            on update cascade on delete restrict;

create table if not exists public."Writer"
(
    tconst varchar(9) not null,
    nconst varchar(9) not null
);

alter table public."Writer"
    add constraint "Writer_pkey"
        primary key (tconst, nconst);

alter table public."Writer"
    add constraint "Writer_tconst_fkey"
        foreign key (tconst) references public."Basic"
            on update cascade on delete restrict;

alter table public."Writer"
    add constraint "Writer_nconst_fkey"
        foreign key (nconst) references public."Person"
            on update cascade on delete restrict;

create table if not exists public."Episode"
(
    tconst         varchar(9) not null,
    parent_tconst  varchar(9) not null,
    season_number  smallint,
    episode_number smallint
);

alter table public."Episode"
    add constraint "Episode_pkey"
        primary key (tconst);

alter table public."Episode"
    add constraint "Episode_tconst_fkey"
        foreign key (tconst) references public."Basic"
            on update cascade on delete restrict;

alter table public."Episode"
    add constraint "Episode_parent_tconst_fkey"
        foreign key (parent_tconst) references public."Basic"
            on update cascade on delete restrict;

create table if not exists public."Akas"
(
    tconst            varchar(9)   not null,
    ordering          smallint     not null,
    local_title       varchar(256) not null,
    region            varchar(32)  not null,
    language          varchar(16),
    types             title_types  not null,
    attributes        varchar(16)[],
    is_original_title boolean      not null
);

alter table public."Akas"
    add constraint "Akas_pkey"
        primary key (tconst, ordering);

alter table public."Akas"
    add constraint "Akas_tconst_fkey"
        foreign key (tconst) references public."Basic"
            on update cascade on delete restrict;

create table if not exists public."User"
(
    uconst   text default gen_random_uuid() not null,
    password varchar(97)                    not null,
    username text
);

alter table public."User"
    add constraint "User_pkey"
        primary key (uconst);

alter table public."User"
    add constraint uname
        unique (username);

create table if not exists public."Rating"
(
    uconst text             not null,
    tconst varchar(9)       not null,
    rating double precision not null,
    review text
);

create index if not exists "Rating_tconst_idx"
    on public."Rating" (tconst);

alter table public."Rating"
    add constraint "Rating_pkey"
        primary key (uconst, tconst);

alter table public."Rating"
    add constraint "Rating_tconst_fkey"
        foreign key (tconst) references public."Basic"
            on update cascade on delete restrict;

alter table public."Rating"
    add constraint "Rating_uconst_fkey"
        foreign key (uconst) references public."User"
            on update cascade on delete restrict;
