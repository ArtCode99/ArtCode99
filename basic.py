# mess=input("Scrie")
# words=mess.split(' ')
# emojis={ ":)":"bomba nucleara"}
# output=''
# for word in words:
#     output+=emojis.get(word, word)+' '
# print(output)
#

   #Scope-uri:

#a=6
# def veri(b):
#     global a
#     a=100
#     return b+a
# print(veri(4))
# print(a)

    # *args -> se itereaza cu for i in args

# def add(*args):
#     sum=0
#     for i in args:
#         sum+=i
#     return sum
# print(add(5,8,9,4,6,7,2))

# def prezenta(*nume):
#     for i in nume:
#         print(i)
# prezenta("COX","VER","GION")

    # **kwargs -> key word args, ia valori de tip dictionar, e mai dubios

# def hello(**kwargs):
#     print("Hello", end=" ")
#     for key,value in kwargs.items():
#         print(value,end=" ")
# hello(first='Bro',last="Gionule", middle="mondial")

    #  Formatari numere si stringuri:

# a="Verificare bRO cOD"
# b=5410.3
# print(f'Ia sa vedem  {a:>100} la dreapta')
# print(f'Ia sa vedem  {a:^100} la mijloc')
# print(f'NUmarul este {b:,}')
# print(f'NUmarul este {b:e}')        #->stiintific
# print(f'NUmarul este {round(b):b}')        #->binary, da nu merge pe zecimale
# print(f'NUmarul este {round(b):X}')        #-> hexa , da nu merge cu zecimale

    # Random:

# import random
# x=random.random()
# y=random.randint(1,1000)
# alege=["da","nu","poate"]
# a=random.choice(alege)
# b=random.shuffle(alege)
# print(b)
# print(x)
# print(y)
# print(a)

    # Try / Exception:

# try:
#     num=int(input("Numarator: "))
#     numitor=int(input("Numitor :"))
#     result=num/numitor
# except ZeroDivisionError as e:
#     print(e)
#     print("YOu can't divide by 0 bruh")
# except ValueError as e:
#     print(e)
#     print("Doar numere qoi")
# except Exception:
#      print("Nasol")
# else:
#     print(result)
# finally:          #-> ce e in finally se va executa indiferent daca apar erori sau nu. E bun pt inchis fisiere, da noi n-avem acum.
#     print("aSTA se executa mereu")
     #f.close()