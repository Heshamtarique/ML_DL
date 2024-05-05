import tez
import pandas as pd
from sklearn import model_selection
import torch
import torch.nn as nn
import numpy as np
from sklearn import metrics, preprocessing

class RecSysModel(tez.Model):     # tez library will be used in here

    def __inti__(self, num_users, num_movies):  # input to the model
        super().__init__()
        self.user_embed = nn.Embedding(num_users, 32)
        self.movie_embed = nn.Embedding(num_movies,32)
        self.out = nn.Linear(64, 1)
        self.step_scheduler_after = "epoch" # schedule after every epoch
        
    def fetch_optimizer(self):
        opt = torch.optim.Adam(self.parameters(), lr = 1e-3)
        return opt
    
    def fetch_scheduler(self):
        sch = torch.optim.lr_scheduler.StepLR(self.optimizer, step_size=3, gamma=0.7)
        return sch
        
    def monitor_metrics(self, output, rating):
        target = target.detach().cpu().numpy()
        rating=rating.detach().cpu().numpy()
        
        return {
            'rmse' : np.sqrt(metrics.mean_squared_error(rating, output) )
        }
        
    def forward(self, users, movies, ratings=None):
        
        user_embed = self.user_embed(users)
        movie_embeds = self.movie_embed(movies)
        
        output = torch.cat([user_embed, movie_embeds], dim=1)
        output = self.out(output)
        
        loss = nn.MSELoss()(output, ratings.view(-1,1))
        calc_metrics = self.monitor_metrics(output, ratings.view(-1,1) )
        
        return output, loss, calc_metrics
    
        
