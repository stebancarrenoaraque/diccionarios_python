def main():
	agenda = {}
	while True:
		print("\nAGENDA TELEFÓNICA")
		print("1 - Agregar un amigo")
		print("2 - Consultar teléfono")
		print("3 - Eliminar un amigo")
		print("0 - Salir")

		opcion = input("Elige una opción: ").strip()

		if opcion == "1":
			nombre = input("Nombre: ").strip().upper()
			if nombre == "":
				print("El nombre no puede estar vacío.")
				continue
			telefono = input("Teléfono: ").strip()
			if telefono == "":
				print("El teléfono no puede estar vacío.")
				continue
			agenda[nombre] = telefono
			print(f"Guardado: {nombre} -> {telefono}")

		elif opcion == "2":
			nombre = input("Nombre a consultar: ").strip().upper()
			if nombre in agenda:
				print(f"{nombre}: {agenda[nombre]}")
			else:
				print("No hay ese contacto en la agenda.")

		elif opcion == "3":
			nombre = input("Nombre a eliminar: ").strip().upper()
			if nombre in agenda:
				del agenda[nombre]
				print(f"{nombre} fue eliminado.")
			else:
				print("No se encontró ese nombre.")

		elif opcion == "0":
			print("Saliendo. ¡Hasta luego!")
			break

		else:
			print("Opción no válida, prueba otra vez.")


if __name__ == "__main__":
	main()