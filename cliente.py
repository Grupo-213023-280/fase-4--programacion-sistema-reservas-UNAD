"""
Sistema Integral de Gestión de Clientes, Servicios y Reservas - Software FJ
Curso: Programación 213023
Universidad Nacional Abierta y Distancia - UNAD

Archivo: cliente.py
Autor: Farid Camilo Buritica Buitrago
Descripción: Clase Cliente con encapsulación y validaciones robustas
"""

from excepciones import DatosInvalidosError

class Cliente:
    def __init__(self, id_cliente: str, nombre: str, email: str, telefono: str):
        self._validar_datos(id_cliente, nombre, email, telefono)
        self._id_cliente = id_cliente
        self._nombre = nombre
        self._email = email
        self._telefono = telefono
        self._reservas = []

    def _validar_datos(self, id_cliente, nombre, email, telefono):
        if not id_cliente or len(id_cliente) < 3:
            raise DatosInvalidosError("ID de cliente inválido")
        if not nombre or len(nombre.strip()) < 3:
            raise DatosInvalidosError("El nombre debe tener mínimo 3 caracteres")
        if "@" not in email or "." not in email:
            raise DatosInvalidosError("Email inválido")
        if not telefono or len(telefono) < 7:
            raise DatosInvalidosError("Teléfono inválido")

    @property
    def id_cliente(self):
        return self._id_cliente

    @property
    def nombre(self):
        return self._nombre

    def agregar_reserva(self, id_reserva):
        self._reservas.append(id_reserva)

    def __str__(self):
        return f"Cliente[{self._id_cliente}] - {self._nombre} | {self._email}"
