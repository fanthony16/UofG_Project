import os
import pandas as pd
from src import logger
from dataclasses import dataclass
from sklearn.model_selection import train_test_split

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts','train.csv')
    test_data_path: str = os.path.join('artifacts','test.csv')
    raw_data_path: str = os.path.join('artifacts','data.csv')

class DataIngestion:
    def __init__(self) :
        self.ingestionConfig = DataIngestionConfig()
    
    def initiate_data_ingestion(self):
            
        try:
            
            df = pd.read_csv("notebook\data\stroke_dataset.csv")
            logger.logging.info("Read Dataset File Successfully")
            os.makedirs(os.path.dirname(self.ingestionConfig.train_data_path),exist_ok=True)
            df.to_csv(self.ingestionConfig.raw_data_path,index=False,header=True)
            logger.logging.info("Train test initiated")
            
            train_set, test_set = train_test_split(df,test_size=0.2, random_state= 42)
            train_set.to_csv(self.ingestionConfig.train_data_path,index=False,header=True)          
            test_set.to_csv(self.ingestionConfig.test_data_path,index=False,header=True)
            
            logger.logging.info("Data Ingestion completed")
            
            return(
                self.ingestionConfig.test_data_path,
                self.ingestionConfig.train_data_path
            )
            
        
        except exception as e :
            logger.logging.info("An Error Occur")
        
if __name__ == "__main__" :
    
    try:
        obj = DataIngestion()
        obj.initiate_data_ingestion()
        logger.logging.info("Testing Logging")
    except Exception as e :
        logger.logging.info("Testing Logging")