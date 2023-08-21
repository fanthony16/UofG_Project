import os
import sys

import numpy as np
import pandas as pd
from dataclasses import dataclass
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from src import logger
from src import exception
from src import util

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join("artifacts","preprocessor.pkl")
    

class DataTransformation:
    def __init__(self) :
        self.data_transformation_config = DataTransformationConfig()
        
    def get_data_transformer_object(self):
        
        try:
            
            numerical_columns = ["age", "hypertension","heart_disease","heart_disease","avg_glucose_level","bmi"]
            categorical_columns = ["gender","ever_married","work_type","Residence_type","smoking_status"]
            
            num_pipeline= Pipeline(
                
                steps=[
                ("imputer",SimpleImputer(strategy="median")),
                ("scaler",StandardScaler())
                ]
            )
            
            cat_pipeline=Pipeline(

                steps=[
                ("imputer",SimpleImputer(strategy="most_frequent")),
                ("one_hot_encoder",OneHotEncoder()),
                ("scaler",StandardScaler(with_mean=False))
                ]

            )
            
            logger.logging.info(f"Categorical columns: {categorical_columns}")
            logger.logging.info(f"Numerical columns: {numerical_columns}")
            
            preprocessor=ColumnTransformer(
                [
                ("num_pipeline",num_pipeline,numerical_columns),
                ("cat_pipelines",cat_pipeline,categorical_columns)

                ]
            )
            
            return preprocessor
            
            
        except Exception as e:
            raise exception.CustomException(e,sys)

    def initiate_data_transformation(self, train_path, test_path):
        try:
            
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            
            logger.logging.info("Read Train and Test Data Completed")
            logger.logging.info("Obtaining Preprocessing Object")
            
            preprocessing_obj = self.get_data_transformer_object()
            
            target_column_name="stroke"
            
            input_feature_train_df = train_df.drop(columns=[target_column_name],axis=1)
            target_feature_train_df = train_df[target_column_name]
            
            input_feature_test_df = test_df.drop(columns=[target_column_name],axis=1)
            target_feature_test_df = test_df[target_column_name]
            
            logger.logging.info(
                f"Applying preprocessing object on training dataframe and testing dataframe."
            )
            
            input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df)
            
            train_arr = np.c_[
                input_feature_train_arr, np.array(target_feature_train_df)
            ]
            
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]
            
            util.save_object(

                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj

            )
            
            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path
            )
            
            
        
        except Exception as e:
            raise exception.CustomException(e,sys)




    

if __name__ == "__main__":
    try:
        1/0
    except Exception as e:
        raise exception.CustomException(e,sys)