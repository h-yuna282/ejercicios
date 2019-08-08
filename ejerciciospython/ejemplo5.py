peso = float(input("Digite su peso"))
estatura = float(input("Digite su estatura"))

imc = peso(estatura*estatura)

if imc<18.5:
    print(imc, " bajo peso" )
elif imc<24.9:
    print(imc, " Normal" )
elif imc<29.9:
    print(imc, " Sobrepeso" )
elif imc<34.9:
    print(imc, " Obesidad I" )
elif imc<39.9:
    print(imc, " Obesidad II" )
elif imc<49.9:
    print(imc, " Obesidad III" )
elif imc>50:
    print(imc, " Sobrepeso" )
else:
    print("Error")
    
