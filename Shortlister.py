import PyPDF2
from collections import Counter
from pyspark import SparkContext
import hdfs3

# Create a SparkContext
sc = SparkContext.getOrCreate()

# Define data scientist resume expectations
data_scientist_keywords = [
    "machine learning",
    "artificial intelligence",
    "data science",
    "algorithms",
    "natural language processing",
    "speech recognition",
    "computer vision",
    "deep learning",
    "big data",
    "data analytics",
    "business intelligence",
    "data mining",
]

# Create functions to mimic KMP algorithm
def calculate_lps_array(pattern):
    lps = [0] * len(pattern)
    i = 0
    j = 1

    while j < len(pattern):
        if pattern[i] == pattern[j]:
            lps[j] = i + 1
            i += 1
            j += 1
        else:
            if i == 0:
                lps[j] = 0
                j += 1
            else:
                i = lps[i - 1]

    return lps

def search_keyword(pattern, text):
    lps = calculate_lps_array(pattern)
    i = 0
    j = 0
    occurrences = 0

    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1

            if j == len(pattern):
                occurrences += 1
                j = lps[j - 1]
        else:
            if j == 0:
                i += 1
            else:
                j = lps[j - 1]

    return occurrences

# Extract text from each PDF file and calculate its score based on data scientist keywords
def process_resume_with_kmp(filename):
    # Connect to the HDFS cluster
    client = hdfs3.InsecureClient('localhost')

    # Read the contents of the PDF file from HDFS
    file_data = client.read('/dataset2/' + filename)

    # Convert the file data to a string
    file_text = file_data.decode('utf-8')

    spark_rdd = sc.parallelize(file_text)

    # Process the file text and calculate the resume score
    keyword_scores = []
    for keyword in data_scientist_keywords:
        occurrences = search_keyword(keyword, file_text)
        keyword_scores.append(occurrences)

    spark_rdd.collect()
    resume_score = sum(keyword_scores) / len(data_scientist_keywords)
    return filename, resume_score

def process_resume_without_kmp(filename):
    # Connect to the HDFS cluster
    client = hdfs3.InsecureClient('namenode.example.com')

    # Read the contents of the PDF file from HDFS
    file_data = client.read('/dataset2/' + filename)

    # Convert the file data to a string
    file_text = file_data.decode('utf-8')

    # Process the file text and calculate the resume score
    keyword_counts = Counter(file_text.split())
    total_occurrences = sum(keyword_counts.values())
    resume_score = total_occurrences / len(data_scientist_keywords)
    return filename, resume_score

# Evaluate resumes using KMP algorithm
resume_scores = {}
for filename in sc.textFile("/dataset2/").collect():
    resume_scores[filename] = process_resume_with_kmp(filename)[1]

# Sort resumes by score in descending order
sorted_scores = sorted(resume_scores.items(), key=lambda item: item[1], reverse=True)

# Create a list of shortlisted filenames
shortlisted_filenames = [item[0] for item in sorted_scores[:5]]

# Copy the shortlisted PDF files from HDFS to the /shortlisted2 directory in HDFS
for filename in shortlisted_filenames:
    client.copyFromLocalFile('/dataset2/' + filename, '/shortlisted2/' + filename)

