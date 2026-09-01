from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from app.db.session import engine

class DatabaseUnavailableError(RuntimeError):
    pass

def verify_database_connection() ->None:
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
    except SQLAlchemyError as e:
        raise DatabaseUnavailableError(
            "Unable to connect to the database. Please check your internet connection."
        ) from exec
