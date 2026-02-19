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


def detectar_suscripciones(transacciones):
    """
    Detecta posibles suscripciones agrupando transacciones por descripción similar.
    Una suscripción se considera un grupo de 2 o más transacciones.
    """
    grupos = {}

    for transaccion in transacciones:
        descripcion_limpia = transaccion["Descripcion"].lower().strip().replace(".", "")
        lista_existente = grupos.get(descripcion_limpia, [])
        lista_existente.append(transaccion)
        grupos[descripcion_limpia] = lista_existente

    suscripciones_detectadas = []

    for grupo in grupos.values():
        if len(grupo) > 1:
            suscripciones_detectadas.append(grupo)
    return suscripciones_detectadas


# Bloque de prueba para nuestros detectores.
if __name__ == "__main__":
    print("--- Probando el Detector de Anormalías por Monto ---")
    
    # Creamos datos de prueba más completos
    transacciones_de_prueba = [
        {'Descripcion': 'Supermercado', 'Monto': 8500.0, 'Categoria': 'Alimentación'},
        {'Descripcion': 'Cena de lujo', 'Monto': 45000.0, 'Categoria': 'Alimentación'},
        {'Descripcion': 'NETFLIX.COM', 'Monto': 7500.0, 'Categoria': 'Ocio'},
        {'Descripcion': 'Compra online', 'Monto': 78000.0, 'Categoria': 'Ocio'},
        {'Descripcion': ' Spotify AB', 'Monto': 4500.0, 'Categoria': 'Ocio'},
        {'Descripcion': 'Taxi', 'Monto': 4500.0, 'Categoria': 'Transporte'},
        {'Descripcion': 'netflix.com ', 'Monto': 7500.0, 'Categoria': 'Ocio'},
        {'Descripcion': 'Spotify AB', 'Monto': 4550.0, 'Categoria': 'Ocio'},
    ]
    
    umbral_de_prueba = 40000.0
    anomalias = detectar_anomalias_por_monto(transacciones_de_prueba, umbral_de_prueba)
    
    print(f"\nSe encontraron {len(anomalias)} anomalías por encima de ${umbral_de_prueba}:")
    for anomalia in anomalias:
        print(f"- {anomalia['Descripcion']} por un monto de ${anomalia['Monto']}")
    if not anomalias:
        print("- Ninguna.")

    print("\n--- Probando el Detector de Suscripciones ---")
    suscripciones = detectar_suscripciones(transacciones_de_prueba)
    print(f"\nSe encontraron {len(suscripciones)} grupos de suscripciones:")
    for grupo in suscripciones:
        # Tomamos la descripción del primer elemento del grupo para nombrarlo
        nombre_suscripcion = grupo[0]['Descripcion'].strip().lower()
        print(f"- Grupo '{nombre_suscripcion}': {len(grupo)} transacciones encontradas.")
        for transaccion in grupo:
            print(f"  - Monto: ${transaccion['Monto']}")
    if not suscripciones:
        print("- Ninguna.")
