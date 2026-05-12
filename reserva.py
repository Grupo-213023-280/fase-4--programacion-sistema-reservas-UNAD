# INFORMACION DEL COMPONENTE PRACTICO  Ejercicio 1
# Fase 4 Componente Práctico-Practicas Simuladas Sistema de Gestion de clienetes, Servicios y Reservas 
# Curso: Programación - UNAD 213023_280
# Autor: William Beltrán
# Claudia Lorena Franco
# Farid Camilo Buitrago
# ============================================================

# ============================================
# NATIONAL OPEN AND DISTANCE UNIVERSITY (UNAD)
# COURSE: PROGRAMMING
# ACTIVITY: PHASE 4 - OOP
# STUDENTS: William Beltrán
# Claudia Lorena Franco
# Farid Camilo Buitrago
# ============================================

# Practical Exercise - Simulated Practices: Customer, Service, and Reservation Management System
# Course: Programming - UNAD 213023_280
# Author: William Beltrán
# Claudia Lorena Franco
# Farid Camilo Buitrago
# Concepts applied:
# including custom exceptions, use of try/except, try/except/else, try/except/finally blocks, and exception chaining.

import tkinter as tk


# ============================================
# BASE CLASS (ENCAPSULATION)
# ============================================

"""
Reservation module
Handles reservation operations
"""

from exceptions import ReservationError


class Reservation:

    def __init__(self, client, service, duration):

        if duration <= 0:
            raise ReservationError("Reservation duration must be positive")

        self.client = client
        self.service = service
        self.duration = duration
        self.status = "Pending"

    def confirm(self):

        self.status = "Confirmed"

    def cancel(self):

        self.status = "Canceled"

    def process(self):

        cost = self.service.calcular_costo(self.duration)

        return cost