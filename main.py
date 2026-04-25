import pandas as pd

from notebook.limpieza import limpiar_users

from simulacion_users import simular_users

from notebook.descripcion import describir_users

users=simular_users(100)

users_ordenados=pd.DataFrame(users)

users_limpios=limpiar_users(users_ordenados)

describir_users(users_limpios)  