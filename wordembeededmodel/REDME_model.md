# Incremental Model Training Script

## Overview

This script incrementally trains a Word2Vec model using preprocessed tokenized text data. The model is updated with new tokens extracted from compressed `.txt.gz` files. The script tracks training progress and performance metrics such as the total number of tokens processed and the time taken for training.

## Purpose

Incremental training of the Word2Vec model is essential for:

- **Model Refinement:** Continuously improving the model by incorporating additional data, which enhances the representation of language in the model.
- **Performance Tracking:** Monitoring the efficiency and effectiveness of the training process to ensure the model is improving over time.
- **Scalability:** Handling large datasets in manageable chunks, which prevents memory overload and supports scalable model training.

## Script Details

- **Model Loading:** The script begins by loading an existing Word2Vec model from the specified `vocab_model_path`.
- **Training Process:** It reads preprocessed tokenized text files from the `preprocessed_dir`, updating the model with tokens from these files.
- **Performance Metrics:** The script tracks and prints the number of tokens processed, the time taken for training, and updates on training progress.
- **Model Saving:** The trained model is saved to the path specified by `model_path`.

## Dependencies

- **Python 3.x**
- **Gensim:** For loading and training the Word2Vec model
- **Standard libraries:** `os`, `gzip`, `time`

Ensure that these libraries are available in your environment. If needed, install them using pip.

## Notes

This script is part of a larger pipeline for developing a custom word embedding model for the Tamil language. It builds upon an initial vocabulary model, incrementally updating it with new data.

The preprocessed datasets should be available in the specified directory. Methods for preprocessing and updating the vocabulary are documented in separate repositories.

## Usage

Run the script with the following parameters:
- `preprocessed_dir`: Path to the directory containing preprocessed tokenized text files.
- `vocab_model_path`: Path to the existing vocabulary model to load.
- `model_path`: Path to save the trained model.

Example:
```python
model_sg = Word2Vec.load(vocab_model_path)
train_model(preprocessed_dir, model_sg)
model_sg.save(model_path)

