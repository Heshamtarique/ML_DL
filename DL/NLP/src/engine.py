import torch
from tqdm import tqdm



# creating a training function---

def train_fn (data_loader, model, optimizer, device, scheduler):
    model.train()
    final_loss = 0
    
    # now we can loop over the batches from the data loader
    for data in tqdm(data_loader, total= len(data_loader)):
        '''The number of expected iterations. If unspecified, len(iterable) is used if possible. 
        If float("inf") or as a last resort, only basic progress statistics are displayed (no ETA, no progressbar). 
        If gui is True and this parameter needs subsequent updating, specify an initial arbitrary large positive number, e.g. 9e9.'''
        
        for k,v in data.items():
            data[k] = v.to(device)    
        optimizer.zero_grad()
        _,_,loss = model(**data)
        # when you build this model -- you should take the same input name such as id, mask, target_tag etc as in dataset.py
        loss.backward()
        optimizer.backwrad()
        scheduler.step()   # in case if we have scheduler
        
        final_loss = final_loss+ loss.item()
    
    return final_loss/len(data_loader)

# Evaluation function 

def eval_fn(data_loader, model, device):
    model.eval()     # putting model in eval model
    final_loss = 0 
    for data in tqdm(data_loader, total=len(data_loader)):
        for k, v in data.items():
            data[k] = v.to(device)
        _, _, loss = model(**data)
        final_loss += loss.item()
    return final_loss / len(data_loader)        
