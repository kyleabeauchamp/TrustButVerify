import pandas as pd
from simtk import unit as u
from trustbutverify import mixture_system
import sys

data = pd.read_csv("./data_dielectric.csv")
rank = int(sys.argv[1])

for k0, k1, components, smiles, cas, temperature, pressure, density, dielectric in data.itertuples():
  if k0 == rank:
    print(k0, k1, components, smiles, cas, temperature, pressure, density)
    model = mixture_system.MixtureSystem([cas], [1000], temperature * u.kelvin, pressure = pressure * u.kilopascal)
    model.build()
    model.equilibrate()
    model.production()