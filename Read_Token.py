import re

class GrammarParser:
    def __init__(self):
        self.Terminas=[]
        self.Nonterminals=[]
        self.Productions=[]
        self.previous=""
    def reader(self,file_path):
        with open(file_path, 'r') as file:
            for line in file:
                self.parse(line)
        print("Terminals:")
        for terminal in sorted(self.terminals):
            print(f"- {terminal}")

        print("\nNon-Terminals:")
        for non_terminal in sorted(self.non_terminals):
            print(f"- {non_terminal}")

        print("\nProductions:")
        for nt, prod in self.productions.items():
            print(f"{nt} ::= {', '.join(prod)}")

    def parse(self,grammar):
        if("::=" in grammar):
            elements=[]
            rule=grammar.split("::=")
            elements.append(rule[0].strip())
            rule=[x.strip() for x in rule[1]]
            elements.extend(rule)
            for i in elements:
                if(('<' in i) and ('>' in i)):
                    
        else:

def parse_grammar(file_path):
    with open(file_path, 'r') as file:
        grammar = file.read()

    # Regular expressions to identify terminals and non-terminals
    terminal_pattern = r"(?<=\| )\w+"
    non_terminal_pattern = r"<(\w+)>"

    # Find all terminals and non-terminals
    terminals = set(re.findall(terminal_pattern, grammar))
    non_terminals = set(re.findall(non_terminal_pattern, grammar))

    # Map non-terminals to their productions
    productions = {}
    for non_terminal in non_terminals:
        # Find productions for each non-terminal
        productions[non_terminal] = re.findall(f"<{non_terminal}> ::= (.+?)(?=\n<|$)", grammar, re.DOTALL)

    return terminals, non_terminals, productions

def main():
    file_path = '/home/coder/auto_compiler/grammar.txt'  # Replace with your grammar file path
    terminals, non_terminals, productions = parse_grammar(file_path)

    
if __name__ == "__main__":
    main()
