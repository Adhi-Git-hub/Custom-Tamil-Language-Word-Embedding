# Preprocessing Tamil Text for Word Embedding

This script is designed to preprocess Tamil text data by tokenizing the text into individual words, specifically focusing on Tamil words, and saving these tokens in compressed chunks. The output is saved in a specified directory in `.txt.gz` format, making it ready for subsequent stages of processing, such as building vocabularies or training word embedding models.

## Script Overview

The script performs the following key functions:
1. **Tokenization of Tamil Text**: It extracts Tamil words from the text files in the specified input directory using regular expressions designed for Tamil Unicode characters.
2. **Chunk Processing**: The script processes the text data in chunks to efficiently handle large datasets, ensuring that memory usage is optimized.
3. **Compressed File Output**: The tokens are saved in compressed `.txt.gz` files to reduce storage space while maintaining easy access for further processing.

## Key Components

### 1. Directory Paths
- **Input Directory (`input_dir`)**: Specifies the location of the raw text files to be processed.
- **Output Directory (`output_dir`)**: Specifies where the preprocessed tokens will be saved.

### 2. Tamil Word Extraction
- **Regular Expression (`tamil_word_regex`)**: This regex pattern matches Tamil words using the Unicode range for Tamil characters (`\u0B80-\u0BFF`).
- **`is_tamil(word)` Function**: Checks if a word consists only of Tamil characters.
- **`tokenize_tamil_text(text)` Function**: Extracts all Tamil words from a given text line.

### 3. Preprocessing and Saving Tokens
- **`preprocess_and_save(directory, output_directory, chunk_size)` Function**:
  - Iterates through all text files in the input directory.
  - Tokenizes the text to extract Tamil words.
  - Accumulates tokens and saves them in chunks of a specified size (`chunk_size`) to compressed `.txt.gz` files in the output directory.
  - The script also prints the progress and file count to the console.

- **`save_tokens_to_compressed_file(tokens, output_directory, count)` Function**:
  - Saves a list of tokens to a compressed file, named according to the chunk count, in the specified output directory.

## How to Use the Script

1. **Set the Directory Paths**:
   - Update the `input_dir` and `output_dir` variables with the correct paths for your dataset and output location.

2. **Run the Script**:
   - The script can be run directly from a Python environment.
   - The `chunk_size` parameter can be adjusted to change the number of tokens processed per file. The default value is `5000000`.

3. **Output**:
   - The output will be saved in the specified `output_dir` as compressed files named `tokens_chunk_X.txt.gz`, where `X` is the chunk number.

## Dependencies

- **Python 3.x**
- **Standard libraries**: `os`, `re`, `gzip`

Ensure these libraries are available in your environment. If needed, install them using `pip`.

## Notes

- This script is part of a larger pipeline for building a custom word embedding model for the Tamil language. It is specifically focused on the preprocessing stage, where raw text data is cleaned and prepared for further processing.
- The datasets used for this script should be placed in the `wordembdataset` folder, which has already been prepared and collected as part of the project. Methods for collecting and scraping the datasets are detailed in a separate repository.

