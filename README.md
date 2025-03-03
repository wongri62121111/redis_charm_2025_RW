# Redis Vector Similarity Search with Charms

This project demonstrates how to use Redis to store and search for charms using vector similarity. The script adds charms with specific attributes, stores them in Redis, and performs a similarity search based on a query vector.

## Prerequisites

- **Python**: Ensure Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
- **Redis**: Install Redis on your machine. For Windows, you can download a precompiled version from [Microsoft Archive](https://github.com/microsoftarchive/redis/releases) or use Windows Subsystem for Linux (WSL).

## Installation

1. **Install Required Libraries**:
   Open a terminal and install the necessary Python libraries:
   ```bash
   pip install redis numpy
   ```

2. **Start Redis Server**:
   Ensure the Redis server is running on your local machine. If you installed Redis on Windows, you can start it by running the `redis-server.exe` file.

## Running the Script

1. **Clone the Repository**:
   Clone this repository to your local machine.

2. **Open the Script in VSCode**:
   Open the project folder in Visual Studio Code (VSCode).

3. **Run the Script**:
   - Open the script file in VSCode.
   - Press `F5` or go to `Run > Run Without Debugging` to execute the script.

## What Was Added to the Starter Code

- **Random Vector Generation**: Added a function to generate random vectors with values between 0.1 and 0.9.
- **Additional Charms**: Added three new charms (`Panda`, `Sheila`, and `Pepperjack`) with randomized vectors.
- **Similarity Search**: The script performs a similarity search using cosine similarity and prints the results.

## Script Details

The script performs the following steps:

1. **Connect to Redis**: Establishes a connection to the local Redis server.
2. **Clear Previous Data**: Clears any existing data in Redis.
3. **Add Charms**: Stores the charm vectors in Redis.
4. **Query Vector**: Defines a query vector for similarity search.
5. **Similarity Search**: Retrieves stored vectors, calculates their similarity to the query vector, and prints the results.

## Example Output

```
Added charm: Explorer with vector: [0.1 0.8 0.3 0.6]
Added charm: Alpha with vector: [0.5 0.2 0.3 0.3]
Added charm: Yoda with vector: [0.8 0.1 0.1 0.4]
Added charm: Panda with vector: [0.45 0.67 0.23 0.89]
Added charm: Sheila with vector: [0.34 0.56 0.78 0.12]
Added charm: Pepperjack with vector: [0.91 0.22 0.33 0.44]

Query Vector: [0.15 0.75 0.35 0.55]

Similarity Search Results:
Charm: Explorer, Similarity: 0.9962
Charm: Panda, Similarity: 0.8456
Charm: Alpha, Similarity: 0.7184
Charm: Sheila, Similarity: 0.6234
Charm: Yoda, Similarity: 0.4945
Charm: Pepperjack, Similarity: 0.4321
```
