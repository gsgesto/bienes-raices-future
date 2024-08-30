from services.propiedad_service import add_property, update_property, delete_property, get_property, list_all_properties
from services.report_service import list_properties_by_status_and_operation

def main():
    while True:
        print("\nBienes Raices Future System")
        print("1. Agregar Propiedad")
        print("2. Actualizar Propiedad")
        print("3. Eliminar Propiedad")
        print("4. Ver Propiedad")
        print("5. Listar Todas las Propiedades")
        print("6. Listar Propiedades Disponibles para Venta")
        print("7. Listar Propiedades Disponibles para Alquiler")
        print("8. Listar Propiedades Vendidas")
        print("9. Listar Propiedades Alquiladas")
        print("0. Salir")

        choice = input("Ingrese una opción: ")

        if choice == '1':
            add_property()
        elif choice == '2':
            update_property()
        elif choice == '3':
            delete_property()
        elif choice == '4':
            get_property()
        elif choice == '5':
            list_all_properties()
        elif choice == '6':
            list_properties_by_status_and_operation(1, 1)
        elif choice == '7':
           list_properties_by_status_and_operation(1, 2)
        elif choice == '8':
           list_properties_by_status_and_operation(2, 1)
        elif choice == '9':
           list_properties_by_status_and_operation(2, 2)
        elif choice == '0':
            break
        else:
            print("Opción no válida, intente nuevamente.")

if __name__ == "__main__":
    main()
