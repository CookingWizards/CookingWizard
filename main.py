from backend.database import utils as dbutils

handler = dbutils.DbHandler("bolt://localhost:7687", "neo4j", "password")
handler.initDb()
