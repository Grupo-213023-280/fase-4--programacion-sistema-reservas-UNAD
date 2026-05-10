"""
Sistema Integral de Gestión de Clientes, Servicios y Reservas - Software FJ
Curso: Programación 213023
Universidad Nacional Abierta y Distancia - UNAD
Archivo: entidad_abstracta.py
Autor: Farid Camilo Buritica Buitrago
Descripción: Clase abstracta principal del sistema
"""

from abc import ABC, abstractmethod


class EntidadAbstracta(ABC):
    """
    Clase abstracta que sirve como base para todas las entidades del sistema.
    """

    def __init__(self, id_entidad: str):
        """Constructor de la entidad abstracta."""
        if not id_entidad or not isinstance(id_entidad, str):
            raise ValueError("El ID de la entidad no puede estar vacío.")
        
        self._id = id_entidad

    @property
    def id(self) -> str:
        """Retorna el ID de la entidad."""
        return self._id

    @abstractmethod
    def obtener_info(self) -> str:
        """Método abstracto que deben implementar las clases hijas."""
        pass

    def __str__(self):
        """Representación en texto de la entidad."""
        return self.obtener_info()
