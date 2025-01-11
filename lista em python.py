# ero 5 vcpres e guardar numa lista
# 
# 
# 
# 
# lista_cores = []
# for i in range(5):
#     lista_cores.append(input('Digite uma cor: '))



# print(lista_cores)



#para numero ilimitado de cores

lista_cores = []
while True:
    
    cor = input('Digite uma cor ou N para parar  ==>  ')

    if cor.upper() == 'N':
        break
    else:
        lista_cores.append(cor)

    



print(lista_cores)