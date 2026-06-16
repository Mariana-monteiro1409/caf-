from fastapi import FastAPI, Query
import requests

print(
                                 ''' \n Ｒｅｃｅｉｔａ ｃａｆé\n''' 
)

litros_cafe = int(input('Quantos litros de café vc quer fazer?: \n'))

print(f'\n Materiais: \n 1- Água ({litros_cafe}l) \n 2- Filtro de papel \n 3- Garrafa \n 4- Pó de café \n ')

litro = 1000
xicara = 250
 
print('Coloque a água pra ferver \n ')

print('Ferva água até 90° Graus\n')

print('Enquanto a água esquenta posicione o filtro sobre a garrafa')

quantidade = int( (litro * litros_cafe) / xicara)

print(f'Coloque {quantidade} de colheres de sopa do pó de café no filtro ')

agua_fervida = input(' A água já ferveu? :')

if agua_fervida == 'sim':
    print('Coloque um pouco de água sobre o pó de café e depois despeje o restante em movimentos circulares')
    print('Espere o processo de filtragem acabar, quando não tiver mais água no filtro')
    termino_filtragem = input('A filtragem acabou?: \n')
elif agua_fervida == 'não':
    print('Espere a água ferver')  
    termino_filtragem = input('A filtragem acabou?: \n')

if termino_filtragem == 'sim':
    print('Seu café está pronto, aproveite! \n')
elif termino_filtragem == 'não':
    print('Espere a filtragem acabar')
    termino_filtragem  

