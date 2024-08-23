# Vocabulary Update Script

## Overview

This script updates an existing Word2Vec vocabulary model by incrementally adding new words from preprocessed text data. The script loads an initial vocabulary model and updates it with additional tokens extracted from compressed `.txt.gz` files.

## Purpose

Updating the vocabulary model is essential for the following reasons:

- **Model Improvement:** Incremental updates refine the vocabulary by including new terms found in additional data. This ensures that the vocabulary remains comprehensive and up-to-date.
- **Efficiency:** Incremental updates allow for gradual improvements to the vocabulary without the need to rebuild the model from scratch, saving time and computational resources.
- **Adaptability:** By incorporating new data, the model adapts to changes in the dataset and reflects the evolving language use within the target domain.

## Script Details

- **Initial Model:** The script starts by loading an initial Word2Vec model from the specified `initial_vocab_path`.
- **Update Process:** It reads preprocessed tokenized text files from the `preprocessed_dir`, updating the vocabulary with tokens from these files.
- **Final Model:** The updated model is saved to the path specified by `updated_vocab_path`.

## Dependencies

- **Python 3.x**
- **Gensim:** For loading and updating the Word2Vec model
- **Standard libraries:** `os`, `gzip`

Ensure that these libraries are available in your environment. If needed, install them using pip.

## Notes

This script is part of a larger pipeline for developing a custom word embedding model for the Tamil language. The vocabulary update is performed after an initial vocabulary model has been built and saved.

The datasets used for this script should be preprocessed and stored in the specified directory. Methods for preprocessing and dataset collection are documented in a separate repository.

## Usage

Run the script with the following parameters:
- `preprocessed_dir`: Path to the directory containing preprocessed tokenized text files.
- `initial_vocab_path`: Path to the initial vocabulary model.
- `updated_vocab_path`: Path to save the updated vocabulary model.

Example:
```python
model_sg = Word2Vec.load(initial_vocab_path)
model_sg = update_vocabulary(preprocessed_dir, model_sg)
model_sg.save(updated_vocab_path)

