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
    Cumple con el requisito de la actividad: "Una clase abstracta que represente 
    entidades generales del sistema".
    """

    def __init__(self, id_entidad: str):
        """
        Constructor de la clase abstracta.
        Valida que el ID no esté vacío.
        """
        if not id_entidad or not isinstance(id_entidad, str):
            raise ValueError("El ID de la entidad no puede estar vacío ni ser nulo.")
        
        self._id = id_entidad  # Atributo protegido

    @property
    def id(self) -> str:
        """Getter para obtener el ID de forma segura."""
        return self._id

    @abstractmethod
    def obtener_info(self) -> str:
        """
        Método abstracto que obliga a todas las clases hijas
        a implementar su propia forma de mostrar información.
        """
        pass

    def __str__(self):
        """Representación en cadena de la entidad."""
        return self.obtener_info()
