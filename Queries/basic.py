def basic_query():
    return """SELECT DISTINCT * FROM "Basic" b;"""


def basic_title_by_name(sub_string: str):
    return f""" SELECT DISTINCT * from "Basic" b WHERE 
        b.original_title LIKE '%{sub_string}%' OR 
        b.promotion_title LIKE '%{sub_string}%';"""


def basic_title_order_by_params(param: str):
    return f"""
    SELECT DISTINCT * FROM "Basic" ORDER BY {param};
    """


def basic_title_filter_by_param_val(param: str, val: str):
    return f"""
    SELECT DISTINCT * FROM "Basic" b WHERE b.{param}='{val}';
    """


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
