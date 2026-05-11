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

from cliente import Cliente
from servicios import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from reserva import Reservation
from logger import log_event


def simulate_operations():

    operations = []

    try:
        c1 = Cliente("William", "william@email.com")
        
        s1 = ReservaSala("Meeting Room", 50, 10)                    # nombre, precio, capacidad
        r1 = Reservation(c1, s1, 2)

        cost = r1.process()
        r1.confirm()

        operations.append((c1.show_client() if hasattr(c1,'show_client') else str(c1), cost, r1.status))

    except Exception as e:
        print("Error en primera reserva:", e)

    try:
        # Email inválido (debe fallar)
        c2 = Cliente("Pedro", "correo_invalido")
    except Exception as e:
        print("Error esperado con email:", e)

    try:
        s2 = AlquilerEquipo("Projector", 30, "Proyector", 8)
        r2 = Reservation(c1, s2, 3)
        cost = r2.process()
        operations.append(("Equipment rental", cost))
    except Exception as e:
        print("Error en alquiler:", e)

    try:
        s3 = AsesoriaEspecializada("Software consulting", 100, "Juan Pérez", 2)
        r3 = Reservation(c1, s3, 5)
        cost = r3.process()
        operations.append(("Consulting", cost))
    except Exception as e:
        print("Error en asesoría:", e)

    return operations


def main():

    results = simulate_operations()

    for r in results:

        print(r)


if __name__ == "__main__":
    main()
