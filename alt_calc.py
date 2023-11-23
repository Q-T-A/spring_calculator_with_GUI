import tkinter as tk
from tkinter import ttk  # Import ttk
import math

class SpringCalculator:
    def __init__(self, root):
        self.root = root
        self.setup_ui()

    def setup_ui(self):
        # Main frame
        main_frame = tk.Frame(self.root)
        main_frame.pack(padx=10, pady=10)

        # Row 0: Material choice
        self.material_options = [
            "Music wire",
            "HD Spring",
            "Chrome-vanadium wire (ASTM No. A232)",
            "Chrome-silicon wire (ASTM No. A401)",
            "302 stainless wire (ASTM No. A313)",
            "Phosphor-bronze wire (ASTM No. B159)"
        ]
        tk.Label(main_frame, text="Select a spring material:").grid(row=0, column=0, sticky="w")
        self.material_choice = tk.StringVar()
        self.material_dropdown = ttk.Combobox(main_frame, textvariable=self.material_choice, values=self.material_options)
        self.material_dropdown.grid(row=0, column=1, sticky="ew")
        tk.Button(main_frame, text="Submit", command=self.submit_material_choice).grid(row=0, column=2)
        self.label_material_result = tk.Label(main_frame, text="Material choice will be shown here")
        self.label_material_result.grid(row=0, column=3, sticky="w")

        # Row 1: End type
        self.end_type_options = [
            "Plain",
            "Plain and Ground",
            "Squared or Closed",
            "Squared and Ground"
        ]

        tk.Label(main_frame, text="Select the end type:").grid(row=1, column=0, sticky="w")
        self.end_type_choice = tk.StringVar()
        self.end_type_dropdown = ttk.Combobox(main_frame, textvariable=self.end_type_choice, values=self.end_type_options)
        self.end_type_dropdown.grid(row=1, column=1, sticky="ew")
        tk.Button(main_frame, text="Submit", command=self.submit_end_type_choice).grid(row=1, column=2)
        self.label_end_type_result = tk.Label(main_frame, text="End type choice will be shown here")
        self.label_end_type_result.grid(row=1, column=3, sticky="w")

        # Row 2: Wire diameter
        tk.Label(main_frame, text="Enter the wire diameter (inches):").grid(row=2, column=0, sticky="w")
        self.wire_diameter_var = tk.StringVar()
        self.wire_diameter_entry = tk.Entry(main_frame, textvariable=self.wire_diameter_var)
        self.wire_diameter_entry.grid(row=2, column=1, sticky="ew")
        tk.Button(main_frame, text="Submit", command=self.submit_wire_diameter).grid(row=2, column=2)
        self.label_wire_diameter_result = tk.Label(main_frame, text="Wire diameter will be shown here")
        self.label_wire_diameter_result.grid(row=2, column=3, sticky="w")

        # Row 3: Outer diameter
        tk.Label(main_frame, text="Enter the outer diameter (inches):").grid(row=3, column=0, sticky="w")
        self.outer_diameter_var = tk.StringVar()
        self.outer_diameter_entry = tk.Entry(main_frame, textvariable=self.outer_diameter_var)
        self.outer_diameter_entry.grid(row=3, column=1, sticky="ew")
        tk.Button(main_frame, text="Submit", command=self.submit_outer_diameter).grid(row=3, column=2)
        self.label_outer_diameter_result = tk.Label(main_frame, text="Outer diameter will be shown here")
        self.label_outer_diameter_result.grid(row=3, column=3, sticky="w")

        # Row 4: Free length (Lo)
        tk.Label(main_frame, text="Enter the free length (Lo) in inches:").grid(row=4, column=0, sticky="w")
        self.free_length_var = tk.StringVar()
        self.free_length_entry = tk.Entry(main_frame, textvariable=self.free_length_var)
        self.free_length_entry.grid(row=4, column=1, sticky="ew")
        tk.Button(main_frame, text="Submit", command=self.submit_free_length).grid(row=4, column=2)
        self.label_free_length_result = tk.Label(main_frame, text="Free length will be shown here")
        self.label_free_length_result.grid(row=4, column=3, sticky="w")

        # Row 5: Shut length (Ls)
        tk.Label(main_frame, text="Enter the shut length (Ls) in inches:").grid(row=5, column=0, sticky="w")
        self.shut_length_var = tk.StringVar()
        self.shut_length_entry = tk.Entry(main_frame, textvariable=self.shut_length_var)
        self.shut_length_entry.grid(row=5, column=1, sticky="ew")
        tk.Button(main_frame, text="Submit", command=self.submit_shut_length).grid(row=5, column=2)
        self.label_shut_length_result = tk.Label(main_frame, text="Shut length will be shown here")
        self.label_shut_length_result.grid(row=5, column=3, sticky="w")

        # Row 6: Peen type
        self.peen_type_options = [
            'Peened',
            'Unpeened'
        ]
        tk.Label(main_frame, text="Select the peen type:").grid(row=6, column=0, sticky="w")
        self.peen_type_choice = tk.StringVar()
        self.peen_type_dropdown = ttk.Combobox(main_frame, textvariable=self.peen_type_choice, values=self.peen_type_options)
        self.peen_type_dropdown.grid(row=6, column=1, sticky="ew")
        tk.Button(main_frame, text="Submit", command=self.submit_peen_type_choice).grid(row=6, column=2)
        self.label_peen_type_result = tk.Label(main_frame, text="Peen choice will be shown here")
        self.label_peen_type_result.grid(row=6, column=3, sticky="w")

        # Row 7: Loading type
        self.loading_type_options = [
            'Static',
            'Cyclic'
        ]
        tk.Label(main_frame, text="Select the loading type:").grid(row=7, column=0, sticky="w")
        self.loading_type_choice = tk.StringVar()
        self.loading_type_dropdown = ttk.Combobox(main_frame, textvariable=self.loading_type_choice, values=self.loading_type_options)
        self.loading_type_dropdown.grid(row=7, column=1, sticky="ew")
        tk.Button(main_frame, text="Submit", command=self.submit_loading_type_choice).grid(row=7, column=2)
        self.label_loading_type_result = tk.Label(main_frame, text="Loading type choice will be shown here")
        self.label_loading_type_result.grid(row=7, column=3, sticky="w")

        # Calculate button
        tk.Button(main_frame, text="Calculate", command=self.perform_calculations).grid(row=8, column=0, columnspan=4)

        # Calculation result
        self.label_calculation_result = tk.Label(main_frame, text="Calculation result will be shown here", wraplength=300)
        self.label_calculation_result.grid(row=9, column=0, columnspan=4)
        main_frame.rowconfigure(9, weight=1)  # This makes row 9 where the label is placed more flexible in height.


        # Adjust column weights for proper expansion
        main_frame.columnconfigure(1, weight=1)
        main_frame.columnconfigure(3, weight=2)

    # ... rest of the methods ...

    def submit_material_choice(self):
        choice = self.material_choice.get()
        self.label_material_result.config(text=f"Material choice: {choice}")
    
    def submit_end_type_choice(self):
        choice = self.end_type_choice.get()
        self.label_end_type_result.config(text=f"End type choice: {choice}")

    def submit_wire_diameter(self):
        wire_diameter = float(self.wire_diameter_var.get())
        self.label_wire_diameter_result.config(text=f"Wire diameter: {wire_diameter} inches")

    def submit_outer_diameter(self):
        outer_diameter = float(self.outer_diameter_var.get())
        self.label_outer_diameter_result.config(text=f"Outer diameter: {outer_diameter} inches")
    
    def submit_free_length(self):
        free_length = float(self.free_length_var.get())
        self.label_free_length_result.config(text=f"Free length (Lo): {free_length} inches")

    def submit_shut_length(self):
        shut_length = float(self.shut_length_var.get())
        self.label_shut_length_result.config(text=f"Shut length (Ls): {shut_length} inches")

    def submit_peen_type_choice(self):
        choice = self.peen_type_choice.get()
        self.label_peen_type_result.config(text=f"End type choice: {choice}")
    
    def submit_loading_type_choice(self):
        loading_type = self.loading_type_choice.get()
        if loading_type == "Static":
            self.show_static_force_input()
        elif loading_type == "Cyclic":
            self.show_cyclic_force_inputs()
        else:
            self.label_loading_type_result.config(text="Please select a loading type.")

    def show_static_force_input(self):
        self.label_static_force = tk.Label(self.root, text="Enter static force applied:")
        self.label_static_force.pack()

        self.label_loading_type_result.config(text="force will be displayed here")

        self.static_force_var = tk.StringVar()
        self.static_force_entry = tk.Entry(self.root, textvariable=self.static_force_var)
        self.static_force_entry.pack()
        submit_button = tk.Button(self.root, text="Submit Static Force", command=self.submit_static_force)
        submit_button.pack()

    def submit_static_force(self):
        self.static_force = float(self.static_force_var.get())
        self.label_loading_type_result.config(text=f"Static force entered: {self.static_force}")
        

    def show_cyclic_force_inputs(self):
        self.label_fmin = tk.Label(self.root, text="Enter Fmin:")
        self.label_fmin.pack()

        self.fmin_var = tk.StringVar()
        self.fmin_entry = tk.Entry(self.root, textvariable=self.fmin_var)
        self.fmin_entry.pack()

        self.label_fmax = tk.Label(self.root, text="Enter Fmax:")
        self.label_fmax.pack()

        self.fmax_var = tk.StringVar()
        self.fmax_entry = tk.Entry(self.root, textvariable=self.fmax_var)
        self.fmax_entry.pack()

        submit_button = tk.Button(self.root, text="Submit Cyclic Forces", command=self.submit_cyclic_forces)
        submit_button.pack()

    def submit_cyclic_forces(self):
        self.f_min = float(self.fmin_var.get())
        self.f_max = float(self.fmax_var.get())

    def perform_calculations(self):
        self.calculate_spring_properties()

    def calculate_spring_properties(self):
        fos_stat = None
        fos_cyclic = None
         # Initialize variables
        materials = [
            "Music wire",
            "HD Spring",
            "Chrome-vanadium wire (ASTM No. A232)",
            "Chrome-silicon wire (ASTM No. A401)",
            "302 stainless wire (ASTM No. A313)",
            "Phosphor-bronze wire (ASTM No. B159)"
        ]
        D = float(self.outer_diameter_var.get()) - float(self.wire_diameter_var.get())
        Ne = 0
        Nt = 0
        Na = 0 
        pitch = 0
        Sy = 0
        G = 0
        Ls = float(self.shut_length_var.get())
        d = float(self.wire_diameter_var.get())
        Lo = float(self.free_length_var.get())
    # Calculate Ne, Nt, and pitch based on end type
        if self.end_type_choice.get() == 'Plain':
            Ne = 0
            Nt = Ls/d - 1
            Nt = math.floor(Nt)
            Na = Nt
            pitch = (Lo - d)/Na
        

        elif self.end_type_choice.get() == 'Plain and Ground':
            Ne = 1
            Nt = Ls/d 
            Nt = math.floor(Nt)
            Na = Nt - 1
            pitch = Lo/(Na+1)

        elif self.end_type_choice.get() == 'Squared or Closed':
            Ne = 2
            Nt = Ls/d - 1
            Nt = math.floor(Nt)
            Na = Nt - 2
            pitch = (Lo - 3 * d) / Na

        elif self.end_type_choice.get() == "Square and Ground":
            Ne = 2
            Nt = Ls/d 
            Nt = math.floor(Nt)
            Na = Nt - 2
            pitch = (Lo - 2 * d) / Na
            C = 0

        # Calculate material properties based on material selection and d
        if self.material_choice.get() ==  materials[0]:
            Sut = 201 / (d ** 0.145)
            Sy = 0.65 * Sut * 10**3
            if d < 0.032:
                E = 29.5*(10**6)
                G = 12*(10**6)
            elif 0.032 <= d < 0.064:
                E = 29*(10**6)
                G = 11.85*(10**6)
            elif 0.064 <= d < 0.126:
                E = 28.5*(10**6)
                G = 11.75*(10**6)
            else:
                E = 28*(10**6)
                G = 11.6*(10**6)
        
        
        elif self.material_choice.get() ==  materials[1]:
            Sut = 140 / (d ** 0.19)
            Sy = 0.6 * Sut * 10**3
            if d < 0.033:
                E = 28.8*(10**6)
                G = 11.7*(10**6)
            elif 0.033 <= d < 0.064:
                E = 28.7*(10**6)
                G = 11.6*(10**6)
            elif 0.064 <= d < 0.126:
                E = 28.6*(10**6)
                G = 11.5*(10**6)
            else:
                E = 28.5*(10**6)
                G = 11.4*(10**6)

        
        elif self.material_choice.get() ==  materials[2]:
            E = 29.5*(10**6)
            G = 11.2*(10**6)
            Sut = 169 / (d ** 0.168)
            Sy = 0.88 * Sut * 10**3

        elif self.material_choice.get() ==  materials[3]:
            E = 29.5*(10**6)
            G = 11.2*(10**6)
            Sut = 202 / (d ** 0.108)
            Sy = 0.85 * Sut* 10**3

        elif self.material_choice.get() ==  materials[4]:
            E = 28*(10**6)
            G = 10*(10**6)
            Sut = 169 / (d ** 0.146)
            Sy = 0.65 * Sut * 10**3

        elif self.material_choice.get() ==  materials[5]:
            E = 15*(10**6)
            G = 6*(10**6)
            Sut = 145 / (d ** 0)
            Sy = 0.75 * Sut * 10**3
        
        # Calculate spring rate, k
        k = (d ** 4 * G) / (8 * D ** 3 * Na)
    
        # Calculate force needed to compress solid to shut length
        force = k * (Lo - Ls)
        C = D/d
        Kb = ((4*C)+2)/((4*C)-3)
        Shear =  Kb * 8 * force * D / ((d**3) * math.pi)

        # Calculate factor of safety
        factor_of_safety = Sy / Shear
        #peen calculation
        Sa = 0
        Sm = 0
        if self.peen_type_choice == 'Unpeened':
            Sa = 35000
            Sm = 55000
        else:
            Sa = 57500
            Sm = 77500

        C = D / d
        Kb = ((4 * C) + 2) / ((4 * C) - 3)
        Ssu = 0.67 * Sut
        Sse = Sa / (1 - Sm / Ssu)
        print(self.static_force)
        if self.loading_type_choice.get() == 'Static':
            shear = Kb * 8 * self.static_force * D / (math.pi * d ** 3)
            fos_stat = Sy / shear
            

        elif self.loading_type_choice.get() == 'Cylcic':
            f_a = (self.f_max - self.f_min) / 2
            f_m = (self.f_max + self.f_min) / 2
            shear_a = Kb * 8 * f_a * D / (math.pi * d ** 3)
            shear_m = Kb * 8 * f_m * D / (math.pi * d ** 3)
            fos_cyclic = (shear_a / Sse + shear_m / Ssu) ** (-1)

    
        result = (f'Spring Properties\n'
            f'Na: {Na}'
            f'Nt: {Nt}'
            f'Pitch: {pitch}'
            f'Spring Rate (k): {k}'
            f'Force to compress: {force}'
            f'factor of safety: {factor_of_safety}\n' )
        
        if fos_stat is not None:
            result += f"Static Loading FOS: {fos_stat}\n"
        if fos_cyclic is not None:
            result += f"Cyclic Loading FOS: {fos_cyclic}\n"
        self.label_calculation_result.config(text=result)
if __name__ == "__main__":
    root = tk.Tk()
    app = SpringCalculator(root)
    root.mainloop()
