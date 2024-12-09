data = [5,6,7,3,1,9,10,2,4,8]
print("data sebelum diurutkan:",data)
for i in range (10-1):
    for j in range (10-1):
        if data[j]>data[j+1]:
            temp = data[j]
            data[j] = data[j+1]
            data[j+1] = temp
print("data setelah diurutkan:",data)
