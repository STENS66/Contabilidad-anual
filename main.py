# -*- coding: utf-8 -*-
"""
Contabilidad Anual - Versión Española 1.7

Copyright © Gaëtan Sencie 2023
Todos los derechos reservados.
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from tkinter.filedialog import asksaveasfilename
import os
import json
from reportlab.lib.pagesizes import letter, landscape
from reportlab.pdfgen import canvas
import openpyxl
import openpyxl.styles as styles
from openpyxl.styles import PatternFill
from openpyxl.styles.colors import Color
from openpyxl.utils import get_column_letter
from openpyxl.styles import Alignment
from openpyxl.styles import Font
from openpyxl import Workbook, chart

"código Python bajo licencia"

if __name__ == "__main__":
    app = ExampleApp()
    app.mainloop()
