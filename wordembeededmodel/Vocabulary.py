from gensim.models import Word2Vec
import os
import gzip

# Paths
preprocessed_dir = 'path\\preprocesss_output_path'
initial_vocab_path = 'path\\initial_vocab.model'
finalvocdir = 'path\\finalvoc'
updated_vocab_path = os.path.join(finalvocdir, "updated_vocab.model")

# Load initial model
model_sg = Word2Vec.load(initial_vocab_path)
print("Model loaded with initial vocabulary")

# Function to incrementally update vocabulary
def update_vocabulary(directory, model):
    i = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.txt.gz'):
                file_path = os.path.join(root, file)
                print(f"Processing file for incremental vocab: {file_path}")
                print(i)  #for printing file count
                i += 1
                with gzip.open(file_path, 'rt', encoding='utf-8') as f:
                    chunk = f.read()
                    tokens = chunk.split()
                    model.build_vocab([tokens], update=True)  # Incrementally update vocab
                    print(f"Vocabulary updated with {file_path}")

    return model

model_sg = update_vocabulary(preprocessed_dir, model_sg)

# Save the updated model
model_sg.save(updated_vocab_path)
print(f"Updated vocabulary saved to {updated_vocab_path}")
