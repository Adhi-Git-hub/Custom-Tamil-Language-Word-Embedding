from gensim.models import Word2Vec

# Load your existing model
model = Word2Vec.load('path\\model\\tamil_word2vec_sg.model')
print("model loaded")
# Save the model as a single binary file
model.wv.save_word2vec_format('path\\finalmodel\\tamil_WE_SG.bin', binary=True)
