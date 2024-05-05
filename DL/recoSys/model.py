
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
        
