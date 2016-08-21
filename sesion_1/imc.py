masa = float(raw_input("Dame el peso: "))
altura = float(raw_input("Dame la altura: "))

imc = masa / altura ** 2

print "IMC:", imc

if imc >= 0 and imc < 18.5:
    print "Bajo de peso :/"
elif imc >= 18.5 and imc < 25:
    print "Peso normal :)"
elif imc >= 25 and imc < 30:
    print "Sobrepeso :O"
elif imc >= 30:
    print "Obesidad D:"
else:
    print "Peso desconocido (negativo)"