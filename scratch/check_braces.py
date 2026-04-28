import sys

def check_braces(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    stack = []
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == '{':
                stack.append((i+1, j+1, '{'))
            elif char == '}':
                if not stack:
                    print(f"Error: unmatched }} at line {i+1}, col {j+1}")
                else:
                    stack.pop()
    
    for line_num, col_num, char in stack:
        print(f"Error: unclosed {char} starting at line {line_num}, col {col_num}")

if __name__ == "__main__":
    check_braces(sys.argv[1])
