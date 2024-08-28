from oct2py import octave

# Carregar o codigo
octave.addpath('tl_p528.m')

# Definir os parâmetros de entrada
d__km = 100  # Exemplo
h_1__meter = 50  # Exemplo
h_2__meter = 50  # Exemplo
f__mhz = 1500  # Exemplo
T_pol = 1  # Exemplo
p = 1  # Exemplo

# Chamar a função Octave
resultado = octave.tl_p528(d__km, h_1__meter, h_2__meter, f__mhz, T_pol, p)
