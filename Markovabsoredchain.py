from fractions import *
from copy import *
def answer(m):
    if sum(m[0]) == 0:
        count = 1
        for i, v in enumerate(m):
            if sum(v) == 0:
                count += 1
        return [1]*count
    
    elif m[0][0] == sum(m[0]):
        return [1]+[0]*(len(m)-1)+[1]
    else:
        pass    
    d = {}
    terminal = []
    interaction = []
    for i,v in enumerate(m):
        if sum(v) == 0 or v[i] == sum(v):
            terminal.append(i)
        else:
            interaction.append(i)        
        for j in range(0,len(m[0])):
            if m[i][j] != 0:
                d[(i,j)] = Fraction('%s/%s' % (m[i][j], sum(m[i]))) 
    R = [[Fraction(0,1) for i in range(0,len(terminal))] for j in range(0,len(interaction))]
    for i in range(len(interaction)):
        for j in range(len(terminal)):
            if (interaction[i],terminal[j]) in d.keys():
                R[i][j] = d[(interaction[i],terminal[j])]
            else:
                R[i][j] = Fraction(0,1)                
    Q = [[Fraction(0,1) for i in range(0,len(interaction))] for j in range(0,len(interaction))]
    for i in range(0,len(Q)):
        for j in range(0,len(Q)):
            if (interaction[i],interaction[j]) in d.keys():
                Q[i][j] = d[(interaction[i],interaction[j])]
    I = [[Fraction(0,1) for i in range(0,len(interaction))] for j in range(0,len(interaction))]
    for i in range(0,len(Q)):
        for j in range(0,len(Q)):    
            if i==j:
                I[i][j] = Fraction(1,1)   
    aF = [[x-y for x,y in zip(I[i],Q[i])] for i in range(0,len(Q))] 
    F = matrix_ni(aF)
    res = matrixMul(F,R)
    de = [i.denominator for i in res[0]]
    b = reduce(lcm,de)
    num = [i.numerator*b/i.denominator for i in res[0]]
    return num+[sum(num)]
def lcm(a,b):
    return a*b/gcd(a,b)    

def matrixMul(A, B):
    res = [[0] * len(B[0]) for i in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                res[i][j] += A[i][k] * B[k][j]
    return res              
def matrix_ni(matrix):
    extend_matrix = deepcopy(matrix)
    l = len(matrix)
    for i in range(0, l):    
        extend_matrix[i].extend([0]*i)
        extend_matrix[i].extend([1])
        extend_matrix[i].extend([0]*(l-i-1))
    for i in range(0, len(extend_matrix)):    
        if extend_matrix[i][i] == 0:
            for j in range(i, len(extend_matrix)):
                if extend_matrix[j][i] != 0:
                    extend_matrix[i], extend_matrix[j] = extend_matrix[j], extend_matrix[i]
                    break
            if j >= len(extend_matrix):
                print 'Impossible'
                return 0
            break
    for i in range(0, len(extend_matrix)):   
        f = extend_matrix[i][i]
        for j in range(0, len(extend_matrix[i])):    
            extend_matrix[i][j] /= f
        for m in range(0, len(extend_matrix)):
            if m == i:
                continue
            b = extend_matrix[m][i]
            for n in range(0, len(extend_matrix[i])):   
                extend_matrix[m][n] -= extend_matrix[i][n] * b
    for i in range(0, len(extend_matrix)):
        extend_matrix[i] = extend_matrix[i][l:]
    return extend_matrix    
m = [[0,1,0,0,0,1],[4,0,0,3,2,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
m2 =[
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0]
]
m3 =[
    [0, 1, 0, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [0, 0, 3, 1, 0]
]
m4 = [[0,1,0],[0,0,0],[0,0,0]]
m5 = [[0,1],[0,0]]
print answer(m)
print answer(m2)
print answer(m3)
print answer(m4)
print answer(m5)

