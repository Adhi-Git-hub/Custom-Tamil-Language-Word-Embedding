# Model Loading and Query Script

## Overview

This script is designed to load a Word2Vec model saved in binary format and perform a similarity query to find the most similar words to a given term. It measures and reports the time taken to load the model.

## Script Details

- **Loading the Model:** The script uses `KeyedVectors.load_word2vec_format()` from the Gensim library to load the pre-trained Word2Vec model saved as a binary file.
- **Measuring Load Time:** The script records the time taken to load the model to monitor performance and efficiency.
- **Similarity Query:** After loading the model, it queries the model to find the most similar words to a specified term ('உலகில்' in this case).

## Purpose

1. **Performance Monitoring:** By measuring the time taken to load the model, you can assess the efficiency and performance of model loading.
2. **Similarity Queries:** The script demonstrates how to use the loaded word vectors to perform similarity queries, which is useful for various NLP tasks such as finding related words or analyzing word semantics.

## Files Used

- **`tamil_WE_SG.bin`**: This is the binary file containing the word vectors for the Tamil Word2Vec model. It is loaded by the script to perform the similarity queries.

## Usage

Run the script to:
1. Load the Word2Vec model from the binary file.
2. Measure and display the time taken to load the model.
3. Query the model for the most similar words to 'உலகில்' (the Tamil word for 'world') and print the results.

##Summary

This script efficiently loads a Word2Vec model from a binary file, measures the loading time, and performs a similarity query. It is useful for evaluating model performance and exploring word relationships in the embedding space.
