# i24-benchmarking

i24-benchmarking repository tests insert times of MongoDB.

## Overview
- **graphing**: graphs write time in seconds against  increasing doc size and against increasing number of docs in the collection.

![alt text](https://github.com/lisaliuu/i24-benchmarking-inserts/blob/main/graphs/insert_one_graph.png)

- **test_write_methods**: tests the speed of batch_inserts and threaded insert_ones.

*thread.py used by test_thread_methods.py*

![alt text](https://github.com/lisaliuu/i24-benchmarking-inserts/blob/main/graphs/dif_methods_graph.png)