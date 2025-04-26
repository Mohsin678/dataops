import os
import sys
from dataclasses import dataclass

from catboost import CatBoostRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor

from mlproject.Exception import CustomException
from mlproject.logger import logging

from src.mlproject.utils import save_object,evaulate_models

@dataclass
class Modeltrainconfig:
    trained_model_path = os.path.join("artifacts","model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = Modeltrainconfig()

    def initiate_model_training(self,train_array,test_array):
        try:
            logging.info("spliting train and test data")
            x_train,y_train,x_test,y_test=(
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )
            models = {
                "Random Forest": RandomForestRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                
                "Linear Regression": LinearRegression(),
               
                "CatBoosting Regressor": CatBoostRegressor(verbose=False),
               
            }

            model_report:dict =evaulate_models(x_train=x_train,y_train=y_train,x_test=x_test,y_test=y_test,models=models)


            #get best model score
            best_model_score = max(sorted(model_report.values()))

            #get best model name
            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]

            best_model = models[best_model_name]

            if best_model_score<0.6:
                raise CustomException("No best model found")
            logging.info(f"Best found model on both training and testing dataset")

            save_object(
                file_path=self.model_trainer_config.trained_model_path,
                obj = best_model
            )

            predicted = best_model.predict(x_test)

            r2_square = r2_score(y_test, predicted)
            return r2_square

    
        except Exception as e:
            raise CustomException(e,sys)