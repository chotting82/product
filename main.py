from decimal import Decimal


if __name__ == '__main__':
    a = 126

    b = Decimal("3.669")
    c = Decimal("1452.6700")

    z = a/(b* c) * Decimal(100)

    print(z)