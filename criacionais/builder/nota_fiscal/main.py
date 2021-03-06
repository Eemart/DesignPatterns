from empresa import Item, NotaFiscal, CriadorDeNotaFiscal


def main():
    """
    Separar o processo de construção de um objeto de sua representação e
    permitir a sua criação passo-a-passo. Diferentes tipos de objetos podem
    ser criados com implementações distintas de cada passo.
    """


    itens = [
        Item('Item A', 100),
        Item('Item B', 200)
    ]

    nota_fiscal = NotaFiscal(
        razao_social='FHSA Limitada',
        cnpj='0123455678989',
        itens=itens
    )

    print('Nota fiscal sem builder:', nota_fiscal.razao_social)

    nota_fiscal = (
        CriadorDeNotaFiscal()
        .com_razao_social('FHSA Limitada')
        .com_cnpj('01292939494999')
        .com_itens(itens)
        .constroi()
    )

    print('Nota fiscal com builder:', nota_fiscal.razao_social)


if __name__ == '__main__':
    main()
