vlan = int(input("Ingrese el número de VLAN: "))
if vlan >= 1 and vlan <= 1005:
    print("La VLAN " + str(vlan) + " pertenece al rango normal.")
elif vlan >= 1006 and vlan <= 4094:
    print("La VLAN " + str(vlan) + " pertenece al rango extendido.")
else:
    print("Número de VLAN inválido.")