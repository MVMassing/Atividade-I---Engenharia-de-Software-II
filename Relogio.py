import time

def simple_clock():
    while True:
        # Obter a hora local
        current_time = time.localtime()
        
        # Formatar a hora e exibi-la
        formatted_time = time.strftime("%H:%M:%S", current_time)
        print(formatted_time, end='\r')  # O argumento end='\r' permite que a próxima linha substitua a atual na saída

        # Aguardar 1 segundo antes de atualizar novamente
        time.sleep(1)

if __name__ == "__main__":
    try:
        simple_clock()
    except KeyboardInterrupt:
        print("\nRelógio interrompido pelo usuário.")
