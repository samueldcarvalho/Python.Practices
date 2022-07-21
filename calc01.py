acumulativo = float(input("Digite um valor:"))
operacao = ""

while(operacao != "="):
    operacao = input("+ - / * =")

    if(operacao != "=") :
        numeroOperacao = float(input("Digite outro valor:"))

    if(operacao == "+"):
        acumulativo += numeroOperacao
    elif(operacao == "-"):
        acumulativo -= numeroOperacao
    elif(operacao == "*"):
        acumulativo *= numeroOperacao
    elif(operacao == "/"):
        acumulativo /= numeroOperacao
    elif(operacao == "="):
        print("Resultado é ", acumulativo)

    
