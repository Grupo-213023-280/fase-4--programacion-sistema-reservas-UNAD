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
# BASE CLASS (ENCAPSULATION)
# ============================================

"""
Main system execution
Simulates system operations
"""

from cliente import Client
from servicio import RoomReservation, EquipmentRental, Consulting
from reserva import Reservation
from logger import log_event


def simulate_operations():

    operations = []

    try:

        c1 = Client("William", "william@email.com")
        s1 = RoomReservation("Meeting Room", 50)
        r1 = Reservation(c1, s1, 2)

        cost = r1.process()
        r1.confirm()

        operations.append((c1.show_client(), cost, r1.status))

    except Exception as e:
        log_event(str(e))


    try:

        # invalid email
        c2 = Client("Pedro", "correo_invalido")

    except Exception as e:
        log_event(str(e))


    try:

        s2 = EquipmentRental("Projector", 30)
        r2 = Reservation(c1, s2, 3)

        cost = r2.process()

        operations.append(("Equipment rental", cost))

    except Exception as e:
        log_event(str(e))


    try:

        s3 = Consulting("Software consulting", 100)
        r3 = Reservation(c1, s3, 5)

        cost = r3.process()

        operations.append(("Consulting", cost))

    except Exception as e:
        log_event(str(e))


    return operations


def main():

    results = simulate_operations()

    for r in results:

        print(r)


if __name__ == "__main__":
    main()