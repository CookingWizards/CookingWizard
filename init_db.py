from backend.database import utils

if __name__ == "__main__":
    handler = utils.DbHandler("bolt://localhost:7687", "neo4j", "password")
    handler.initDb()
    handler.close()
