# hackcode.py
class Code:
    @staticmethod
    def dest(mnemonic):
        dest = ''
        dest += '1' if 'A' in mnemonic else '0'
        dest += '1' if 'D' in mnemonic else '0'
        dest += '1' if 'M' in mnemonic else '0'
        return dest

    @staticmethod
    def comp(mnemonic):
        comp_table = {
            '0': '0101010', '1': '0111111', '-1': '0111010',
            'D': '0001100', 'A': '0110000', 'M': '1110000'
        }
        return comp_table.get(mnemonic, '0000000')

    @staticmethod
    def jump(mnemonic):
        jump_table = {
            '': '000', 'JGT': '001', 'JEQ': '010', 'JGE': '011'
        }
        return jump_table.get(mnemonic, '000')