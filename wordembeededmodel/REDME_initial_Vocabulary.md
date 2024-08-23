# Initial Vocabulary Model Builder

## Overview

This script is responsible for creating an initial vocabulary model from preprocessed text data. The vocabulary model serves as a foundational component in building a more comprehensive word embedding model. The initial vocabulary is built using tokenized text data stored in compressed `.txt.gz` files.

## Purpose

The initial vocabulary model is crucial for several reasons:

- **Vocabulary Initialization:** It provides a preliminary set of words and their frequencies that will be used to initialize the Word2Vec model. This is a necessary step before training the model with the full dataset.
- **Sample Representation:** By using a sample of preprocessed files, we can quickly build a vocabulary that represents the common terms in the dataset. This helps in speeding up the training process and ensuring that the model has a solid starting point.
- **Efficiency:** Building an initial vocabulary with a smaller sample allows for faster iterations and adjustments. Once the vocabulary is established, it can be used to build a more robust model with the full dataset.

## Script Details

- **Path to Preprocessed Files:** The script reads preprocessed tokenized text files from the directory specified by `preprocessed_dir`.
- **Initial Vocabulary Path:** The vocabulary model is saved to the path specified by `initial_vocab_path`.

## Dependencies

- **Python 3.x**
- **Gensim:** For building the Word2Vec model
- **Standard libraries:** `os`, `gzip`

Ensure that these libraries are available in your environment. If needed, install them using pip.

## Notes

This script is part of a larger pipeline for building a custom word embedding model for the Tamil language. The vocabulary model created here is a preliminary version that will be updated and refined during the full model training phase.

The datasets used for this script should be preprocessed and stored in the specified directory. The preprocessing stage and dataset collection methods are documented in a separate repository.

## Usage

Run the script with the following parameters:
- `preprocessed_dir`: Path to the directory containing preprocessed tokenized text files.
- `sample_size`: Number of sample files to use for building the initial vocabulary.

Example:
```python
build_initial_vocabulary(preprocessed_dir, sample_size=1)

