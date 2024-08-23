import time
from gensim.models import KeyedVectors

# Start the timer
start_time = time.time()

# Load the binary model
word_vectors = KeyedVectors.load_word2vec_format('C:\\Users\\adhit\\Documents\\projects\\badwordsproject\\finalmodel\\tamil_WE_SG.bin', binary=True)

# Stop the timer
end_time = time.time()

# Calculate loading time
loading_time = end_time - start_time
print(f"Model loading completed in {loading_time:.2f} seconds")
# %%
words = word_vectors.most_similar('உலகில்')
print(words)


# %%
