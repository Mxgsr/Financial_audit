# Pista 1: Para poder usar la función que creaste en otro archivo,
# necesitas "importarla".
# Desde el módulo "src.ingestion.file_reader", importa la función "leer_transacciones_csv".
from src.ingestion.file_reader import leer_transacciones_csv

def main():
    """
    Función principal que orquesta la aplicación.
    """
    # Pista 2: Crea una variable llamada "ruta_archivo" que contenga
    # el texto "data/raw/sample_transactions.csv".
    # Esta variable nos dirá dónde están los datos que queremos leer.
    ruta_archivo = "data/raw/sample_transactions.csv"


    # Pista 3: Llama a la función "leer_transacciones_csv" que importaste.
    # Pásale como argumento la variable "ruta_archivo" que acabas de crear.
    # Guarda el resultado que te devuelve la función en una nueva variable llamada "transacciones".
    transacciones = leer_transacciones_csv(ruta_archivo)

    # Pista 4: Para verificar que todo funcionó, imprime la variable "transacciones" en la consola.
    # Puedes usar la función print().
    print(f"{transacciones}")



# Este bloque es el punto de entrada. Le dice a Python que ejecute
# la función "main" cuando corras el programa directamente.
if __name__ == "__main__":
    main()
