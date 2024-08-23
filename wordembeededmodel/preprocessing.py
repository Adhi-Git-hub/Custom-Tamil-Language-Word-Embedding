import os
import re
import gzip

# Paths to the directories
input_dir = 'C:\\Users\\student\\Documents\\adhi-p1\\wordembdataset'
output_dir = 'C:\\Users\\student\\Documents\\adhi-p3'

# Regular expression to match Tamil words
tamil_word_regex = re.compile(r'[\u0B80-\u0BFF]+')

# Function to check if a word is Tamil
def is_tamil(word):
    return bool(tamil_word_regex.fullmatch(word))

# Function to tokenize Tamil text properly
def tokenize_tamil_text(text):
    return tamil_word_regex.findall(text)

# Function to preprocess and save tokens in compressed chunks
def preprocess_and_save(directory, output_directory, chunk_size=50000):
    i=1
    os.makedirs(output_directory, exist_ok=True)
    file_count = 0
    tokens = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            print(f"Processing file: {file_path}")
            print(i)
            i+=1
            with open(file_path, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    tamil_words = tokenize_tamil_text(line)
                    if tamil_words:
                        tokens.extend(tamil_words)
                    if len(tokens) >= chunk_size:
                        save_tokens_to_compressed_file(tokens, output_directory, file_count)
                        tokens = []
                        file_count += 1
                        
    # Save remaining tokens
    if tokens:
        save_tokens_to_compressed_file(tokens, output_directory, file_count)

# Function to save tokens in a compressed file
def save_tokens_to_compressed_file(tokens, output_directory, count):
    output_file = os.path.join(output_directory, f"tokens_chunk_{count}.txt.gz")
    with gzip.open(output_file, 'wt', encoding='utf-8') as f:
        f.write(' '.join(tokens))
    print(f"Saved {len(tokens)} tokens to {output_file}")

preprocess_and_save(input_dir, output_dir, chunk_size=5000000)
