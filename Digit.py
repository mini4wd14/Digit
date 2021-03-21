def digitAwal(x,y):
    temp = str(x**y)    #convert x pangkat y menjadi string agar dapat di print karakter ke-sekian
    return temp[0]  #return ke karakter pertama

def digitAkhir(x,y):
    temp = str(x**y)    #convert x pangkat y menjadi string agar dapat di print karakter ke-sekian
    return temp[-1] #return ke karakter terakhir

print(digitAwal(10,8))
print(digitAwal(2,3))
print(digitAwal(6,3))

print(digitAkhir(10,8))
print(digitAkhir(2,3))
print(digitAkhir(6,3))

    