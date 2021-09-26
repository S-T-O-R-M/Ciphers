S = [0,1,2,3,4,5,6,7]
inputKey = [1,2,3,6]
plaintext = [1,3,2,3]
K = []
keystreamBits=[]
ciphertext = []

def key_scheduling_algorithm():
    for x in range(0,len(S)):
        K.append(inputKey[x % len(inputKey)])
    
    j=0

    for i in range(0,len(S)):
        j =  (j + S[i] + K[i]) % len(S)
        S[i],S[j] = S[j],S[i]

def pseudo_random_generation_algorithm():
    i = j = 0
    numberOfBitsNeeded = 4
    while numberOfBitsNeeded > 0:
        i = (i+1)%len(S)
        j = (j+S[i])%len(S)
        S[i],S[j] = S[j],S[i]
        
        KS = S[(S[i]+S[j]) % len(S)]
        
        keystreamBits.append(KS)
        numberOfBitsNeeded-=1


def encrypt():
    for chr in range(len(plaintext)):
        ciphertext.append(plaintext[chr] ^ keystreamBits[chr])

key_scheduling_algorithm()
print("S after KSA = ", S)
pseudo_random_generation_algorithm()
encrypt()

print('S after PRGA = ', S)   
print("Keystream bits = ",keystreamBits)
print("Ciphertext",ciphertext)


