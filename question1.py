"""Laboratorio 8 - Problema 1.

Implementa una CLI que calcule carga por punto de soporte.
"""

import sys
 
try:
    total_load = float(sys.argv[1])
    num_supports = float(sys.argv[2])
except (IndexError, ValueError):
    print("Error: Invalid input! Enter numeric values only.")
    sys.exit(1)
 
if num_supports == 0:
    print("Error: Cannot divide by zero! Supports must be greater than zero.")
    sys.exit(1)
 
load_per_support = total_load / num_supports
print(f"Load per support point: {load_per_support:.2f} N")
 
