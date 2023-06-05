lista=[1,2,3,4,5,6,7,8,9,10]    
nueva=[]     
n=int(input("Introduzca un número entero: "))    
def creador(v, l, n):    
    v=[1,2,3,4,5,6,7,8,9,10]
    l=[]    

    for item in v:    
        if item>n:    
            l.append(item)
        
    return(l)    

total=creador(lista, nueva, n)    
print(total)