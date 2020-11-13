#By Omar Moya Romero 14/11/2020


import math
print("BIENVENIDO A LA CALCULADORA DE TRIÁNGULOS")
print("--------------------------------------------------------------")
print("En primer lugar: ¿Es el triángulo rectángulo? (s/n)")
rectrue = input ("")
if rectrue == "s":
    print("-----------------------------------------------------------------------------")
    print ("Seleccione los datos con los que ya cuenta: (1/2/3/4)")
    print ("1)  Dos catetos.")
    print ("2)  Un cateto y la hipotenusa.")
    print ("3)  Un ángulo agudo y la hipotenusa.")
    print ("4) Un ángulo agudo y un cateto")
    print ("-----------------------------------------------------------------------------")
    rectdatatype = input ("")
    if rectdatatype == "1":
        b = input("Cateto 1 (b)=")
        c = input("Cateto 2 (c)=")
        a2 = pow(float(b),2) + pow(float(c),2)
        a = math.sqrt(a2)
        print ( "a = " + str(a))
        print ("-----------------------------------------------------------------------------")
    elif rectdatatype == "2":
        a = input("Hipotenusa (a)=")
        b = input("Cateto (b)=")
        c2 = pow(float(a),2) - pow(float(b),2)
        c = math.sqrt(c2)
        print ( "a = " + str(c))
        print ("-----------------------------------------------------------------------------")
    elif rectdatatype == "3":
        a = input("Hipotenusa (a)=")
        B = input("Ángulo (B) (grados)=")
        Brad = float(B)*((2*math.pi)/360)
        b = float(a)*math.sin(Brad)
        c = float(a)*math.cos(Brad)
        C = 180-90-float(B)

        print("b=  " + str(b))
        print("c=  " + str(b))
        print ("A = 90º")
        print ("C = " + str(C) + "º")
    elif rectdatatype == "4":
        b = input("Cateto (b) =  ")
        D = input("Ángulo (grados)(Posibilidad 1: B) (Posibilidad 2: C)=  ")
        print ("Hay dos posibles soluciones:")
        print ("Posibilidad 1 (Dado el ángulo B):")
        Drad = float(D)*((2*math.pi)/360)
        cp1 = float(b)/math.tan(Drad)
        ap1 = float(b)/math.sin(Drad)
        print("c= " +str(cp1))
        print("a= " +str(ap1))
        print ("C = "+ str(180-90-float(D)) + "º")
        print ("A = 90º")
        print("------")
        print ("Posibilidad 2 (Dado el ángulo C):")
        cp2 = float(b)*math.tan(Drad)
        ap2 = float(b)/math.cos(Drad)
        print("c (pos2)= " +str(cp2))
        print("a (pos2)= " +str(ap2))
        print ("B = "+ str(180-90-float(D)) + "º")
        print ("A = 90º")
        






elif rectrue == "n":
    print("-----------------------------------------------------------------------------")
    print ("Lo sentimos, la función de calcular triángulos no rectángulos llegará próximamente. Disculpe las molestias")
    print("-----------------------------------------------------------------------------")

else:
    print("-----------------------------------------------------------------------------")
    print ("Respuesta inválida, por favor, responda Sí (s) o no (n)")




