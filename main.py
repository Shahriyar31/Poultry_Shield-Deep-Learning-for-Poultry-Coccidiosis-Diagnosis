import sys
from pathlib import Path

# Add the 'src' directory to the Python path
sys.path.append(str(Path(__file__).resolve().parent / "src"))

# Import the necessary modules
from Poultry_Shield import logger
from Poultry_Shield.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception("An error occurred during the data ingestion stage")
    raise e
