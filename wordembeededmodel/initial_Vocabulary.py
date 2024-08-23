from gensim.models import Word2Vec
import os
import gzip

# Path to preprocessed files directory
preprocessed_dir = 'C:\\Users\\student\\Documents\\adhi-p3'
initial_vocab_path = 'C:\\Users\\student\\Documents\\invoc-adhi-p4\\initial_vocab.model'

# Build initial vocabulary model
def build_initial_vocabulary(directory, sample_size=1):
    model_sg = Word2Vec(vector_size=300, window=5, min_count=5, workers=4, sg=1)
    
    file_count = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.txt.gz'):
                file_path = os.path.join(root, file)
                print(f"Processing file for initial vocab: {file_path}")
                with gzip.open(file_path, 'rt', encoding='utf-8') as f:
                    tokens = f.read().split()
                    model_sg.build_vocab([tokens], update=False)
                    print(f"Initial vocabulary built with {file_path}")
                    file_count += 1
                    if file_count >= sample_size:
                        model_sg.save(initial_vocab_path)
                        print(f"Initial vocabulary saved to {initial_vocab_path}")
                        return model_sg

    return model_sg

build_initial_vocabulary(preprocessed_dir, sample_size=1)  # Example with 1 sample file
