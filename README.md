# IMDB DBIS LAB PROJECT
**DBIS Lab project || IMDB Clone || Backend**

Developed by a group of four students:

    - Saksham Chhimwal(210010046)
    - Shubh Agarwal(210020047)
    - Shivesh Pandey(2100200044)
    - Aryan Gulhane(210010006)

### Replication guidelines

Making a virtualenv using venv, virtualenv, conda or something is recommended. If you have made the virtualenv then 
execute the following commands:

```shell
python -m pip install -r requirements.txt
mkdir logs
```

make a `.env` file with following environment variables:
```
DATABASE_NAME=imdb
DATABASE_HOST=localhost
DATABASE_USER=postgres
DATABASE_PASSWORD=<anything>
DATABASE_PORT=5432
```

Now use the sql commands written in [`script.sql`](./script.sql) to replicate our imdb schema. You can also use the 
[`dummydata.sql`](./tests/dummydata.sql) to fill in some dummy data to perform some tests, or you can head to 
[datasets.imdbws.com](https://datasets.imdbws.com/) to fill in your database, but still you will have to fill in some 
extra attributes like rating, genres, image_link in `Basic` yourself with help of some randomizer.
