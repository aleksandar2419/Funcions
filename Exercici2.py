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
    preu_final = preu - (preu * descompte / 100)
    return preu_final

print(aplicar_descompte(100, "particular"))   # 100.0
print(aplicar_descompte(100, "Empresa"))      # 90.0
print(aplicar_descompte(100, "HABITUAL"))     # 85.0
print(aplicar_descompte(100, "vip"))          # Error + 100