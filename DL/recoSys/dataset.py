import tez
import pandas as pd
from sklearn import model_selection
import torch
import torch.nn as nn
import numpy as np
from sklearn import metrics, preprocessing


# building datapipeline

class MovieDataset:
  
    def __init__(self, users, movies, ratings):
        
        # these features we saw in the dataaset... explore the features !
        self.users= users
        self.movies = movies
        self.ratings = ratings

    def __len__(self):
        return len(self.users)   
      # how many samples we have 

    def __getitem__(self, item):
        user = self.users[item]
        movie = self.movies[item]
        rating = self.ratings[item]
        
        return {
            "user": torch.tensor(user, dtype = torch.long),
            "movie": torch.tensor(movie, dtype = torch.long ),
            "rating": torch.tensor( rating, dtype=torch.float)    # rating could be float
        }

