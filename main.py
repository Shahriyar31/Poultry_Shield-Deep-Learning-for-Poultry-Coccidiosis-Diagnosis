import sys

# Add the 'src' directory to the Python path
sys.path.append('/home/farhan-shahriyar/Deep_Learning/Poultry_Shield-Deep-Learning-for-Poultry-Coccidiosis-Diagnosis/src')

# Now import the necessary modules
from Poultry_Shield import logger
from Poultry_Shield.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from Poultry_Shield.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline        
from Poultry_Shield.pipeline.stage_03_training import ModelTrainingPipeline
from Poultry_Shield.pipeline.stage_04_evaluation import EvaluationPipeline


STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e




STAGE_NAME = "Prepare base model"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   prepare_base_model = PrepareBaseModelTrainingPipeline()
   prepare_base_model.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e



STAGE_NAME = "Training"
try:
    logger.info(f"*******************")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    model_trainer = ModelTrainingPipeline()
    model_trainer.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
         logger.exception(e)
         raise e




STAGE_NAME = "Evaluation stage"
try:
    logger.info(f"*******************")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    model_evaluation = EvaluationPipeline()
    model_evaluation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
         logger.exception(e)
         raise e