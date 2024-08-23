from gensim.models import Word2Vec
import os
import gzip
import time

# Paths to directories
preprocessed_dir = 'C:\\Users\\student\\Documents\\adhi-p3'
vocab_model_path = 'C:\\Users\\student\\Documents\\adhi-p4\\updated_vocab.model'

# Load the vocabulary model
model_sg = Word2Vec.load(vocab_model_path)

# Function to train the model incrementally and track details
def train_model(directory, model):
    i=0
    total_tokens = 0
    start_time = time.time()
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.txt.gz'):  # Ensure we're processing the correct files
                file_path = os.path.join(root, file)
                print(f"Training on file: {file_path}")
                print(i)
                i+=1
                with gzip.open(file_path, 'rt', encoding='utf-8') as f:
                    chunk = f.read()
                    tokens = chunk.split()
                    if tokens:  # Avoid training on empty data
                        model.train([tokens], total_examples=1, epochs=model.epochs)
                        total_tokens += len(tokens)
                        print(f"Trained on {file_path} with {len(tokens)} tokens")

    end_time = time.time()
    training_time = end_time - start_time
    print(f"Training completed in {training_time:.2f} seconds")
    print(f"Total tokens processed: {total_tokens}")

# Train the model
train_model(preprocessed_dir, model_sg)

# Save the trained model
model_path = 'C:\\Users\\student\\Documents\\adhi-we-p5\\tamil_word2vec_sg.model'
model_sg.save(model_path)
print(f"Model training completed and saved to {model_path}")
