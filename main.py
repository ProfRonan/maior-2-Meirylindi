"""Arquivo principal que será interpretado pelo interpretador."""


def main():
    """Função principal que será rodada quando o script for passado para o interpretador."""
    print('Digite um número:')
    n_1 = float(input('> '))
    print('Digite outro número:')
    n_2 = float(input('> '))

    if n_1 > n_2:
      maior = n_1
    else:
      maior = n_2

    print(f'{maior}')

if __name__ == '__main__':
    main()
