import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import math

import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np

from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.scrolled import ScrolledText
from ttkbootstrap.style import Style

import solution


def is_valid(input_val, min_val):
    return int(input_val) >= min_val


def create_matrix():
    try:
        rows_count = int(rows.get())
        cols_count = int(cols.get())
        if is_valid(rows_count, 1) and is_valid(cols_count, 1):
            print(f"Creating matrix with {rows_count} rows and {cols_count} columns.")
            clear_below_row(4, rref_frame)
            global matrix
            matrix = []
            poly_heading = tb.Label(rref_frame, text="Input matrix", font=underlined_font)
            poly_heading.grid(row=4, column=0, columnspan=2, padx=20, pady=20, sticky=W)
            for i in range(0, rows_count):
                vector = []
                row_label = tb.Label(rref_frame, text="Row " + str(i+1) + ":")
                row_label.grid(row=5+i, column=0, padx=20, pady=10, sticky=W)
                for j in range(0, cols_count):
                    entry = tb.Entry(rref_frame, width=5)
                    entry.grid(row=5+i, column=j+1, padx=4, pady=10, sticky=W)
                    vector.append(entry)
                matrix.append(vector)
            matB1 = tb.Button(rref_frame, text="Solve Matrix", bootstyle="success", command=calculate_rref)
            matB1.grid(row=5+rows_count, column=0, padx=20, pady=10, sticky=W)
        else:
            messagebox.showerror("Input Error", "Rows and columns must be an integer >= 1.")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for rows and columns.")


def create_array():
    try:
        degree = int(deg.get())
        if is_valid(degree, 0):
            print(f"Creating array for polynomial of degree {degree}.")
            clear_below_row(3, sdiv_frame)
            global array
            array = []
            global lin_div
            lin_div = []
            poly_heading = tb.Label(sdiv_frame, text="Input polynomials", font=underlined_font)
            poly_heading.grid(row=3, column=0, columnspan=2, padx=20, pady=20, sticky=W)
            poly_label = tb.Label(sdiv_frame, text="Polynomial coefficients:")
            poly_label.grid(row=4, column=0, padx=20, pady=10, sticky=W)
            for i in range(0, degree+1):
                entry = tb.Entry(sdiv_frame, width=5)
                entry.grid(row=4, column=i+1, padx=4, pady=10, sticky=W)
                array.append(entry)
            lin_label = tb.Label(sdiv_frame, text="Linear divisor coefficients:")
            lin_label.grid(row=5, column=0, padx=20, pady=10, sticky=W)
            lin_entry1 = tb.Entry(sdiv_frame, width=5)
            lin_entry1.grid(row=5, column=1, padx=4, pady=10, sticky=W)
            lin_entry2 = tb.Entry(sdiv_frame, width=5)
            lin_entry2.grid(row=5, column=2, padx=4, pady=10, sticky=W)
            lin_div.append(lin_entry1)
            lin_div.append(lin_entry2)
            polB2 = tb.Button(sdiv_frame, text="Calculate", bootstyle="success", command=calculate_sdiv)
            polB2.grid(row=6, column=0, padx=20, pady=10, sticky=W)
        else:
            messagebox.showerror("Input Error", "Degree must be an integer >= 0.")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid polynomial degree.")


def calculate_rref():
    global matrix
    values_matrix = [[0] * len(matrix[0]) for _ in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            input_str = matrix[i][j].get()
            if input_str != "":
                try:
                    val = int(input_str)
                    values_matrix[i][j] = val
                except ValueError:
                    messagebox.showerror("Input Error", "Please only enter integers or leave blank")

    clear_below_row(6+len(matrix), rref_frame)

    orig_matrix = values_matrix
    orig_label = tb.Label(rref_frame, text="Original matrix:")
    orig_label.grid(row=6+len(orig_matrix), column=0, padx=20, pady=20, sticky=W)
    orig_frame = tb.Frame(rref_frame)
    orig_frame.grid(row=7+len(orig_matrix), column=0, padx=20, pady=20, sticky=W)
    on_render(render_latex_matrix(orig_matrix), orig_frame)

    # pass values_matrix to c++ Solution::int_rref function
    values_matrix = solution.PySolution.int_rref(solution.PySolution, values_matrix)
    # take output and assign it to values_matrix

    sol_label = tb.Label(rref_frame, text="Solved matrix:")
    sol_label.grid(row=8+len(orig_matrix), column=0, padx=20, pady=20, sticky=W)
    sol_frame = tb.Frame(rref_frame)
    sol_frame.grid(row=9+len(orig_matrix), column=0, padx=20, pady=20, sticky=W)
    on_render(render_latex_matrix(values_matrix), sol_frame)


def calculate_sdiv():
    global array
    global lin_div
    coefficients = [0] * len(array)
    for i in range(len(array)):
        input_str = array[i].get()
        if input_str != "":
            try:
                val = int(input_str)
                coefficients[i] = val
            except ValueError:
                messagebox.showerror("Input Error", "Please only enter integers or leave blank")
    linear_co = [0] * 2
    for i in range(len(lin_div)):
        input_str = lin_div[i].get()
        if input_str != "":
            try:
                val = int(input_str)
                linear_co[i] = val
            except ValueError:
                messagebox.showerror("Input Error", "Please only enter integers or leave blank")

    clear_below_row(7, sdiv_frame)

    # pass coefficients and linear_co to c++ Solution::int_sdiv function
    result = solution.PySolution.int_sdiv(solution.PySolution, coefficients, linear_co)

    orig_label = tb.Label(sdiv_frame, text="Polynomial:")
    orig_label.grid(row=7, column=0, padx=20, pady=20, sticky=W)
    orig_frame = tb.Frame(sdiv_frame)
    orig_frame.grid(row=8, column=0, padx=20, pady=20, sticky=W)
    on_render(poly_render(coefficients), orig_frame)

    lin_label = tb.Label(sdiv_frame, text="Linear divisor:")
    lin_label.grid(row=9, column=0, padx=20, pady=20, sticky=W)
    lin_frame = tb.Frame(sdiv_frame)
    lin_frame.grid(row=10, column=0, padx=20, pady=20, sticky=W)
    on_render(poly_render(linear_co), lin_frame)

    q_label = tb.Label(sdiv_frame, text="Quotient:")
    q_label.grid(row=11, column=0, padx=20, pady=20, sticky=W)
    q_frame = tb.Frame(sdiv_frame)
    q_frame.grid(row=12, column=0, padx=20, pady=20, sticky=W)
    numer = result[len(result)-1]
    result.pop()
    on_render(poly_render(result), q_frame)

    r_label = tb.Label(sdiv_frame, text="Remainder:")
    r_label.grid(row=13, column=0, padx=20, pady=20, sticky=W)
    r_frame = tb.Frame(sdiv_frame)
    r_frame.grid(row=14, column=0, padx=20, pady=20, sticky=W)
    on_render(frac_render(numer, linear_co), r_frame)


def render_latex_matrix(input_matrix):
    fig, ax = plt.subplots(figsize=(math.ceil(len(input_matrix[0])+1 / 3), math.ceil(len(input_matrix) / 2)))
    ax.axis('off')

    maxCols = max(40, len(input_matrix[0]))

    latex_preamble = f"\\setcounter{{MaxMatrixCols}}{{{maxCols}}}"

    latex_matrix = r'\begin{bmatrix}'
    latex_matrix += r' \\ '.join([' & '.join(map(str, row)) for row in input_matrix])
    latex_matrix += r'\end{bmatrix}'

    full_latex = f"${latex_preamble} {latex_matrix}$"

    ax.text(0.5, 0.5, f"${full_latex}$", fontsize=20, ha='center', va='center')

    return fig


def on_render(fig, canvas_frame):
    canvas = FigureCanvasTkAgg(fig, master=canvas_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)


def poly_render(coeffs):
    fig, ax = plt.subplots(figsize=(4, 2))
    ax.axis('off')

    n = len(coeffs)
    terms = []

    for i in range(n):
        coeff = coeffs[i]
        degree = n - i - 1

        if coeff == 0:
            continue

        if degree == 0:
            term = f"{coeff}"
        elif degree == 1:
            term = f"{coeff}x"
        else:
            term = f"{coeff}x^{degree}"

        if coeff > 0 and terms:
            term = f"+{term}"

        terms.append(term)

    latex_poly = " ".join(terms)

    if latex_poly == " " or latex_poly == "":
        latex_poly += r'0'

    ax.text(0.5, 0.5, f"${latex_poly}$", fontsize=20, ha='center', va='center')

    return fig


def frac_render(n, coeffs):
    fig, ax = plt.subplots(figsize=(4, 4))
    ax.axis('off')

    a, b = coeffs

    if n == 0:
        latex = "0"
    elif a == 0:
        if b == 0:
            latex = "0"
        else:
            latex = f"\\frac{{{n}}}{{{b}}}"
    elif b == 0:
        latex = f"\\frac{{{n}}}{{{a}x}}"
    elif b < 0:
        c = abs(b)
        latex = f"\\frac{{{n}}}{{{a}x - {c}}}"
    else:
        latex = f"\\frac{{{n}}}{{{a}x + {b}}}"

    ax.text(0.5, 0.5, f"${latex}$", fontsize=20, ha='center', va='center')

    return fig


def clear_below_row(start_row, frame):
    for widget in frame.winfo_children():
        row = widget.grid_info().get('row')
        if row and int(row) > start_row:
            widget.destroy()


def setup_tab(tab):
    canvas = tk.Canvas(tab)
    h_scrollbar = tk.Scrollbar(tab, orient="horizontal", command=canvas.xview)
    v_scrollbar = tk.Scrollbar(tab, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(scrollregion=canvas.bbox("all"))

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.grid(row=0, column=0, sticky="nsew")
    v_scrollbar.grid(row=0, column=1, sticky="ns")
    h_scrollbar.grid(row=1, column=0, sticky="ew")

    canvas.config(xscrollcommand=h_scrollbar.set, yscrollcommand=v_scrollbar.set)

    tab.grid_rowconfigure(0, weight=1)
    tab.grid_columnconfigure(0, weight=1)
    tab.grid_rowconfigure(1, weight=0)
    tab.grid_columnconfigure(1, weight=0)

    return scrollable_frame


matrix = []
array = []
lin_div = []

mpl.rcParams.update(mpl.rcParamsDefault)
mpl.rcParams['font.size'] = 20
mpl.rcParams['text.usetex'] = True
mpl.rcParams['text.latex.preamble'] = r'\usepackage{{amsmath}}'

# Begin GUI
root = tb.Window(title="Math Tools", themename="litera")
root.geometry("1200x800")
style = Style(theme="flatly")

nb = tb.Notebook(root, bootstyle="dark")
nb.pack(pady=20, fill="both", expand=True)

rref_frame_outer = tb.Frame(nb)
sdiv_frame_outer = tb.Frame(nb)
doc_frame = tb.Frame(nb)

nb.add(rref_frame_outer, text='Matrix RREF')
nb.add(sdiv_frame_outer, text='Synthetic Division')
nb.add(doc_frame, text='Instructions for use')

rref_frame = setup_tab(rref_frame_outer)
sdiv_frame = setup_tab(sdiv_frame_outer)

underlined_font = ("Arial", 10, "underline")

# Matrix RREF
dim1 = tb.Label(rref_frame, text="Input matrix dimensions", font=underlined_font)
dim1.grid(row=0, column=0, columnspan=2, padx=20, pady=20, sticky=W)

r1 = tb.Label(rref_frame, text="Rows:")
r1.grid(row=1, column=0, padx=20, pady=10, sticky=W)

rows = tb.Entry(rref_frame, width=5)
rows.grid(row=1, column=1, padx=4, pady=10, sticky=W)

c1 = tb.Label(rref_frame, text="Columns:")
c1.grid(row=2, column=0, padx=20, pady=10, sticky=W)

cols = tb.Entry(rref_frame, width=5)
cols.grid(row=2, column=1, padx=4, pady=10, sticky=W)

dimB1 = tb.Button(rref_frame, text="Create Matrix", bootstyle="success", command=create_matrix)
dimB1.grid(row=3, column=0, padx=20, pady=10, sticky=W)

# Synthetic Division
dim2 = tb.Label(sdiv_frame, text="Input polynomial degree", font=underlined_font)
dim2.grid(row=0, column=0, columnspan=2, padx=20, pady=20, sticky=W)

d1 = tb.Label(sdiv_frame, text="Degree:")
d1.grid(row=1, column=0, padx=20, pady=10, sticky=W)

deg = tb.Entry(sdiv_frame, width=5)
deg.grid(row=1, column=1, padx=4, pady=10, sticky=W)

degB2 = tb.Button(sdiv_frame, text="Create Array", bootstyle="success", command=create_array)
degB2.grid(row=2, column=0, padx=20, pady=10, sticky=W)

# Instructions for use
i0 = tb.Label(doc_frame, text="Matrix RREF Instructions:", font=underlined_font)
i0.grid(row=0, column=0, padx=20, pady=20, sticky=W)

i1 = tb.Label(doc_frame, text="1. Enter row and column dimensions and click \"Create Matrix\". "
                              "Dimensions must be >= 1.")
i1.grid(row=1, column=0, padx=20, pady=5, sticky=W)

i2 = tb.Label(doc_frame, text="2. If necessary, resize the matrix by repeating the previous step.")
i2.grid(row=2, column=0, padx=20, pady=5, sticky=W)

i3 = tb.Label(doc_frame, text="3. Input matrix values and click \"Solve Matrix\". Values must be integers. "
                              "Empty fields will be treated as \'0\'.")
i3.grid(row=3, column=0, padx=20, pady=5, sticky=W)

i4 = tb.Label(doc_frame, text="Synthetic Division Instructions:", font=underlined_font)
i4.grid(row=4, column=0, padx=20, pady=20, sticky=W)

i5 = tb.Label(doc_frame, text="1. Enter the degree of the polynomial dividend and click \"Create Array\". "
                              "Degree must be >= 0.")
i5.grid(row=5, column=0, padx=20, pady=5, sticky=W)

i6 = tb.Label(doc_frame, text="2. Enter the coefficients of the polynomial dividend and linear divisor "
                              "in order of successive decreasing term powers and click \"Calculate\".")
i6.grid(row=6, column=0, padx=20, pady=5, sticky=W)

i7 = tb.Label(doc_frame, text="       If a term is absent, enter \'0\' or leave the corresponding field blank "
                              "(empty fields are interpreted as \'0\').")
i7.grid(row=7, column=0, padx=20, pady=5, sticky=W)

# End GUI
nb.pack(side=LEFT, anchor=NW, fill=BOTH, expand=TRUE, pady=10, padx=10)

root.mainloop()
