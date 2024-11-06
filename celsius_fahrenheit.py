print("Conversão Celsius-Fahrenheit")
escolha = input("Digite a inicial da temperatura que deseja converter. Converter para Celsius (C) ou Fahrenheit (F)? ")

if escolha == "C":
    temp_F = float(input("Digite a temperatura em Fahrenheit: "))
    temp_C = (temp_F - 32) / 1.8
    print("Temperatura em Celsius:", temp_C)
elif escolha == "F":
    temp_C = float(input("Digite a temperatura em Celsius: "))
    temp_F = (temp_C * 1.8) + 32
    print("Temperatura em Fahrenheit:", temp_F)