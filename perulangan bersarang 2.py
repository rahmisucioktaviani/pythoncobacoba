buku_alamat = [("john doe ", "555-1234") ,("jane smith ", "555-5678") , ("bob johnson" , "555-7890")]
for alamat in buku_alamat :
    for address in alamat :
        print(address)
    print("=================")
              


for i in range(1,6) :
    print(i)
    for j in range(1, i + 1):
        print( i * j ,  end= " " )
    print()