# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from itertools import combinations, permutations

def permutacion(arr=[]):
    
    permutacions = list(permutations(arr))
    #imprimir = print(permutacions)
    return permutacions
    
#fin funcion permutacion  

def factorial(numero):
    fact = 1
    for i in range(1, numero + 1):  
        fact = fact * i 
        #resul = print ("el factorial de ", numero ," es: ", fact)
    return fact
#fin funcion factorial

def combinacion(arr=[]):
    r=len(arr)
    a=r-1
    comb = list(combinations(arr,a))
    #imp=print(comb)
    return comb
    
#fin funcion combinacion    

def union(arr1=[], arr2=[]):
    imp2 = sorted(arr1 + arr2)
    #set1 = {2, 4, 5, 6} 
    #set2 = {4, 6, 7, 8} 
    #set3 = {7, 8, 9, 10}
    #imp2 = arr1.union(arr2)
    #imp=print("set1 U set2 : ", set1.union(set2)) 
    #print("set1 U set2 U set3 :", set1.union(set2, set3))
    return imp2
#fin funcion union        
        
def interseccion(arr1=[], arr2=[]):
    #setA = {1, 2, 3, 4, 5}
    #setB = {0, 2, 4, 6}
    imp = sorted(list(filter(lambda x:x in arr1,arr2)))
    #imp=print(setA & setB)
    #print(imp)
    return imp
#fin funcion interseccion
        
def diferencia(arr1=[], arr2=[]):
    #set1 = set([1,2,3,4,5,6])
    #set2 = set([2,3,6,8])

    #diff_set = set(set1) ^ set(set2)       #otro metodo para encontrar la diferencia
    a = list(set(arr1) - set(arr2))
    b = list(set(arr2) - set(arr1))
    imp = sorted(a+b)
    #imp=print(diff_set)
    return imp
#fin funcion diferencia

def potencia(numero1, numero2):
    imp = numero1 ** numero2
    return imp
    
#fin funcion potencia

def binominal(n, x, p):
    #F=p
    C=p
    D=p
    A=1
    E=1
    for i in range(x): #exponente
        A *= C

    B=1-D
    for i in range(n-x): #exponente
        E *= B

    #resultado = A*E
    imp = A*E
    #print("La distribucion binominal es"+resultado+"\n")
    #imp=print(f"""
    #({n})     {x}      {n}-{x}
    #({x}) * {F}^  *({1}-{F})^  = {resultado}
    #""")
    return imp
#fin funcion binomial

def geometrica(x, p):
    C=p
    A=1-p

    R= A**x
    Resultado=C*R
    #print("La distribucion geometrica es:")
    imp=Resultado
    #imp=print(Resultado)
    return imp
#fin funcion geometrica

def poisson(media, exitos):
    e=2.7182818284590452
    C=exitos

    R1=1
    for i in range(C): #exponente
        R1 *= media

    R2=e**-C

    fact = 1
    for i in range(1, C + 1):  
        fact = fact * i

    Resultado = (R1*R2)/fact
    #print("Distribucion poisson: ")
    imp=Resultado
    #imp=print(Resultado)
    return imp
#fin funcion poisson




