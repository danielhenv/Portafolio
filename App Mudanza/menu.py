from services import ReservationService
from colorama import init, Fore, Style

#colorama para que funcione en Windows y otros SO
init(autoreset=True)

service = ReservationService()

def menu():
    while True:
        print(Fore.CYAN + "\n=== SISTEMA DE RESERVAS DE MUDANZAS ===" + Style.RESET_ALL)
        print("1. Crear reserva")
        print("2. Listar todas las reservas")
        print("3. Buscar reserva por ID")
        print("4. Modificar reserva")
        print("5. Eliminar reserva")
        print("6. Buscar reservas por cliente")
        print("7. Buscar reservas por fecha")
        print("0. Salir")

        opcion = input(Fore.YELLOW + "Seleccione una opción: " + Style.RESET_ALL).strip()

        if opcion == "1":
            crear_reserva()
        elif opcion == "2":
            listar_reservas()
        elif opcion == "3":
            buscar_por_id()
        elif opcion == "4":
            modificar_reserva()
        elif opcion == "5":
            eliminar_reserva()
        elif opcion == "6":
            buscar_por_cliente()
        elif opcion == "7":
            buscar_por_fecha()
        elif opcion == "0":
            print(Fore.GREEN + "Gracias por usar el sistema. ¡Hasta luego!" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Opción inválida." + Style.RESET_ALL)

# --- Funciones del menú ---

def crear_reserva():
    try:
        data = {
            "customer_name": input("Nombre del cliente: ").strip(),
            "email": input("Email: ").strip(),
            "phone": input("Teléfono: ").strip(),
            "pickup_address": input("Dirección de recogida: ").strip(),
            "delivery_address": input("Dirección de entrega: ").strip(),
            "date": input("Fecha (AAAA-MM-DD): ").strip(),
            "time": input("Hora (HH:MM): ").strip(),
            "service_type": input("Tipo de servicio (mudanza local/nacional/internacional): ").strip(),
            "notes": input("Notas adicionales (opcional): ").strip()
        }
        service.create(**data)
    except ValueError as e:
        print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)

def listar_reservas():
    reservas = service.list_all()
    if not reservas:
        print(Fore.YELLOW + "No hay reservas registradas." + Style.RESET_ALL)
    else:
        for r in reservas:
            print(Fore.CYAN + "\n" + service.format_reservation(r) + Style.RESET_ALL)

def buscar_por_id():
    rid = input("Ingrese el ID de la reserva: ").strip()
    res = service.get(rid)
    if res:
        print(Fore.CYAN + "\n" + service.format_reservation(res) + Style.RESET_ALL)
    else:
        print(Fore.RED + "No se encontró una reserva con ese ID." + Style.RESET_ALL)

def modificar_reserva():
    rid = input("Ingrese el ID de la reserva a modificar: ").strip()
    res = service.get(rid)
    if not res:
        print(Fore.RED + "No se encontró la reserva." + Style.RESET_ALL)
        return

    print("Deje en blanco para mantener el valor actual.")
    data = {
        "customer_name": input(f"Nombre ({res.customer_name}): ").strip() or res.customer_name,
        "email": input(f"Email ({res.email}): ").strip() or res.email,
        "phone": input(f"Teléfono ({res.phone}): ").strip() or res.phone,
        "pickup_address": input(f"Dirección de recogida ({res.pickup_address}): ").strip() or res.pickup_address,
        "delivery_address": input(f"Dirección de entrega ({res.delivery_address}): ").strip() or res.delivery_address,
        "date": input(f"Fecha ({res.date}): ").strip() or res.date,
        "time": input(f"Hora ({res.time}): ").strip() or res.time,
        "service_type": input(f"Servicio ({res.service_type}): ").strip() or res.service_type,
        "notes": input(f"Notas ({res.notes or '-'}): ").strip() or res.notes
    }
    try:
        service.update(rid, **data)
    except ValueError as e:
        print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)

def eliminar_reserva():
    rid = input("Ingrese el ID de la reserva a eliminar: ").strip()
    service.delete(rid)

def buscar_por_cliente():
    nombre = input("Ingrese parte del nombre del cliente: ").strip()
    resultados = service.search_by_customer(nombre)
    if resultados:
        for r in resultados:
            print(Fore.CYAN + "\n" + service.format_reservation(r) + Style.RESET_ALL)
    else:
        print(Fore.YELLOW + "No se encontraron reservas para ese cliente." + Style.RESET_ALL)

def buscar_por_fecha():
    fecha = input("Ingrese la fecha (AAAA-MM-DD): ").strip()
    resultados = service.search_by_date(fecha)
    if resultados:
        for r in resultados:
            print(Fore.CYAN + "\n" + service.format_reservation(r) + Style.RESET_ALL)
    else:
        print(Fore.YELLOW + "No se encontraron reservas para esa fecha." + Style.RESET_ALL)

if __name__ == "__main__":
    menu()