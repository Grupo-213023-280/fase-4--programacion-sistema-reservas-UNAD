"""
Sistema Integral de Gestión de Clientes, Servicios y Reservas - Software FJ
Curso: Programación 213023
Universidad Nacional Abierta y Distancia - UNAD

Archivo: excepciones.py
Autor: Faid Camilo Buritica Buitrago
Descripción: Excepciones personalizadas para el manejo de errores del sistema
"""

class SistemaException(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class DatosInvalidosError(SistemaException):
    pass

class ClienteNoExisteError(SistemaException):
    pass

class ServicioNoDisponibleError(SistemaException):
    pass

class ReservaInvalidaError(SistemaException):
    pass
