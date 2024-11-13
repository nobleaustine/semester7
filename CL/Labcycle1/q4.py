# 4. Implement the Minimum Edit Distance algorithm to find the edit distance between any
#    two given strings. Also, list the edit operations.
from tabulate import tabulate
import re

def MED(string1,string2):

    N = len(string2) + 2
    M = len(string1) + 2
    start = "\033[92m"
    end = "\033[0m"

    string1 = "##"+string1
    string2 = "##"+string2

    # Initialization
    matrix = [[0 for _ in range(N)] for _ in range(M)]
    mat = [[0 for _ in range(N)] for _ in range(M)]
    N=N-1
    M=M-1
    for i,letter in enumerate(reversed(string1)):
          matrix[i][0] = letter
          mat[i][0] = letter
          if M-i-1 > 0: 
               matrix[i][1] = M-i-1
               mat[i][1] = M-i-1

    # calculating minimum distance
    for j,letter in enumerate(string2):
          matrix[M][j] = letter
          mat[M][j] = letter
          if j-1>=0: 
               matrix[M-1][j] = j-1
               mat[M-1][j] = j-1
               
    # print(tabulate(matrix, tablefmt="grid"))
    # print(tabulate(mat, tablefmt="grid"))

    string1=string1[2:]
    string2=string2[2:]

    # operation matrix
    for i in range(M-2,-1,-1):
         for j in range(2,N+1):
              same = 0 if matrix[i][0]==matrix[M][j] else 2
              d = matrix[i+1][j]+1
              ins = matrix[i][j-1]+1
              s = matrix[i+1][j-1]+same
              matrix[i][j]=min(d,ins,s)
              if d==ins==s:
                   mat[i][j]="--/|"
              elif matrix[i][j]==d==ins:
                   mat[i][j]="--|"
              elif matrix[i][j]==d==s:
                   mat[i][j]="/|"
              elif matrix[i][j]==ins==s:
                   mat[i][j]="--/"
              elif matrix[i][j]==d:
                   mat[i][j]="|"
              elif matrix[i][j]==ins:
                   mat[i][j]="--"
              elif matrix[i][j]==s:
                   mat[i][j]="/"

    # drawing operation path
    row =0
    col =N
    while row!=M and col!=0:
         pattern = mat[row][col]
         if isinstance(pattern, int): pattern = str(pattern)
         mat[row][col]=start + pattern + end
         if re.search(r"[/]",pattern):
              row = row + 1
              col = col - 1
         elif re.search(r"[--]",pattern):
              col = col - 1 
         elif re.search(r"[|]",pattern):
              row = row + 1
         elif re.search(r"[1]",pattern):
               if mat[row+1][col] == 0:
                    row = row + 1
               else:
                    col= col - 1
         else:
              row = row + 1
              col = col - 1
              
    print(tabulate(matrix, tablefmt="grid"))  
    print(" ")       
    print(tabulate(mat, tablefmt="grid"))

if __name__=="__main__":
    # MED("INTENTION","EXECUTION") 
    print(" ")
    print("          Minimum Edit Distance")  
    string1 = input("Enter string1: ")
    string2 = input("Enter string2: ")
    print(" ")
    MED(string1,string2)
    print(" ")
