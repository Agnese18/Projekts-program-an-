m=input("CO2 izmesu daudzums ir 27,5g/km, kam sis videjais izmesu daudzums atbilst")
a = int(input("ievadi 1 ja tas ir BMW, 2-Renault, 3-Audi -"))
sum = 0
for i in range ( a==1) :
    print( "pareizi")
for i in range ( a!=1) :
    print( "nepareizi, tas ir BMW")
def izmasas_menesi(e):
        return e/12
x=int(input("ievadi 1, ja velies aprekinat tikai vienai automasinai CO2 izmaksas, vai ievadi 2 ja velies aprekinat 2 automasinam CO2 izmaksas - "))
if x==1 :
    a=int(input("ievadi savas automasinas co2 daudzumu g/km - "))
    if 0<=a<=50 : print("jamaksa 0 euro gada.","---" ,"izmaksas menesi ir ",  0/12)
    if 51<=a<=95 : print("jamaksa 12 euro gada.","---" , "izmaksas menesi ir ", 12/12)
    if 96<=a<=115 : print("jamaksa 48 euro gada.", "---" ,"izmaksas menesi ir ", 48/12)
    if 116<=a<=130 : print("jamaksa 84 euro gada.", "---" ,"izmaksas menesi ir ",  84/12)
    if 131<=a<=155 : print("jamaksa 120 euro gada.", "---" ,"izmaksas menesi ir ",  120/12)
    if 156<=a<=175 : print("jamaksa 144 euro gada.", "---" ,"izmaksas menesi ir ", 144/12)
    if 176<=a<=200 : print("jamaksa 168 euro gada.", "---" ,"izmaksas menesi ir ", 168/12)
    if 201<=a<=250 : print("jamaksa 264 euro gada.","---" , "izmaksas menesi ir ",264/12)
    if 251<=a<=300 : print("jamaksa 408 euro gada.", "---" ,"izmaksas menesi ir ",  408/12)
    if 301<=a<=350 : print("jamaksa 552 euro gada.","---" , "izmaksas menesi ir ", 552/12)
elif x==2 : 
    c=int(input("ievadi automasinas co2 daudzumu nr.1. g/km - "))
    d=int(input("ievadi automasinas co2 daudzumu nr.2. g/km - "))
    if 0<=c<=50 : print("jamaksa 0 euro gada")
    if 51<=c<=95 : print("jamaksa 12 euro gada")
    if 96<=c<=115 : print("jamaksa 48 euro gada")
    if 116<=c<=130 : print("jamaksa 84 euro gada")
    if 131<=c<=155 : print("jamaksa 120 euro gada")
    if 156<=c<=175 : print("jamaksa 144 euro gada")
    if 176<=c<=200 : print("jamaksa 168 euro gada")
    if 201<=c<=250 : print("jamaksa 264 euro gada")
    if 251<=c<=300 : print("jamaksa 408 euro gada")
    if 301<=c<=350 : print("jamaksa 552 euro gada")
    if 0<=d<=50 : print("jamaksa 0 euro gada")
    if 51<=d<=95 : print("jamaksa 12 euro gada")
    if 96<=d<=115 : print("jamaksa 48 euro gada")
    if 116<=d<=130 : print("jamaksa 84 euro gada")
    if 131<=d<=155 : print("jamaksa 120 euro gada")
    if 156<=d<=175 : print("jamaksa 144 euro gada")
    if 176<=d<=200 : print("jamaksa 168 euro gada")
    if 201<=d<=250 : print("jamaksa 264 euro gada")
    if 251<=d<=300 : print("jamaksa 408 euro gada")
    if 301<=d<=350 : print("jamaksa 552 euro gada")
    e1=int(input("ievadi gada izmaksas euro 1. automasinai - "))
    e2=int(input("ievadi gada izmaksas euro 2.automasinai- "))
    i1=izmasas_menesi(e1)
    i2=izmasas_menesi(e2)
    print("izmaksas menesi ir -", round(e1/12,2))
    print("izmaksas menesi ir -", round(e2/12,2))
    print("amplituda gada -",abs(e2-e1)) 
    print("amplituda menesi -",abs(i2-i1))
    

   
  

