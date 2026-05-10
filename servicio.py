# ============================================================
# SISTEMA DE CONTROL DE DISPOSITIVOS INTELIGENTES- EJERCISIO 5 
# Fase 3 - Modelos de herencia y polimorfismo y gestion de metodos 
# Curso: Programación - UNAD
# Autor: William Beltrán
# ============================================================

# ============================================
# NATIONAL OPEN AND DISTANCE UNIVERSITY (UNAD)
# COURSE: PROGRAMMING
# ACTIVITY: PHASE 3 - OOP
# STUDENT: [YOUR NAME]
# ============================================

# This program implements a Smart Device Control System using
# Object-Oriented Programming (OOP) principles.
#
# Concepts applied:
# - Inheritance
# - Polymorphism
# - Method Overloading (simulated with optional parameters)
# - Encapsulation
#
# A graphical user interface (GUI) is also implemented using Tkinter,
# allowing user interaction with the system.

import tkinter as tk

# ============================================
# BASE CLASS (ENCAPSULATION)
# ============================================

"""
Service module
Defines different services offered by the company
"""

from abc import ABC, abstractmethod


# Abstract base class
class Service(ABC):

    def __init__(self, name, price):
        self.name = name
        self.price = price

    @abstractmethod
    def calculate_cost(self, duration):
        pass


# Room reservation service
class RoomReservation(Service):

    def calculate_cost(self, hours):
        return self.price * hours


# Equipment rental service
class EquipmentRental(Service):

    def calculate_cost(self, days):
        return self.price * days


# Consulting service
class Consulting(Service):

    def calculate_cost(self, hours):
        return self.price * hours * 1.2