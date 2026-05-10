"""
Sistema Integral de Gestión de Clientes, Servicios y Reservas - Software FJ
Curso: Programación 213023
Universidad Nacional Abierta y Distancia - UNAD
Archivo: cliente.py
Autor: Farid Camilo Buritica Buitrago
Descripción: Clase Cliente con encapsulación y validaciones robustas
"""

from entidad_abstracta import EntidadAbstracta
from excepciones import DatosInvalidosError

class Cliente(EntidadAbstracta):
    """
    Clase Cliente que hereda de EntidadAbstracta.
    Implementa encapsulación y validaciones estrictas de datos.
    """

    def __init__(self, id_cliente: str, nombre: str, email: str, telefono: str):
        """
        Constructor de la clase Cliente.
        Llama al constructor de la clase padre y valida los datos.
        """
        super().__init__(id_cliente)                    # Llamada a la clase abstracta
        self._validar_datos(nombre, email, telefono)    # Validaciones robustas

        # Atributos privados (encapsulación)
        self._nombre = nombre
        self._email = email
        self._telefono = telefono
        self._reservas = []  
        
        #Lista para guardar IDs de reservas futuras
        print(f"✓ Cliente {id_cliente} creado exitosamente.")  
        
    # Mensaje de confirmación
    def _validar_datos(self, nombre: str, email: str, telefono: str):
        """
        Método privado para validar todos los datos del cliente.
        Lanza excepciones personalizadas si los datos son inválidos.
        """
        if not nombre or len(nombre.strip()) < 3:
            raise DatosInvalidosError("El nombre debe tener al menos 3 caracteres.")

        if "@" not in email or "." not in email:
            raise DatosInvalidosError("El email proporcionado no es válido.")

        if not telefono or len(telefono) < 7:
            raise DatosInvalidosError("El número de teléfono no es válido.")

    # ENCAPSULACIÓN 
    @property
    def nombre(self) -> str:
        """Permite leer el nombre de forma segura."""
        return self._nombre

    @property
    def email(self) -> str:
        """Permite leer el email de forma segura."""
        return self._email

    @property
    def telefono(self) -> str:
        """Permite leer el teléfono de forma segura."""
        return self._telefono

    #MÉTODOS 
    def agregar_reserva(self, id_reserva: str):
        """Agrega un ID de reserva al historial del cliente."""
        self._reservas.append(id_reserva)

    def obtener_info(self) -> str:
        """Implementación del método abstracto."""
        return f"Cliente[{self.id}] - {self._nombre} | {self._email}"

    def __str__(self):
        return self.obtener_info()
