class Config:
    DB_USER="root"
    DB_PASS="mysql"
    DB_HOST="127.0.0.0.1"
    DB_PORT="3306"
    DB_TYPE="mysql"
    DB_NAME="cv"
    SQLALCHEMY_DATABASE_URI = f"{DB_TYPE}://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
