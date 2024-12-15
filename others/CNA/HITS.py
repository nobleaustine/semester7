import numpy as np
from fractions import Fraction

def hits_algorithm(adj_matrix, max_iter=100, tol=1e-6):
    n = adj_matrix.shape[0]
    hubs = np.ones(n)
    authorities = np.ones(n)
    
    for i in range(max_iter):
        new_authorities = np.dot(adj_matrix.T, hubs)
        new_hubs = np.dot(adj_matrix, authorities)
        new_authorities /= np.sum(new_authorities)
        new_hubs /= np.sum(new_hubs)
        
        print(f"Iteration {i+1}:")
        print("Authority scores:", [f"{Fraction(x).limit_denominator()}" for x in new_authorities])
        print("Hub scores:", [f"{Fraction(x).limit_denominator()}" for x in new_hubs])
        print("-" * 30)
        
        if (np.linalg.norm(new_authorities - authorities, ord=1) < tol and
            np.linalg.norm(new_hubs - hubs, ord=1) < tol):
            break
        
        authorities = new_authorities
        hubs = new_hubs
    
    return hubs, authorities

if __name__ == "__main__":
    adj_matrix = np.array([
        [0, 1, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
        [0, 0, 0, 0]
    ])
    
    hubs, authorities = hits_algorithm(adj_matrix)
    print("Final Hub scores:", [f"{Fraction(x).limit_denominator()}" for x in hubs])
    print("Final Authority scores:", [f"{Fraction(x).limit_denominator()}" for x in authorities])
