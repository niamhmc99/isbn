def is_valid(isbn):
    isbn = isbn.replace('-', '').replace('', '')
    if len(isbn) !=10:
        return False
    sum = 0
    for idx, char in enumerate(isbn):
        if (idx==9) and (char=='X'):
            val = 10
        else: 
            try:
            	val = int(char)
            except:
                return False
        sum += val*(10-idx)
    if sum%11==0:
        return True
    else:
        return False





