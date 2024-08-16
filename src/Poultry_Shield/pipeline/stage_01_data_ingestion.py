import sys
sys.path.append('/home/farhan-shahriyar/Deep_Learning/Poultry_Shield-Deep-Learning-for-Poultry-Coccidiosis-Diagnosis/src')

from Poultry_Shield.config.configuration import ConfigurationManager
from Poultry_Shield.components.data_ingestion import DataIngestion
from Poultry_Shield import logger



STAGE_NAME = "Data Ingestion stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()




if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e