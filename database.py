import os

from sqlalchemy import create_engine, text
from dotenv import load_dotenv
load_dotenv()

host = os.getenv("DB_HOST")
user = os.getenv("DB_USERNAME")
passwd = os.getenv("DB_PASSWORD")
db = os.getenv("DB_NAME")
uri = f"mysql+pymysql://{user}:{passwd}@{host}/{db}?charset=utf8mb4"
ssl = {
    "ssl": {"ssl_ca": "/etc/ssl/cert.pem"}
}

engine = create_engine(
    uri,
    connect_args=ssl
)

if __name__ == '__main__':
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        result_dicts = []
        for row in result.all():
            result_dicts.append(dict(row))
