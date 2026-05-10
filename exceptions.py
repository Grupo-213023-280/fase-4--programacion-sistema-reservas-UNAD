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
Custom exceptions module
Defines specific system errors
"""


class ClientError(Exception):
    """Raised when client data is invalid"""
    pass


class ServiceError(Exception):
    """Raised when a service is invalid"""
    pass


class ReservationError(Exception):
    """Raised when reservation cannot be processed"""
    pass