a = hex(ord('ñ'))
print(a)
print('ñ' == '\xf1' == '\u00f1' == '\U000000f1')

print('we have some character, ñ')
dec = ord("ñ")
print(f'its value in decimal is {dec}')
print('thats above 127 slots that ascii has!')
print('means its encoded using utf-8, which is a type of encoding for unicode')
a = ascii("ñ")
print(f'to prove it, lets try to convert it to ascii - see what happens: {a}')
a2 = ascii('n')
print(f'compare that to normal n - {a2}')

print('-'*50)

print('lets print its values in other forms')
print(f'bin form is {bin(dec)}')
print(f'hex form is {hex(dec)}')
print(f'oct form is {oct(dec)}')

print('-'*50)

norm = chr(dec)
print(f'enoughs playing. lets convert it back to character = {norm}')
