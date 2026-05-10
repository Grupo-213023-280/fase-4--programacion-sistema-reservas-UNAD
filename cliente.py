# ============================================================
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
# STUDENT: William Beltrán
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
# BASE CLASS (ENCAPSULATION) 1
# ============================================

"""
Client class
Represents a company client
"""

from exceptions import ClientError


class Client:

    def __init__(self, name, email):

        if not name:
            raise ClientError("Client name cannot be empty")

        if "@" not in email:
            raise ClientError("Invalid email address")

        self.__name = name
        self.__email = email

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def show_client(self):

        return f"Client: {self.__name} | Email: {self.__email}"