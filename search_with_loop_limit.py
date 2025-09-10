def search_with_loop_limit(sorted_lst,n):
    loops=0
    left=0
    right=len(sorted_lst)-1

    while left<=right and loops<10:
        loops+=1
        mid=(left+right)//2
        if sorted_lst[mid]==n:
            return (True,loops)
        loops+=1
        if sorted_lst[mid]<n:
            left=mid+1
        else:
            right=mid-1
    return (False,loops)

if __name__=="__main__":
    integers=[77,88,99,101,203,555,896]
    print(search_with_loop_limit(integers,101))
    print(search_with_loop_limit(integers,1001))
        
