import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)

df = pd.read_csv("files/ventas.csv", index_col=0)
df2 = pd.read_csv("files/productos.csv", sep=";", index_col=0)
df3 = pd.read_csv("files/clientes.csv", index_col=0)