#x = 1010101010101010101
#y = 1100110011001100110011
#z = 11100001111000011110000

# registerX=input("Enter contents of X \n")
# registerY=input("Enter contents of Y \n")
# registerZ=input("Enter contents of Z \n")

keyStreamBits = []
ciphertext = []

registerX=[int(x) for x in '1010101010101010101']
registerY=[int(y) for y in '1100110011001100110011']
registerZ=[int(z) for z in '11100001111000011110000']
plaintext=[ int(p) for p in bin(15)[2:]]


if(len(registerX)==19 and len(registerY)==22 and len(registerZ)==23):

    keystreamRequirement=int(input("Number of Keystream Bits Needed? \t\t"))


    while(keystreamRequirement > 0):
        clockingBits=[registerX[8],registerY[10],registerZ[10]]
        m = max(set(clockingBits),key=clockingBits.count)
        
        if(clockingBits[0] == m):
            tX = registerX[13]^registerX[16]^registerX[17]^registerX[18]
            
            for i in range(len(registerX)-1,-1,-1):
                if i==0:
                    registerX[0] = tX
                else:
                    registerX[i]=registerX[i-1]
        
        if(clockingBits[1] == m):
            tY = registerY[20]^registerY[21]
            
            for i in range(len(registerY)-1,-1,-1):
                if i==0:
                    registerY[0] = tY
                else:
                    registerY[i]=registerY[i-1]
        
        if(clockingBits[2] == m):
            tZ = registerZ[7]^registerZ[20]^registerZ[21]^registerZ[22]
            
            for i in range(len(registerZ)-1,-1,-1):
                if i==0:
                    registerZ[0] = tZ
                else:
                    registerZ[i]=registerZ[i-1]
        
            
        
        keystreamRequirement-=1
        keyStreamBits.append(registerX[-1]^registerY[-1]^registerZ[-1])


    print("Register X = ", registerX, end="\n\n")
    print("Register Y = ", registerY, end="\n\n")
    print("Register Z = ", registerZ, end="\n\n")
    print("Keystream = ", keyStreamBits)



    if (len(plaintext)  == len(keyStreamBits)):
        for chr in range (len(plaintext)):
            ciphertext.append(plaintext[chr] ^ keyStreamBits[chr])


    print("Ciphertext = ", int(''.join(str(x) for x in ciphertext),2))