import pandas as pd

noticias = [
    {
        "titulo":"Accidente en carretera Panamericana",
        "fuente":"Portal Noticias"
    },
    {
        "titulo":"Campaña de seguridad vial",
        "fuente":"Portal Noticias"
    }
]

df = pd.DataFrame(noticias)

df.to_csv(
    "data/raw/noticias_accidentes.csv",
    index=False
)

print("Archivo generado")
