create table if not exists public."Basic"
(
    tconst          varchar(9)                   not null,
    title_type      text                         not null,
    original_title  varchar(256)                 not null,
    promotion_title varchar(256)                 not null,
    is_adult        boolean                      not null,
    start_year      smallint                     not null,
    end_year        smallint,
    genres          "Genres"[]       default ARRAY ['NOTA'::"Genres"],
    rating          double precision default 6.9 not null,
    image_link      text
);

alter table public."Basic"
    add primary key (tconst);

grant delete, insert, references, select, trigger, truncate, update on public."Basic" to anon;

grant delete, insert, references, select, trigger, truncate, update on public."Basic" to authenticated;

grant delete, insert, references, select, trigger, truncate, update on public."Basic" to service_role;

create table if not exists public."Person"
(
    nconst             varchar(9)  not null,
    name               varchar(32) not null,
    birty_year         smallint    not null,
    death_year         smallint,
    primary_profession varchar(16)[]
);

alter table public."Person"
    add primary key (nconst);

grant delete, insert, references, select, trigger, truncate, update on public."Person" to anon;

grant delete, insert, references, select, trigger, truncate, update on public."Person" to authenticated;

grant delete, insert, references, select, trigger, truncate, update on public."Person" to service_role;

create table if not exists public."Linker"
(
    nconst varchar(9) not null,
    tconst varchar(9) not null,
    rank   smallint   not null
);

alter table public."Linker"
    add primary key (nconst, tconst);

alter table public."Linker"
    add foreign key (nconst) references public."Person"
        on update cascade on delete restrict;

alter table public."Linker"
    add foreign key (tconst) references public."Basic"
        on update cascade on delete restrict;

grant delete, insert, references, select, trigger, truncate, update on public."Linker" to anon;

grant delete, insert, references, select, trigger, truncate, update on public."Linker" to authenticated;

grant delete, insert, references, select, trigger, truncate, update on public."Linker" to service_role;

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
    add primary key (tconst, ordering);

alter table public."Principal"
    add foreign key (tconst) references public."Basic"
        on update cascade on delete restrict;

alter table public."Principal"
    add foreign key (nconst) references public."Person"
        on update cascade on delete restrict;

grant delete, insert, references, select, trigger, truncate, update on public."Principal" to anon;

grant delete, insert, references, select, trigger, truncate, update on public."Principal" to authenticated;

grant delete, insert, references, select, trigger, truncate, update on public."Principal" to service_role;

create table if not exists public."Director"
(
    tconst varchar(9) not null,
    nconst varchar(9) not null
);

alter table public."Director"
    add primary key (tconst, nconst);

alter table public."Director"
    add foreign key (tconst) references public."Basic"
        on update cascade on delete restrict;

alter table public."Director"
    add foreign key (nconst) references public."Person"
        on update cascade on delete restrict;

grant delete, insert, references, select, trigger, truncate, update on public."Director" to anon;

grant delete, insert, references, select, trigger, truncate, update on public."Director" to authenticated;

grant delete, insert, references, select, trigger, truncate, update on public."Director" to service_role;

create table if not exists public."Writer"
(
    tconst varchar(9) not null,
    nconst varchar(9) not null
);

alter table public."Writer"
    add primary key (tconst, nconst);

alter table public."Writer"
    add foreign key (tconst) references public."Basic"
        on update cascade on delete restrict;

alter table public."Writer"
    add foreign key (nconst) references public."Person"
        on update cascade on delete restrict;

grant delete, insert, references, select, trigger, truncate, update on public."Writer" to anon;

grant delete, insert, references, select, trigger, truncate, update on public."Writer" to authenticated;

grant delete, insert, references, select, trigger, truncate, update on public."Writer" to service_role;

create table if not exists public."Episode"
(
    tconst         varchar(9) not null,
    parent_tconst  varchar(9) not null,
    season_number  smallint,
    episode_number smallint
);

alter table public."Episode"
    add primary key (tconst);

alter table public."Episode"
    add foreign key (tconst) references public."Basic"
        on update cascade on delete restrict;

alter table public."Episode"
    add foreign key (parent_tconst) references public."Basic"
        on update cascade on delete restrict;

grant delete, insert, references, select, trigger, truncate, update on public."Episode" to anon;

grant delete, insert, references, select, trigger, truncate, update on public."Episode" to authenticated;

grant delete, insert, references, select, trigger, truncate, update on public."Episode" to service_role;

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
    add primary key (tconst, ordering);

alter table public."Akas"
    add foreign key (tconst) references public."Basic"
        on update cascade on delete restrict;

grant delete, insert, references, select, trigger, truncate, update on public."Akas" to anon;

grant delete, insert, references, select, trigger, truncate, update on public."Akas" to authenticated;

grant delete, insert, references, select, trigger, truncate, update on public."Akas" to service_role;

