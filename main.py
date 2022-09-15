from random import randint

start_default = 1
end_default = 10
quantity_default = 1
op_default = 'Y'


def gerar_numero(start, end, quantity, number_repeat: bool = False) -> list:
    numeros = [*range(start, end + 1)]
    sorteados = []
    while len(sorteados) < quantity:
        n = randint(0, len(numeros) - 1) if len(numeros) > 1 else 0
        if number_repeat:
            sorteados.append(int(numeros[n]))
        else:
            sorteados.append(int(numeros.pop(n)))
    return sorted(sorteados)


def menu() -> bool:
    width = 50
    print(end='')
    print(f'#{"=" * width}#')
    print(f'|{"RANDOM NUMBER GENERATOR":^50}|')
    print(f'#{"=" * width}#')
    print(f'Qual intervalo?')
    while True:
        start = input(f'\tNúmero inicial: (default: {start_default})\n\t\t>_ ')
        if start:
            try:
                start = int(start.strip())
                if start < 0:
                    print(f'\tPor favor digite um valor numérico inteiro POSITIVO.\n')
                else:
                    break
            except ValueError:
                print(f'\tPor favor digite um valor NUMÉRICO INTEIRO POSITIVO.\n')
        else:
            start = start_default
            break
    while True:
        end = input(f'\tNúmero final: (default: {end_default})\n\t\t>_ ')
        if end:
            try:
                end = int(end.strip())
                if end < 0:
                    print(f'\tPor favor digite um valor numérico inteiro POSITIVO.\n')
                elif start is not None and end < start:
                    print(f'\tPor favor digite um valor numérico maior que {start}.\n')
                else:
                    break
            except ValueError:
                print(f'\tPor favor digite um valor NUMÉRICO inteiro positivo.\n')
        else:
            end = end_default
            break
    while True:
        start = start_default if start is None else start
        end = start if end is None else end
        max_qt = end - start
        max_qt = 1 if max_qt == 0 else max_qt
        quantity = input(f'Quantos números deseja sortear? (default: 1) (máx.: {max_qt})\n\t>_ ')
        if quantity:
            try:
                quantity = int(quantity.strip())
                if quantity > max_qt:
                    print(f'\tA quantidade máxima permitida é {max_qt}\n')
                    continue
                else:
                    break
            except ValueError:
                print(f'\tPor favor digite um valor numérico inteiro\n')
        else:
            quantity = quantity_default
            break
    op = input(f'Permitir números repetidos? (default: N) [Y|N]\n\t>_ ')
    op = op.strip()[0].upper() if len(op) > 0 else 'N'
    number_repeat = True if op == 'Y' else False
    numeros = map(str, gerar_numero(start=start, end=end, quantity=quantity, number_repeat=number_repeat))
    print(f'\nNúmero(s) sorteado(s): {", ".join(numeros)}.')
    op = input(f'Deseja continuar? (default: {op_default}) [Y|N]\n\t>_ ')
    op = op.strip()[0].upper() if len(op) > 0 else op_default
    print()
    return True if op == 'Y' else False


if __name__ == '__main__':
    while True:
        if not menu():
            break
