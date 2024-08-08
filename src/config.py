from nest.core.database.orm_provider import AsyncOrmProvider
import os
from dotenv import load_dotenv

load_dotenv()

db_user = os.getenv("DB_USER", "root")
db_password = os.getenv("DB_PASSWORD", "root")
db_host = os.getenv("DB_HOST", "localhost")
db_port = os.getenv("DB_PORT", "5432")
db_name = os.getenv("DB_NAME", "postgresql")
database_url = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

config = AsyncOrmProvider(
    db_type="postgresql",
    config_params=dict(
        host=db_host,
        db_name=db_name,
        user=db_user,
        password=db_password,
        port=int(db_port),
    ),
)
