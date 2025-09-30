def adjacency_matrix(matrix):
    print("Adjacency Matrix")
    for i in matrix:
        print(i,end="\n")
def adjecency_list(matrix,vertex):
    print("Adjacency List")
    for i in range(len(vertex)):
        print(f'{vertex[i]}: ',end="")
        for j in  range(len(vertex)):
            if matrix[i][j]:
                print(f'{vertex[j]} ',end="")
        print()
vertex=['A','B','C','D']
matrix=[
    [0,1,1,0],
    [1,0,0,1],
    [1,0,0,1],
    [0,1,1,0]
]
print('Vertex \n',vertex)
adjacency_matrix(matrix)
adjecency_list(matrix,vertex)