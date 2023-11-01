description = """
**DBIS Lab project || IMDB Clone || Backend**

Developed by a group of four students:

    - Shubh Agarwal(210020047)
    - Saksham Chhimwal(210010046)
    - Shivesh Pandey(2100200044)
    - Aryan Gulhane(210010006)
"""

tags_metadata = [
    {
        "name": "Basic",
        "description": """This returns a json, with movies and status_code keys.
        The movie return the list of json objects which contains the following keys:
        - tconst
        - title_type
        - original_title
        - promotion_title
        - is_adult
        - start_year
        - end_data
        """
    },
    {
        "name": "Person",
        "description": """Endpoints related to persons (actors, directors, writers, etc.).
        - `GET /actors`: Retrieves details for actors.
        - `GET /directors`: Retrieves details for directors.
        - `GET /titles/person`: Retrieves titles related to a person.
        - `GET /person/details`: Retrieves detailed information about a person.
        """
    },
    {
        "name": "Auth",
        "description": "Endpoints requiring JWT authentication."
    },
    {
        "name": "User",
        "description": """Endpoints related to user actions and authentication.
        - `GET /user/rated_titles`: Retrieves the list of movies rated by the user.
        - `POST /user/signup`: Registers a new user.
        - `POST /user/signin`: Authenticates and provides an access token.
        - `POST /user/rate`: Allows users to rate a specific movie.
        - `GET /user/titles/{username}`: Retrieves movies rated by a specific user.
        """
    },
    {
        "name": "Episodes",
        "description": """Endpoints related to episodes and TV shows.
        - `GET /title/episodes`: Retrieves information about episodes.
        - `GET /title/tv_show/og_title`: Retrieves TV shows by original title.
        - `GET /title/tv_show/start_year`: Retrieves TV shows by the start year.
        - `GET /title/tv_show/end_year`: Retrieves TV shows by the end year.
        - `GET /title/tv_show/genre`: Retrieves TV shows by genre.
        """
    },
    {
        "name": "tv-shows",
        "description": """Endpoints related to TV shows.
        - `GET /title/tv_show/og_title`: Retrieves TV shows by original title.
        - `GET /title/tv_show/start_year`: Retrieves TV shows by the start year.
        - `GET /title/tv_show/end_year`: Retrieves TV shows by the end year.
        - `GET /title/tv_show/genre`: Retrieves TV shows by genre.
        """
    }
]