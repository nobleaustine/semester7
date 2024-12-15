# Define the transition matrix
transition_matrix = [
    [0, 1, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 0],
    [0, 1, 0, 0]
]

# Parameters
alpha = 0.85  # damping factor
n = len(transition_matrix)  # number of pages
epsilon = 1e-6  # convergence threshold

# Handle dangling nodes (rows that sum to 0)
for i in range(n):
    row_sum = sum(transition_matrix[i])
    if row_sum == 0:
        transition_matrix[i] = [1 / n for _ in range(n)]  # Replace with uniform distribution

# Normalize the transition matrix to ensure stochasticity
for i in range(n):
    row_sum = sum(transition_matrix[i])
    if row_sum > 0:
        transition_matrix[i] = [value / row_sum for value in transition_matrix[i]]

# Add the teleportation factor to create the Google matrix
teleportation_matrix = [[1 / n for _ in range(n)] for _ in range(n)]
google_matrix = [[0 for _ in range(n)] for _ in range(n)]  # Initialize empty Google matrix
for i in range(n):
    for j in range(n):
        google_matrix[i][j] = (1-alpha )* transition_matrix[i][j] + (alpha) * teleportation_matrix[i][j]


# Initialize the PageRank vector
pagerank = [1 , 0, 0, 0]  # Start with the first node

# Iterative computation
iteration = 0
while True:
    new_pagerank = [0] *n
    # Calculate the new PageRank vector
    for i in range(n):
        new_pagerank[i] = 0  # Initialize the sum for the ith node
        for j in range(n):
            new_pagerank[i] += google_matrix[j][i] * pagerank[j]  # Accumulate the contributions

    
    # Calculate the difference (L1 norm)
    diff = sum(abs(new_pagerank[i] - pagerank[i]) for i in range(n))
    
    # Update the PageRank vector
    pagerank = new_pagerank
    print(f"Iteration {iteration}: {pagerank}")
    iteration += 1
    
    # Check convergence
    if diff < epsilon:
        break

print("\nFinal PageRank:", pagerank)
