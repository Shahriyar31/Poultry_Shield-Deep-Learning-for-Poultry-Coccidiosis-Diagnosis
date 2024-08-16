from Poultry_Shield.entity.config_entity import TrainingConfig
import tensorflow as tf
from pathlib import Path

class Training:
    def __init__(self, config: TrainingConfig):
        self.config = config
        self.model = None
        self.optimizer = None
        self.train_generator = None
        self.valid_generator = None
    
    def get_base_model(self):
        try:
            # Load the base model
            self.model = tf.keras.models.load_model(
                self.config.updated_base_model_path
            )
            # Default learning rate if not specified
            learning_rate = 0.001  # Adjust as needed
            self.optimizer = tf.keras.optimizers.Adam(learning_rate=learning_rate)
            # Compile the model with the new optimizer
            self.model.compile(optimizer=self.optimizer, loss='categorical_crossentropy', metrics=['accuracy'])
        except Exception as e:
            print(f"Error in getting base model: {e}")
            raise
    
    def train_valid_generator(self):
        try:
            datagenerator_kwargs = dict(
                rescale=1./255,
                validation_split=0.20
            )

            dataflow_kwargs = dict(
                target_size=self.config.params_image_size[:-1],
                batch_size=self.config.params_batch_size,
                interpolation="bilinear"
            )

            valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
                **datagenerator_kwargs
            )

            self.valid_generator = valid_datagenerator.flow_from_directory(
                directory=self.config.training_data,
                subset="validation",
                shuffle=False,
                **dataflow_kwargs
            )

            if self.config.params_is_augmentation:
                train_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
                    rotation_range=40,
                    horizontal_flip=True,
                    width_shift_range=0.2,
                    height_shift_range=0.2,
                    shear_range=0.2,
                    zoom_range=0.2,
                    **datagenerator_kwargs
                )
            else:
                train_datagenerator = valid_datagenerator

            self.train_generator = train_datagenerator.flow_from_directory(
                directory=self.config.training_data,
                subset="training",
                shuffle=True,
                **dataflow_kwargs
            )
        except Exception as e:
            print(f"Error in setting up data generators: {e}")
            raise
    
    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        try:
            model.save(path)
        except Exception as e:
            print(f"Error in saving model: {e}")
            raise
    
    def train(self, callback_list: list):
        try:
            if not self.model:
                raise ValueError("Model is not initialized. Call get_base_model() first.")
            if not self.train_generator or not self.valid_generator:
                raise ValueError("Data generators are not initialized. Call train_valid_generator() first.")
            
            self.steps_per_epoch = self.train_generator.samples // self.train_generator.batch_size
            self.validation_steps = self.valid_generator.samples // self.valid_generator.batch_size

            # Ensure model is compiled with the optimizer before fitting
            self.model.compile(optimizer=self.optimizer, loss='categorical_crossentropy', metrics=['accuracy'])

            self.model.fit(
                self.train_generator,
                epochs=self.config.params_epochs,
                steps_per_epoch=self.steps_per_epoch,
                validation_steps=self.validation_steps,
                validation_data=self.valid_generator,
                callbacks=callback_list
            )

            self.save_model(
                path=self.config.trained_model_path,
                model=self.model
            )
        except Exception as e:
            print(f"Error during training: {e}")
            raise
