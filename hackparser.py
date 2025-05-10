# hackparser.py
class Parser:
    def __init__(self, filename):
        with open(filename, 'r') as f:
            self.lines = []
            for line in f:
                if '//' in line:
                    line = line[:line.index('//')]
                line = line.strip()
                if line:
                    self.lines.append(line)
        
        self.current_line = 0
        self.current_command = None

    def has_more_commands(self):
        return self.current_line < len(self.lines)

    def advance(self):
        if self.has_more_commands():
            self.current_command = self.lines[self.current_line]
            self.current_line += 1
            return True
        return False

    def reset(self):
        self.current_line = 0
        self.current_command = None

    def command_type(self):
        if self.current_command.startswith('@'):
            return 'A_COMMAND'
        elif self.current_command.startswith('(') and self.current_command.endswith(')'):
            return 'L_COMMAND'
        else:
            return 'C_COMMAND'

    def symbol(self):
        if self.command_type() == 'A_COMMAND':
            return self.current_command[1:]
        elif self.command_type() == 'L_COMMAND':
            return self.current_command[1:-1]
        else:
            return None

    def dest(self):
        if self.command_type() != 'C_COMMAND':
            return None
        
        if '=' in self.current_command:
            return self.current_command.split('=')[0]
        else:
            return ''

    def comp(self):
        if self.command_type() != 'C_COMMAND':
            return None
        
        command = self.current_command
        if '=' in command:
            command = command.split('=')[1]
        
        if ';' in command:
            return command.split(';')[0]
        else:
            return command

    def jump(self):
        if self.command_type() != 'C_COMMAND':
            return None
        
        if ';' in self.current_command:
            return self.current_command.split(';')[1]
        else:
            return ''