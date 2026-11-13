# ---------- FUNCIONS DE CÀLCUL ----------

def calcular_preu(preu_peces, cost_ma_obra):
    # Preu inicial de la reparació (peces + mà d'obra)
    return preu_peces + cost_ma_obra


def tipus_valid(tipus_client):
    # Comprova si el tipus de client és un dels permesos
    # (accepta majúscules i minúscules gràcies a lower())
    return tipus_client.lower() in ("particular", "empresa", "habitual")


def aplicar_descompte(preu, tipus_client):
    tipus = tipus_client.lower()

    if tipus == "particular":
        descompte = 0
    elif tipus == "empresa":
        descompte = 10
    elif tipus == "habitual":
        descompte = 15
    else:
        print(f"Error: el tipus de client '{tipus_client}' no és vàlid.")
        return preu

    return preu - (preu * descompte / 100)


def calcular_iva(preu):
    # Retorna només l'import de l'IVA (21 %)
    return preu * 21 / 100


def calcular_factura(preu, tipus_client):
    # Reutilitza les funcions anteriors
    preu_descompte = aplicar_descompte(preu, tipus_client)
    iva = calcular_iva(preu_descompte)
    return preu_descompte + iva


# ---------- FUNCIONS D'INTERFÍCIE ----------

def mostrar_menu():
    print("\n===== SERVEI TÈCNIC INFORMÀTIC =====\n")
    print("1. Introduir una nova reparació")
    print("2. Consultar el nombre de reparacions")
    print("3. Consultar la facturació acumulada")
    print("4. Sortir\n")


def mostrar_factura(nom, preu_inicial, descompte, iva, total):
    print("\n------------- FACTURA -------------")
    print(f"Client:          {nom}")
    print(f"Preu inicial:    {preu_inicial:.2f} €")
    print(f"Descompte:      -{descompte:.2f} €")
    print(f"IVA (21 %):      {iva:.2f} €")
    print(f"TOTAL A PAGAR:   {total:.2f} €")
    print("-----------------------------------")


def nova_reparacio():
    # Demana les dades, calcula i mostra la factura.
    # Retorna el total facturat, o None si la reparació no s'ha pogut registrar.
    nom = input("Nom del client: ")
    peces = float(input("Cost de les peces (€): "))
    ma_obra = float(input("Cost de la mà d'obra (€): "))
    tipus = input("Tipus de client (particular / empresa / habitual): ")

    if not tipus_valid(tipus):
        print("Error: tipus de client no vàlid. La reparació no s'ha registrat.")
        return None

    preu_inicial = calcular_preu(peces, ma_obra)
    preu_descompte = aplicar_descompte(preu_inicial, tipus)
    descompte = preu_inicial - preu_descompte
    iva = calcular_iva(preu_descompte)
    total = calcular_factura(preu_inicial, tipus)

    mostrar_factura(nom, preu_inicial, descompte, iva, total)
    return total


# ---------- PROGRAMA PRINCIPAL ----------

def main():
    # Variables que mantenen l'estat del programa
    num_reparacions = 0
    facturacio_total = 0

    opcio = ""
    while opcio != "4":
        mostrar_menu()
        opcio = input("Selecciona una opció: ")

        if opcio == "1":
            total = nova_reparacio()
            if total is not None:
                num_reparacions += 1
                facturacio_total += total
        elif opcio == "2":
            print(f"Reparacions realitzades: {num_reparacions}")
        elif opcio == "3":
            print(f"Facturació acumulada: {facturacio_total:.2f} €")
        elif opcio == "4":
            print("Fins aviat!")
        else:
            print("Opció no vàlida. Tria un número de l'1 al 4.")


main()