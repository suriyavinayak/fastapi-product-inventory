from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Replace '0000' with your PostgreSQL password if you set a different one during installation
db_url = "postgresql+psycopg2://postgres:root@localhost:5432/telusko"
engine = create_engine(db_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
