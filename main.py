import sys
import json
import time
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm

# Carrega o autômato do arquivo JSON
def load_automaton(filename):
    with open(filename, 'r') as file:
        automaton_data = json.load(file)
    return automaton_data

# Leitura Eficiente do Arquivo de Entrada em Lotes
def read_input_file_in_batches(filename, batch_size):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    batches = [lines[i:i + batch_size] for i in range(1, len(lines), batch_size)]  # Ignora a primeira linha (cabeçalho)
    return batches

# Cria um dicionário de transições para otimização
def create_transition_dict(transitions):
    transition_dict = {}
    for transition in transitions:
        key = (int(transition["from"]), transition["read"])
        transition_dict[key] = int(transition["to"])
    return transition_dict

# Executa o autômato na entrada dada usando o dicionário de transições
def run_automaton_with_dict(automaton, input_string, transition_dict):
    current_state = automaton["initial"]
    for char in input_string:
        key = (current_state, char)
        next_state = transition_dict.get(key)
        if next_state is None:
            return 0  # Rejeita a palavra
        current_state = next_state
        time.sleep(1.0e-6)  # Atraso de 1 microssegundo a cada caractere processado
    return 1 if current_state in automaton["final"] else 0

# Processamento do Lote de Entradas usando processamento paralelo
def process_input_batch_parallel(batch, automaton, transition_dict):
    with ThreadPoolExecutor() as executor:
        batch_results = list(executor.map(lambda item: process_input_item(item, automaton, transition_dict), batch))
    return batch_results

# Processamento de cada item individual em paralelo
def process_input_item(item, automaton, transition_dict):
    word, expected_result = item.strip().split(';')
    result = run_automaton_with_dict(automaton, word, transition_dict)
    return word, int(expected_result), result

# Escreve os resultados no arquivo de saída
def write_output(results, output_filename):
    with open(output_filename, 'w') as file:
        for result in results:
            word, expected_result, obtained_result, time_taken = result
            # Formata o valor do tempo com precisão de 3 casas decimais
            time_str = "{:.3f}".format(time_taken)
            file.write(f"{word};{expected_result};{obtained_result};{time_str}\n")

def main():
    if len(sys.argv) != 3:
        print("Uso: python main.py <arquivo_automato> <arquivo_entrada>")
        return
    
    automaton_data = load_automaton(sys.argv[1])
    transition_dict = create_transition_dict(automaton_data["transitions"])
    
    with open(sys.argv[2], 'r') as file:
        total_lines = sum(1 for _ in file) - 1  # Desconta o cabeçalho
    
    input_batches = read_input_file_in_batches(sys.argv[2], batch_size=100)  # Altere o tamanho do lote conforme necessário
    
    start_script_time = time.perf_counter_ns()  # Registro do tempo de início do script em nanossegundos
    processed_results = []
    
    with tqdm(total=total_lines, desc=f"Processing ({total_lines} lines)", unit="word") as pbar:
        for batch in input_batches:
            batch_results = process_input_batch_parallel(batch, automaton_data, transition_dict)
            processed_results.extend(batch_results)
            pbar.update(len(batch))  # Atualiza a barra de progresso
    
    end_script_time = time.perf_counter_ns()  # Registro do tempo de término do script em nanossegundos
    
    adjusted_results = []
    accumulated_time = 0
    for result in processed_results:
        word, expected_result, obtained_result = result
        accumulated_time += 1.0e-6 * len(word)  # Ajuste para o atraso total
        adjusted_results.append((word, expected_result, obtained_result, accumulated_time))
    
    write_output(adjusted_results, "output.out")

if __name__ == "__main__":
    main()