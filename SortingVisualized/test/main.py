def get_code():
    code = ""
    newline = input("Enter code to run:\n\n")
    while newline != '\nexit()':
        code += newline
        newline = "\n"+input()
    return code

def save_code(code, filename):
    with open(filename, 'w') as file:
        file.write(code)
        
def delete_module(modname, paranoid=None):
    from sys import modules
    try:
        thismod = modules[modname]
    except KeyError:
        raise ValueError(modname)
    these_symbols = dir(thismod)
    if paranoid:
        try:
            paranoid[:]  # sequence support
        except:
            raise ValueError('must supply a finite list for paranoid')
        else:
            these_symbols = paranoid[:]
    del modules[modname]
    for mod in modules.values():
        try:
            delattr(mod, modname)
        except AttributeError:
            pass
        if paranoid:
            for symbol in these_symbols:
                if symbol[:2] == '__':  # ignore special symbols
                    continue
                try:
                    delattr(mod, symbol)
                except AttributeError:
                    pass


import importlib

code = get_code()
modulename = 'custommodule'
save_code(code, modulename+".py")
importlib.import_module(name = modulename)


delete_module(modulename)



class mylst(int):
    pass