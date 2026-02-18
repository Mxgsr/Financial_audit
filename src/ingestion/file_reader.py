import csv

def leer_transacciones_csv(ruta_archivo):
    """
    Lee un archivo CSV y devuelve una lista de datos.
    """
    transacciones_finales = []
    print(f"Intentando leer el archivo: {ruta_archivo}")
    try:
        with open(ruta_archivo, mode='r', encoding='utf-8') as archivo:
            #Pista 1: El modulo 'csv' tiene una función para leer archivos.
            #Necesito crear un lector que entienda el formato CSV
            #Necesito Buscar como usar csv.reader()
            lector_csv = csv.DictReader(archivo)

            #Pista 2: Un lector de CSV es un objeto que se puede recorrer.
            # Usemos un bucle 'for' para leer cada fila, una por una.
            for fila_original in lector_csv:
                monto_texto_sucio = fila_original['Monto']
                monto_numerico_limpio = limpiar_monto(monto_texto_sucio)
                fila_original['Monto'] =monto_numerico_limpio
                transacciones_finales.append(fila_original)
    except FileNotFoundError:
        # Si el 'try' falla porque el archivo no existe, este bloque no se ejecuta
        print(f"Error, no se pudo encontrar el archivo en la ruta: {ruta_archivo}")
        return [] #Devuelve una lista vacia.
    return transacciones_finales
def limpiar_monto(monto_en_texto):
    """
    Toma un monto en texto y lo convierte a integer
    """
    # Pista 1: Un str tiene un método llamado .replace()
    # .replace() sirve para eliminar el texto como '$' y '.'
    monto_sin_simbolos = monto_en_texto.replace('$', '').replace('.','')
    # texto_limpio = monto_sin_simbolos.replace('.','')

    # Pista 2: Ahora que el texto es un numero limpio
    # Hay que convertirlo a un tipo de dato numérico.
    # float() permite decimales.
    try:
        return float(monto_sin_simbolos)
    except ValueError:
        print(f"No se pudo convertir el valor '{monto_en_texto}' a un número.")
        return 0.0

if __name__== "__main__":
    # Pista 3: Crea una variable que contenga la ruta a tu archivo CSV.
    # Ruta relativa a la raíz del proyecto
    ruta_archivo_prueba = 'data/raw/sample_transactions.csv'

    # Llamamosa nuestra función para probarla
    leer_transacciones_csv(ruta_archivo_prueba)
    transacciones_limpias = leer_transacciones_csv(ruta_archivo_prueba)

    print("\n Resultado Final")
    for transaccion in transacciones_limpias:
        print(transaccion)