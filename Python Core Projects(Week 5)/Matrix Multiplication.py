def dismat ():
    print("-"*30,"Matrix A","-"*30)
    print()
    r=0
    c=0
    for r in range (nR1):
        print("| " ,end="")
        for c in range (nC1):
            print("%10.3f" % (Mat1[r][c]) , end = "\t")
        print("|")
        print()
    print("\t"*2)

def dismat2 ():
    print("-"*30,"Matrix B","-"*30)
    print()
    r=0
    c=0
    for r in range (nR2):
        print("| " ,end="")
        for c in range (nC2):
            print("%10.3f" % (Mat2[r][c]) , end = "\t")
        print("|")
        print()
    print("\t"*2)

def dismat3_Sym ():
    print("-"*30,"Resultant Matrix","-"*30)
    print()
    r=0
    c=0
    k=0
    for r in range (nR1): #2
        print("|",end="")
        for c in range (nC2):#2
            for k in range(1):#2
                print("%10.3f" % (Mat3[r][c][k]) , end = "\t")
        print("|")
        print()

def dismat3_NonSym ():
    print("-"*30,"Resultant Matrix","-"*30)
    r=0
    c=0
    for r in range (nR1):
        print("|",end="")
        for c in range (nC2):
            for k in range(nR1-1):
                print("%10.3f" % (Mat3[r][c][k]) , end = "\t")
        print("|")
        print()
Mat1=[]
Mat2=[]
Mat3=[]
nR1=int(input("Enter No. Of Rows Of 1st Matrix : \n"))
nC1=int(input("Enter No. Of Columns Of 1st Matrix : \n"))
for rows in range (nR1):
    Resultant1=[]
    for coulumns in range (nC1):
        element = float(input("M[" + str(rows) + "," + str(coulumns) + "]="))
        Resultant1.append(element)
    Mat1.append(Resultant1)
dismat()

nR2=int(input("Enter No. Of Rows Of 2nd Matrix : \n"))
nC2=int(input("Enter No. Of Columns Of 2nd Matrix : \n"))
for rows in range (nR2):
    Resultant2=[]
    for coulumns in range (nC2):
        element = float(input("M[" + str(rows) + "," + str(coulumns) + "]="))
        Resultant2.append(element)
    Mat2.append(Resultant2)
if(nC1 != nR2):
    print("Multiplication Can't Be Possible Because No. of Coulumns of Matrix 1 is not equal to No. of Rows Of Matrix 2")
    

else:
    dismat2()    
    for i in range (nR1):
        O=[]
        for j in range (nC2):
            P=[]
            t=0
            for k in range (nR2):
                    y=Mat1[i][k]*Mat2[k][j]
                    t=t+y
            P.append(t)
            O.append(P)
        Mat3.append(O)
    
    dismat3_Sym()
    # else:
    #     dismat3_NonSym()