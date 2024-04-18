produtos = ("Mouse", 50, "Teclado", 180, "Monitor", 980, "Placa de Vídeo", 1300, "Processador", 603,
          "Mousepad", 35, "Headset", 540, "Cadeira", 1299.99, "Gabinete c/ led", 139.99)
print(f"""{"-=" * 19}-
{"\033[35mLOJINHA DO RUAN\033[m":^45}
{"-=" * 19}-
{"\033[34mPRODUTOS":^42} 
{"\033[m-" * 39}""")
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f"\033[37m{produtos[pos]:.<30}\033[m", end="")
    else:
        print(f"\033[32mR${produtos[pos]:>7.2f}\033[m")
print("-" * 39)
