# Este será nuestro primer auditor. Se enfocará en una tarea simple:
# detectar transacciones que superen un cierto monto.

def detectar_anomalias_por_monto(transacciones, umbral):
    """
    Revisa una lista de transacciones y devuelve aquellas cuyo monto supera un umbral.

    :param transacciones: Una lista de diccionarios, donde cada diccionario es una transacción.
    :param umbral: Un número (float o int) que representa el monto a superar.
    :return: Una lista con las transacciones consideradas anómalas.
    """
    anomalias_encontradas = []

    for transaccion in transacciones:
        if transaccion['Monto'] > umbral:
            anomalias_encontradas.append(transaccion)

    return anomalias_encontradas


# Bloque de prueba para nuestro detector de anomalías.
if __name__ == "__main__":
    print("--- Probando el Detector de Anormalías ---")
    
    # Creamos datos de prueba
    transacciones_de_prueba = [
        {'Descripcion': 'Supermercado', 'Monto': 8500.0, 'Categoria': 'Alimentación'},
        {'Descripcion': 'Cena de lujo', 'Monto': 45000.0, 'Categoria': 'Alimentación'},
        {'Descripcion': 'Compra online', 'Monto': 78000.0, 'Categoria': 'Ocio'},
        {'Descripcion': 'Taxi', 'Monto': 4500.0, 'Categoria': 'Transporte'},
    ]
    
    umbral_de_prueba = 40000.0
    
    # Llamamos a nuestra nueva función
    anomalias = detectar_anomalias_por_monto(transacciones_de_prueba, umbral_de_prueba)
    
    print(f"Se encontraron {len(anomalias)} anomalías por encima de ${umbral_de_prueba}:")
    for anomalia in anomalias:
        print(f"- {anomalia['Descripcion']} por un monto de ${anomalia['Monto']}")

    if not anomalias:
        print("- Ninguna.")
