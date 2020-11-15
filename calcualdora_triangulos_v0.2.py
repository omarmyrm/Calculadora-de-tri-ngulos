#By Omar Moya Romero 15/11/2020
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
    print ("Seleccione los datos con los que ya cuenta: (1/2/3/4)")
    print ("1)  Los tres ángulos.")
    print ("2)  Tres lados.")
    print ("3)  2 ángulos y un lado.")
    print ("4) 2 lados y un ángulo.")
    print ("-----------------------------------------------------------------------------")
    rectdatatype = input ("")
    if rectdatatype == "1":
        print("Hay infinitos triángulos que cumplan estas condiciones.")
        print ("-----------------------------------------------------------------------------")


    elif rectdatatype == "2":
         a = input("Lado (a) = ")
         b = input("Lado (b) = ")
         c = input("Lado (c) = ")
         cosA = 1.5
         cosA = (pow(float(a),2)-pow(float(b),2)-pow(float(c),2))/(-2*float(b)*float(c))
         A = math.acos(cosA)
         #cosB = (pow(float(b),2)-pow(float(a),2)-pow(float(c),2))/(-2*float(a)*float(c))
         senB = (float(b)*math.sin(A))/float(a)
         B = math.asin(senB)
         C = 180 - math.degrees(B+A)
         print ("Ángulo A = "+ str(math.degrees(A)) + "º")
         print ("Ángulo B = "+ str(math.degrees(B)) + "º")
         print ("Ángulo C = "+ str(C) + "º")
         print ("-----------------------------------------------------------------------------")


    elif rectdatatype == "3": 
        A = float(input("Ángulo (A) = "))
        B = float(input("Ángulo (B) = "))
        C = 180-A-B
        Arad = math.radians(A)
        Brad = math.radians(B)
        Crad = math.radians (C)
        x = input("Lado conocido(a/b/c)")
        if x == "a":
            a = float(input("Lado (a) = "))
            b = (a*math.sin(Brad))/math.sin(Arad)
            c = (a*math.sin(Crad))/math.sin(Arad)
            print ("Lado (b) = "+ str(b) +"º")
            print ("Lado (c) = "+ str(c) +"º")
        elif x == "b":
            b = float(input("Lado (b) = "))
            a = (b*math.sin(Arad))/math.sin(Brad)
            c = (b*math.sin(Crad))/math.sin(Brad)
            print ("Lado (a) = "+ str(a) +"º")
            print ("Lado (c) = "+ str(c) +"º")
        elif x == "c":
            c = float(input("Lado (c) = "))
            a = (c*math.sin(Arad))/math.sin(Crad)
            b = (c*math.sin(Brad))/math.sin(Crad)
            print ("Lado (a) = "+ str(a) +"º")
            print ("Lado (b) = "+ str(b) +"º")
        else:
            print ("Respuesta inválida, por favor, responda con a, b o c.")

        print("Ángulo C = "+str(C)+"º")
        
       
    elif rectdatatype == "4":
        print("No programado")
        #Falta por programar esta parte.  
else:
    print ("Respuesta no válida")
