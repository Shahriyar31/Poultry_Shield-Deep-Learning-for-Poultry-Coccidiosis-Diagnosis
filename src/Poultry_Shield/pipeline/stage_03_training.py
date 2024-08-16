import sys
sys.path.append('/home/farhan-shahriyar/Deep_Learning/Poultry_Shield-Deep-Learning-for-Poultry-Coccidiosis-Diagnosis/src')

from Poultry_Shield.config.configuration import ConfigurationManager
from Poultry_Shield.components.prepare_callbacks import PrepareCallback
from Poultry_Shield.components.training import Training
from Poultry_Shield import logger

STAGE_NAME = "Training"

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        # Load configuration
        config = ConfigurationManager()
        
        # Get callback configuration and initialize the PrepareCallback object
        prepare_callbacks_config = config.get_prepare_callback_config()
        prepare_callbacks = PrepareCallback(config=prepare_callbacks_config)  # Corrected
        callback_list = prepare_callbacks.get_tb_ckpt_callbacks()

        # Get training configuration and initialize the Training object
        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        
        # Start training
        training.train(
            callback_list=callback_list
        )

if __name__ == '__main__':
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
