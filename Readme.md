##
Discussion: Efficient Log Retrieval
Approaches Considered
1. Brute Force (Inefficient)
Read the entire file line by line and check for the given date.
Issue: Slow and consumes too much memory.
2. Optimized Approach (Chosen)
Use memory-efficient streaming to process the file line by line.
Store results in an output file instead of keeping all data in memory.

Final Solution Summary
Streaming method ensures minimal memory usage.
Efficient filtering using Python’s startswith() avoids unnecessary processing.
Direct output writing prevents excessive memory usage.

Steps to Run
Clone the repository:

git clone https://github.com/Yashika-Singh-Panwar/tech-campus-recruitment-2025.git  

Navigate to the repository:

cd tech-campus-recruitment-2025  
Run the script:

python src/extract_logs.py YYYY-MM-DD  

Performance Optimization
Uses stream processing instead of loading the entire file into memory.
Optimized for sequential disk access.
Suitable for large files (~1TB).





