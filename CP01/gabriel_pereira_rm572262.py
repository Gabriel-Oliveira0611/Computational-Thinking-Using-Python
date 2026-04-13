#Exercício 03
#Item A

cp1 = 5
cp2 = 9
sprint1 = 6
sprint2 = 8
gs1 = 10

#Item B
mediaCps = 7.0
mediaSprints = 7.0
mediaGS = 10.0

mediaFinal = 8.0

#Item C
nome = "Gabriel"
sobrenome = "Pereira de Oliveira"

#Item D
passou = True
naoPassou = False

#---------------------------------------------------------------------------

#Exercício 04
#Item A

somaCPs = cp1 + cp2
somaSprints = sprint1 + sprint2

#Item B
mediaCps = somaCPs / 2
mediaSprints = somaSprints / 2

#Item C
notaCPs = mediaCps * 0.2
notaSprints = mediaSprints * 0.2
notaGS = gs1 * 0.6

#Item D
notaFinal = notaCPs + notaSprints + notaGS

#Item E
mediaAprovação = 6
faltaParaPassar = notaFinal - mediaAprovação
#print(f"Falta para passar: {faltaParaPassar}")

#----------------------------------------------------------------------

#Exercício 05
#notaInputToFloat = float(input("Insira a nota no input"))

#Exercício 06
#Item A

passou = notaFinal >= mediaAprovação

#Item B
#inputVsNotaFinal = notaFinal != notaInputToFloat

#Exercício 07

print(notaFinal)

print(f"""- Is it true that {nome} {sobrenome}'s approved?
    -{passou}.""")