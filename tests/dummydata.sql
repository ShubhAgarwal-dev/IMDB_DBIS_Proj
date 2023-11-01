truncate table "Linker";
truncate table "Principal";
truncate table "Director";
truncate table "Writer";
truncate table "Person";
truncate table "Episode";
truncate table "Akas";
truncate table "Rating";
truncate table "Basic";
truncate table "User";

INSERT INTO "Basic" ("tconst", "title_type", "original_title", "promotion_title", "is_adult", "start_year", "end_year",
                     "genres", "rating", "image_link")
VALUES ('tt001', 'dvd', 'Movie Title 1', 'Promotion Title 1', true, 2000, NULL, '{Action, Drama}', 7.2,
        'https://m.media-amazon.com/images/M/MV5BMTAxNDhiM2UtZTE2Ny00NmI5LThhOTYtMjIyY2Y1ZmRiZjhhXkEyXkFqcGdeQXVyMTUzMTg2ODkz._V1_UX100_CR0,0,100,100_AL_.jpg'),
       ('tt002', 'television', 'Movie Title 2', 'Promotion Title 2', false, 2010, 2015, '{Romance}', 6.5,
        'https://m.media-amazon.com/images/M/MV5BMGJkNmIzYjQtYTZkYS00NDY3LTlhMGItMGVlMjNjNzNkN2I2XkEyXkFqcGdeQXVyODk4OTc3MTY@._V1_UX100_CR0,0,100,100_AL_.jpg'),
       ('tt003', 'television', 'Movie Title 3', 'Promotion Title 3', false, 2015, NULL, '{NOTA}', 8.0,
        'https://m.media-amazon.com/images/M/MV5BMDYxMzEyMjEtYjc3MS00MjU4LWE5ZjAtODU0NTNlMGUwNWFhXkEyXkFqcGdeQXVyODk4OTc3MTY@._V1_UX100_CR0,0,100,100_AL_.jpg'),
       ('tt004', 'dvd', 'Movie Title 4', 'Promotion Title 4', true, 2008, NULL, '{Horror}', 6.3,
        'https://m.media-amazon.com/images/M/MV5BZjAyMWFmZWUtMzdlNy00M2FjLTg0NmEtNTM3ZWY3MWMwNDVkXkEyXkFqcGdeQXVyMTkxNjUyNQ@@._V1_UX100_CR0,0,100,100_AL_.jpg'),
       ('tt005', 'television', 'Movie Title 5', 'Promotion Title 5', false, 2012, 2016, '{Action, Fiction}', 7.5,
        'https://m.media-amazon.com/images/M/MV5BMzFiNGM3MDYtZWVmYi00ZTIwLThhOWQtNzgzMjBlYTQ0OTQ1XkEyXkFqcGdeQXVyMTUzMTg2ODkz._V1_UX100_CR0,0,100,100_AL_.jpg'),
       ('tt006', 'television', 'Movie Title 6', 'Promotion Title 6', true, 2005, 2010, '{Erotic}', 6.7,
        'hhttps://m.media-amazon.com/images/M/MV5BZWQ3NDE5YzUtZWFlMy00N2I0LWFmNzAtNDdiZjFiOTZjOWIzXkEyXkFqcGdeQXVyMTUzMTg2ODkz._V1_UX100_CR0,0,100,100_AL_.jpg'),
       ('tt007', 'dvd', 'Movie Title 7', 'Promotion Title 7', false, 2018, NULL, '{Drama}', 7.8,
        'https://m.media-amazon.com/images/M/MV5BZjZkNThjNTMtOGU0Ni00ZDliLThmNGUtZmMxNWQ3YzAxZTQ1XkEyXkFqcGdeQXVyMTUzMTg2ODkz._V1_UX100_CR0,0,100,100_AL_.jpg'),
       ('tt008', 'television', 'Movie Title 8', 'Promotion Title 8', true, 2014, NULL, '{Romance, Drama}', 7.2,
        'https://m.media-amazon.com/images/M/MV5BMDc3ODNmYzYtNGEzOC00NzY4LWFhNzEtOGE4YmUyODJlZDBkXkEyXkFqcGdeQXVyMTUzMTg2ODkz._V1_UX100_CR0,0,100,100_AL_.jpg'),
       ('tt009', 'dvd', 'Movie Title 9', 'Promotion Title 9', false, 2007, NULL, '{Mystery}', 6.9,
        'https://m.media-amazon.com/images/M/MV5BMjFiZDE0YjEtNDY2Ni00ZmM4LThkYjctNDEyNzA3MzdjMTRlXkEyXkFqcGdeQXVyMTUzMTg2ODkz._V1_UX100_CR0,0,100,100_AL_.jpg'),
       ('tt010', 'dvd', 'Movie Title 10', 'Promotion Title 10', true, 2011, NULL, '{Fantasy}', 8.5,
        'https://m.media-amazon.com/images/M/MV5BZDYzYzM2NGUtOGY5ZS00YjFmLWIxNWMtNjdlZTRkYTQ2YzNmXkEyXkFqcGdeQXVyMTUzMTg2ODkz._V1_UX100_CR0,0,100,100_AL_.jpg'),
       ('tt011', 'television', 'Movie Title 11', 'Promotion Title 11', false, 2013, 2017, '{Adventure, Action}', 7.1,
        'https://m.media-amazon.com/images/M/MV5BZTRkNGYyZmItZTNlYy00MzgwLThhZTYtY2ZiOTZkNWU1YWYwXkEyXkFqcGdeQXVyMTUzMTg2ODkz._V1_UX100_CR0,0,100,100_AL_.jpg'),
       ('tt012', 'dvd', 'Movie Title 12', 'Promotion Title 12', true, 2009, NULL, '{Fiction, Fantasy}', 8.2,
        'https://m.media-amazon.com/images/M/MV5BZjAxNDA2MmMtNTk1Ni00N2RhLWE4ZjYtYWM2YWYxMzc3YjE4XkEyXkFqcGdeQXVyMDA4NzMyOA@@._V1_UX100_CR0,0,100,100_AL_.jpg'),
       ('tt013', 'dvd', 'Movie Title 13', 'Promotion Title 13', false, 2016, NULL, '{Crime}', 7.0,
        'https://m.media-amazon.com/images/M/MV5BNGY1ZWU2ZGUtMTlmNy00NTNlLTllZDctMGM3MzI2MzZkNjY2XkEyXkFqcGdeQXVyMTUzMTg2ODkz._V1_UX100_CR0,0,100,100_AL_.jpg'),
       ('tt014', 'television', 'Movie Title 14', 'Promotion Title 14', true, 2019, NULL, '{Horror, Erotic}', 6.8,
        'https://m.media-amazon.com/images/M/MV5BY2VkMTM5NGUtN2VjYi00YWEyLTg1N2EtNDg5OWZiOTU2YWUyXkEyXkFqcGdeQXVyMTUzMTg2ODkz._V1_UX100_CR0,0,100,100_AL_.jpg'),
       ('tt015', 'dvd', 'Movie Title 15', 'Promotion Title 15', false, 2006, NULL, '{Romance}', 7.3,
        'https://m.media-amazon.com/images/M/MV5BM2FiN2RiOWItOGEwMS00ZGYxLWJkMDUtM2Q4YjU4ZmI0YjBhXkEyXkFqcGdeQXVyMTMzNDE5NDM2._V1_UX100_CR0,0,100,100_AL_.jpg'),
       ('tt016', 'television', 'Movie Title 16', 'Promotion Title 16', true, 2010, 2014, '{Drama, Mystery}', 7.9,
        'https://m.media-amazon.com/images/M/MV5BYmU2ZDk1MDgtMzhiMS00NTc0LThkYjItOTMwM2RiMjc5NzhkXkEyXkFqcGdeQXVyMTkxNjUyNQ@@._V1_UX100_CR0,0,100,100_AL_.jpg'),
       ('tt017', 'dvd', 'Movie Title 17', 'Promotion Title 17', false, 2017, NULL, '{Action, Erotic}', 7.4,
        'https://m.media-amazon.com/images/M/MV5BYmU2ZDk1MDgtMzhiMS00NTc0LThkYjItOTMwM2RiMjc5NzhkXkEyXkFqcGdeQXVyMTkxNjUyNQ@@._V1_UX100_CR0,0,100,100_AL_.jpg'),
       ('tt018', 'dvd', 'Movie Title 18', 'Promotion Title 18', true, 2008, NULL, '{Fantasy, Adventure}', 8.1,
        'https://m.media-amazon.com/images/M/MV5BMWJmNzczMmYtZjE5Yy00NTM0LTg5NjAtN2I4OWE4OGI2NjUwXkEyXkFqcGdeQXVyMTUzMTg2ODkz._V1_UX100_CR0,0,100,100_AL_.jpg'),
       ('tt019', 'television', 'Movie Title 19', 'Promotion Title 19', false, 2012, 2016, '{Fiction, Mystery}', 7.7,
        'https://m.media-amazon.com/images/M/MV5BMWJmNzczMmYtZjE5Yy00NTM0LTg5NjAtN2I4OWE4OGI2NjUwXkEyXkFqcGdeQXVyMTUzMTg2ODkz._V1_UX100_CR0,0,100,100_AL_.jpg'),
       ('tt020', 'dvd', 'Movie Title 20', 'Promotion Title 20', true, 2015, NULL, '{Action, Adventure}', 8.3,
        'https://m.media-amazon.com/images/M/MV5BMWJmNzczMmYtZjE5Yy00NTM0LTg5NjAtN2I4OWE4OGI2NjUwXkEyXkFqcGdeQXVyMTUzMTg2ODkz._V1_UX100_CR0,0,100,100_AL_.jpg');

INSERT INTO "Person" ("nconst", "name", "birty_year", "death_year", "primary_profession")
VALUES ('nm001', 'Actor One', 1970, NULL, ARRAY ['Actor']),
       ('nm002', 'Actress Two', 1985, NULL, ARRAY ['Actress']),
       ('nm003', 'Director One', 1965, NULL, ARRAY ['Director']),
       ('nm004', 'Writer One', 1978, NULL, ARRAY ['Writer']),
       ('nm005', 'Actor Three', 1982, NULL, ARRAY ['Actor']),
       ('nm006', 'Actress Four', 1973, NULL, ARRAY ['Actress']),
       ('nm007', 'Director Two', 1971, NULL, ARRAY ['Director']),
       ('nm008', 'Writer Two', 1980, NULL, ARRAY ['Writer']),
       ('nm009', 'Actor Five', 1968, NULL, ARRAY ['Actor']),
       ('nm010', 'Actress Six', 1989, NULL, ARRAY ['Actress']);

INSERT INTO "Linker" ("nconst", "tconst", "rank")
VALUES ('nm001', 'tt001', 1),
       ('nm002', 'tt001', 2),
       ('nm003', 'tt002', 1),
       ('nm004', 'tt002', 2),
       ('nm005', 'tt003', 1),
       ('nm006', 'tt003', 2),
       ('nm007', 'tt004', 1),
       ('nm008', 'tt004', 2),
       ('nm009', 'tt005', 1),
       ('nm010', 'tt005', 2);

INSERT INTO "Principal" ("tconst", "ordering", "nconst", "category", "job", "role")
VALUES ('tt001', 1, 'nm001', 'actor', NULL, 'Lead Actor'),
       ('tt001', 2, 'nm002', 'actress', NULL, 'Supporting Actress'),
       ('tt002', 1, 'nm003', 'director', NULL, 'Director One'),
       ('tt002', 2, 'nm004', 'writer', NULL, 'Writer One'),
       ('tt003', 1, 'nm005', 'actor', NULL, 'Lead Actor'),
       ('tt003', 2, 'nm006', 'actress', NULL, 'Supporting Actress'),
       ('tt004', 1, 'nm007', 'director', NULL, 'Director Two'),
       ('tt004', 2, 'nm008', 'writer', NULL, 'Writer Two'),
       ('tt005', 1, 'nm009', 'actor', NULL, 'Lead Actor'),
       ('tt005', 2, 'nm010', 'actress', NULL, 'Supporting Actress');

-- Data for Director Table
INSERT INTO "Director" ("tconst", "nconst")
VALUES ('tt001', 'nm003'),
       ('tt002', 'nm003'),
       ('tt003', 'nm007'),
       ('tt004', 'nm007'),
       ('tt005', 'nm007');

-- Data for Writer Table
INSERT INTO "Writer" ("tconst", "nconst")
VALUES ('tt001', 'nm004'),
       ('tt002', 'nm004'),
       ('tt003', 'nm008'),
       ('tt004', 'nm008'),
       ('tt005', 'nm008');


INSERT INTO "Episode" ("tconst", "parent_tconst", "season_number", "episode_number")
VALUES ('tt006', 'tt001', 1, 1),
       ('tt007', 'tt001', 1, 2),
       ('tt008', 'tt002', 2, 1),
       ('tt009', 'tt002', 2, 2),
       ('tt010', 'tt003', 1, 1),
       ('tt011', 'tt003', 1, 2),
       ('tt012', 'tt004', 1, 1),
       ('tt013', 'tt004', 1, 2),
       ('tt014', 'tt005', 1, 1),
       ('tt015', 'tt005', 1, 2);

INSERT INTO "Akas" ("tconst", "ordering", "local_title", "region", "language", "types", "attributes",
                    "is_original_title")
VALUES ('tt001', 1, 'Movie Title 1 - French', 'France', 'French', 'dvd', ARRAY ['dubbed'], false),
       ('tt002', 1, 'Movie Title 2 - Spanish', 'Spain', 'Spanish', 'television', NULL, true),
       ('tt003', 1, 'Movie Title 3 - German', 'Germany', 'German', 'television', NULL, false),
       ('tt004', 1, 'Movie Title 4 - Italian', 'Italy', 'Italian', 'dvd', NULL, false),
       ('tt005', 1, 'Movie Title 5 - Russian', 'Russia', 'Russian', 'television', NULL, true),
       ('tt006', 1, 'Movie Title 6 - Portuguese', 'Portugal', 'Portuguese', 'dvd', NULL, false),
       ('tt007', 1, 'Movie Title 7 - Dutch', 'Netherlands', 'Dutch', 'dvd', NULL, false),
       ('tt008', 1, 'Movie Title 8 - Chinese', 'China', 'Chinese', 'television', NULL, true),
       ('tt009', 1, 'Movie Title 9 - Japanese', 'Japan', 'Japanese', 'dvd', NULL, false),
       ('tt010', 1, 'Movie Title 10 - Arabic', 'United Arab Emirates', 'Arabic', 'dvd', NULL, true);