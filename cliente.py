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
    """

    def __init__(self, id_cliente: str, nombre: str, email: str, telefono: str):
        super().__init__(id_cliente)
        self._validar_datos(nombre, email, telefono)
        
        self._nombre = nombre
        self._email = email
        self._telefono = telefono
        self._reservas = []

    def _validar_datos(self, nombre: str, email: str, telefono: str):
        if not nombre or len(nombre.strip()) < 3:
            raise DatosInvalidosError("El nombre debe tener al menos 3 caracteres.")

        if "@" not in email or "." not in email:
            raise DatosInvalidosError("El email no es válido.")

        if not telefono or len(telefono) < 7:
            raise DatosInvalidosError("El teléfono no es válido.")

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def email(self) -> str:
        return self._email

    @property
    def telefono(self) -> str:
        return self._telefono

    def agregar_reserva(self, id_reserva: str):
        self._reservas.append(id_reserva)

    def obtener_info(self) -> str:
        return f"Cliente[{self.id}] - {self._nombre} | {self._email}"

    def __str__(self):
        return self.obtener_info()
