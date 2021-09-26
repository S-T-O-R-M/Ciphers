charset="ABCDEFGHIJKLMNOPQRSTUVWXYZ"


ciphertext=input("Enter the Ciphertext\n")
ciphertext = "".join(e for e in ciphertext.upper() if e.isalpha())
print(ciphertext)



def decrypt():
    potentialPlainText=""
    for shift in range(0,26):
        for x in ciphertext:
            potentialPlainText+=charset[(charset.index(x)+ shift)%len(charset)]
        print ("Forward Shift with "+str(shift)+" "+potentialPlainText)
        potentialPlainText=""
    

decrypt()
