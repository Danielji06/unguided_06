def pagar_vertikal(n):
    print("pagar Vertikal")
    for i in range(1, n+1):
        print("#")
    print()

def pagar_horizontal(n):
    print("pagar Horizontal")
    for i in range(1, n+1):
        print("#", end="")
    print()

def persegi(n):
    print("Pagar Persegi")
    for baris in range(n):
        for kolom in range(n):
            print("#", end="")
        print()
    print()

def persegi_bolong(n):
    print("Persegi Bolong")
    for baris in range(1, n+1):
        if baris == 1 or baris == n:
            for kolom in range(n):
                print("#", end="")
        else:
            spasi = n - 2
            print("#", end="")
            for i in range (spasi):
                print(" ", end="")
            print("#", end="")
        print()
    print()

def huruf_x(n):
    print("Huruf_x")
    for baris in range(1, n+1):
        for kolom in range(1, n+1):
            if baris == kolom:
                print("#", end="")
            elif baris + kolom == n+1:
                print("#", end="")
            else:
                print(" ", end="")
        print()
    print()

def huruf_z(n):
    print("huruf z")
    for baris in range(1, n+1):
        for kolom in range(1, n+1):
            if baris == 1 or baris == n:
                print("#", end="")
            elif baris + kolom == n+1:
                print("#", end="")
            else:
                print(" ", end="")
        print()
    print()

def huruf_n(n):
    print("Huruf N")
    for baris in range(1, n+1):
        for kolom in range(1, n+1):
            if kolom == 1 or kolom == n:
                print("#", end="")
            elif baris == kolom:
                print("#", end="")
            else:
                print(" ", end="")
        print()
    print()

def tanda_plus(n):
    print("Tanda plus")
    tengah = 1 + (n // 2)
    for baris in range(1, n+1):
        for kolom in range(1, n+1):
            if baris == tengah or kolom == tengah:
                print("#", end="")
            else:
                print(" ", end="")
        print()
    print()

def segitiga_kiri(n):
    print("Segitiga Kiri")
    for baris in range(1, n+1):
        for kolom in range(1, baris+1):
            print("#", end="")
        print()
    print()
        

def segitiga_kanan(n):
    print("Segitiga Kanan")
    for baris in range(1, n+1):
        pagar = baris
        spasi = n - pagar
        for kolom in range(spasi):
            print(" ", end="")
        for kolom in range(pagar):
            print("#",end="")
        print()
    print()


def segitiga(n):
    print("segitiga")
    for baris in range(1, n+1):
        spasi = n - baris
        pagar = 2 * baris - 1
        for i in range(spasi):
            print(" ", end="")
        for i in range(pagar):
            print("#", end="")
        print()
    print()


def zigzag(n):
    print("Zigzag")
    for baris in range(1, n+1):
        for kolom in range(1, n+1):
            if baris % 2  == 1:
                print("#", end="")
            elif baris % 4 == 0:
                print("#", end="")
                break
            else:
                if kolom == n:
                    print("#", end="")
                else:
                    print(" ", end="")
        print()
    print()

n = int(input("Masukkan n: "))
pagar_vertikal(n)
pagar_horizontal(n)
persegi(n)
persegi_bolong(n)    
huruf_x(n)
huruf_z(n)
huruf_n(n)
tanda_plus(n)
segitiga_kiri(n)
segitiga_kanan(n)
segitiga(n)
zigzag(n)