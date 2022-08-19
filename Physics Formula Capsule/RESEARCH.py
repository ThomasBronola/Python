'''
Author: Cuyong, Janaia B.
Year & Section: CEAT-33-302A
Research Title: Computational Methods for Physics in Space
Mentor: Eng. Camille F. Embalzado
Program Tite: CoMPiS
'''
import tkinter as tk
from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def scratch():
    print('WELCOME TO CoMPiS!')
    print('Computational Methods for Physics in Space\n')
    print('This program will help the user compute Physics formulas used in Space\n')
    print('Choose from the formulas below:')
    print('1. Stellar Properties')
    #brightness
    #luminosity (given apparent brightness or surface temperature)
    #surface temperature

    print('2. Hubble\'s Law')
    #x can be: distance (using hubble's law)

    print('3. Escape Velocity')
    #x can be: E.V. ONLY

    print('4. Kinetic Energy')
    #KE 1: object
        #x can be: KE, mass or speed
    #KE 2: atom or molecule
        #KE ONLY + velocity (bonus)

    print('5. Kepler\'s Equation (Law of Periods)')
    #ask if with or without the effect of gravity
    #x can be: p ONLY

    print('6. Use of Planck Constant')
    #ask if in relation to frequency or wavelength

    print('7. Schwarzschild Radius')
    #x can be: S.R. ONLY

    print('8. Relativity')
    #x can be: time dilation, length contraction

    print('9. Eccentricity')
    #x can be: eccentricity, aphelion or perihelion

    print('10. Telescope Related')
    #magnification
    #resolution
    #limiting magnitude

    print('Type * to see Constants Mostly Used by Astronomers')
    print( '''
    -astronomical unit
    -light year
    -parsec (in meters and lightyears)
    -hubble constant
    -boltzmann constant
    -speed of light
    -gravitational constant
    -planck constant
    -stefan-boltzmann constant
    -solar mass, radius & luminosity
    -earth's mass & radius
    -mass of proton, electron & neutron
    -mass of H atom
    ''')

def main():
    root =Tk()
    root.geometry("682x493+610+150")
    root.resizable(0,0)
    root.title('testing')
    mainCanvas = tk.Frame(root, background="#000000")
    
    isChecked = IntVar()
    chkBox = tk.Checkbutton(mainCanvas, text='Add gravity?', foreground="#FFFFFF", onvalue=1, offvalue=0, variable=isChecked)
    chkBox.place(relx=0.015, rely=0.02, relheight=0.957, relwidth=0.974)
    
    if isChecked.get():
        print('May gravity')
    
    root.mainloop()
    
    
main()