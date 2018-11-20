# Inclusions
from math import *
values = []
exponents = []

########################################################
#     Constants                                       #
########################################################

progression_display = True # True / False
exponent_minmax = 4
precision = 0.00002 # add or remove 0 for precision's accuracy
number_min_Zero = 1

values.append(['a/137',log(137.0359991)-log(137)])
#values.append(['9a9/4',log(137.0359991)*9+log(9/4)])
#values.append(['3/150',log(3)/150])
#values.append(['22/7pi0',log(1.000378931)])
#values.append(['8pi0/25',log(1.005333333)])
#values.append(['8pi/25',log(1.005309649)])
#values.append(['Pt/piB',log(1.005333333)])
#values.append(['22/21',log(1.047619048)])
#values.append(['aH/p',log(137.1106292)])
#values.append(['a/p2',log(1902.69684)])
#values.append(['a/z',log(42.67707595)])
#values.append(['P/6',49.73599417])
#values.append(['1.616',log(1.6)*16])
#values.append(['pi/pi0',log(3.141592654)-log(377)+log(120)])
#values.append(['2',log(2)])
#values.append(['3',log(3)])
#values.append(['5',log(5)])
#values.append(['pi',log(3.141592654)])
#values.append(['F/rpH',log(311.9846006)])
#values.append(['rpH/pg',log(1.002796175)])
#values.append(['f',log(8.434501737)])
#values.append(['r137',log(137)/2])
#values.append(['6F',log(573007.3249)+log(6)])
#values.append(['P/2F',37.57595268])
#values.append(['pg/',log(1831.531308)-log(1836.118109)])
values.append(['pg',log(1831.531308)-log(1836.152672)*0])
values.append(['pK',log(1842.604127)-log(1836.118109)*0])
#values.append(['d',log(1.001159652)*1])
values.append(['H',log(1837.152645)-log(1836.118109)*0])
values.append(['p',log(1836.152672)+log(1836.118109)*0])
#values.append(['rpH',log(1836.65259)])
values.append(['n',log(1838.683659)])
#values.append(['n/',log(1838.683659)-log(1836.152672)])
#values.append(['p5',log(1836.152672)*5])
#values.append(['phol/',log(1853.856244)-log(1836.118109)*1])
#values.append(['phol0',log(1852.342853)])
values.append(['1sH-p',-log(0.999973)])
#values.append(['H2',log(1837.152645)*2])
#values.append(['n3',log(1838.683659)*3])
#values.append(['6p5',log(1836.118109)])
#values.append(['W',log(157338.9065)])
#values.append(['Z',log(178451.2342)])
#values.append(['9mu',log(206.7682796)+log(9)])
#values.append(['tau',log(3477.441588)])
#values.append(['2piWZ',25.89610511])
#values.append(['pK/',log(1842.604127)-log(1836.118109)*1])
#values.append(['rpH',log(1836.65259)])
#values.append(['H-p',log(0.999973)])
#values.append(['H0',log(1848.574949)])
#values.append(['2P/aF3',log(1853.249431)])
#values.append(['a12/P',log(1835.679992)-log(1836.118109)])
#values.append(['F5/Pa3',log(1.004795741)])
#values.append(['1834',log(1834)-log(1836.118109)])
#values.append(['epi',log(1842.083214)-log(1836.118109)])
#values.append(['X',log(1836.323077)-log(1836.118109)])
#values.append(['X',log(1835.717214)-log(1836.152672)*0])
#eee/aee = 1836.72019
#2a^11/9)^(1/7) = 1838.937547
#values.append(['X',log(1.006103418)])
#values.append(['r3pi/2e',log(1.000889245)])
#values.append(['H',log(1837.152645)-log(1836.152672)*0])
#values.append(['X',log(1841.154903)-log(1836.152672)*0])
#values.append(['a',log(137.0359991)])
values.append(['d',log(1.001159652)])



########################################################
#     The Program in itself                            #
########################################################

print ("Start ...")
length = len(values)
precedent=-exponent_minmax

# Min exponent set for each value 
for i in range (0,length):
    exponents.append(-exponent_minmax)
    print(values[i][0],end='\t')

print("Zeros",end='\t');
print("Pr");


nbSolutions = 0
#<= 0 Do not make twice the same calculation with the inverses
while exposants[longueur-1]<=0:
    # Calculate and process the result
    result= 0
    j=0
    while j<length:
        result=result + (values[j][1])*(exponents[j])
        j+=1
    #if result<0:
    #    result*=(-1)

    # Display or not the results
    if result<=precision and result>=-precision:
        # counting zeros
        nbzero=0
        for j in range (0,length):
            if (exponents[j] == 0):
                nbzero+=1
        if nbzero >= nombre_min_Zero:
            for j in range (0,longueur):
                print(exponents[j],end='\t')
            print(nbzero,end='\t')
            print(int(resultat*1000000000))
            nbSolutions = nbSolutions + 1
    
    # Add + Exponents Rotation
    exponents[0]+=1
    for j in range (0,longueur-1):
        if exponents[j]>exponent_minmax:
            exponents[j]=-exponent_minmax
            exponents[j+1]+=1
    if (display_progression):
        if (exponents[longueur-2]!=precedent):
            precedent=exponents[longueur-2]
            #print("Status:",end=' ')
            #print(exponents[j+1]);

print ("All results lead to nbSolutions =", nbSolutions)
print("Pr"),d;
