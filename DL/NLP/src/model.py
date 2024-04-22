import config
import torch
import transformers
import torch.nn as nn


def loss_fn(output, target, mask, num_labels):
    lfn = nn.CrossEntropyLoss()
    active_loss = mask.view(-1) == 1   # its a loss wheer attention mask value is 1
    active_logits = output.view(-1, num_labels)
    active_labels = torch.where(
        active_loss,
        target.view(-1),
        torch.tensor(lfn.ignore_index).type_as(target)
    )
    loss = lfn(active_logits, active_labels)
    return loss
    
    

class EntityModel(nn.Module):
    
    def __init__(self, num_tag,num_pos):
        super(EntityModel, self).__init__()
        self.bert = transformers.BertModel.from_pretrained(config.BASE_MODEL_PATH)
        # if you are looking for RoBerta model just change from bert to roberta, and change the tokenizer inside the config file.
        self.num_tag = num_tag
        self.num_pos = num_pos
        self.bert_drop_1 = nn.Dropout(0.1)
        self.bert_drop_2 = nn.Dropout(0.2)   # same for the POS
        self.out_tag = nn.Linear(768, self.num_tag)
        self.out_pos = nn.Linear(768, self.num_pos)
    
        
        
    def forward(self, ids, mask, token_type_ids, target_pos, target_tag):
        o1, _ = self.bert(ids, attention_mask = mask, token_type_ids= token_type_ids)
        # we have taken here the first input which is sequence output... 
        # as in this problem we are predictiing one value each token not just one value
        bo_tag = self.bert_drop_1(o1)  # bert ooutput 1
        bo_pos = self.bert_drop_2(o1)
        
        tag = self.out_tag(bo_tag)# kind of linear output for each owrd... its length should be determined by the unique tags you have in the tag variable
        pos =  self.out_pos(bo_pos)
        
        loss_tag = loss_fn(tag, target_tag, mask, self.num_tag)      # params of  the loss function 
        loss_pos = loss_fn(pos, target_pos, mask, self.num_pos)
        
        loss = (loss_tag + loss_pos)/2
        return tag, pos, loss
        
        
        
        
