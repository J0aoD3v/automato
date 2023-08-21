import sys
import re
from bigO import BigO

def analyze_complexity(function, input_type):
    # Instantiate BigO class with the provided function
    bigO = BigO(function)
    
    # Determine complexity based on the input type
    if input_type == "random":
        return bigO.random()
    elif input_type == "sorted":
        return bigO.sorted()
    elif input_type == "reversed":
        return bigO.reversed()
    elif input_type == "partial":
        return bigO.partial()
    elif input_type == "Ksorted":
        return bigO.Ksorted()
    else:
        return None

def extract_functions_from_code(code):
    # Use regular expression to find function names in the code
    return re.findall(r"def\s+[a-zA-Z0-9_]+\s*\(", code)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python analyze.py <filename>")
    else:
        filename = sys.argv[1]
        
        try:
            with open(filename, 'r') as file:
                code = file.read()
                function_names = extract_functions_from_code(code)

                if not function_names:
                    print("No functions found in the input code.")
                else:
                    print("Available input types: random, sorted, reversed, partial, Ksorted")
                    input_type = input("Select an input type: ")

                    if input_type not in ["random", "sorted", "reversed", "partial", "Ksorted"]:
                        print("Invalid input type.")
                    else:
                        for function_name in function_names:
                            code_namespace = {}
                            exec(code, code_namespace)

                            function_to_test = code_namespace.get(function_name)
                            if function_to_test and callable(function_to_test):
                                cmplx_result = analyze_complexity(function_to_test, input_type)
                                print(f"Complexity for function '{function_name}' and input type '{input_type}': {cmplx_result}")
                            else:
                                print(f"Function '{function_name}' not found in the input code.")
        except FileNotFoundError:
            print(f"File '{filename}' not found.")

# eu ia fazer tmb analize da complexidade do automato mas esta incompleto e nao tive tempo infelismente :/
# enfim codigo é igual mexer num ninho de rato quando mais mexe menos vc vai conseguir resolver isso, so estressa...
