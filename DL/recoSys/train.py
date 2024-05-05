import tez
import pandas as pd
from sklearn import model_selection
import torch
import torch.nn as nn
import numpy as np
from sklearn import metrics, preprocessing



def train():
    df = pd.read_csv(".../Users/recoSys/train_v2.csv")

    lbl_user = preprocessing.LabelEncoder()  # encoding user
    lbl_movie = preprocessing.LabelEncoder()
    
    df.user = lbl_user.fit_transform(df.user.values)
    df.movie = lbl_movie.fit_transform(df.movie.values)
    
    
    # ID user movie ratinf
    df_train, df_valid = model_selection.train_test_split(
        df, test_size=0.1,
        random_state=42,
        stratify=df.rating.values
        )
    
    train_dataset = MovieDataset(
        users= df_train.user.values, 
        movies=df_train.movie.values, 
        ratings= df_train.rating.values )
    
    valid_dataset = MovieDataset(
        users= df_valid.user.values, 
        movies=df_valid.movie.values, 
        ratings= df_valid.rating.values )
    model = RecSysModel(num_users = len(lbl_user.classes_), num_movies = len(lbl_movie.classes_))
    
    model.fit(
        train_dataset, valid_dataset,
        train_bs=102,
        valid_bs=1024,
        fp16=True
        
    )
if __name__ == "__main__":
    train()
    print("Service Running Successfully")
    
    
    
