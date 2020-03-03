# -*- coding: utf-8 -*-

import numpy as np


def jacobi(a,b,x,X):
    d = np.diag(a)
    D = np.diagflat(d)
    R = a - D
    i = 0
    while np.linalg.norm(x-X) >= 0.01:
        x = (b-R.dot(x))/d
        i = i + 1
    return x,i

def gauss_seidel(a,b,x,X):
    L = np.tril(a,k=0)
    U = np.triu(a,k=1)
    i = 0
    while np.linalg.norm(x-X) >= 0.01:
        x = np.linalg.solve(L,b-U.dot(x))
        i = i + 1
    return x,i

def relaxation(a,b,x,X,w):
    L = np.tril(a,k=-1)
    D = np.diagflat(np.diag(a))
    U = np.triu(a,k=1)
    i = 0
    while np.linalg.norm(x-X) >= 0.01:
        x = np.linalg.solve(D+w*L,w*b - np.dot(w*U + (w-1)*D,x))
        i = i + 1
    return x,i

def conjugate_gradient(a,b,x,X):
    r = b - a.dot(x)
    p = r
    i = 0
    while np.linalg.norm(r) >= 0.1:
        i = i + 1
        alpha = r.dot(r)/(p.dot(A.dot(p)))
        x = x + alpha*p
        r_new = r - alpha*A.dot(p)
        beta = r_new.dot(r_new)/(r.dot(r))
        p = r_new + beta*p
        r = r_new
    return x,i



X = np.array([7.859713071,0.422926408,-0.073592239,-0.540643016,0.010626163])

A = np.array([[0.2,0.1,1,1,0],[0.1,4,-1,1,-1],[1,-1,60,0,-2],[1,1,0,8,4],[0,-1,-2,4,700]])

B = np.array([1,2,3,4,5])


x = np.zeros(X.shape)
x,i = jacobi(A,B,x,X)
print("Jacobi Method result:\n")
print("X = ", x)
print("Number of iterations = ",i,"\n")

x = np.zeros(X.shape)
x,i = gauss_seidel(A,B,x,X)
print("Gauss-Seidel Method result:\n")
print("X = ", x)
print("Number of iterations = ",i,'\n')

x = np.zeros(X.shape)
w = 1.25
x,i = relaxation(A,B,x,X,w)
print("Relaxation Method result: (w = 1.25)\n")
print("X = ", x)
print("Number of iterations = ",i,'\n')

x = np.zeros(X.shape)
x,i = conjugate_gradient(A,B,x,X)
print("Conjugate Gradient Method result:\n")
print("X = ", x)
print("Number of iterations = ",i,'\n')

