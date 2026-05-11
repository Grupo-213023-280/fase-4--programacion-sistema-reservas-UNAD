"""
Sistema Integral de Gestión de Clientes, Servicios y Reservas - Software FJ
Curso: Programación 213023
Universidad Nacional Abierta y Distancia - UNAD
Archivo: excepciones.py
Autor: Farid Camilo Buritica Buitrago
Descripción: Excepciones personalizadas
"""

class ReservationError(Exception):
    """Excepción para errores en reservas"""
    def __init__(self, message="Error en la reserva"):
        self.message = message
        super().__init__(self.message)


class ClientError(Exception):
    """Excepción para errores en clientes"""
    def __init__(self, message="Error en el cliente"):
        self.message = message
        super().__init__(self.message)


class ServiceError(Exception):
    """Excepción para errores en servicios"""
    def __init__(self, message="Error en el servicio"):
        self.message = message
        super().__init__(self.message)


class DatosInvalidosError(Exception):
    """Excepción para datos inválidos (usada en Cliente)"""
    def __init__(self, message="Datos inválidos"):
        self.message = message
        super().__init__(self.message)
