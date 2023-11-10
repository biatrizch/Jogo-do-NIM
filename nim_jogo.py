num_peças = int(input())
máx_peças = int(input())

def quem_começa(num_peças, máx_peças):
    vez = 0
    if num_peças % (máx_peças + 1)==0:
        vez = 0
        return vez
    else:
        vez = 1
        return vez

if __name__ == "__main__":
    vez = quem_começa(num_peças, máx_peças)
    while num_peças > 0:
        if vez == 0:
            jogador_peças = int(input())
            
            while jogador_peças > máx_peças or jogador_peças < 1:
                print('Digite um número válido')
                jogador_peças = int(input())

            else:
                print(f'Jogador: {jogador_peças} peças')

            num_peças = num_peças - jogador_peças
            print(f'Restam: {num_peças} peças')
            vez = vez + 1

        if vez == 1:
            # ele deve deixar um num_peças que seja multilo de m+1
            pc_peças = máx_peças
            
            for num in range(1, máx_peças + 1):
                if (num_peças - num) % (máx_peças + 1) == 0:
                    pc_peças = num
             
            print(f'Computador: {pc_peças} peças')
            num_peças = num_peças - pc_peças                
            print(f'Restam: {num_peças} peças')

            vez = vez - 1

    if num_peças <= 0:
        if vez == 0:
            print('Computador venceu')
        else:
            print('Jogador venceu')