
nh = 0 # número de habitantes
vkwh = 0 

while nh <= 0 or vkwh <= 0 :
    print('Para a cidade: ')
    nh = int(input('Digite o número de habitantes da cidade: '))
    vkwh = float(input('Digite o valor do kwh para a cidade: '))

habConsumoMes = 0
habCodConsumidor = 0
contHabit1 = 0
contHabit2 = 0
contHabit3 = 0
contHabit = 0
maiorConsumoMes = 0
menorConsumoMes = 10000000000000000 # coloquei esse número enorme apenas para referência com a troca do menor consumo, pq se for zero sempre vai ser zero
totalConsumoHabit = 0 #farei a média total com ele
totalConsumoHabit1 = 0
totalConsumoHabit2 = 0
totalConsumoHabit3 = 0

print('Para o habitante: ')
while contHabit < nh :    
    print('Código do Consumidor: ')
    print('1 - Residencial')
    print('2 - Comercial')
    print('3 - Industrial')
    habCodConsumidor = int(input('Digite o código do consumidor: '))
     
    if (habCodConsumidor < 1) or (habCodConsumidor > 3):
        print('Código inexistente, tente novamente.')

    else:

        habConsumoMes = float(input('Digite o consumo do habitante em kwh: '))

        if habCodConsumidor == 1:
            contHabit1 += 1
            totalConsumoHabit1 += habConsumoMes
        elif habCodConsumidor == 2:
            contHabit2 += 1
            totalConsumoHabit2 += habConsumoMes
        elif habCodConsumidor == 3:
            contHabit3 += 1
            totalConsumoHabit3 += habConsumoMes

        if habConsumoMes < menorConsumoMes:
            menorConsumoMes = habConsumoMes
        else: 
            maiorConsumoMes = habConsumoMes

        contHabit = contHabit1+contHabit2+contHabit3
        totalConsumoHabit = totalConsumoHabit1+totalConsumoHabit2+totalConsumoHabit3           
        
print()
print(f'Maior Consumo entre todos os habitantes: {maiorConsumoMes*vkwh} kwh')
print(f'Menor Consumo entre todos os habitantes: {menorConsumoMes*vkwh} kwh')
print(f'Média de Consumo entre todos os habitantes: {(totalConsumoHabit*vkwh)/contHabit} kwh')
print()
print(f'Total de Consumo entre todos os habitantes do Código 1 - Residencial: {(totalConsumoHabit1*vkwh)/contHabit1} kwh')
print(f'Total de Consumo entre todos os habitantes do Código 2 - Comercial: {(totalConsumoHabit2*vkwh)/contHabit2} kwh')
print(f'Total de Consumo entre todos os habitantes do Código 3 - Industrial: {(totalConsumoHabit3*vkwh)/contHabit3} kwh')
