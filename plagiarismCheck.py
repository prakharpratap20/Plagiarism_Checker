import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Step 1: Load and Extract Text from Files
user_files = [doc for doc in os.listdir() if doc.endswith(".txt")]
user_notes = [open(_file, encoding="utf-8").read() for _file in user_files]

# Step 2: Vectorization Function
def vectorize(Text):
    return TfidfVectorizer().fit_transform(Text).toarray()

# Step 3: Similarity Calculation Function
def similarity(doc1, doc2): 
    return cosine_similarity([doc1], [doc2])[0][0]

# Step 4: Vectorization of User Notes
vectors = vectorize(user_notes)
s_vectors = list(zip(user_files, vectors))

# Step 5: Plagiarism Detection
plagiarism_results = []

# Step 6: Plagiarism Check Function
def check_plagiarism():
    global s_vectors, plagiarism_results
    for i, (student_a, text_vector_a) in enumerate(s_vectors):
        for j, (student_b, text_vector_b) in enumerate(s_vectors):
            if i != j:
                sim_score = similarity(text_vector_a, text_vector_b)
                student_pair = sorted((student_a, student_b))
                score = (student_pair[0], student_pair[1], sim_score)
                plagiarism_results.append(score)
    return plagiarism_results

# Perform Plagiarism Check
plagiarism_results = check_plagiarism()

# Print Plagiarism Results
for doc1, doc2, sim_score in plagiarism_results:
    print(f"Plagiarism detected between '{doc1}' and '{doc2}', Similarity Score: {sim_score:.4f}")
