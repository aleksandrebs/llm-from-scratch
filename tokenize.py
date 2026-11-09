#Python re library for basic splitting of text
import re

# Read the raw text file and print num of chars and first 99 chars
with open("data/the-verdict.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()
#print("Total number of characters:", len(raw_text))
#print(raw_text[:99])

#Basic splitting of text into sentences using re
text = "Hello, world. This is a test."
#Text split on punctuation and whitespace
result = re.split(r'([,.:;?_!"()\']|\s)', text)
#Remove empty strings
result = [item.strip() for item in result if item.strip()]
#print(result)

#Splitting Edith Wharton's text
preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
preprocessed = [item.strip() for item in preprocessed if item.strip()]
#print(len(preprocessed))
#print(preprocessed[:30])

#Assigning Token IDs
all_words = sorted(set(preprocessed))
vocab_size = len(all_words)
#print(vocab_size)

#Create vocabulary and print first 50 items
vocab = {token:integer for integer,token in enumerate(all_words)}
for i, item in enumerate(vocab.items()):
    print(item)
    if i >= 50:
        break

#Class for simple tokenization
class SimpleTokenizer:
    def __init__(self, vocab):
        #Store the vocabulary as a class attribute to access in decode and encode methods
        self.str_to_int = vocab
        #Create an inverse vocabulary that maps token IDs back to the text tokens
        self.int_to_str = {i:s for s, i in vocab.items()}

    #Process text into token IDs
    def encode(self, text):
        preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', text)
        preprocessed = [item.strip() for item in preprocessed if item.strip()]
        ids = [self.str_to_int[s] for s in preprocessed]
        return ids

    def decode(self, ids):
        #Convert IDs to text
        text = " ".join([self.int_to_str[i] for i in ids])
        
        #Remove spaces before punctuation
        text = re.sub(r'\s+([,.?!"()\'])', r'\1', text)
        return text

tokenizer = SimpleTokenizer(vocab)
text = """"It's the last he painted, you know,"
       Mrs. Gisburn said with pardonable pride."""
#Encode text into token IDs and print
ids = tokenizer.encode(text)
print(ids)
#Decode token IDs back to text and print
print(tokenizer.decode(ids))