Resume Shortlister

Developed By:
B Ayshwarya, C B Ananya and Gayathri Venkatesan

Overview:

In the context of resume shortlisting, manually screening a large volume of resumes poses significant challenges, particularly in the initial or level 0 screening phase. The sheer quantity of incoming resumes makes it impractical for recruiters to thoroughly evaluate each one, leading to potential oversights and an inefficient use of time. Additionally, the unstructured nature of resume data, coupled with variations in formats, makes it difficult to extract consistent and relevant information manually.

Resume Shortlister addresses these challenges by automating the screening process for level 0 evaluations. With the Knuth-Morris-Pratt algorithm and PySpark's distributed computing capabilities, it efficiently scans resumes for predefined keywords associated with the job description. This automated approach not only accelerates the screening process but also ensures a consistent and objective evaluation, mitigating the limitations of manual screening in handling large datasets and diverse resume formats at the initial screening stage.

Functionality:

The project performs the following key tasks:

1. Keyword Definition:
   - Defines a set of keywords representing the skills and qualifications expected in a data scientist resume.

2. Keyword Matching Algorithm:
   - Implements a variation of the Knuth-Morris-Pratt (KMP) algorithm to efficiently search for keyword occurrences in the resume text.

3. Resume Processing:
   - Reads PDF files from the specified HDFS directory (/dataset2/).
   - Converts PDF data to text format for analysis.
   - Computes a resume score based on the frequency of data scientist keywords in the resume.

4. Resume Evaluation:
   - Applies the KMP-based scoring algorithm to evaluate each resume in the dataset.

5. Sorting and Shortlisting:
   - Ranks resumes based on their computed scores in descending order.
   - Selects the top 5 resumes with the highest scores for further consideration.

6. Result Storage:
   - Copies the shortlisted resumes to a new directory in HDFS (/shortlisted2/).

Usage:

Ensure that the necessary dependencies are installed and the Hadoop cluster is correctly configured. The provided code assumes access to an HDFS cluster and a PySpark environment.

Example Usage:
from pyspark import SparkContext

Create a SparkContext
sc = SparkContext.getOrCreate()

... (Copy and paste the provided code here)

Stop the SparkContext
sc.stop()

Dependencies:

- PySpark
- PyPDF2
- hdfs3

Configuration:

- Modify the HDFS connection details in the code ('localhost') to match your Hadoop cluster configuration.
- Adjust the keyword set (data_scientist_keywords) as needed for different job descriptions.

Notes:

- Ensure that the HDFS directories (/dataset2/ and /shortlisted2/) exist before running the code.
- This README assumes basic familiarity with PySpark, Hadoop Distributed File System, and the Knuth-Morris-Pratt algorithm.

Feel free to customize the code and configuration based on your specific requirements and environment. Happy resume shortlisting!
