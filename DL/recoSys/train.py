import tez
import pandas as pd
from sklearn import model_selection


class MovieDataset:
    def __init__(self, users, movies, ratings):
        self.users= users
        self.movies = movies
        self.ratings = ratings
        
        

    def __len__(self):
        return len(self.users)


def train():
    df = pd.read_csv(".../user/recoSys/train.csv")

    # ID user movie ratinf
    df_train, df_valid = model_selection.train_test_split(df, test_size=0.1,
                                                          random_state=42,
                                                          stratify=df.rating.values)
    ...
    
