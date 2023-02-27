def number_of_groups(n, k):
    
    def factorial_n (n):
        if n == 0:
            return 1
        else:
            print (n)
            return n * factorial_n(n-1)
    fac_n = factorial_n(50)
    print (fac_n)

    def factorial_k (k):
        if k == 0:
            return 1
        else:
            print (k)
            return k * factorial_k(k-1)
        
    fac_k = factorial_k(7)
    print (fac_k)

    def factorial_nk (nk):
        if (n-k) == 0:
            
            return 1
        else:
            print (nk)
            return (n-k) * factorial_nk((n-k)-1)
    fac_nk = factorial_nk(43)
    print (fac_nk)

result = number_of_groups(50, 7)
print (result)

c = fac_n()/(fac_nk()*fac_k())  
print(c)