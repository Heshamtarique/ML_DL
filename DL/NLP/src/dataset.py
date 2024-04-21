

class EntityDataset:
    def __init__(self, texts, pos, tags):
        # text in the data is list of list   [["hi", "my", "name" ,"is" ,"Hesham"], .... ]  - so we will tokenize on the basis of spaces
        # pos/tag -- [[1 2 3 4 1 6 ], [....], [...] ] -- same for pos,tag 
        self.texts = texts
        self.pos = pos
        self.tags = tags
    
    def __len__(self):
        return  len(self.texts)   # self.texts is a list of list -- remember
    
    def __getitem__(self, item):
        # get item function --- whenever you enter one index say - 0 to len(dataset) it will return one item which consist of some torch tensor in our case
        text = self.texts[item]
        pos = self.pos[item]
        tags = self.tags[item]
        # now comes the tokeniniizing wrt BERT as the text is already tokenized as list of list (see above)
        # let us tokenize it with respect to the BERt model 
        
        # creating empty lists
        ids = []
        target_pos = []
        target_tag = []
        
        for i,s in enumerate(text):
            inputs = config.TOKENIZER.encode(
                s,    # sentence, which is just 1 word in our case
                add_special_tokens = False# specaial and cls tokens will be added. we dont need them so False                
            )
            # hesham : he ##sh ##am
            input_len = len(inputs)
            ids.extend(inputs)  # Note: extending not appending
            target_pos.extend( [pos[i]] * input_len )   # if the names is noun -- so all will be noun -- # hesham : he ##sh ##am
            target_tag.extend( [tags[i]] * input_len )
            
        # now lets pad the sentence 
        ids = ids[: config.MAX_LEN - 2]  # -2 is for special token cls+sep
        target_pos = target_pos[: config.MAX_LEN -2]
        target_tag = target_tag[: config.MAX_LEN -2]
        
        ids = [101] + ids + [102]
        target_pos = [0] + target_pos + [0]
        target_tag = [0] + target_tag + [0]
        # now all of this has the same length
        
        # attention mask
        mask = [1] *len(ids) 
        teken_type_ids = [0] * len(ids)
        
        # pad the input incase if its not of same length
        padding_len = config.MAX_LEN - len(ids)
        ids = ids + ([0] * padding_len)
        mask = mask + ([0] * padding_len)
        token_type_ids = token_type_ids + ([0] * padding_len)
        target_pos = target_pos + ([0] * padding_len)
        target_tag = target_tag + ([0] * padding_len)
        
        return {
            "ids": torch.tensor(ids, dtype=torch.long),
            "mask": torch.tensor(mask, dtype=torch.long),
            "token_type_ids": torch.tensor(token_type_ids, dtype=torch.long),
            "target_pos": torch.tensor(target_pos, dtype=torch.long),
            "target_tag": torch.tensor(target_tag, dtype=torch.long),
        }        
        
    
