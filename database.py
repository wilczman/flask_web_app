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
        for row in result.mappings().all():
            print(dict(row))


def add_application_to_db(job_id, data):
    with engine.connect() as conn:
        query = text(
            '''INSERT INTO applications (
            job_id, full_name, email, linkedin_url, education, work_experience, resume_url
            ) VALUES (
            :job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url
            )
            '''
        )
        conn.execute(
            query,
            {
                "job_id": job_id,
                "full_name": data['full_name'],
                "email": data['email'],
                "linkedin_url": data['linkedin_url'],
                "education": data['education'],
                "work_experience": str(data['work_experience']),
                "resume_url": '',#data['resume_url'],
            }
        )


def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        result_dicts = []
        for row in result.mappings().all():
            result_dicts.append(dict(row))
        return result_dicts


def load_specific_job_from_db(id_: int):
    with engine.connect() as conn:
        sql = f"SELECT * FROM jobs WHERE id = :val"
        result = conn.execute(
            text(sql),
            {"val": id_},
        )
        row = result.mappings().fetchone()
        return dict(row) if row else None
