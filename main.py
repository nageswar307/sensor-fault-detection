from sensor.configuration.mongo_db_connection import MongoDBClient


if __name__ == "__main__":
    mongodb_cleint = MongoDBClient()
    print(mongodb_cleint.database.list_collection_names())