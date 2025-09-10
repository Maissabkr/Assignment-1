def is_prime(n):
    if n<=1:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            return False
    return True

if __name__=="__main__":

    def list_prime(n):
        p=[]
        for i in range(1,n):
            if is_prime(i):
                p.append(i)
        return p
    print(list_prime(10000))


        
    