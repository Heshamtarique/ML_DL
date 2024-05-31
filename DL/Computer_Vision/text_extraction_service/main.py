class PDFTextExtractor:
    def __init__(self, directory):   # essential to pass as args
        self.directory = directory
        self.extracted_text = {}
        
    
    def clean_text(self, text):
        try:
            text = re.sub(r'\s+', ' ', text)# multiple spaces in data wit single space
            text = re.sub(r'\n', ' ', text)  # new line with one space
            return text.strip()
        except Exception as e:
            print(f"Error1: {e}")
         
