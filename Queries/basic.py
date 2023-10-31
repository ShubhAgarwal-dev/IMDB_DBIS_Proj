def basic_query():
    return """SELECT DISTINCT * FROM "Basic" b;"""


def basic_movie_data(t_const: str):
    return f"""SELECT * FROM "Basic" b WHERE 
        b.tconst = '{t_const}';"""


def basic_title_by_name(sub_string: str):
    return f""" SELECT DISTINCT * from "Basic" b WHERE 
        b.original_title LIKE '%{sub_string}%' OR 
        b.promotion_title LIKE '%{sub_string}%';"""


def basic_title_order_by_params(param: str):
    return f"""
    SELECT DISTINCT * FROM "Basic" ORDER BY {param};
    """


def basic_title_filter_by_param_val(param: str, val: str):
    if param == "genres":
        val = "{" + val + "}"
        return f"""
        SELECT DISTINCT * FROM "Basic" B WHERE B.{param} = '{val}';
        """
    return f"""
    SELECT DISTINCT * FROM "Basic" b WHERE b.{param}='{val}';
    """


def basic_title_with_genre(options: str):
    print(options.find(","))
    if options.find(",") == -1:
        option = options
        return f"""SELECT * FROM "Basic" B WHERE '{option}' = ANY (b.genres);
        """
    else:
        options = options.split(",")
        for index, option in enumerate(options):
            options[index] = option.strip()
        base = """SELECT * FROM "Basic" B WHERE """
        for i in range(len(options) - 1):
            base += f"""'{options[i]}' = ANY (B.genres) AND """
        base += f"""'{options[len(options) - 1]}' = ANY (B.genres);"""
        return base


def basic_title_by_director(director: str):
    return f"""
    SELECT DISTINCT * FROM "Basic" b WHERE b.tconst IN 
    (SELECT d.tconst FROM "Director" d 
    JOIN "Person" P ON d.nconst = P.nconst 
    WHERE P.name LIKE '%{director}%' );
    """


def basic_title_by_writers(writer: str):
    return f"""
    SELECT DISTINCT * FROM "Basic" b WHERE b.tconst IN 
    (SELECT w.tconst FROM "Writer" w 
    JOIN "Person" P ON w.nconst = P.nconst 
    WHERE P.name LIKE '%{writer}%' );
    """


def basic_title_by_person(name: str):
    return f"""
    SELECT DISTINCT *
    FROM "Basic" b
    WHERE b.tconst IN (SELECT L.tconst
                   FROM "Linker" L
                            JOIN "Person" P on P.nconst = L.nconst
                   WHERE P.name LIKE '%{name}%')
    """


def update_urating(tconst, new_rating):
    return f"""
    UPDATE "Basic" SET urating={new_rating}  WHERE tconst='{tconst}';
    """


def get_urating(tconst):
    return f"""
    SELECT urating FROM "Basic" WHERE tconst='{tconst}';
    """
