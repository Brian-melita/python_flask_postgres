from flask_sqlalchemy.extension import SQLAlchemy
from sqlalchemy import MetaData

# Db connection
metadata = MetaData()
db = SQLAlchemy(metadata=metadata)
