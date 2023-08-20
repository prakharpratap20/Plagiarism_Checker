## Plagiarism Detection Script Documentation

### Introduction
This script performs plagiarism detection on a collection of text documents using the TF-IDF (Term Frequency-Inverse Document Frequency) vectorization technique and cosine similarity metric. It calculates the similarity between pairs of text documents and identifies potential instances of plagiarism.

### Prerequisites
1. **Python:** Make sure you have Python installed on your system.
2. **Required Libraries:** This script uses the `os` module for file operations and the `sklearn` library for TF-IDF vectorization and cosine similarity calculations.

### Usage
1. Place the script in the directory containing the text files you want to analyze for plagiarism.
2. Ensure that the text files to be analyzed have the `.txt` extension.
3. Run the script using a Python interpreter (e.g., `python plagiarism_detector.py`).

### Script Overview
The script follows these main steps:

1. **File Loading and Text Extraction:**
    - It retrieves a list of text files with the `.txt` extension present in the same directory as the script.
    - For each text file, it reads the content and stores it in the `user_notes` list.

2. **Vectorization Function:**
    - The `vectorize` function takes a list of text documents as input and converts them into TF-IDF vectors using the `TfidfVectorizer` class from `sklearn`.
    - It returns a matrix of TF-IDF vectors corresponding to the input text documents.

3. **Similarity Calculation Function:**
    - The `similarity` function calculates the cosine similarity between two input vectors.
    - It uses the `cosine_similarity` function from the `sklearn.metrics.pairwise` module.
    - The function returns the cosine similarity score between the two input vectors.

4. **Vectorization of User Notes:**
    - The script vectorizes the `user_notes` using the `vectorize` function, resulting in a matrix of TF-IDF vectors representing each document.

5. **Plagiarism Detection:**
    - The script initializes an empty list named `plagiarism_results` to store tuples of document names and their similarity scores.

6. **Plagiarism Check Function:**
    - The `check_plagiarism` function iterates through each pair of documents and calculates their similarity scores.
    - If the similarity score between two documents exceeds a certain threshold, they are considered potential instances of plagiarism.
    - The function returns a list of tuples containing document names and similarity scores.

7. **Performing Plagiarism Check and Printing Results:**
    - The script invokes the `check_plagiarism` function to perform the plagiarism check and stores the results in the `plagiarism_results` list.
    - The script then iterates through the `plagiarism_results` list and prints the detected plagiarism pairs along with their similarity scores.

### Conclusion
This script provides a functional example of how to perform basic plagiarism detection using TF-IDF vectorization and cosine similarity. However, it's important to note that plagiarism detection is a complex task that may require more sophisticated algorithms and techniques for accurate results in real-world scenarios.