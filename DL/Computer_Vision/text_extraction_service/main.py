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


          
    # text extraction from pdf files from multiple databases...
    def extract_text_from_pdf(self, file_path):
        try:
            document = fitz.open(file_path)
            text = ''
            
            for page_num in range(len(document)):
                page = document.load_page(page_num)
                text+=page.get_text()
            cleaned_text = self.clean_text(text)
            return cleaned_text
        except Exception as e:
            print(f"Error while extracting text form {file_path}: {e} ")
            
            
            
    # extracting text from all pdf files in the folder we are keeping
    def extract_text_from_directory(self):
        for filename in os.listdir(self.directory):
            if filename.endswith('.pdf'):
                file_path = os.path.join(self.directory, filename)
                
                # extracted_text is a DS of type dicts
                self.extracted_text[filename] = self.extract_text_from_pdf(file_path)
                
        return self.extracted_text
         
            
    @classmethod        
    def from_dictionary(cls, directory):
        # creating instance of the class defined above from  a dict
        return  cls(directory)
    
    
    def save_extracted_text(self, output_file):
        
        try:
            with open(output_file, 'w', encoding='uft-8') as f:
                for filename, text in self.extracted_text.items():
                    f.write(f"extracted text from {filename}: \n{text}\n\n")
            print(f"extracted text saved to {output_file}")

        except Exception as e:
            print(f"Error saving the extracted text: {e}")
    
    
