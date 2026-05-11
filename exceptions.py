"""
Sistema Integral de Gestión de Clientes, Servicios y Reservas - Software FJ
Curso: Programación 213023
Universidad Nacional Abierta y Distancia - UNAD
Archivo: excepciones.py
Autor: Farid Camilo Buritica Buitrago
Descripción: Excepciones personalizadas
"""

class SistemaException(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class DatosInvalidosError(SistemaException):
    pass
