def search(lst,n):
    loops=0
    for item in lst:
        loops+=1
        if item==n:
            return(True,loops)
    return (False,loops)

if __name__=="__main__":
    integers=[99,88,77,101,203,896,555]
    print(search(integers,101))
    print(search(integers,1001))