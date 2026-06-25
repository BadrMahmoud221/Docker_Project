import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv
# Load variables from the .env file
load_dotenv()
# Securely retrieve the database URL
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")
# Establish the connection engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

BOOK_DATASTORE = {
    1 : {
        'id' : 1 , 
        'title' : 'Python Basics' ,
        'author' : 'Badr Mahmoud' ,
        'is_read' : True

    },
    2 : {
        'id' : 2 , 
        'title' : 'FastAPI Basics' ,
        'author' : 'Mahmoud Badr' ,
        'is_read' : False
    }
}

# Dependency to yield database sessions to our FastAPI routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

