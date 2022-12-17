from sensor.configuration.mongo_db_connection import MongoDBClient
from sensor.exception import SensorException
from os import sys
from sensor.logger import logging
from sensor.entity.config_entity import TrainingPipelineConfig,DataIngestionConfig

def test_exception():
    try:
        logging.info("we are dividing by zero")
        x = 1/0
    except Exception as e:
        raise SensorException(e,sys)


if __name__ == "__main__":
    # mongodb_cleint = MongoDBClient()
    # print(mongodb_cleint.database.list_collection_names())/
    # try :
    #     test_exception()
    # except Exception as e:
    #     print(e)
    training_pipeline_config = TrainingPipelineConfig()
    data_ingestion_config = DataIngestionConfig(training_pipeline_config=training_pipeline_config)
    print(data_ingestion_config.__dict__)