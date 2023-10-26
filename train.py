import numpy as np
import pandas as pd
import pickle
from sklearn import preprocessing
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import roc_auc_score, roc_curve
from xgboost import XGBClassifier

# parameters
random_state = 57
d = 5
eta = 0.1
n_estimators = 60 
scale_pos_weight = 1
output_file = 'xgb_model.bin'


# Data preparation
df_full_train = pd.read_csv('data/train.csv', index_col = "id")
y = df_full_train.pop("defects")
X = np.log1p(df_full_train)

# Validation
def cross_validation(model):
    
    #initiate prediction arrays and score lists
    train_scores, val_scores = [], []
    kf = StratifiedKFold(shuffle=True, random_state=random_state, n_splits = 5)
    
    for fold, (train_idx, val_idx) in enumerate(kf.split(X, y)):
        #Train dataset
        X_train = X.iloc[train_idx]
        y_train = y.iloc[train_idx]
        
        #Validation dataset
        X_val = X.iloc[val_idx]
        y_val = y.iloc[val_idx]
                
        #Train model    
        model.fit(X_train, y_train)
    
        #Predictions
        train_preds = model.predict_proba(X_train)[:, 1]
        val_preds = model.predict_proba(X_val)[:, 1]
    
        #Evaluation for a fold
        train_score = roc_auc_score(y_train, train_preds)
        val_score = roc_auc_score(y_val, val_preds)
    
        #Saving the model score for a fold
        train_scores.append(train_score)
        val_scores.append(val_score)
    
    print(f'val score: {np.mean(val_scores):.5f} ± {np.std(val_scores):.5f} | train score: {np.mean(train_scores):.5f} ± {np.std(train_scores):.5f}')
    return val_scores
 
model =  XGBClassifier(random_state = random_state,
                        n_estimators = n_estimators,
                        eta = eta, max_depth = d,
                        scale_pos_weight = scale_pos_weight)
score_list = cross_validation( model)

#final model 
XGBClassifier(random_state = random_state,
                        n_estimators = n_estimators,
                        eta = eta, max_depth = d,
                        scale_pos_weight = scale_pos_weight)
model.fit(X, y)

with open(output_file, 'wb') as f_out:
    pickle.dump((model), f_out)

print(f'the model is saved to {output_file}')