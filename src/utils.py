import os 
import sys
import numpy as np
import pandas as pd
from src.exception import CustomException
import dill
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

def save_object(file_path, obj):
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
    except Exception as e:
        raise CustomException(e, sys)
    
def evaluate_model(X_train, y_train, X_test, y_test, models,param):
    try:
        report = {}
        for i in range(len(models)):
            model = list(models.values())[i]
            para=param[list(models.keys())[i]]
            gs=GridSearchCV(model,para,cv=3)
            # Train model
            #model.fit(X_train, y_train)

            gs.fit(X_train, y_train)
            model.set_params(**gs.best_params_)
            model.fit(X_train, y_train)


            # Predict Testing data
            y_test_pred = model.predict(X_test)

            # Get R2 score for test data
            test_model_score = r2_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = test_model_score

        return report
    except Exception as e:
        raise CustomException(e, sys)
