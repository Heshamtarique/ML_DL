
import transformers

MAX_LEN = 128
TRAIN_BATCH_SIZE = 32
VALID_BATCH_SIZE = 8
EPOCHS = 10
BASE_MODEL_PATH = ".../bertModel/input/bert_base_uncased"
MODEL_PATH = "model.bin"    # model saving path -- will be saved in src folder
TRAINING_FILE = ".../bertModel/input/ner_dataset.csv"
TOKENIZER = transformers.BertTokenizer.from_pretrained(
    
    BASE_MODEL_PATH,
    do_lower_case = True
    
)
