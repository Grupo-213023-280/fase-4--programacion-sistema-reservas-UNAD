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
Logger module
Stores system events and errors
"""

from datetime import datetime


def log_event(message):

    with open("logs.txt", "a") as file:

        timestamp = datetime.now()

        file.write(f"{timestamp} - {message}\n")
        