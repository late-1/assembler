
import sys
import os
from hackparser import Parser
from hackcode import Code
from hacksymboltable import SymbolTable

def assemble(input_file, output_file=None):
    if output_file is None:
        output_file = os.path.splitext(input_file)[0] + '.hack'
    
    symbol_table = SymbolTable()
    
    parser = Parser(input_file)
    rom_address = 0
    
    while parser.has_more_commands():
        parser.advance()
        command_type = parser.command_type()
        
        if command_type == 'L_COMMAND':
            symbol_table.add_entry(parser.symbol(), rom_address)
        else:
            rom_address += 1
    
    parser.reset()
    with open(output_file, 'w') as f:
        while parser.has_more_commands():
            parser.advance()
            command_type = parser.command_type()
            
            if command_type == 'A_COMMAND':
                symbol = parser.symbol()
                if symbol.isdigit():
                    address = int(symbol)
                else:
                    address = symbol_table.add_variable(symbol)
                
                binary = format(address, '016b')
                f.write(binary + '\n')
                
            elif command_type == 'C_COMMAND':
                dest = Code.dest(parser.dest())
                comp = Code.comp(parser.comp())
                jump = Code.jump(parser.jump())
                
                binary = '111' + comp + dest + jump
                f.write(binary + '\n')
    
    print(f"Assembly complete. Output written to {output_file}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python hackassembler.py [syöttö.asm] [ulostulo.hack]")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    assemble(input_file, output_file)