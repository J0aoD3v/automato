import sys
import json
import random
from tqdm import tqdm  # Importa a classe tqdm para a barra de progresso

# Carrega o autômato do arquivo JSON
def load_automaton(filename):
    with open(filename, 'r') as file:
        automaton_data = json.load(file)
    return automaton_data

# Executa o autômato na entrada dada
def run_automaton(automaton, input_string):
    current_state = automaton["initial"]
    for char in input_string:
        transitions = automaton["transitions"]
        found_transition = False
        for transition in transitions:
            if transition["from"] == str(current_state) and transition["read"] == char:
                current_state = int(transition["to"])
                found_transition = True
                break
        if not found_transition:
            return 0  # Rejeita a palavra
    return 1 if current_state in automaton["final"] else 0

# Gera uma palavra aleatória baseada nas letras presentes nas transições
def generate_random_word(transitions, length):
    alphabet = set()
    for transition in transitions:
        alphabet.add(transition["read"])
    alphabet = list(alphabet)
    return ''.join(random.choice(alphabet) for _ in range(length))

def main():
    if len(sys.argv) != 2:
        print("Uso: python gen.py <arquivo_automato>")
        return
    
    automaton_data = load_automaton(sys.argv[1])
    transitions = automaton_data["transitions"]
    
    with open("input.in", "w") as input_file:
        input_file.write("palavra de entrada;resultadoesperado\n")
        # Use tqdm para criar a barra de progresso
        for _ in tqdm(range(1000000), desc="Generating words"):
            word_length = random.randint(1, 20)
            word = generate_random_word(transitions, word_length)
            result = run_automaton(automaton_data, word)
            input_file.write(f"{word};{result}\n")

if __name__ == "__main__":
    main()
