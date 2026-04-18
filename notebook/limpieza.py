import pandas as pd

def limpiar_users(data_frame_sucio):
    data_frame_limpio=data_frame_sucio.copy()

 #1. Limpiar las columnas del DataFrame que son palabras (Strings)
    columnas_string=["role","name","email","password"]
    for columna in columnas_string: 
        data_frame_limpio[columna]=data_frame_limpio[columna].astype("string").str.strip()

#2. Definir valores esperados para cada columna de texto
    roles_validos=["U1","U2"]
    data_frame_limpio["role"]=data_frame_limpio["role"].where(data_frame_limpio["role"].isin(roles_validos), pd.NA)
    names_validos=["admin","student"]
    data_frame_limpio["name"]=data_frame_limpio["name"].where(data_frame_limpio["name"].isin(names_validos), pd.NA)
    email_validos=["example.com", "test.com", "sample.com"]
    data_frame_limpio["email"]=data_frame_limpio["email"].where(data_frame_limpio["email"].isin(email_validos), pd.NA)
    password_validos=["password123", "admin2024", "user2024"]
    data_frame_limpio["password"]=data_frame_limpio["password"].where(data_frame_limpio["password"].isin(password_validos), pd.NA)    
    
#3. Evaluar columnas numéricas para detectar valores atípicos o no válidos
    data_frame_limpio["id"]=pd.to_numeric(data_frame_limpio["id"])

#4. Evaluar columna de fechaCreacion para detectar valores no válidos
    data_frame_limpio["fechaCreacion"]=pd.to_datetime(data_frame_limpio["fechaCreacion"])

 #5 Reemplazar fechaCreacions nulas con una fechaCreacion por default
    fechaCreacion_default=pd.to_datetime("2026-01-01")
    data_frame_limpio["fechaCreacion"]=data_frame_limpio["fechaCreacion"].fillna(fechaCreacion_default)

#6. Eliminar registros nulos de campos obligatorios
    columnas_obligatorias=["id","role","name","email","password"]
    data_frame_limpio=data_frame_limpio.dropna(subset=columnas_obligatorias)

#7. Eliminar valores invalidos a nivel numérico
    data_frame_limpio=data_frame_limpio[data_frame_limpio["id"]>0]  

#8. Eliminar valores duplicados
    data_frame_limpio=data_frame_limpio.drop_duplicates()

    return data_frame_limpio      
