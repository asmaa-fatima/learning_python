
def format_name(f_name, l_name):
    #docstrings
    '''Take a first and last name and format it to
    return the title case version of the name.'''
    full_name = f_name + ' ' + l_name
    return full_name.title()

name = format_name('asMa' , 'FatiMa')


print(name)