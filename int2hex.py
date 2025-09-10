def int_to_hexa(int_code):
    hex_digits="0123456789ABCDEF"
    if int_code==0:
        return "0"
    result=''
    while int_code>0:
        remainder=int_code%16
        result=hex_digits[remainder]+result
        int_code=int_code//16
    return result
if __name__=="__main__":
    int_code=12
    hexadecimal_code=int_to_hexa(int_code)
    print(int_code,'converts to',hexadecimal_code)

    int_code=16
    hexadecimal_code=int_to_hexa(int_code)
    print(int_code,'converts to',hexadecimal_code)

    int_code=255
    hexadecimal_code=int_to_hexa(int_code)
    print(int_code,"converts to",hexadecimal_code)


