# Her udleveres kode til løsning af opgave 1

def pace2velocity(p):
    return (1000/60)/p

assert pace2velocity(10) == 1.666666666666666666

def v2p(v):
    return (1000/60)/v

assert v2p(1.666666666666666666) == 10

# Her udleveres kode til at løse opgave 2
# virker med stien når du har mappen `projektopgave` aktiv`

def indlaes_fra_fit(fname = "data/hok_klubmesterskab_2022/CA8D1347.FIT"):
    from fit_file import read
    points = read.read_points(fname)
    return points

punkter = indlaes_fra_fit()

print(f"Der er indlæst {len(punkter)} punkter fra filen")
print(punkter[300])