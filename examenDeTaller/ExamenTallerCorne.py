def examen(archNum):
    Pdp = {"^": 3,
           "*": 2,
           "/": 2,
           "+": 1,
           "-": 1,
           "(": 0}
    Pfp = {"^": 4,
           "*": 2,
           "/": 2,
           "+": 1,
           "-": 1,
           "(": 5}

    file = open("Examen/Arch"+archNum+".txt")
    worklist=[archNum]

    listaPila=[]
    listaPost=[]

    for line in file:
        line = line.rstrip("\n")
        worklist += [line]

    for item in worklist[1:]:
        if item.isdigit():
            listaPost+=[item]
        else:
            if listaPila==[]:
                listaPila+=[item]
            elif item == ")":
                i=len(listaPila)-1
                while listaPila[i]!="(":
                    operand= listaPila.pop(i)
                    listaPost+=[operand]
                    i-=1
                del listaPila[i]
            elif Pdp[listaPila[len(listaPila)-1]]>=Pfp[item]:
                temp = listaPila.pop(len(listaPila)-1)
                listaPila+=[item]
                listaPost+=[temp]
            elif Pdp[listaPila[len(listaPila)-1]]<Pfp[item]:
                listaPila+=[item]
    if listaPila!=[]:
        i=len(listaPila)-1
        while listaPila!=[]:
            operand=listaPila.pop(i)
            listaPost+=[operand]

    listaRes = []

    for i in listaPost:

        if i == "+":
            temp =int(listaRes[len(listaRes) - 2]) + int(listaRes[len(listaRes) - 1])
            for x in range(2):
                del listaRes[len(listaRes) - 1]
            listaRes+=[temp]
        elif i == "-":
            temp =int(listaRes[len(listaRes) - 2]) - int(listaRes[len(listaRes) - 1])
            for x in range(2):
                del listaRes[len(listaRes) - 1]
            listaRes += [temp]
        elif i == "*":
            temp = int(listaRes[len(listaRes) - 2]) * int(listaRes[len(listaRes) - 1])
            for x in range(2):
                del listaRes[len(listaRes) - 1]
            listaRes += [temp]
        elif i == "/":
            try:
                temp =int(listaRes[len(listaRes) - 2]) / int(listaRes[len(listaRes) - 1])
                for x in range(2):
                    del listaRes[len(listaRes) - 1]
                listaRes += [temp]
            except ZeroDivisionError:
                print("Can't divide by zero")
                break
        elif i == "^":
            temp =int(listaRes[len(listaRes) - 2]) ** int(listaRes[len(listaRes) - 1])
            for x in range(2):
                del listaRes[len(listaRes) - 1]
            listaRes += [temp]
        else:
            listaRes+=[int(i)]

    print(listaPost)
    print(listaRes)
if __name__ == '__main__':
    examen("1")
    examen("2")
    examen("3")
    examen("4")
    examen("5")