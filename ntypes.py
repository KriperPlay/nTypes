
'''
███╗░░██╗██╗░░░██╗░█████╗░██████╗░
████╗░██║██║░░░██║██╔══██╗██╔══██╗
██╔██╗██║╚██╗░██╔╝███████║██████╔╝
██║╚████║░╚████╔╝░██╔══██║██╔══██╗
██║░╚███║░░╚██╔╝░░██║░░██║██║░░██║
╚═╝░░╚══╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝
'''

numbers = ['0','1','2','3','4','5','6','7','8','9', '.']
bool_types = ["fake", "real"]

def string_to_hex(s):
    return s.encode('utf-8').hex()

def hex_to_string(h):
    bytes_object = bytes.fromhex(h)
    return bytes_object.decode('utf-8')


class nVar:
    def __init__(self) -> None:
        self.types = {}
        self.numbersf = numbers[0:9]

    def create_var(self, var: str, _type, filling) -> None:
        if _type == "nstr":
            _str = []
            for i in filling:
                _str += string_to_hex(i)
            
            self.types[var] = (_type, _str)
        
        if _type == "nint":
            _int = []
            if not "." in str(filling):
                for i in str(filling):
                    if i in numbers:
                        _int += string_to_hex(i)
                    else:
                        raise "ValueError"
            else:
                raise "TypeError"
            
            self.types[var] = (_type, _int)

        if _type == "nfloat":
            _float = []
            for i in str(filling):
                if i in numbers and "." in str(filling):
                    _float += string_to_hex(i)
                else:
                    raise "ValueError"
            
            self.types[var] = (_type, _float)

        if _type == "narray":
            _array = []
            for i in filling:
                _array += [string_to_hex(str(i))]
            
            self.types[var] = (_type, _array)

        if _type == "nbool":
            _bool = ""
            if filling in bool_types:
                _bool = string_to_hex(filling)
                self.types[var] = (_type, _bool)
            else:
                raise "TypeError"


    def nvar_var(self, var: str) -> (int | str | float | bool | list):
        res = ""
        if self.types[var][0] == "nstr":
            for i in self.types[var][1]:
                res += i
            res = hex_to_string(res)      

        if self.types[var][0] == "nint":
            for i in self.types[var][1]:
                res += i
            res = int(hex_to_string(res))  

        if self.types[var][0] == "nfloat":
            for i in self.types[var][1]:
                res += i
            res = float(hex_to_string(res))
        
        if self.types[var][0] == "narray":
            _res = []
            for i in self.types[var][1]:
                for x in hex_to_string(i):
                    if x in numbers and "." not in hex_to_string(i):
                        _res += [int(hex_to_string(i))]
                        break
                    if x in numbers and "." in hex_to_string(i):
                        _res += [float(hex_to_string(i))]
                        break
                    if hex_to_string(i) not in numbers and hex_to_string(i) not in self.numbersf:
                        _res += [hex_to_string(i)]
                        break
            return _res

        if self.types[var][0] == "nbool":
            if hex_to_string(self.types[var][1]) == "fake":
                res = False
            if hex_to_string(self.types[var][1]) == "real":
                res = True

        return res


    def isinstance(self, var: str, _type: str) -> bool:
        if self.types[var][0] == _type:
            return True
        else:
            return False