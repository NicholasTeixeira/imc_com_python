def calculo_imc():
    
    seguir = ("s")

    while (seguir == "s"):
        print("USE '.' AO INVÉZ DE ',' OK?")
        peso = float(input("Digite seu peso: "))
        altura = float(input("Digite sua altura: "))

        if peso <= 0 or altura <= 0:
            print("Por favor, insira um peso e altura válidos.")
            continue

        imc = round(peso / altura ** 2)
        
        if imc < 17:
            print(f"Tenha Cuidado, seu IMC foi {imc}, você está muito abaixo do peso!")
        elif imc >= 17 and imc <= 18.49:
            print(f"Atenção, seu IMC foi {imc}, você está abaixo do peso!")
        elif imc >= 18.50 and imc <= 24.99:
            print(f"seu IMC foi {imc}, PARABENS VOCÊ ESTÁ NO PESO IDEAL")
        elif imc >= 25 and imc <= 29.99:
            print(f"Atenção, seu IMC foi {imc}, você está acima do peso!")
        elif imc >= 30 and imc <= 34.99:
            print(f"Tenha Cuidado, seu IMC foi {imc}, você está com (obesidade) nível 1!")
        elif imc >= 35 and imc <= 39.99:
            print(f"Tenha Cuidado, seu IMC foi {imc}, você está com (obesidade severa)  ou seja nível 2!")
        elif imc >= 40:
            print(f"Tenha Cuidado, seu IMC foi {imc}, você está com (obesidade mórbida)  ou seja nível 3! Já considerou procurar um nutricionista?")  
        else:
            print(f"Então, seu IMC foi {imc}, o valor não foi identificado não!")
        seguir = input("Deseja Repetir?(s/n): ")
    else:
        print("Então amigo, até a próxima!")

respostas_validas = ["s", "sim", "vamos"]
resposta = input("Olá, tudo bom? Vamos calcular seu 'IMC'? ").lower()
if resposta in respostas_validas:
    calculo_imc()
else:
    print("Ok, então Tchau amigo!")