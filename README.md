# I24 Benchmarking Inserts

## Benchmarking and optimizing data insertion times to MongoDB with Python threading.
This Python module is developed for the [I24-MOTION testbed](https://i24motion.org/) data processing pipeline. 

### Motivation
To determine the most efficient method for inserting data into MongoDB using Python and to guarantee that the data insertion rate matches or surpasses the rate of data collection from the cameras.

### Result
Implementing MongoDB single-document insertions with Python threading led to a 13% performance improvement compared to multi-document insertions of the same size, meeting the data collection speed.

<img width="739" alt="insert_benchmarks" src="https://github.com/lisaliuu/i24-benchmarking-inserts/assets/82255401/73511e0d-7f2c-49c5-84df-9b3af3d66462">
