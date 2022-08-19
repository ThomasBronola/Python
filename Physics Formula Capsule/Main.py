import tkinter as tk
from tkinter import *
import math

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

#function gui
def SRadiusGUI():
    clrscr()
    root.withdraw()
    sR = Toplevel()
    sR.deiconify()
    sR.geometry("785x583+389+50")
    sR.resizable(0, 0)
    sR.title('Schwarzchild Radius')
        
    mainCanvas = tk.Frame(sR, background="#CAEAE5")
    mainCanvas.place(relx=0.015, rely=0.02, relheight=0.957, relwidth=0.974)
        
    lblSRadius = tk.Label(mainCanvas, background="#CAEAE5", text='''Schwarzschild Radius''', font = "-size 14 -weight bold")
    lblSRadius.place(relx=0.246, rely=0.042, height=37, width=350) #width=641 relx=0.015
    
    btnBack = tk.Button(mainCanvas, background='#F7BAB9', text='''Back''', command =lambda:[sR.withdraw(), root.deiconify()])
    btnBack.place(relx=0.015, rely=0.042, height=37, width=80)
    
    #picture
    imgSr = PhotoImage(file='pictures/SchwarzchildRadius.png')
    IMAGE_ONE = tk.Label(mainCanvas, background="#CAEAE5", image=imgSr)
    IMAGE_ONE.place(relx=0.013, rely=0.179, height=215, width=738)
    
    lblFirstInput = tk.Label(mainCanvas, background="#CAEAE5", text='''M =''')
    lblFirstInput.place(relx=0.117, rely=0.681, height=26, width=72)
    
    inpFirstInput = tk.Entry(mainCanvas, justify ="center", textvariable=SRadiusM)
    inpFirstInput.place(relx=0.209, rely=0.681, height=34, relwidth=0.175)
    
    lblExponent = tk.Label(mainCanvas, background="#CAEAE5", text='''x 10''')
    lblExponent.place(relx=0.392, rely=0.699, height=26, width=42)
    
    inpExponent = tk.Entry(mainCanvas, justify='center', textvariable=SRadiusExponent)
    inpExponent.place(relx=0.444, rely=0.681,height=34, relwidth=0.07)
    
    lblFirstType = tk.Label(mainCanvas, background="#CAEAE5", text='''in kg''')
    lblFirstType.place(relx=0.522, rely=0.699, height=26, width=42)
    
    lblResult = tk.Label(mainCanvas, background="#CAEAE5", text='''Result =''')
    lblResult.place(relx=0.117, rely=0.789, height=37, width=72)
    
    lblResultTwo = tk.Label(mainCanvas, textvariable=SRadiusResult)
    lblResultTwo.place(relx=0.209, rely=0.789, height=34, width=275)
    
    btnCompute = tk.Button(mainCanvas, background="#F7BAB9", text='''Compute''', command=SRadiusCompute)
    btnCompute.place(relx=0.64, rely=0.681, height=33, width=136)
    
    btnClear = tk.Button(mainCanvas, background="#F7BAB9", text='''Clear Fields''', command=clrscr)
    btnClear.place(relx=0.64, rely=0.789, height=33, width=136)
        
    sR.mainloop()
    
def SRadiusCompute():
    m = SRadiusM.get()
    exponent = SRadiusExponent.get()
    c = 29792458
    g = 6.6742
    mass = m * (pow(10, exponent))
    light = pow(c, 2)
    gravity = 2 * g
    numerator = gravity * mass
    result = numerator / light
    SRadiusResult.set(str(result) + ' m')
    #SRadiusResult.set(mass)

def HubbleLawGUI():
    root.withdraw()
    clrscr()
    hL = Toplevel()
    hL.deiconify()
    hL.geometry("785x583+389+50")
    hL.resizable(0, 0)
    hL.title("Hubble's Law")
    
    mainCanvas = tk.Frame(hL, background="#CAEAE5")
    mainCanvas.place(relx=0.015, rely=0.021, relheight=0.957, relwidth=0.973)

    lblHubble = tk.Label(mainCanvas, background="#CAEAE5", text='''Hubble's law''', font = "-size 14 -weight bold")
    lblHubble.place(relx=0.366, rely=0.054, height=44, width=188)
    
    btnBack = tk.Button(mainCanvas, background="#F7BAB9", text='''Back''', command =lambda:[hL.withdraw(), root.deiconify()])
    btnBack.place(relx=0.039, rely=0.054, height=37, width=80)
    
    #picture one
    imgHubbleFormulaOne = PhotoImage(file='pictures/HubbleLaw.png')
    lblGuide = tk.Label(mainCanvas, background="#CAEAE5", image=imgHubbleFormulaOne)
    lblGuide.place(relx=0.014, rely=0.168, height=215, width=738)

    lblFirstInput = tk.Label(mainCanvas, background="#CAEAE5", text='''v =''')
    lblFirstInput.place(relx=0.117, rely=0.681, height=26, width=72)
    
    inpFirstInput = tk.Entry(mainCanvas, textvariable=hubbleLawV, justify='center')
    inpFirstInput.place(relx=0.209, rely=0.681, height=34, relwidth=0.175)
    
    lblExponent = tk.Label(mainCanvas, background="#CAEAE5", text='''x 10''')
    lblExponent.place(relx=0.392, rely=0.699, height=26, width=42)
    
    inpExponent = tk.Entry(mainCanvas, justify='center', textvariable=hubbleExponent)
    inpExponent.place(relx=0.444, rely=0.681,height=34, relwidth=0.07)
    
    lblFirstType = tk.Label(mainCanvas, background="#CAEAE5", text='''in km/sec''')
    lblFirstType.place(relx=0.522, rely=0.699, height=26, width=50)
    
    lblResult = tk.Label(mainCanvas, background="#CAEAE5", text='''Result =''')
    lblResult.place(relx=0.117, rely=0.789, height=37, width=72)

    lblResultTwo = tk.Label(mainCanvas, background="#FFFFFF", textvariable=hubbleLawResult)
    lblResultTwo.place(relx=0.209, rely=0.789, height=34, width=275)
    
    btnCompute = tk.Button(mainCanvas, background="#F7BAB9", text='''Compute''', command=hubbleLawCompute)
    btnCompute.place(relx=0.64, rely=0.681, height=33, width=136)
    
    btnClear = tk.Button(mainCanvas, background="#F7BAB9", text='''Clear Fields''', command=clrscr)
    btnClear.place(relx=0.64, rely=0.789, height=33, width=136)
    
    hL.mainloop()
    
def hubbleLawCompute():
    v =hubbleLawV.get()
    exponent = hubbleExponent.get()
    mass = v * (pow(10, exponent))
    h = 73.8
    result = mass/ h
    hubbleLawResult.set(str(result)+' mpc')

def constantFormulasGUI():
    root.withdraw()
    cF = Toplevel()
    cF.deiconify()
    cF.geometry("897x676+389+50")
    cF.resizable(0, 0)
    cF.title("Astronomers Constant Values")

    #
    #Title and Back button
    #
    mainCanvas = tk.Frame(cF, background="#CAEAE5")
    mainCanvas.place(relx=0.01, rely=0.022, relheight=0.964, relwidth=0.979)
        
    lblConstants = tk.Label(mainCanvas, background="#CAEAE5", text='''Constants''', font="-weight bold -size 11")
    lblConstants.place(relx=0.394, rely=0.021, height=49, width=177)
    
        
    btnBack = tk.Button(mainCanvas, background="#F7BAB9", text='''Back''', command =lambda:[cF.withdraw(), root.deiconify()])  
    btnBack.place(relx=0.021, rely=0.021, height=37, width=80) #width=116 height=43

    #
    #labels/titles
    #
    lblAstronomicalUnit = tk.Label(mainCanvas, background="#F7BAB9", text='''Astronomical Unit''', font="-weight bold -size 11")
    lblAstronomicalUnit.place(relx=0.064, rely=0.11, height=30, width=350)

    lblLightYear = tk.Label(mainCanvas, background="#F7BAB9", text='''Light Year''', font="-weight bold -size 11")
    lblLightYear.place(relx=0.532, rely=0.11, height=32, width=350)

    lblParsec = tk.Label(mainCanvas, background="#F7BAB9", text='''Parsec (in meters and lightyears)''', font="-weight bold -size 11")
    lblParsec.place(relx=0.064, rely=0.222, height=31, width=350)

    lblPlanck = tk.Label(mainCanvas, background="#F7BAB9",text='''Planck Constant''', font="-weight bold -size 11")
    lblPlanck.place(relx=0.532, rely=0.443, height=32, width=350)

    lblHubble = tk.Label(mainCanvas, background="#F7BAB9", text='''Hubble Constant''', font="-weight bold -size 11")
    lblHubble.place(relx=0.532, rely=0.222, height=31, width=350)

    lblBoltzmann = tk.Label(mainCanvas, background="#F7BAB9", text='''Boltzmann Constant''', font="-weight bold -size 11")
    lblBoltzmann.place(relx=0.064, rely=0.333, height=31, width=350)

    lblSpeedofLight = tk.Label(mainCanvas, background="#F7BAB9", text='''Speed of Light''', font="-weight bold -size 11")
    lblSpeedofLight.place(relx=0.532, rely=0.333, height=32, width=350)

    lblMassHydrogen = tk.Label(mainCanvas, background="#F7BAB9", text='''Mass of a Hydrogen atom''', font="-weight bold -size 11")
    lblMassHydrogen.place(relx=0.064, rely=0.555, height=31, width=350)

    lblSolar = tk.Label(mainCanvas, background="#F7BAB9", text='''Solar mass, radius & luminosity''', font="-weight bold -size 11")
    lblSolar.place(relx=0.532, rely=0.676, height=33, width=350)

    lblEarth = tk.Label(mainCanvas, background="#F7BAB9", text='''Earth's mass & radius''', font="-weight bold -size 11")
    lblEarth.place(relx=0.064, rely=0.676, height=32, width=350)    

    lblGravity = tk.Label(mainCanvas, background="#F7BAB9", text='''Gravitational Constant''', font="-weight bold -size 11")
    lblGravity.place(relx=0.064, rely=0.443, height=32, width=350)

    lblStefanBoltzmann = tk.Label(mainCanvas, background="#F7BAB9", text='''Stefan-Boltzmann Constant''', font="-weight bold -size 11")
    lblStefanBoltzmann.place(relx=0.532, rely=0.555, height=31, width=350)

    lblMassProtonElectronNeutron = tk.Label(mainCanvas, background="#F7BAB9", text='''Mass of Proton, Electron & Neutron''', font="-weight bold -size 11")
    lblMassProtonElectronNeutron.place(relx=0.298, rely=0.788, height=32, width=350)

    #
    #labels with the values
    #
    lblValueMassHydrogen = tk.Label(mainCanvas, background="#F7BAB9", text='''mH= 1.6735x10^-27 kg''')
    lblValueMassHydrogen.place(relx=0.064, rely=0.587, height=32, width=350)

    lblValueStefanBoltzmann = tk.Label(mainCanvas, background="#F7BAB9", text='''σ= 5.670 × 10^−8 J/(s·m^2 deg^4)^1''')
    lblValueStefanBoltzmann.place(relx=0.532, rely=0.587, height=32, width=350)

    lblValueEarth = tk.Label(mainCanvas, background="#F7BAB9", text='''R= 5.974 × 1024 kg | 6.378 × 106 m''')
    lblValueEarth.place(relx=0.064, rely=0.71, height=32, width=350)

    lblValueLightYear = tk.Label(mainCanvas, background="#F7BAB9", text='''ly =9.4605x10^15 m''')
    lblValueLightYear.place(relx=0.532, rely=0.144, height=31, width=350)

    lblValueParsec = tk.Label(mainCanvas, background="#F7BAB9", text='''Meters: 3.0857E+16          Light year: 3.26156378''')
    lblValueParsec.place(relx=0.064, rely=0.255, height=32, width=350)

    lblValueAstronomicalUnit = tk.Label(mainCanvas, background="#F7BAB9", text='''A.U.= 1.5x10^8 km''')
    lblValueAstronomicalUnit.place(relx=0.064, rely=0.144, height=31, width=350)

    lblValueBoltzmann = tk.Label(mainCanvas, background="#F7BAB9", text='''k= 1.3806505x10^-23 J K^-1''')
    lblValueBoltzmann.place(relx=0.064, rely=0.367, height=31, width=350)

    lblValueSpeedofLight = tk.Label(mainCanvas, background="#F7BAB9", text='''c= 2.9979 × 10^8 m/s''')
    lblValueSpeedofLight.place(relx=0.532, rely=0.367, height=32, width=350)

    lblValueGravity = tk.Label(mainCanvas, background="#F7BAB9", text='''G = 6.67430(15) x 10^-11 m^3 *kg^-1 *s^-2''')
    lblValueGravity.place(relx=0.064, rely=0.477, height=32, width=350)

    lblValuePlanck = tk.Label(mainCanvas, background="#F7BAB9", text='''h= 6.626 × 10^−34 J-s''')
    lblValuePlanck.place(relx=0.532, rely=0.477, height=31, width=350)

    lblValueHubble = tk.Label(mainCanvas, background="#F7BAB9", text='''H0= 73.8 kms/sec/Mpc''')
    lblValueHubble.place(relx=0.532, rely=0.255, height=32, width=350)

    lblValueSolar = tk.Label(mainCanvas, background="#F7BAB9", text='''1.989x10^30 kg | 6.9599x10^8 m | 3.90x10^26 W''')
    lblValueSolar.place(relx=0.532, rely=0.71, height=33, width=350)

    lblValueMassProtonElectron = tk.Label(mainCanvas, background="#F7BAB9", text='''mp=1.67262171x10^-27 kg | me=9.1093826x10^-31 kg''')
    lblValueMassProtonElectron.place(relx=0.298, rely=0.821, height=33, width=350)

    lblValueMassNeutron = tk.Label(mainCanvas, background="#F7BAB9", text='''mn= 1.67492728x10^-27 kg''')
    lblValueMassNeutron.place(relx=0.298, rely=0.867, height=19, width=350)

    cF.mainloop()
    
def escapeVelocityGUI():
    root.withdraw()
    clrscr()
    eV = Toplevel()
    eV.deiconify()
    eV.geometry("785x583+389+50")
    eV.resizable(0, 0)
    eV.title("Escape Velocity")
    
    mainCanvas = tk.Frame(eV, background="#CAEAE5")
    mainCanvas.place(relx=0.015, rely=0.021, relheight=0.957, relwidth=0.973)
    
    lblEscapeVelocity = tk.Label(mainCanvas, background="#CAEAE5", text='''Escape Velocity''', font = "-size 14 -weight bold")
    lblEscapeVelocity.place(relx=0.366, rely=0.054, height=44, width=188)
    
    btnBack = tk.Button(mainCanvas, background="#F7BAB9", text ='''Back''', command =lambda:[eV.withdraw(), root.deiconify()])
    btnBack.place(relx=0.039, rely=0.054, height=37, width=80)
    
    #picture one
    imgEscapeVelocityFormulaOne = PhotoImage(file='pictures/EscapeVelocityGuide.png')
    lblGuide = tk.Label(mainCanvas, background="#CAEAE5", image=imgEscapeVelocityFormulaOne)
    lblGuide.place(relx=0.014, rely=0.168, height=215, width=738)
    
    lblFirstInput = tk.Label(mainCanvas, background="#CAEAE5", text='''M =''')
    lblFirstInput.place(relx=0.117, rely=0.681, height=26, width=72)
    
    inpFirstInput = tk.Entry(mainCanvas, justify= 'center', textvariable=EscapeVelocityM)
    inpFirstInput.place(relx=0.209, rely=0.681, height=34, relwidth=0.175)
    
    lblExponent = tk.Label(mainCanvas, background="#CAEAE5", text='''x 10''')
    lblExponent.place(relx=0.392, rely=0.699, height=26, width=42)
    
    inpExponent = tk.Entry(mainCanvas, justify= 'center', textvariable=EscapeVelocityExponent)
    inpExponent.place(relx=0.444, rely=0.681,height=34, relwidth=0.07)
    
    lblFirstType = tk.Label(mainCanvas, background="#CAEAE5", text='''in kg''')
    lblFirstType.place(relx=0.522, rely=0.699, height=29, width=50)
    
    lblSecondInput = tk.Label(mainCanvas, background="#CAEAE5", text='''R =''')
    lblSecondInput.place(relx=0.117, rely=0.789, height=26, width=72)
    
    inpSecondInput = tk.Entry(mainCanvas, justify= 'center', textvariable=EscapeVelocityR)
    inpSecondInput.place(relx=0.209, rely=0.789, height=34, relwidth=0.175)
    
    lblSecondExponent = tk.Label(mainCanvas, background="#CAEAE5", text='''x 10''')
    lblSecondExponent.place(relx=0.392, rely=0.806, height=26, width=42)
    
    inpSecondExponent = tk.Entry(mainCanvas, justify='center', textvariable=EscapeVelocitySecondExponent)
    inpSecondExponent.place(relx=0.444, rely=0.789, height=34, relwidth=0.07)
     
    lblSecondType = tk.Label(mainCanvas, background="#CAEAE5", text='''in m''')
    lblSecondType.place(relx=0.522, rely=0.806, height=29, width=50) 
     
    lblResult = tk.Label(mainCanvas, background="#CAEAE5", text='''Result =''')
    lblResult.place(relx=0.117, rely=0.878, height=36, width=72)
    
    lblResultTwo = tk.Label(mainCanvas, textvariable=EscapeVelocityResult)
    lblResultTwo.place(relx=0.209, rely=0.878, height=34, width=275)
    
    btnCompute = tk.Button(mainCanvas, background="#F7BAB9", text='''Compute''', command=escapeVelocityCompute)
    btnCompute.place(relx=0.64, rely=0.681, height=33, width=136)
    
    btnClear = tk.Button(mainCanvas, background="#F7BAB9", text='''Clear Fields''', command=clrscr)
    btnClear.place(relx=0.64, rely=0.789, height=33, width=136)
    
    eV.mainloop()
    
def escapeVelocityCompute():
    r =EscapeVelocityR.get()
    m =EscapeVelocityM.get()
    fe =EscapeVelocityExponent.get()
    se =EscapeVelocitySecondExponent.get()
    g = 6.6742
    gravity = 2 * g
    mass = m * pow(10, fe)
    numerator = gravity * mass
    radius = r * pow(10, se)
    result = math.sqrt(numerator/ radius)
    EscapeVelocityResult.set(str(result) + ' m')
    
def relativityOptionsGUI():
    root.withdraw()
    rev = Toplevel()
    rev.deiconify()
    rev.geometry("785x583+389+50")
    rev.resizable(0, 0)
    rev.title("Relativity")
    
    mainCanvas = tk.Frame(rev, background="#CAEAE5")
    mainCanvas.place(relx=0.015, rely=0.021, relheight=0.957, relwidth=0.973)
    
    lblEscapeVelocity = tk.Label(mainCanvas, background="#CAEAE5", text='''Relativity Options''', font = "-size 14 -weight bold")
    lblEscapeVelocity.place(relx=0.366, rely=0.054, height=44, width=188)
    
    btnBack = tk.Button(mainCanvas, background="#F7BAB9", text ='''Back''', command =lambda:[rev.withdraw(), root.deiconify()])
    btnBack.place(relx=0.039, rely=0.054, height=37, width=80)
    
    btnTimeDilation = tk.Button(mainCanvas, background="#F7BAB9", text='''Time Dilation''', command=relativityTimeGUI)
    btnTimeDilation.place(relx=0.321, rely=0.411, height=53, width=266)

    btnLengthContraction = tk.Button(mainCanvas, background="#F7BAB9", text='''Length Contraction''', command=relativityLengthGUI)
    btnLengthContraction.place(relx=0.321, rely=0.554, height=53, width=266)
 
def relativityTimeGUI():
    clrscr()
    revT = Toplevel()
    revT.deiconify()
    revT.geometry("785x583+389+50")
    revT.resizable(0, 0)
    revT.title("Relativity Time Dilation")
 
    mainCanvas = tk.Frame(revT, background="#CAEAE5")
    mainCanvas.place(relx=0.015, rely=0.021, relheight=0.957, relwidth=0.973)
    
    lblRelativityT = tk.Label(mainCanvas, background="#CAEAE5", text='''Relativity ( Time Dilation )''', font = "-size 14 -weight bold")
    lblRelativityT.place(relx=0.209, rely=0.054, height=44, width=457)
    
    btnBack = tk.Button(mainCanvas, background="#F7BAB9", text ='''Back''', command =revT.withdraw)
    btnBack.place(relx=0.039, rely=0.054, height=37, width=80)
    
    #picture one
    img_one = PhotoImage(file='pictures/RelativityTimeDilation.png')
    IMAGE_ONE = tk.Label(mainCanvas, background="#CAEAE5", image=img_one)
    IMAGE_ONE.place(relx=0.014, rely=0.168, height=215, width=738)
    
    img_two = PhotoImage(file='pictures/To.png')
    lblFirstInput = tk.Label(mainCanvas, background="#CAEAE5", image=img_two)
    lblFirstInput.place(relx=0.117, rely=0.681, height=26, width=72)
    
    inpFirstInput = tk.Entry(mainCanvas, justify ="center", textvariable =RelativityTimeT)
    inpFirstInput.place(relx=0.209, rely=0.681, height=34, relwidth=0.175)
    
    lblExponent = tk.Label(mainCanvas, background="#CAEAE5", text='''x 10''')
    lblExponent.place(relx=0.392, rely=0.699, height=26, width=42)

    inpExponent = tk.Entry(mainCanvas, justify='center', textvariable=RelativityTimeFE)
    inpExponent.place(relx=0.444, rely=0.681,height=34, relwidth=0.07)

    lblFirstType = tk.Label(mainCanvas, background="#CAEAE5", text='''in min''')
    lblFirstType.place(relx=0.522, rely=0.699, height=29, width=50)
    
    lblSecondInput = tk.Label(mainCanvas, background="#CAEAE5", text='''v =''')
    lblSecondInput.place(relx=0.117, rely=0.789, height=26, width=72)
    
    inpSecondInput = tk.Entry(mainCanvas, justify ="center", textvariable=RelativityTimeV)
    inpSecondInput.place(relx=0.209, rely=0.789, height=34, relwidth=0.175)
    
    lblSecondExponent = tk.Label(mainCanvas, background="#CAEAE5", text='''x 10''')
    lblSecondExponent.place(relx=0.392, rely=0.806, height=26, width=42)

    inpSecondExponent = tk.Entry(mainCanvas, justify='center', textvariable=RelativityTimeSE)
    inpSecondExponent.place(relx=0.444, rely=0.789, height=34, relwidth=0.07)

    lblSecondType = tk.Label(mainCanvas, background="#CAEAE5", text='''in m/sec''')
    lblSecondType.place(relx=0.522, rely=0.806, height=29, width=50)
    
    lblResult = tk.Label(mainCanvas, background="#CAEAE5", text='''Result =''')
    lblResult.place(relx=0.117, rely=0.878, height=36, width=72)
    
    lblResultTwo = tk.Label(mainCanvas, textvariable=RelativityTimeResult)
    lblResultTwo.place(relx=0.209, rely=0.878, height=34, width=275)
 
    btnCompute = tk.Button(mainCanvas, background="#F7BAB9", text='''Compute''', command=relativityTimeCompute)
    btnCompute.place(relx=0.64, rely=0.681, height=33, width=136)
    
    btnClear = tk.Button(mainCanvas, background="#F7BAB9", text='''Clear Fields''', command=clrscr)
    btnClear.place(relx=0.64, rely=0.789, height=33, width=136)
    
    revT.mainloop()
     
def relativityTimeCompute():
    t =RelativityTimeT.get()
    v =RelativityTimeV.get()
    fe =RelativityTimeFE.get()
    se =RelativityTimeSE.get()
    c = 29792458
    velocity = v * pow(10, se)
    time = t * pow(10, fe)
    first = velocity / c
    second = pow(first, 2)
    denominator = math.sqrt(1-second)
    result = time / denominator
    RelativityTimeResult.set(str(result) + ' minutes')    

def relativityLengthGUI():
    clrscr()
    revL = Toplevel()
    revL.deiconify()
    revL.geometry("785x583+389+50")
    revL.resizable(0, 0)
    revL.title("Relativity Length Contraction")
 
    mainCanvas = tk.Frame(revL, background="#CAEAE5")
    mainCanvas.place(relx=0.015, rely=0.021, relheight=0.957, relwidth=0.973)
    
    lblRelativityL = tk.Label(mainCanvas, background="#CAEAE5", text='''Relativity ( Length Contraction )''', font = "-size 14 -weight bold")
    lblRelativityL.place(relx=0.209, rely=0.054, height=44, width=457)
    
    btnBack = tk.Button(mainCanvas, background="#F7BAB9", text ='''Back''', command =revL.withdraw)
    btnBack.place(relx=0.039, rely=0.054, height=37, width=80)
    
    #picture one
    img_one = PhotoImage(file='pictures/RelativityLength.png')
    IMAGE_ONE = tk.Label(mainCanvas, background="#CAEAE5", image=img_one)
    IMAGE_ONE.place(relx=0.014, rely=0.168, height=215, width=738)
    
    #picture two
    img_two = PhotoImage(file='pictures/Lo.png')
    lblFirstInput = tk.Label(mainCanvas, background="#CAEAE5", image=img_two)
    lblFirstInput.place(relx=0.117, rely=0.681, height=26, width=72)
    
    inpFirstInput = tk.Entry(mainCanvas, justify ="center", textvariable =RelativityLengthL)
    inpFirstInput.place(relx=0.209, rely=0.681, height=34, relwidth=0.175)
    
    lblExponent = tk.Label(mainCanvas, background="#CAEAE5", text='''x 10''')
    lblExponent.place(relx=0.392, rely=0.699, height=26, width=42)

    inpExponent = tk.Entry(mainCanvas, justify='center', textvariable=RelativityLengthFE)
    inpExponent.place(relx=0.444, rely=0.681,height=34, relwidth=0.07)

    lblFirstType = tk.Label(mainCanvas, background="#CAEAE5", text='''in m''')
    lblFirstType.place(relx=0.522, rely=0.699, height=29, width=50)
    
    ########
    lblSecondInput = tk.Label(mainCanvas, background="#CAEAE5", text='''v =''')
    lblSecondInput.place(relx=0.117, rely=0.789, height=26, width=72)
    
    inpSecondInput = tk.Entry(mainCanvas, justify ="center", textvariable=RelativityLengthV)
    inpSecondInput.place(relx=0.209, rely=0.789, height=34, relwidth=0.175)
    
    lblSecondExponent = tk.Label(mainCanvas, background="#CAEAE5", text='''x 10''')
    lblSecondExponent.place(relx=0.392, rely=0.806, height=26, width=42)

    inpSecondExponent = tk.Entry(mainCanvas, justify='center', textvariable=RelativityLengthSE)
    inpSecondExponent.place(relx=0.444, rely=0.789, height=34, relwidth=0.07)

    lblSecondType = tk.Label(mainCanvas, background="#CAEAE5", text='''in m/sec''')
    lblSecondType.place(relx=0.522, rely=0.806, height=29, width=50)
    
    ######
    lblResult = tk.Label(mainCanvas, background="#CAEAE5", text='''Result =''')
    lblResult.place(relx=0.117, rely=0.878, height=36, width=72)
    
    lblResultTwo = tk.Label(mainCanvas, textvariable=RelativityLengthResult)
    lblResultTwo.place(relx=0.209, rely=0.878, height=34, width=275)
 
    btnCompute = tk.Button(mainCanvas, background="#F7BAB9", text='''Compute''', command=relativityLengthCompute)
    btnCompute.place(relx=0.64, rely=0.681, height=33, width=136)
    
    btnClear = tk.Button(mainCanvas, background="#F7BAB9", text='''Clear Fields''', command=clrscr)
    btnClear.place(relx=0.64, rely=0.789, height=33, width=136)
    
    revL.mainloop()

def relativityLengthCompute():
    l =RelativityLengthL.get()
    v =RelativityLengthV.get()
    fe =RelativityLengthFE.get()
    se =RelativityLengthSE.get()
    c = 29792458
    length = l * pow(10, fe)
    velocity = v * pow(10, se)
    first = velocity / c
    second = pow(first, 2)
    result = length * math.sqrt(1-second)
    RelativityLengthResult.set(str(result) + ' m')  

def keplerOptionsGUI():
    root.withdraw()
    kep = Toplevel()
    kep.deiconify()
    kep.geometry("785x583+389+50")
    kep.resizable(0, 0)
    kep.title("Kepler")
    
    mainCanvas = tk.Frame(kep, background="#CAEAE5")
    mainCanvas.place(relx=0.015, rely=0.021, relheight=0.957, relwidth=0.973)
    
    lblKepler = tk.Label(mainCanvas, background="#CAEAE5", text='''Kepler Options''', font = "-size 14 -weight bold")
    lblKepler.place(relx=0.366, rely=0.054, height=44, width=188)
    
    btnBack = tk.Button(mainCanvas, background="#F7BAB9", text ='''Back''', command =lambda:[kep.withdraw(), root.deiconify()])
    btnBack.place(relx=0.039, rely=0.054, height=37, width=80)
    
    btnKeplerGravity = tk.Button(mainCanvas, background="#F7BAB9", text='''Kepler with Gravity''', command=keplerGravityGUI)
    btnKeplerGravity.place(relx=0.321, rely=0.411, height=53, width=266)

    btnKeplerNoGravity = tk.Button(mainCanvas, background="#F7BAB9", text='''Kepler with no Gravity''', command=keplerGUI)
    btnKeplerNoGravity.place(relx=0.321, rely=0.554, height=53, width=266)
    
    kep.mainloop()
    
#3 USER INPUTS
def keplerGravityGUI():
    clrscr()
    kepG = Toplevel()
    kepG.deiconify()
    kepG.geometry("785x583+389+50")
    kepG.resizable(0, 0)
    kepG.title("Kepler with gravity")
 
    mainCanvas = tk.Frame(kepG, background="#CAEAE5")
    mainCanvas.place(relx=0.015, rely=0.021, relheight=0.957, relwidth=0.973)
    
    lblKeplerG = tk.Label(mainCanvas, background="#CAEAE5", text='''Kepler with gravity''', font = "-size 14 -weight bold")
    lblKeplerG.place(relx=0.209, rely=0.054, height=44, width=457)
    
    btnBack = tk.Button(mainCanvas, background="#F7BAB9", text ='''Back''', command =kepG.withdraw)
    btnBack.place(relx=0.039, rely=0.054, height=37, width=80)
    
    #picture
    img_one = PhotoImage(file='pictures/KeplerWithGravity.png')
    IMAGE_ONE = tk.Label(mainCanvas, background="#CAEAE5", image=img_one)
    IMAGE_ONE.place(relx=0.014, rely=0.168, height=215, width=738)
    
    ######
    lblFirstInput = tk.Label(mainCanvas, background="#CAEAE5", text='''a''', font = "-size 11")
    lblFirstInput.place(relx=0.117, rely=0.627, height=26, width=72)
    
    inpFirstInput = tk.Entry(mainCanvas, justify ="center", textvariable=KeplerGA)
    inpFirstInput.place(relx=0.209, rely=0.627, height=34, relwidth=0.175)
    
    lblExponent = tk.Label(mainCanvas, background="#CAEAE5", text='''x 10''')
    lblExponent.place(relx=0.392, rely=0.645, height=26, width=42)
    
    inpExponent = tk.Entry(mainCanvas, justify ="center", textvariable=KeplerGFirstExponent)
    inpExponent.place(relx=0.444, rely=0.627,height=34, relwidth=0.07)
    
    lblFirstType = tk.Label(mainCanvas, background="#CAEAE5", text='''in m''')
    lblFirstType.place(relx=0.522, rely=0.645, height=29, width=50)
    
    #####
    img_m1 = PhotoImage(file='pictures/m1.png')
    lblSecondInput = tk.Label(mainCanvas, background="#CAEAE5", image=img_m1, text='''=''')
    lblSecondInput.place(relx=0.117, rely=0.717, height=26, width=72)
    
    inpSecondInput = tk.Entry(mainCanvas, justify ="center", textvariable=KeplerGMOne)
    inpSecondInput.place(relx=0.209, rely=0.717, height=34, relwidth=0.175)
    
    lblSecondExponent = tk.Label(mainCanvas, background="#CAEAE5", text='''x 10''')
    lblSecondExponent.place(relx=0.392, rely=0.735, height=26, width=42)
    
    inpSecondExponent = tk.Entry(mainCanvas, justify ="center", textvariable=KeplerGSecondExponent)
    inpSecondExponent.place(relx=0.444, rely=0.717, height=34, relwidth=0.07)
    
    lblSecondType = tk.Label(mainCanvas, background="#CAEAE5", text='''in kg''')
    lblSecondType.place(relx=0.522, rely=0.735, height=29, width=50)
    
    #####
    img_m2 = PhotoImage(file='pictures/m2.png')
    lblThirdInput = tk.Label(mainCanvas, background="#CAEAE5", image=img_m2, text='''=''')
    lblThirdInput.place(relx=0.117, rely=0.806, height=26, width=72)
    
    inpThirdInput = tk.Entry(mainCanvas, justify="center", textvariable=KeplerGMTwo)
    inpThirdInput.place(relx=0.209, rely=0.806, height=34, relwidth=0.175)
    
    lblThirdExponent = tk.Label(mainCanvas, background="#CAEAE5", text='''x 10''')
    lblThirdExponent.place(relx=0.392, rely=0.824, height=26, width=42)
    
    inpThirdExponent = tk.Entry(mainCanvas, justify ="center", textvariable=KeplerGThirdExponent)
    inpThirdExponent.place(relx=0.444, rely=0.806, height=34, relwidth=0.07)
    
    lblThirdType = tk.Label(mainCanvas, background="#CAEAE5", text='''in kg''')
    lblThirdType.place(relx=0.522, rely=0.824, height=29, width=50)

    #######
    lblResult = tk.Label(mainCanvas, background="#CAEAE5", text='''Result =''')
    lblResult.place(relx=0.117, rely=0.896, height=36, width=72)
    
    lblResultTwo = tk.Label(mainCanvas, textvariable=KeplerGResult)
    lblResultTwo.place(relx=0.209, rely=0.896, height=34, width=275)
 
    btnCompute = tk.Button(mainCanvas, background="#F7BAB9", text='''Compute''', command=keplerGCompute)
    btnCompute.place(relx=0.64, rely=0.627, height=33, width=136)
    
    btnClear = tk.Button(mainCanvas, background="#F7BAB9", text='''Clear Fields''', command=clrscr)
    btnClear.place(relx=0.64, rely=0.717, height=33, width=136)
    
    kepG.mainloop()
     
def keplerGCompute():
    a =KeplerGA.get()
    m_one =KeplerGMOne.get()
    m_two =KeplerGMTwo.get()
    fe =KeplerGFirstExponent.get()
    se =KeplerGSecondExponent.get()
    te =KeplerGThirdExponent.get()
    g = 6.6742
    
    semimajor = a * pow (10, fe)
    m1 = m_one * pow(10, se)
    m2 = m_two * pow(10, te)
    numerator = 4* pow(math.pi, 2)
    totalMass = m1 + m2
    denominator = g * totalMass

    result = (numerator / denominator) * pow(semimajor, 3)
    KeplerGResult.set(str(result) + ' sec')    

def keplerGUI():
    clrscr()
    kep = Toplevel()
    kep.deiconify()
    kep.geometry("785x583+389+50")
    kep.resizable(0, 0)
    kep.title("Kepler")
 
    mainCanvas = tk.Frame(kep, background="#CAEAE5")
    mainCanvas.place(relx=0.015, rely=0.021, relheight=0.957, relwidth=0.973)
    
    lblKepler = tk.Label(mainCanvas, background="#CAEAE5", text='''Kepler''', font = "-size 14 -weight bold")
    lblKepler.place(relx=0.209, rely=0.054, height=44, width=457)
    
    btnBack = tk.Button(mainCanvas, background="#F7BAB9", text ='''Back''', command =kep.withdraw)
    btnBack.place(relx=0.039, rely=0.054, height=37, width=80)
    
    #picture
    img_one = PhotoImage(file='pictures/KeplerNoGravity.png')
    IMAGE_ONE = tk.Label(mainCanvas, background="#CAEAE5", image=img_one)
    IMAGE_ONE.place(relx=0.014, rely=0.168, height=215, width=738)
    
    lblFirstInput = tk.Label(mainCanvas, background="#CAEAE5", text='''p''')
    lblFirstInput.place(relx=0.117, rely=0.681, height=26, width=72)
    
    inpFirstInput = tk.Entry(mainCanvas, justify ="center", textvariable=KeplerA)
    inpFirstInput.place(relx=0.209, rely=0.681, height=34, relwidth=0.175)
    
    lblExponent = tk.Label(mainCanvas, background="#CAEAE5", text='''x 10''')
    lblExponent.place(relx=0.392, rely=0.699, height=26, width=42)

    inpExponent = tk.Entry(mainCanvas, justify='center', textvariable=KeplerExponent)
    inpExponent.place(relx=0.444, rely=0.681,height=34, relwidth=0.07)

    lblFirstType = tk.Label(mainCanvas, background="#CAEAE5", text='''in yrs''')
    lblFirstType.place(relx=0.522, rely=0.699, height=26, width=42)
    
    lblResult = tk.Label(mainCanvas, background="#CAEAE5", text='''Result =''')
    lblResult.place(relx=0.117, rely=0.789, height=37, width=72)
    
    lblResultTwo = tk.Label(mainCanvas, textvariable=KeplerResult)
    lblResultTwo.place(relx=0.209, rely=0.789, height=34, width=275)
 
    btnCompute = tk.Button(mainCanvas, background="#F7BAB9", text='''Compute''', command=keplerCompute)
    btnCompute.place(relx=0.64, rely=0.681, height=33, width=136)
        
    btnClear = tk.Button(mainCanvas, background="#F7BAB9", text='''Clear Fields''', command=clrscr)
    btnClear.place(relx=0.64, rely=0.789, height=33, width=136)
    
    kep.mainloop()
     
def keplerCompute():
    p = KeplerA.get()
    fe = KeplerExponent.get()
    first = p * pow(10, fe)
    second = pow(first, 2)
    result = second**(1/3)
    KeplerResult.set(str(result) + ' AU')    

def planckOptionsGUI():
    root.withdraw()
    pl = Toplevel()
    pl.deiconify()
    pl.geometry("785x583+389+50")
    pl.resizable(0, 0)
    pl.title("Planck Options")
    
    mainCanvas = tk.Frame(pl, background="#CAEAE5")
    mainCanvas.place(relx=0.015, rely=0.021, relheight=0.957, relwidth=0.973)
    
    lblEscapeVelocity = tk.Label(mainCanvas, background="#CAEAE5", text='''Planck Options''', font = "-size 14 -weight bold")
    lblEscapeVelocity.place(relx=0.366, rely=0.054, height=44, width=188)
    
    btnBack = tk.Button(mainCanvas, background="#F7BAB9", text ='''Back''', command =lambda:[pl.withdraw(), root.deiconify()])
    btnBack.place(relx=0.039, rely=0.054, height=37, width=80)
    
    btnKeplerGravity = tk.Button(mainCanvas, background="#F7BAB9", text='''Planck in relation to frequency''', command=planckFGUI)
    btnKeplerGravity.place(relx=0.321, rely=0.411, height=53, width=266)

    btnKeplerNoGravity = tk.Button(mainCanvas, background="#F7BAB9", text='''Planck in relation to wavelength''', command=planckWGUI)
    btnKeplerNoGravity.place(relx=0.321, rely=0.554, height=53, width=266)
    
    pl.mainloop()  

def planckFGUI():
    clrscr()
    pLF = Toplevel()
    pLF.deiconify()
    pLF.geometry("785x583+389+50")
    pLF.resizable(0, 0)
    pLF.title("Planck Frequency")
 
    mainCanvas = tk.Frame(pLF, background="#CAEAE5")
    mainCanvas.place(relx=0.015, rely=0.021, relheight=0.957, relwidth=0.973)
    
    lblPlanckF = tk.Label(mainCanvas, background="#CAEAE5", text='''Planck Frequency''', font = "-size 14 -weight bold")
    lblPlanckF.place(relx=0.209, rely=0.054, height=44, width=457)
    
    btnBack = tk.Button(mainCanvas, background="#F7BAB9", text ='''Back''', command =pLF.withdraw)
    btnBack.place(relx=0.039, rely=0.054, height=37, width=80)
    
    #picture
    img_one = PhotoImage(file='pictures/PlanckFrequency.png')
    IMAGE_ONE = tk.Label(mainCanvas, background="#CAEAE5", image=img_one)
    IMAGE_ONE.place(relx=0.014, rely=0.168, height=215, width=738)
    
    lblFirstInput = tk.Label(mainCanvas, background="#CAEAE5", text='''v =''')
    lblFirstInput.place(relx=0.117, rely=0.681, height=26, width=72)
    
    inpFirstInput = tk.Entry(mainCanvas, justify ="center", textvariable=PlanckFV)
    inpFirstInput.place(relx=0.209, rely=0.681, height=34, relwidth=0.175)
    
    lblExponent = tk.Label(mainCanvas, background="#CAEAE5", text='''x 10''')
    lblExponent.place(relx=0.392, rely=0.699, height=26, width=42)

    inpExponent = tk.Entry(mainCanvas, justify='center', textvariable=PlanckFFE)
    inpExponent.place(relx=0.444, rely=0.681,height=34, relwidth=0.07)

    lblFirstType = tk.Label(mainCanvas, background="#CAEAE5", text='''in W''')
    lblFirstType.place(relx=0.522, rely=0.699, height=29, width=50)
     
    lblResult = tk.Label(mainCanvas, background="#CAEAE5", text='''Result =''')
    lblResult.place(relx=0.117, rely=0.789, height=37, width=72)
    
    lblResultTwo = tk.Label(mainCanvas, textvariable=PlanckFResult)
    lblResultTwo.place(relx=0.209, rely=0.789, height=34, width=275)
 
    btnCompute = tk.Button(mainCanvas, background="#F7BAB9", text='''Compute''', command=planckFCompute)
    btnCompute.place(relx=0.64, rely=0.681, height=33, width=136)
    
    btnClear = tk.Button(mainCanvas, background="#F7BAB9", text='''Clear Fields''', command=clrscr)
    btnClear.place(relx=0.64, rely=0.789, height=33, width=136)
    
    pLF.mainloop()    
 
def planckFCompute():
    v = PlanckFV.get()
    fe = PlanckFFE.get()
    h = 6.6260693
    velocity = v * pow(10, fe)
    result = h * velocity
    PlanckFResult.set(str(result) + ' joules')  

def planckWGUI():
    clrscr()
    pLW = Toplevel()
    pLW.deiconify()
    pLW.geometry("785x583+389+50")
    pLW.resizable(0, 0)
    pLW.title("Planck Wavelength")
 
    mainCanvas = tk.Frame(pLW, background="#CAEAE5")
    mainCanvas.place(relx=0.015, rely=0.021, relheight=0.957, relwidth=0.973)
    
    lblPlanckW = tk.Label(mainCanvas, background="#CAEAE5", text='''Planck Wavelength''', font = "-size 14 -weight bold")
    lblPlanckW.place(relx=0.209, rely=0.054, height=44, width=457)
    
    btnBack = tk.Button(mainCanvas, background="#F7BAB9", text ='''Back''', command =pLW.withdraw)
    btnBack.place(relx=0.039, rely=0.054, height=37, width=80)
    
    #picture
    img_one = PhotoImage(file='pictures/PlanckWave.png')
    IMAGE_ONE = tk.Label(mainCanvas, background="#CAEAE5", image=img_one)
    IMAGE_ONE.place(relx=0.014, rely=0.168, height=215, width=738)
    
    lblFirstInput = tk.Label(mainCanvas, background="#CAEAE5", text='''λ =''')
    lblFirstInput.place(relx=0.117, rely=0.681, height=26, width=72)
    
    inpFirstInput = tk.Entry(mainCanvas, justify ="center", textvariable=PlanckWV)
    inpFirstInput.place(relx=0.209, rely=0.681, height=34, relwidth=0.175)
    
    lblExponent = tk.Label(mainCanvas, background="#CAEAE5", text='''x 10''')
    lblExponent.place(relx=0.392, rely=0.699, height=26, width=42)

    inpExponent = tk.Entry(mainCanvas, justify='center', textvariable=PlanckWFE)
    inpExponent.place(relx=0.444, rely=0.681,height=34, relwidth=0.07)

    lblFirstType = tk.Label(mainCanvas, background="#CAEAE5", text='''in m/sec''')
    lblFirstType.place(relx=0.522, rely=0.699, height=29, width=50)
    
    ####
    lblResult = tk.Label(mainCanvas, background="#CAEAE5", text='''Result =''')
    lblResult.place(relx=0.117, rely=0.789, height=37, width=72)
    
    lblResultTwo = tk.Label(mainCanvas, textvariable=PlanckWResult)
    lblResultTwo.place(relx=0.209, rely=0.789, height=34, width=275)
 
    btnCompute = tk.Button(mainCanvas, background="#F7BAB9", text='''Compute''', command=planckWCompute)
    btnCompute.place(relx=0.64, rely=0.681, height=33, width=136)
    
    btnClear = tk.Button(mainCanvas, background="#F7BAB9", text='''Clear Fields''', command=clrscr)
    btnClear.place(relx=0.64, rely=0.789, height=33, width=136)
    
    pLW.mainloop()    
 
def planckWCompute():
    wv = PlanckWV.get()
    fe = PlanckWFE.get()
    h = 6.6260693
    c = 29792458
    numerator = h * c
    wavelength = wv * pow(10, fe)
    
    
    result = numerator / wavelength
    PlanckWResult.set(str(result) + ' joules')  

def stellarPropertyOptionsGUI():
    clrscr()
    root.withdraw()
    window = Toplevel()
    window.deiconify()
    window.geometry("785x583+389+50")
    window.resizable(0, 0)
    window.title("Stellar Properties")
 
    mainCanvas = tk.Frame(window, background="#CAEAE5")
    mainCanvas.place(relx=0.015, rely=0.021, relheight=0.957, relwidth=0.973)

    lblTitle = tk.Label(mainCanvas, background="#CAEAE5", text='''Stellar Property Options''', font = "-size 14 -weight bold")
    lblTitle.place(relx=0.222, rely=0.054, height=44, width=409)

    btnBack = tk.Button(mainCanvas, background="#F7BAB9", text ='''Back''', command =lambda:[window.withdraw(), root.deiconify()])
    btnBack.place(relx=0.039, rely=0.054, height=37, width=80)

    btnOption1 = tk.Button(mainCanvas, background="#F7BAB9", text='''Brightness''', command=brightnessGUI)
    btnOption1.place(relx=0.326, rely=0.305, height=53, width=266)

    btnOption2 = tk.Button(mainCanvas, background="#F7BAB9", text='''Luminosity''', command=luminosityOptionGUI)
    btnOption2.place(relx=0.326, rely=0.448, height=53, width=266)
    
    btnOption3 = tk.Button(mainCanvas, background="#F7BAB9", text='''Surface Temperature''', command=surfaceTempGUI)
    btnOption3.place(relx=0.326, rely=0.591, height=53, width=266)
    
    window.mainloop()

def luminosityOptionGUI():
    clrscr()
    window = Toplevel()
    window.deiconify()
    window.geometry("785x583+389+50")
    window.resizable(0, 0)
    window.title("Luminosity Options")
 
    mainCanvas = tk.Frame(window, background="#CAEAE5")
    mainCanvas.place(relx=0.015, rely=0.021, relheight=0.957, relwidth=0.973)
    
    lblTitle = tk.Label(mainCanvas, background="#CAEAE5", text='''Luminosity Property Options''', font = "-size 14 -weight bold")
    lblTitle.place(relx=0.222, rely=0.054, height=44, width=409)
    
    btnBack = tk.Button(mainCanvas, background="#F7BAB9", text ='''Back''', command=window.withdraw)
    btnBack.place(relx=0.039, rely=0.054, height=37, width=80)
        
    btnOption1 = tk.Button(mainCanvas, background="#F7BAB9", text='''Luminosity (Apparent Brightness)''', command=luminosityAPGUI)
    btnOption1.place(relx=0.321, rely=0.411, height=53, width=266)

    btnOption2 = tk.Button(mainCanvas, background="#F7BAB9", text='''Luminosity (Surface Temperature)''', command=luminositySTGUI)
    btnOption2.place(relx=0.321, rely=0.554, height=53, width=266)
    
    window.mainloop()
        
def brightnessGUI():
    clrscr()
    window = Toplevel()
    window.deiconify()
    window.geometry("785x583+389+50")
    window.resizable(0, 0)
    window.title("Brightness")
 
    mainCanvas = tk.Frame(window, background="#CAEAE5")
    mainCanvas.place(relx=0.015, rely=0.021, relheight=0.957, relwidth=0.973)
    
    lblTitle = tk.Label(mainCanvas, background="#CAEAE5", text='''Brightness''', font = "-size 14 -weight bold")
    lblTitle.place(relx=0.222, rely=0.054, height=44, width=409)
    
    btnBack = tk.Button(mainCanvas, background="#F7BAB9", text ='''Back''', command =window.withdraw)
    btnBack.place(relx=0.039, rely=0.054, height=37, width=80)
    
    #picture
    pic = PhotoImage(file='pictures/brightness.png')
    lblGuide = tk.Label(mainCanvas, background="#CAEAE5", image=pic)
    lblGuide.place(relx=0.014, rely=0.168, height=215, width=738)

    lblFirstInput = tk.Label(mainCanvas, background="#CAEAE5", text='''L =''')
    lblFirstInput.place(relx=0.117, rely=0.681, height=26, width=72)
    
    inpFirstInput = tk.Entry(mainCanvas, justify= 'center', textvariable= BrightnessL)
    inpFirstInput.place(relx=0.209, rely=0.681, height=34, relwidth=0.175)
    
    lblExponent = tk.Label(mainCanvas, background="#CAEAE5", text='''x 10''')
    lblExponent.place(relx=0.392, rely=0.699, height=26, width=42)

    inpExponent = tk.Entry(mainCanvas, justify='center', textvariable=BrightnessFE)
    inpExponent.place(relx=0.444, rely=0.681,height=34, relwidth=0.07)

    lblFirstType = tk.Label(mainCanvas, background="#CAEAE5", text='''in W''')
    lblFirstType.place(relx=0.522, rely=0.699, height=29, width=50)
    
    ######
    lblSecondInput = tk.Label(mainCanvas, background="#CAEAE5", text='''d =''')
    lblSecondInput.place(relx=0.117, rely=0.789, height=26, width=72)
    
    inpSecondInput = tk.Entry(mainCanvas, justify= 'center', textvariable=BrightnessD)
    inpSecondInput.place(relx=0.209, rely=0.789, height=34, relwidth=0.175)
    
    lblSecondExponent = tk.Label(mainCanvas, background="#CAEAE5", text='''x 10''')
    lblSecondExponent.place(relx=0.392, rely=0.806, height=26, width=42)

    inpSecondExponent = tk.Entry(mainCanvas, justify='center', textvariable=BrightnessSE)
    inpSecondExponent.place(relx=0.444, rely=0.789, height=34, relwidth=0.07)

    lblSecondType = tk.Label(mainCanvas, background="#CAEAE5", text='''in m''')
    lblSecondType.place(relx=0.522, rely=0.806, height=29, width=50)
    
    ######
    lblResult = tk.Label(mainCanvas, background="#CAEAE5", text='''Result =''')
    lblResult.place(relx=0.117, rely=0.878, height=36, width=72)
    
    lblResultTwo = tk.Label(mainCanvas, textvariable=BrightnessResult)
    lblResultTwo.place(relx=0.209, rely=0.878, height=34, width=275)
    
    btnCompute = tk.Button(mainCanvas, background="#F7BAB9", text='''Compute''', command= brightnessCompute)
    btnCompute.place(relx=0.64, rely=0.681, height=33, width=136)
    
    btnClear = tk.Button(mainCanvas, background="#F7BAB9", text='''Clear Fields''', command=clrscr)
    btnClear.place(relx=0.64, rely=0.789, height=33, width=136)
    
    window.mainloop()
    
def brightnessCompute():
    l =BrightnessL.get()
    d =BrightnessD.get()
    fe = BrightnessFE.get()
    se = BrightnessSE.get()
    
    luminosity = l * pow(10, fe)
    distance = d * pow(10, se)

    first =4 * math.pi
    second = (pow(distance, 2))
    denominator = first * second
    result = luminosity / denominator
    BrightnessResult.set(str(result) + ' W')  
    
def surfaceTempGUI():
    clrscr()
    window = Toplevel()
    window.deiconify()
    window.geometry("785x583+389+50")
    window.resizable(0, 0)
    window.title("Surface Temperature")
 
    mainCanvas = tk.Frame(window, background="#CAEAE5")
    mainCanvas.place(relx=0.015, rely=0.021, relheight=0.957, relwidth=0.973)
    
    lblTitle = tk.Label(mainCanvas, background="#CAEAE5", text='''Surface Temperature''', font = "-size 14 -weight bold")
    lblTitle.place(relx=0.222, rely=0.054, height=44, width=409)
    
    btnBack = tk.Button(mainCanvas, background="#F7BAB9", text ='''Back''', command =window.withdraw)
    btnBack.place(relx=0.039, rely=0.054, height=37, width=80)
    
    #picture
    pic = PhotoImage(file='pictures/SurfaceTemp.png')
    lblGuide = tk.Label(mainCanvas, background="#CAEAE5", image=pic)
    lblGuide.place(relx=0.014, rely=0.168, height=215, width=738)

    lblFirstInput = tk.Label(mainCanvas, background="#CAEAE5", text='''L =''')
    lblFirstInput.place(relx=0.117, rely=0.681, height=26, width=72)
    
    inpFirstInput = tk.Entry(mainCanvas, justify= 'center', textvariable= SurfaceTempL)
    inpFirstInput.place(relx=0.209, rely=0.681, height=34, relwidth=0.175)
    
    lblExponent = tk.Label(mainCanvas, background="#CAEAE5", text='''x 10''')
    lblExponent.place(relx=0.392, rely=0.699, height=26, width=42)

    inpExponent = tk.Entry(mainCanvas, justify='center', textvariable=SurfaceTempFE)
    inpExponent.place(relx=0.444, rely=0.681,height=34, relwidth=0.07)

    lblFirstType = tk.Label(mainCanvas, background="#CAEAE5", text='''in W''')
    lblFirstType.place(relx=0.522, rely=0.699, height=29, width=50)
    
    #########
    lblSecondInput = tk.Label(mainCanvas, background="#CAEAE5", text='''R =''')
    lblSecondInput.place(relx=0.117, rely=0.789, height=26, width=72)
    
    inpSecondInput = tk.Entry(mainCanvas, justify= 'center', textvariable=SurfaceTempR)
    inpSecondInput.place(relx=0.209, rely=0.789, height=34, relwidth=0.175)
    
    lblSecondExponent = tk.Label(mainCanvas, background="#CAEAE5", text='''x 10''')
    lblSecondExponent.place(relx=0.392, rely=0.806, height=26, width=42)

    inpSecondExponent = tk.Entry(mainCanvas, justify='center', textvariable=SurfaceTempSE)
    inpSecondExponent.place(relx=0.444, rely=0.789, height=34, relwidth=0.07)

    lblSecondType = tk.Label(mainCanvas, background="#CAEAE5", text='''in m''')
    lblSecondType.place(relx=0.522, rely=0.806, height=29, width=50)

    #######
    lblResult = tk.Label(mainCanvas, background="#CAEAE5", text='''Result =''')
    lblResult.place(relx=0.117, rely=0.878, height=36, width=72)
    
    lblResultTwo = tk.Label(mainCanvas, textvariable=SurfaceTempResult)
    lblResultTwo.place(relx=0.209, rely=0.878, height=34, width=275)
    
    btnCompute = tk.Button(mainCanvas, background="#F7BAB9", text='''Compute''', command= surfaceTempCompute)
    btnCompute.place(relx=0.64, rely=0.681, height=33, width=136)
    
    btnClear = tk.Button(mainCanvas, background="#F7BAB9", text='''Clear Fields''', command=clrscr)
    btnClear.place(relx=0.64, rely=0.789, height=33, width=136)
    
    window.mainloop()
    
def surfaceTempCompute():
    l =SurfaceTempL.get()
    r =SurfaceTempR.get()
    fe =SurfaceTempFE.get()
    se =SurfaceTempSE.get()

    luminosity = l * pow(10, fe)
    radius = r * pow(10, se)
    boltzmann = 5.670400

    first = 4 * math.pi
    second = pow(radius, 2)
    third = second * boltzmann
    denominator = first * third
    fraction = luminosity / denominator
    
    result = fraction ** (1/4)
    
    SurfaceTempResult.set(str(result) + ' Kelvin')    
    
def luminosityAPGUI():
    clrscr()
    window = Toplevel()
    window.deiconify()
    window.geometry("785x583+389+50")
    window.resizable(0, 0)
    window.title("Luminosity (Apparent Brightness)")
 
    mainCanvas = tk.Frame(window, background="#CAEAE5")
    mainCanvas.place(relx=0.015, rely=0.021, relheight=0.957, relwidth=0.973)
    
    lblTitle = tk.Label(mainCanvas, background="#CAEAE5", text='''Luminosity (Apparent Brightness)''', font = "-size 14 -weight bold")
    lblTitle.place(relx=0.222, rely=0.054, height=44, width=409)
    
    btnBack = tk.Button(mainCanvas, background="#F7BAB9", text ='''Back''', command =window.withdraw)
    btnBack.place(relx=0.039, rely=0.054, height=37, width=80)
    
    #picture
    pic = PhotoImage(file='pictures/LuminosityApparentBrightness.png')
    lblGuide = tk.Label(mainCanvas, background="#CAEAE5", image=pic)
    lblGuide.place(relx=0.014, rely=0.168, height=215, width=738)

    lblFirstInput = tk.Label(mainCanvas, background="#CAEAE5", text='''d =''')
    lblFirstInput.place(relx=0.117, rely=0.681, height=26, width=72)
    
    inpFirstInput = tk.Entry(mainCanvas, justify= 'center', textvariable= LuminosityAPD)
    inpFirstInput.place(relx=0.209, rely=0.681, height=34, relwidth=0.175)
    
    lblExponent = tk.Label(mainCanvas, background="#CAEAE5", text='''x 10''')
    lblExponent.place(relx=0.392, rely=0.699, height=26, width=42)

    inpExponent = tk.Entry(mainCanvas, justify='center', textvariable=LuminosityAPFE)
    inpExponent.place(relx=0.444, rely=0.681,height=34, relwidth=0.07)

    lblFirstType = tk.Label(mainCanvas, background="#CAEAE5", text='''in m''')
    lblFirstType.place(relx=0.522, rely=0.699, height=29, width=50)
    
    #######
    lblSecondInput = tk.Label(mainCanvas, background="#CAEAE5", text='''b =''')
    lblSecondInput.place(relx=0.117, rely=0.789, height=26, width=72)
    
    inpSecondInput = tk.Entry(mainCanvas, justify= 'center', textvariable=LuminosityAPB)
    inpSecondInput.place(relx=0.209, rely=0.789, height=34, relwidth=0.175)
    
    lblSecondExponent = tk.Label(mainCanvas, background="#CAEAE5", text='''x 10''')
    lblSecondExponent.place(relx=0.392, rely=0.806, height=26, width=42)

    inpSecondExponent = tk.Entry(mainCanvas, justify='center', textvariable=LuminosityAPSE)
    inpSecondExponent.place(relx=0.444, rely=0.789, height=34, relwidth=0.07)

    lblSecondType = tk.Label(mainCanvas, background="#CAEAE5", text='''in W/m^2''', font = "-size 9")
    lblSecondType.place(relx=0.522, rely=0.806, height=29, width=50)
    
    
    #######
    lblResult = tk.Label(mainCanvas, background="#CAEAE5", text='''Result =''')
    lblResult.place(relx=0.117, rely=0.878, height=36, width=72)
    
    lblResultTwo = tk.Label(mainCanvas, textvariable=LuminosityAPResult)
    lblResultTwo.place(relx=0.209, rely=0.878, height=34, width=275)
    
    btnCompute = tk.Button(mainCanvas, background="#F7BAB9", text='''Compute''', command= LuminosityAPCompute)
    btnCompute.place(relx=0.64, rely=0.681, height=33, width=136)
    
    btnClear = tk.Button(mainCanvas, background="#F7BAB9", text='''Clear Fields''', command=clrscr)
    btnClear.place(relx=0.64, rely=0.789, height=33, width=136)
    
    window.mainloop()
    
def LuminosityAPCompute():
    b =LuminosityAPB.get()
    d =LuminosityAPD.get()
    fe = LuminosityAPFE.get()
    se =LuminosityAPSE.get()
    
    distance = d * pow(10, fe)
    brightness = b * pow(10, se)
    
    first = 4 * math.pi
    second = pow(distance, 2)
    numerator = first * second
    
    result = numerator / brightness
    LuminosityAPResult.set(str(result) + ' W')    
      
def luminositySTGUI():
    clrscr()
    window = Toplevel()
    window.deiconify()
    window.geometry("785x583+389+50")
    window.resizable(0, 0)
    window.title("Luminosity (Surface Temperature)")
 
    mainCanvas = tk.Frame(window, background="#CAEAE5")
    mainCanvas.place(relx=0.015, rely=0.021, relheight=0.957, relwidth=0.973)
    
    lblTitle = tk.Label(mainCanvas, background="#CAEAE5", text='''Luminosity (Surface Temperature)''', font = "-size 14 -weight bold")
    lblTitle.place(relx=0.222, rely=0.054, height=44, width=409)
    
    btnBack = tk.Button(mainCanvas, background="#F7BAB9", text ='''Back''', command =window.withdraw)
    btnBack.place(relx=0.039, rely=0.054, height=37, width=80)
    
    #picture
    pic = PhotoImage(file='pictures/LuminositySurfaceTemp.png')
    lblGuide = tk.Label(mainCanvas, background="#CAEAE5", image=pic)
    lblGuide.place(relx=0.014, rely=0.168, height=215, width=738)

    lblFirstInput = tk.Label(mainCanvas, background="#CAEAE5", text='''R =''')
    lblFirstInput.place(relx=0.117, rely=0.681, height=26, width=72)
    
    inpFirstInput = tk.Entry(mainCanvas, justify= 'center', textvariable= LuminositySTR)
    inpFirstInput.place(relx=0.209, rely=0.681, height=34, relwidth=0.175)
    
    lblExponent = tk.Label(mainCanvas, background="#CAEAE5", text='''x 10''')
    lblExponent.place(relx=0.392, rely=0.699, height=26, width=42)

    inpExponent = tk.Entry(mainCanvas, justify='center', textvariable=LuminositySTFE)
    inpExponent.place(relx=0.444, rely=0.681,height=34, relwidth=0.07)

    lblFirstType = tk.Label(mainCanvas, background="#CAEAE5", text='''in m''')
    lblFirstType.place(relx=0.522, rely=0.699, height=29, width=50)
    
    ########
    lblSecondInput = tk.Label(mainCanvas, background="#CAEAE5", text='''T =''')
    lblSecondInput.place(relx=0.117, rely=0.789, height=26, width=72)
    
    inpSecondInput = tk.Entry(mainCanvas, justify= 'center', textvariable=LuminositySTT)
    inpSecondInput.place(relx=0.209, rely=0.789, height=34, relwidth=0.175)
    
    lblSecondExponent = tk.Label(mainCanvas, background="#CAEAE5", text='''x 10''')
    lblSecondExponent.place(relx=0.392, rely=0.806, height=26, width=42)

    inpSecondExponent = tk.Entry(mainCanvas, justify='center', textvariable=LuminositySTSE)
    inpSecondExponent.place(relx=0.444, rely=0.789, height=34, relwidth=0.07)

    lblSecondType = tk.Label(mainCanvas, background="#CAEAE5", text='''in K''')
    lblSecondType.place(relx=0.522, rely=0.806, height=29, width=50)

    ##########
    lblResult = tk.Label(mainCanvas, background="#CAEAE5", text='''Result =''')
    lblResult.place(relx=0.117, rely=0.878, height=36, width=72)
    
    lblResultTwo = tk.Label(mainCanvas, textvariable=LuminositySTResult)
    lblResultTwo.place(relx=0.209, rely=0.878, height=34, width=275)
    
    btnCompute = tk.Button(mainCanvas, background="#F7BAB9", text='''Compute''', command=LuminositySTCompute)
    btnCompute.place(relx=0.64, rely=0.681, height=33, width=136)
    
    btnClear = tk.Button(mainCanvas, background="#F7BAB9", text='''Clear Fields''', command=clrscr)
    btnClear.place(relx=0.64, rely=0.789, height=33, width=136)
    
    window.mainloop()   
    
def LuminositySTCompute():   
    r =LuminositySTR.get()
    t =LuminositySTT.get()
    fe =LuminositySTFE.get()
    se =LuminositySTSE.get()
    boltzmann = 5.670400
    
    radius = r * pow(10, fe)
    temperature = t * pow(10, se)
    
    first = 4 * math.pi
    second = pow(radius, 2)
    third = boltzmann * pow(temperature, 4)
    
    result = first * second * third
    LuminositySTResult.set(str(result) + ' W') 
    
def eccentricityOptionsGUI():
    clrscr()
    root.withdraw()
    window = Toplevel()
    window.deiconify()
    window.geometry("785x583+389+50")
    window.resizable(0, 0)
    window.title("Eccentricity Properties")
 
    mainCanvas = tk.Frame(window, background="#CAEAE5")
    mainCanvas.place(relx=0.015, rely=0.021, relheight=0.957, relwidth=0.973)

    lblTitle = tk.Label(mainCanvas, background="#CAEAE5", text='''Eccentricity Property Options''', font = "-size 14 -weight bold")
    lblTitle.place(relx=0.222, rely=0.054, height=44, width=409)

    btnBack = tk.Button(mainCanvas, background="#F7BAB9", text ='''Back''', command =lambda:[window.withdraw(), root.deiconify()])
    btnBack.place(relx=0.039, rely=0.054, height=37, width=80)

    btnOption1 = tk.Button(mainCanvas, background="#F7BAB9", text='''Eccentricity''', command=EccentricityGUI)
    btnOption1.place(relx=0.326, rely=0.305, height=53, width=266)

    btnOption2 = tk.Button(mainCanvas, background="#F7BAB9", text='''Perihilion''', command=PerihilionGUI)
    btnOption2.place(relx=0.326, rely=0.448, height=53, width=266)
    
    btnOption3 = tk.Button(mainCanvas, background="#F7BAB9", text='''Aphelion''', command=AphelionGUI)
    btnOption3.place(relx=0.326, rely=0.591, height=53, width=266)
    
    window.mainloop()

def EccentricityGUI():
    clrscr()
    window = Toplevel()
    window.deiconify()
    window.geometry("785x583+389+50")
    window.resizable(0, 0)
    window.title("Eccentricity")
 
    mainCanvas = tk.Frame(window, background="#CAEAE5")
    mainCanvas.place(relx=0.015, rely=0.021, relheight=0.957, relwidth=0.973)
    
    lblTitle = tk.Label(mainCanvas, background="#CAEAE5", text='''Eccentricity''', font = "-size 14 -weight bold")
    lblTitle.place(relx=0.222, rely=0.054, height=44, width=409)
    
    btnBack = tk.Button(mainCanvas, background="#F7BAB9", text ='''Back''', command =window.withdraw)
    btnBack.place(relx=0.039, rely=0.054, height=37, width=80)
    
    #picture
    pic = PhotoImage(file='pictures/Eccentricity.png')
    lblGuide = tk.Label(mainCanvas, background="#CAEAE5", image=pic)
    lblGuide.place(relx=0.014, rely=0.168, height=215, width=738)

    lblFirstInput = tk.Label(mainCanvas, background="#CAEAE5", text='''Q =''')
    lblFirstInput.place(relx=0.117, rely=0.681, height=26, width=72)
    
    inpFirstInput = tk.Entry(mainCanvas, justify= 'center', textvariable= EccentricityQ)
    inpFirstInput.place(relx=0.209, rely=0.681, height=34, relwidth=0.175)
    
    lblExponent = tk.Label(mainCanvas, background="#CAEAE5", text='''x 10''')
    lblExponent.place(relx=0.392, rely=0.699, height=26, width=42)

    inpExponent = tk.Entry(mainCanvas, justify='center', textvariable=EccentricityFE)
    inpExponent.place(relx=0.444, rely=0.681,height=34, relwidth=0.07)

    lblFirstType = tk.Label(mainCanvas, background="#CAEAE5", text='''in AU''')
    lblFirstType.place(relx=0.522, rely=0.699, height=29, width=50)
    
    ################
    lblSecondInput = tk.Label(mainCanvas, background="#CAEAE5", text='''q =''')
    lblSecondInput.place(relx=0.117, rely=0.789, height=26, width=72)
    
    inpSecondInput = tk.Entry(mainCanvas, justify= 'center', textvariable=Eccentricityq)
    inpSecondInput.place(relx=0.209, rely=0.789, height=34, relwidth=0.175)
    
    lblSecondExponent = tk.Label(mainCanvas, background="#CAEAE5", text='''x 10''')
    lblSecondExponent.place(relx=0.392, rely=0.806, height=26, width=42)

    inpSecondExponent = tk.Entry(mainCanvas, justify='center', textvariable=EccentricitySE)
    inpSecondExponent.place(relx=0.444, rely=0.789, height=34, relwidth=0.07)

    lblSecondType = tk.Label(mainCanvas, background="#CAEAE5", text='''in AU''')
    lblSecondType.place(relx=0.522, rely=0.806, height=29, width=50)
    
    ############
    lblResult = tk.Label(mainCanvas, background="#CAEAE5", text='''Result =''')
    lblResult.place(relx=0.117, rely=0.878, height=36, width=72)
    
    lblResultTwo = tk.Label(mainCanvas, textvariable=EccentricityResult)
    lblResultTwo.place(relx=0.209, rely=0.878, height=34, width=275)
    
    btnCompute = tk.Button(mainCanvas, background="#F7BAB9", text='''Compute''', command=eccentricityCompute)
    btnCompute.place(relx=0.64, rely=0.681, height=33, width=136)
    
    btnClear = tk.Button(mainCanvas, background="#F7BAB9", text='''Clear Fields''', command=clrscr)
    btnClear.place(relx=0.64, rely=0.789, height=33, width=136)
    
    window.mainloop()   
    
def eccentricityCompute():  
    Q =EccentricityQ.get()
    q =Eccentricityq.get()
    fe =EccentricityFE.get()
    se =EccentricitySE.get()

    Perihelion = Q * pow(10, fe)
    Aphelion = q * pow(10, se)
    
    first = Perihelion - Aphelion
    second = Perihelion + Aphelion
    
    result = first / second
    EccentricityResult.set(str(result)) 

def PerihilionGUI():
    clrscr()
    window = Toplevel()
    window.deiconify()
    window.geometry("785x583+389+50")
    window.resizable(0, 0)
    window.title("Perihilion")
 
    mainCanvas = tk.Frame(window, background="#CAEAE5")
    mainCanvas.place(relx=0.015, rely=0.021, relheight=0.957, relwidth=0.973)
    
    lblTitle = tk.Label(mainCanvas, background="#CAEAE5", text='''Perihilion''', font = "-size 14 -weight bold")
    lblTitle.place(relx=0.222, rely=0.054, height=44, width=409)
    
    btnBack = tk.Button(mainCanvas, background="#F7BAB9", text ='''Back''', command =window.withdraw)
    btnBack.place(relx=0.039, rely=0.054, height=37, width=80)
    
    #picture
    pic = PhotoImage(file='pictures/perihilion.png')
    lblGuide = tk.Label(mainCanvas, background="#CAEAE5", image=pic)
    lblGuide.place(relx=0.014, rely=0.168, height=215, width=738)

    lblFirstInput = tk.Label(mainCanvas, background="#CAEAE5", text='''a =''')
    lblFirstInput.place(relx=0.117, rely=0.681, height=26, width=72)
    
    inpFirstInput = tk.Entry(mainCanvas, justify= 'center', textvariable= PerihilionA)
    inpFirstInput.place(relx=0.209, rely=0.681, height=34, relwidth=0.175)
    
    lblExponent = tk.Label(mainCanvas, background="#CAEAE5", text='''x 10''')
    lblExponent.place(relx=0.392, rely=0.699, height=26, width=42)

    inpExponent = tk.Entry(mainCanvas, justify='center', textvariable=PerihilionFE)
    inpExponent.place(relx=0.444, rely=0.681,height=34, relwidth=0.07)

    # lblFirstType = tk.Label(mainCanvas, background="#CAEAE5", text='''in **''')
    # lblFirstType.place(relx=0.522, rely=0.699, height=29, width=50)

    #########
    lblSecondInput = tk.Label(mainCanvas, background="#CAEAE5", text='''e =''')
    lblSecondInput.place(relx=0.117, rely=0.789, height=26, width=72)
    
    inpSecondInput = tk.Entry(mainCanvas, justify= 'center', textvariable=PerihilionE)
    inpSecondInput.place(relx=0.209, rely=0.789, height=34, relwidth=0.175)
    
    lblSecondExponent = tk.Label(mainCanvas, background="#CAEAE5", text='''x 10''')
    lblSecondExponent.place(relx=0.392, rely=0.806, height=26, width=42)

    inpSecondExponent = tk.Entry(mainCanvas, justify='center', textvariable=PerihilionSE)
    inpSecondExponent.place(relx=0.444, rely=0.789, height=34, relwidth=0.07)

    # lblSecondType = tk.Label(mainCanvas, background="#CAEAE5", text='''in **''')
    # lblSecondType.place(relx=0.522, rely=0.806, height=29, width=50)
    
    ##########
    lblResult = tk.Label(mainCanvas, background="#CAEAE5", text='''Result =''')
    lblResult.place(relx=0.117, rely=0.878, height=36, width=72)
    
    lblResultTwo = tk.Label(mainCanvas, textvariable=PerihilionResult)
    lblResultTwo.place(relx=0.209, rely=0.878, height=34, width=233)
    
    btnCompute = tk.Button(mainCanvas, background="#F7BAB9", text='''Compute''', command=perihilionCompute)
    btnCompute.place(relx=0.64, rely=0.681, height=33, width=136)
    
    btnClear = tk.Button(mainCanvas, background="#F7BAB9", text='''Clear Fields''', command=clrscr)
    btnClear.place(relx=0.64, rely=0.789, height=33, width=136)
    
    window.mainloop()   
    
def perihilionCompute():  
    a =PerihilionA.get()
    e =PerihilionE.get()
    fe =PerihilionFE.get()
    se =PerihilionSE.get()
    
    semimajor = a * pow(10, fe)
    eccentricity = e * pow(10, Se)

    result = semimajor * (1 + eccentricity)
    PerihilionResult.set(str(result) + ' AU') 

def AphelionGUI():
    clrscr()
    window = Toplevel()
    window.deiconify()
    window.geometry("785x583+389+50")
    window.resizable(0, 0)
    window.title("Aphelion")
 
    mainCanvas = tk.Frame(window, background="#CAEAE5")
    mainCanvas.place(relx=0.015, rely=0.021, relheight=0.957, relwidth=0.973)
    
    lblTitle = tk.Label(mainCanvas, background="#CAEAE5", text='''Aphelion''', font = "-size 14 -weight bold")
    lblTitle.place(relx=0.222, rely=0.054, height=44, width=409)
    
    btnBack = tk.Button(mainCanvas, background="#F7BAB9", text ='''Back''', command =window.withdraw)
    btnBack.place(relx=0.039, rely=0.054, height=37, width=80)
    
    #picture
    pic = PhotoImage(file='pictures/Aphelion.png')
    lblGuide = tk.Label(mainCanvas, background="#CAEAE5", image=pic)
    lblGuide.place(relx=0.014, rely=0.168, height=215, width=738)

    lblFirstInput = tk.Label(mainCanvas, background="#CAEAE5", text='''a =''', font = "-size 11")
    lblFirstInput.place(relx=0.117, rely=0.681, height=26, width=72)
    
    inpFirstInput = tk.Entry(mainCanvas, justify= 'center', textvariable= AphelionA)
    inpFirstInput.place(relx=0.209, rely=0.681, height=34, relwidth=0.175)
    
    lblExponent = tk.Label(mainCanvas, background="#CAEAE5", text='''x 10''')
    lblExponent.place(relx=0.392, rely=0.699, height=26, width=42)

    inpExponent = tk.Entry(mainCanvas, justify='center', textvariable=AphelionFE)
    inpExponent.place(relx=0.444, rely=0.681,height=34, relwidth=0.07)

    # lblFirstType = tk.Label(mainCanvas, background="#CAEAE5", text='''in **''')
    # lblFirstType.place(relx=0.522, rely=0.699, height=29, width=50)
    
    ########
    lblSecondInput = tk.Label(mainCanvas, background="#CAEAE5", text='''e =''', font = "-size 11")
    lblSecondInput.place(relx=0.117, rely=0.789, height=26, width=72)
    
    inpSecondInput = tk.Entry(mainCanvas, justify= 'center', textvariable=AphelionE)
    inpSecondInput.place(relx=0.209, rely=0.789, height=34, relwidth=0.175)
    
    lblSecondExponent = tk.Label(mainCanvas, background="#CAEAE5", text='''x 10''')
    lblSecondExponent.place(relx=0.392, rely=0.806, height=26, width=42)

    inpSecondExponent = tk.Entry(mainCanvas, justify='center', textvariable=AphelionSE)
    inpSecondExponent.place(relx=0.444, rely=0.789, height=34, relwidth=0.07)

    # lblSecondType = tk.Label(mainCanvas, background="#CAEAE5", text='''in **''')
    # lblSecondType.place(relx=0.522, rely=0.806, height=29, width=50)
    
    ########
    lblResult = tk.Label(mainCanvas, background="#CAEAE5", text='''Result =''')
    lblResult.place(relx=0.117, rely=0.878, height=36, width=72)
    
    lblResultTwo = tk.Label(mainCanvas, textvariable=AphelionResult)
    lblResultTwo.place(relx=0.209, rely=0.878, height=34, width=233)
    
    btnCompute = tk.Button(mainCanvas, background="#F7BAB9", text='''Compute''', command=aphelionCompute)
    btnCompute.place(relx=0.64, rely=0.681, height=33, width=136)
    
    btnClear = tk.Button(mainCanvas, background="#F7BAB9", text='''Clear Fields''', command=clrscr)
    btnClear.place(relx=0.64, rely=0.789, height=33, width=136)
    
    window.mainloop()   
    
def aphelionCompute():  
    a =AphelionA.get()
    e =AphelionE.get()
    fe =AphelionFE.get()
    se =AphelionSE.get()
    
    semimajor = a * pow(10, fe)
    eccentricity = e * pow(10, se)

    result = semimajor * (1 - eccentricity)
    AphelionResult.set(str(result) + ' AU')   
  
def telescopeOptionsGUI():
    clrscr()
    root.withdraw()
    window = Toplevel()
    window.deiconify()
    window.geometry("785x583+389+50")
    window.resizable(0, 0)
    window.title("Telescope Related Properties")
 
    mainCanvas = tk.Frame(window, background="#CAEAE5")
    mainCanvas.place(relx=0.015, rely=0.021, relheight=0.957, relwidth=0.973)

    lblTitle = tk.Label(mainCanvas, background="#CAEAE5", text='''Telescope Related Options''', font = "-size 14 -weight bold")
    lblTitle.place(relx=0.222, rely=0.054, height=44, width=409)

    btnBack = tk.Button(mainCanvas, background="#F7BAB9", text ='''Back''', command =lambda:[window.withdraw(), root.deiconify()])
    btnBack.place(relx=0.039, rely=0.054, height=37, width=80)

    btnOption1 = tk.Button(mainCanvas, background="#F7BAB9", text='''Magnification''', command=magnificationGUI)
    btnOption1.place(relx=0.326, rely=0.305, height=53, width=266)

    btnOption2 = tk.Button(mainCanvas, background="#F7BAB9", text='''Resolution''', command=resolutionGUI)
    btnOption2.place(relx=0.326, rely=0.448, height=53, width=266)
    
    btnOption3 = tk.Button(mainCanvas, background="#F7BAB9", text='''Limiting Magnitude''', command=limMagnitudeGUI)
    btnOption3.place(relx=0.326, rely=0.591, height=53, width=266)
    
    window.mainloop()
  
# do not copy this
def magnificationGUI():
    clrscr()
    window = Toplevel()
    window.deiconify()
    window.geometry("785x583+389+50")
    window.resizable(0, 0)
    window.title("Magnification")
 
    mainCanvas = tk.Frame(window, background="#CAEAE5")
    mainCanvas.place(relx=0.015, rely=0.021, relheight=0.957, relwidth=0.973)
    
    lblTitle = tk.Label(mainCanvas, background="#CAEAE5", text='''Magnification''', font = "-size 14 -weight bold")
    lblTitle.place(relx=0.222, rely=0.054, height=44, width=409)
    
    btnBack = tk.Button(mainCanvas, background="#F7BAB9", text ='''Back''', command =window.withdraw)
    btnBack.place(relx=0.039, rely=0.054, height=37, width=80)
    
    #picture
    pic = PhotoImage(file='pictures/magnification.png')
    lblGuide = tk.Label(mainCanvas, background="#CAEAE5", image=pic)
    lblGuide.place(relx=0.014, rely=0.168, height=215, width=738)

    lblFirstInput = tk.Label(mainCanvas, background="#CAEAE5", text='''Focal length in cm =''', font = "-size 11")
    lblFirstInput.place(relx=0.092, rely=0.609, height=26, width=262)
    
    inpFirstInput = tk.Entry(mainCanvas, justify= 'center', textvariable= MagnificationFL)
    inpFirstInput.place(relx=0.092, rely=0.663,height=34, relwidth=0.343)
    
    lblSecondInput = tk.Label(mainCanvas, background="#CAEAE5", text='''Eyepiece Diameter in cm =''', font = "-size 11")
    lblSecondInput.place(relx=0.092, rely=0.735, height=26, width=262)
    
    inpSecondInput = tk.Entry(mainCanvas, justify= 'center', textvariable=MagnificationED)
    inpSecondInput.place(relx=0.092, rely=0.789,height=34, relwidth=0.343)
    
    lblResult = tk.Label(mainCanvas, background="#CAEAE5", text='''Result =''', font = "-size 11")
    lblResult.place(relx=0.092, rely=0.86, height=34, width=262)
    
    lblResultTwo = tk.Label(mainCanvas, textvariable=MagnificationResult)
    lblResultTwo.place(relx=0.092, rely=0.914, height=34, width=262)
    
    btnCompute = tk.Button(mainCanvas, background="#F7BAB9", text='''Compute''', command=magnificationCompute)
    btnCompute.place(relx=0.615, rely=0.663, height=33, width=136)
    
    btnClear = tk.Button(mainCanvas, background="#F7BAB9", text='''Clear Fields''', command=clrscr)
    btnClear.place(relx=0.615, rely=0.789, height=33, width=136)
    
    window.mainloop()   
    
def magnificationCompute():  
    fl =MagnificationFL.get()
    ed =MagnificationED.get()
    result = fl / ed
    MagnificationResult.set(str(result) + ' sec') 
     
def resolutionGUI():
    clrscr()
    window = Toplevel()
    window.deiconify()
    window.geometry("785x583+389+50")
    window.resizable(0, 0)
    window.title("Resolution")
 
    mainCanvas = tk.Frame(window, background="#CAEAE5")
    mainCanvas.place(relx=0.015, rely=0.021, relheight=0.957, relwidth=0.973)
    
    lblTitle = tk.Label(mainCanvas, background="#CAEAE5", text='''Resolution''', font = "-size 14 -weight bold")
    lblTitle.place(relx=0.222, rely=0.054, height=44, width=409)
    
    btnBack = tk.Button(mainCanvas, background="#F7BAB9", text ='''Back''', command =window.withdraw)
    btnBack.place(relx=0.039, rely=0.054, height=37, width=80)
    
    #picture
    pic = PhotoImage(file='pictures/resolution.png')
    lblGuide = tk.Label(mainCanvas, background="#CAEAE5", image=pic)
    lblGuide.place(relx=0.014, rely=0.168, height=215, width=738)

    lblFirstInput = tk.Label(mainCanvas, background="#CAEAE5", text='''D in mm''', font = "-size 10")
    lblFirstInput.place(relx=0.144, rely=0.681, height=26, width=52)
    
    inpFirstInput = tk.Entry(mainCanvas, justify= 'center', textvariable= ResolutionD)
    inpFirstInput.place(relx=0.209, rely=0.681, height=34, relwidth=0.267)
    
    lblResult = tk.Label(mainCanvas, background="#CAEAE5", text='''Result =''')
    lblResult.place(relx=0.144, rely=0.771, height=36, width=62)
    
    lblResultTwo = tk.Label(mainCanvas, textvariable=ResolutionResult)
    lblResultTwo.place(relx=0.209, rely=0.771, height=34, width=204)
    
    btnCompute = tk.Button(mainCanvas, background="#F7BAB9", text='''Compute''', command=resolutionCompute)
    btnCompute.place(relx=0.615, rely=0.681, height=33, width=136)
    
    btnClear = tk.Button(mainCanvas, background="#F7BAB9", text='''Clear Fields''', command=clrscr)
    btnClear.place(relx=0.615, rely=0.771, height=33, width=136)
    
    window.mainloop()   
    
def resolutionCompute():  
    d =ResolutionD.get()
    result = 116/d
    ResolutionResult.set(result)   
    
def limMagnitudeGUI():
    clrscr()
    window = Toplevel()
    window.deiconify()
    window.geometry("785x583+389+50")
    window.resizable(0, 0)
    window.title("Limiting Magnitude")
 
    mainCanvas = tk.Frame(window, background="#CAEAE5")
    mainCanvas.place(relx=0.015, rely=0.021, relheight=0.957, relwidth=0.973)
    
    lblTitle = tk.Label(mainCanvas, background="#CAEAE5", text='''Limiting Magnitude''', font = "-size 14 -weight bold")
    lblTitle.place(relx=0.222, rely=0.054, height=44, width=409)
    
    btnBack = tk.Button(mainCanvas, background="#F7BAB9", text ='''Back''', command =window.withdraw)
    btnBack.place(relx=0.039, rely=0.054, height=37, width=80)
    
    #picture
    pic = PhotoImage(file='pictures/limitingMagnitude.png')
    lblGuide = tk.Label(mainCanvas, background="#CAEAE5", image=pic)
    lblGuide.place(relx=0.014, rely=0.168, height=215, width=738)

    lblFirstInput = tk.Label(mainCanvas, background="#CAEAE5", text='''D =''', font = "-size 11")
    lblFirstInput.place(relx=0.144, rely=0.681, height=26, width=52)
    
    inpFirstInput = tk.Entry(mainCanvas, justify= 'center', textvariable= limMagnitudeD)
    inpFirstInput.place(relx=0.209, rely=0.681, height=34, relwidth=0.267)
    
    lblResult = tk.Label(mainCanvas, background="#CAEAE5", text='''Result =''')
    lblResult.place(relx=0.144, rely=0.771, height=36, width=62)
    
    lblResultTwo = tk.Label(mainCanvas, textvariable=limMagnitudeResult)
    lblResultTwo.place(relx=0.209, rely=0.771, height=34, width=204)
    
    btnCompute = tk.Button(mainCanvas, background="#F7BAB9", text='''Compute''', command=limMagnitudeCompute)
    btnCompute.place(relx=0.615, rely=0.681, height=33, width=136)
    
    btnClear = tk.Button(mainCanvas, background="#F7BAB9", text='''Clear Fields''', command=clrscr)
    btnClear.place(relx=0.615, rely=0.771, height=33, width=136)
    
    window.mainloop()   
    
def limMagnitudeCompute():  
    d =limMagnitudeD.get()
    result = 2.7 + 5 *  math.log(d, 10)
    limMagnitudeResult.set(result)   
       
def KineticEnergyOptionGUI():
    clrscr()
    window = Toplevel()
    window.deiconify()
    window.geometry("785x583+389+50")
    window.resizable(0, 0)
    window.title("Kinetic Energy Options")
 
    mainCanvas = tk.Frame(window, background="#CAEAE5")
    mainCanvas.place(relx=0.015, rely=0.021, relheight=0.957, relwidth=0.973)
    
    lblTitle = tk.Label(mainCanvas, background="#CAEAE5", text='''Kinetic Energy Options''', font = "-size 14 -weight bold")
    lblTitle.place(relx=0.222, rely=0.054, height=44, width=409)
    
    btnBack = tk.Button(mainCanvas, background="#F7BAB9", text ='''Back''', command=window.withdraw)
    btnBack.place(relx=0.039, rely=0.054, height=37, width=80)
        
    btnOption1 = tk.Button(mainCanvas, background="#F7BAB9", text='''Kinetic energy of an object''', command=KineticEnergyObjGUI)
    btnOption1.place(relx=0.321, rely=0.411, height=53, width=266)

    btnOption2 = tk.Button(mainCanvas, background="#F7BAB9", text='''Kinetic energy of an atom''', command=KineticEnergyAtomGUI)
    btnOption2.place(relx=0.321, rely=0.554, height=53, width=266)
    
    window.mainloop()
    
def KineticEnergyObjGUI():
    clrscr()
    window = Toplevel()
    window.deiconify()
    window.geometry("785x583+389+50")
    window.resizable(0, 0)
    window.title("Kinetic energy of an object")
 
    mainCanvas = tk.Frame(window, background="#CAEAE5")
    mainCanvas.place(relx=0.015, rely=0.021, relheight=0.957, relwidth=0.973)
    
    lblTitle = tk.Label(mainCanvas, background="#CAEAE5", text='''Kinetic energy of an object''', font = "-size 14 -weight bold")
    lblTitle.place(relx=0.222, rely=0.054, height=44, width=409)
    
    btnBack = tk.Button(mainCanvas, background="#F7BAB9", text ='''Back''', command =window.withdraw)
    btnBack.place(relx=0.039, rely=0.054, height=37, width=80)
    
    #picture
    pic = PhotoImage(file='pictures/KEObject.png')
    lblGuide = tk.Label(mainCanvas, background="#CAEAE5", image=pic)
    lblGuide.place(relx=0.014, rely=0.168, height=215, width=738)

    lblFirstInput = tk.Label(mainCanvas, background="#CAEAE5", text='''m =''', font = "-size 11")
    lblFirstInput.place(relx=0.117, rely=0.681, height=26, width=72)
    
    inpFirstInput = tk.Entry(mainCanvas, justify= 'center', textvariable= KEObjectM)
    inpFirstInput.place(relx=0.209, rely=0.681, height=34, relwidth=0.175)
    
    lblExponent = tk.Label(mainCanvas, background="#CAEAE5", text='''x 10''')
    lblExponent.place(relx=0.392, rely=0.699, height=26, width=42)

    inpExponent = tk.Entry(mainCanvas, justify='center', textvariable=KEObjectFE)
    inpExponent.place(relx=0.444, rely=0.681,height=34, relwidth=0.07)

    lblFirstType = tk.Label(mainCanvas, background="#CAEAE5", text='''in kg''')
    lblFirstType.place(relx=0.522, rely=0.699, height=29, width=50)
    
    #######
    lblSecondInput = tk.Label(mainCanvas, background="#CAEAE5", text='''v =''', font = "-size 11")
    lblSecondInput.place(relx=0.117, rely=0.789, height=26, width=72)
    
    inpSecondInput = tk.Entry(mainCanvas, justify= 'center', textvariable=KEObjectV)
    inpSecondInput.place(relx=0.209, rely=0.789, height=34, relwidth=0.175)
    
    lblSecondExponent = tk.Label(mainCanvas, background="#CAEAE5", text='''x 10''')
    lblSecondExponent.place(relx=0.392, rely=0.806, height=26, width=42)

    inpSecondExponent = tk.Entry(mainCanvas, justify='center', textvariable=KEObjectSE)
    inpSecondExponent.place(relx=0.444, rely=0.789, height=34, relwidth=0.07)

    lblSecondType = tk.Label(mainCanvas, background="#CAEAE5", text='''in m/sec''')
    lblSecondType.place(relx=0.522, rely=0.806, height=29, width=50)
    
    ######
    lblResult = tk.Label(mainCanvas, background="#CAEAE5", text='''Result =''')
    lblResult.place(relx=0.117, rely=0.878, height=36, width=72)
    
    lblResultTwo = tk.Label(mainCanvas, textvariable=KEObjectResult)
    lblResultTwo.place(relx=0.209, rely=0.878, height=34, width=275)
    
    btnCompute = tk.Button(mainCanvas, background="#F7BAB9", text='''Compute''', command=kEObjectCompute)
    btnCompute.place(relx=0.64, rely=0.681, height=33, width=136)
    
    btnClear = tk.Button(mainCanvas, background="#F7BAB9", text='''Clear Fields''', command=clrscr)
    btnClear.place(relx=0.64, rely=0.789, height=33, width=136)
    
    window.mainloop()   
    
def kEObjectCompute():  
    m =KEObjectM.get()
    v =KEObjectV.get()
    fe =KEObjectFE.get()
    se =KEObjectSE.get()
    
    mass = m * pow(10, fe)
    velocity = v * pow(10, se)

    result = 1/2*(mass*pow(velocity, 2))
    KEObjectResult.set(str(result) + ' joules')   
      
def KineticEnergyAtomGUI():
    clrscr()
    window = Toplevel()
    window.deiconify()
    window.geometry("785x583+389+50")
    window.resizable(0, 0)
    window.title("Kinetic energy of an atom")
 
    mainCanvas = tk.Frame(window, background="#CAEAE5")
    mainCanvas.place(relx=0.015, rely=0.021, relheight=0.957, relwidth=0.973)
    
    lblTitle = tk.Label(mainCanvas, background="#CAEAE5", text='''Kinetic energy of an atom''', font = "-size 14 -weight bold")
    lblTitle.place(relx=0.222, rely=0.054, height=44, width=409)
    
    btnBack = tk.Button(mainCanvas, background="#F7BAB9", text ='''Back''', command =window.withdraw)
    btnBack.place(relx=0.039, rely=0.054, height=37, width=80)
    
    #picture
    pic = PhotoImage(file='pictures/KEAtom.png')
    lblGuide = tk.Label(mainCanvas, background="#CAEAE5", image=pic)
    lblGuide.place(relx=0.014, rely=0.168, height=215, width=738)

    lblFirstInput = tk.Label(mainCanvas, background="#CAEAE5", text='''T =''', font = "-size 11")
    lblFirstInput.place(relx=0.117, rely=0.681, height=26, width=72)
    
    inpFirstInput = tk.Entry(mainCanvas, justify= 'center', textvariable= KEAtomT)
    inpFirstInput.place(relx=0.209, rely=0.681, height=34, relwidth=0.175)
    
    lblExponent = tk.Label(mainCanvas, background="#CAEAE5", text='''x 10''')
    lblExponent.place(relx=0.392, rely=0.699, height=26, width=42)

    inpExponent = tk.Entry(mainCanvas, justify='center', textvariable=KEAtomFE)
    inpExponent.place(relx=0.444, rely=0.681,height=34, relwidth=0.07)

    lblFirstType = tk.Label(mainCanvas, background="#CAEAE5", text='''in K''')
    lblFirstType.place(relx=0.522, rely=0.699, height=29, width=50)
    
    #######
    lblResult = tk.Label(mainCanvas, background="#CAEAE5", text='''Result =''')
    lblResult.place(relx=0.117, rely=0.789, height=37, width=72)
    
    lblResultTwo = tk.Label(mainCanvas, textvariable=KEAtomResult)
    lblResultTwo.place(relx=0.209, rely=0.789, height=34, width=275)
    
    btnCompute = tk.Button(mainCanvas, background="#F7BAB9", text='''Compute''', command=KEAtomCompute)
    btnCompute.place(relx=0.64, rely=0.681, height=33, width=136)
    
    btnClear = tk.Button(mainCanvas, background="#F7BAB9", text='''Clear Fields''', command=clrscr)
    btnClear.place(relx=0.64, rely=0.789, height=33, width=136)
    
    btnAdditional = tk.Button(mainCanvas, background="#FF6961", text='''Additional''', command=KineticEnergyAtomBonusGUI)
    btnAdditional.place(relx=0.640, rely=0.878, height=33, width=136)
    
    window.mainloop()   
    
def KEAtomCompute():  
    t =KEAtomT.get()
    fe =KEAtomFE.get()
    
    temperature = t * pow(10, fe)
    k = 1.38
    
    result = 3/2 * (k * temperature)
    KEAtomResult.set(str(result) + ' joules')        
      
def KineticEnergyAtomBonusGUI():
    clrscr()
    window = Toplevel()
    window.deiconify()
    window.geometry("785x583+389+50")
    window.resizable(0, 0)
    window.title("Kinetic energy of an atom (velocity)")
 
    mainCanvas = tk.Frame(window, background="#CAEAE5")
    mainCanvas.place(relx=0.015, rely=0.021, relheight=0.957, relwidth=0.973)
    
    lblTitle = tk.Label(mainCanvas, background="#CAEAE5", text='''Kinetic energy of an atom (velocity)''', font = "-size 14 -weight bold")
    lblTitle.place(relx=0.222, rely=0.054, height=44, width=409)
    
    btnBack = tk.Button(mainCanvas, background="#F7BAB9", text ='''Back''', command =window.withdraw)
    btnBack.place(relx=0.039, rely=0.054, height=37, width=80)
    
    #picture
    pic = PhotoImage(file='pictures/KEAtomBonus.png')
    lblGuide = tk.Label(mainCanvas, background="#CAEAE5", image=pic)
    lblGuide.place(relx=0.014, rely=0.168, height=215, width=738)

    lblFirstInput = tk.Label(mainCanvas, background="#CAEAE5", text='''m =''', font = "-size 11")
    lblFirstInput.place(relx=0.117, rely=0.681, height=26, width=72)
    
    inpFirstInput = tk.Entry(mainCanvas, justify= 'center', textvariable= KEAtomBonusM)
    inpFirstInput.place(relx=0.209, rely=0.681, height=34, relwidth=0.175)
    
    lblExponent = tk.Label(mainCanvas, background="#CAEAE5", text='''x 10''')
    lblExponent.place(relx=0.392, rely=0.699, height=26, width=42)

    inpExponent = tk.Entry(mainCanvas, justify='center', textvariable=KEAtomBonusFE)
    inpExponent.place(relx=0.444, rely=0.681,height=34, relwidth=0.07)

    lblFirstType = tk.Label(mainCanvas, background="#CAEAE5", text='''in kg''')
    lblFirstType.place(relx=0.522, rely=0.699, height=29, width=50)
    
    ######
    lblSecondInput = tk.Label(mainCanvas, background="#CAEAE5", text='''T =''', font = "-size 11")
    lblSecondInput.place(relx=0.117, rely=0.789, height=26, width=72)
    
    inpSecondInput = tk.Entry(mainCanvas, justify= 'center', textvariable=KEAtomBonusT)
    inpSecondInput.place(relx=0.209, rely=0.789, height=34, relwidth=0.175)
    
    lblSecondExponent = tk.Label(mainCanvas, background="#CAEAE5", text='''x 10''')
    lblSecondExponent.place(relx=0.392, rely=0.806, height=26, width=42)

    inpSecondExponent = tk.Entry(mainCanvas, justify='center', textvariable=KEAtomBonusSE)
    inpSecondExponent.place(relx=0.444, rely=0.789, height=34, relwidth=0.07)

    lblSecondType = tk.Label(mainCanvas, background="#CAEAE5", text='''in K''')
    lblSecondType.place(relx=0.522, rely=0.806, height=29, width=50)
    
    ######
    lblResult = tk.Label(mainCanvas, background="#CAEAE5", text='''Result =''')
    lblResult.place(relx=0.117, rely=0.878, height=36, width=72)
    
    lblResultTwo = tk.Label(mainCanvas, textvariable=KEAtomBonusResult)
    lblResultTwo.place(relx=0.209, rely=0.878, height=34, width=275)
    
    btnCompute = tk.Button(mainCanvas, background="#F7BAB9", text='''Compute''', command=kEAtomBonusCompute)
    btnCompute.place(relx=0.64, rely=0.681, height=33, width=136)
    
    btnClear = tk.Button(mainCanvas, background="#F7BAB9", text='''Clear Fields''', command=clrscr)
    btnClear.place(relx=0.64, rely=0.789, height=33, width=136)
    
    window.mainloop()   
    
def kEAtomBonusCompute():  
    m =KEAtomBonusM.get()
    t =KEAtomBonusT.get()
    fe =KEAtomBonusFE.get()
    se =KEAtomBonusSE.get()
    
    mass = m * pow(10, fe)
    temperature = t *pow(10, se)
    k = 1.38
    first = 3 * (k * temperature)
    numerator = math.sqrt(first)
    
    result = numerator / mass
    KEAtomBonusResult.set(str(result) + ' m/sec')   
        
def clrscr():
    hubbleLawResult.set('')
    hubbleLawV.set('')
    EscapeVelocityR.set('')
    EscapeVelocityM.set('')
    EscapeVelocityResult.set('')
    RelativityTimeT.set('')
    RelativityTimeV.set('')
    RelativityTimeResult.set('')
    RelativityLengthL.set('')
    RelativityLengthV.set('')
    RelativityLengthResult.set('')
    KeplerGA.set('')
    KeplerGMOne.set('')
    KeplerGMTwo.set('')
    KeplerGResult.set('')
    KeplerA.set('')
    KeplerResult.set('')
    PlanckFV.set('')
    PlanckFResult.set('')
    PlanckWV.set('')
    PlanckWResult.set('')
    BrightnessL.set('')
    BrightnessD.set('')
    BrightnessResult.set('')
    SurfaceTempL.set('')
    SurfaceTempR.set('')
    SurfaceTempResult.set('')
    LuminosityAPB.set('')
    LuminosityAPD.set('')
    LuminosityAPResult.set('')
    LuminositySTResult.set('')
    LuminositySTT.set('')
    LuminositySTR.set('')
    Eccentricityq.set('')
    EccentricityQ.set('')
    EccentricityResult.set('')
    PerihilionA.set('')
    PerihilionE.set('')
    PerihilionResult.set('')
    AphelionA.set('')
    AphelionE.set('')
    AphelionResult.set('')
    MagnificationFL.set('')
    MagnificationED.set('')
    MagnificationResult.set('')
    ResolutionD.set('')
    ResolutionResult.set('')
    limMagnitudeD.set('')
    limMagnitudeResult.set('')
    KEObjectM.set('')
    KEObjectV.set('')
    KEObjectResult.set('')
    KEAtomK.set('')
    KEAtomT.set('')
    KEAtomResult.set('')
    KEAtomBonusM.set('')
    KEAtomBonusT.set('')
    KEAtomBonusResult.set('')
    SRadiusM.set('')
    SRadiusResult.set('')
    SRadiusExponent.set(0)
    EscapeVelocityExponent.set(0)
    EscapeVelocitySecondExponent.set(0)
    KeplerGFirstExponent.set(0)
    KeplerGSecondExponent.set(0)
    KeplerGThirdExponent.set(0)
    hubbleExponent.set(0)
    KeplerExponent.set(0)
    RelativityTimeFE.set(0)
    RelativityTimeSE.set(0)
    RelativityLengthFE.set(0)
    RelativityLengthSE.set(0)
    PlanckFFE.set(0)
    PlanckWFE.set(0)
    BrightnessFE.set(0)
    BrightnessSE.set(0)
    SurfaceTempFE.set(0)
    SurfaceTempSE.set(0)
    LuminosityAPFE.set(0)
    LuminosityAPSE.set(0)
    LuminositySTFE.set(0)
    LuminositySTSE.set(0)
    EccentricityFE.set(0)
    EccentricitySE.set(0)
    PerihilionFE.set(0)
    PerihilionSE.set(0)
    AphelionFE.set(0)
    AphelionSE.set(0)
    KEObjectFE.set(0)
    KEObjectSE.set(0)
    KEAtomFE.set(0)
    KEAtomSE.set(0)
    KEAtomBonusFE.set(0)
    KEAtomBonusSE.set(0)

if __name__ == "__main__":
    #home screen GUI
    root = Tk()
    root.geometry("772x632+389+50")
    root.resizable(0, 0)
    root.title("Capsule")
    
    #string variables to be manipulated
    hubbleLawResult = StringVar()
    hubbleLawV = DoubleVar()
    EscapeVelocityR = DoubleVar()
    EscapeVelocityM = DoubleVar()
    EscapeVelocityResult = StringVar()
    RelativityTimeT = DoubleVar()
    RelativityTimeV = DoubleVar()
    RelativityTimeResult = StringVar()
    RelativityLengthL = DoubleVar()
    RelativityLengthV = DoubleVar()
    RelativityLengthResult = StringVar()
    KeplerGA = DoubleVar()
    KeplerGMOne = DoubleVar()
    KeplerGMTwo = DoubleVar()
    KeplerGResult = StringVar()
    KeplerA = DoubleVar()
    KeplerResult = DoubleVar()
    PlanckFV = DoubleVar()
    PlanckFResult = StringVar()
    PlanckWV = DoubleVar()
    PlanckWResult = StringVar()
    BrightnessL = DoubleVar()
    BrightnessD = DoubleVar()
    BrightnessResult = StringVar()
    SurfaceTempL = DoubleVar()
    SurfaceTempR = DoubleVar()
    SurfaceTempResult = StringVar()
    LuminosityAPB = DoubleVar()
    LuminosityAPD = DoubleVar()
    LuminosityAPResult = StringVar()
    LuminositySTResult = StringVar()
    LuminositySTT = DoubleVar()
    LuminositySTR = DoubleVar()
    Eccentricityq = DoubleVar()
    EccentricityQ = DoubleVar()
    EccentricityResult = StringVar()
    PerihilionA = DoubleVar()
    PerihilionE = DoubleVar()
    PerihilionResult = StringVar()
    AphelionA = DoubleVar()
    AphelionE = DoubleVar()
    AphelionResult = StringVar()
    MagnificationFL = DoubleVar()
    MagnificationED = DoubleVar()
    MagnificationResult = StringVar()
    ResolutionD = DoubleVar()
    ResolutionResult = StringVar()
    limMagnitudeD = DoubleVar()
    limMagnitudeResult = StringVar()
    KEObjectM = DoubleVar()
    KEObjectV = DoubleVar()
    KEObjectResult = StringVar()
    KEAtomK = DoubleVar()
    KEAtomT = DoubleVar()
    KEAtomResult = StringVar()
    KEAtomBonusM = DoubleVar()
    KEAtomBonusT = DoubleVar()
    KEAtomBonusResult = StringVar()
    SRadiusM = DoubleVar()
    SRadiusResult = StringVar()
    SRadiusExponent = DoubleVar()
    EscapeVelocityExponent = DoubleVar()
    EscapeVelocitySecondExponent = DoubleVar()
    KeplerGFirstExponent = DoubleVar()
    KeplerGSecondExponent = DoubleVar()
    KeplerGThirdExponent = DoubleVar()
    hubbleExponent = DoubleVar()
    KeplerExponent = DoubleVar()
    RelativityTimeFE = DoubleVar()
    RelativityTimeSE = DoubleVar()
    RelativityLengthFE = DoubleVar()
    RelativityLengthSE = DoubleVar()
    PlanckFFE = DoubleVar()
    PlanckWFE = DoubleVar()
    BrightnessFE = DoubleVar()
    BrightnessSE = DoubleVar()
    SurfaceTempFE = DoubleVar()
    SurfaceTempSE = DoubleVar()
    LuminosityAPFE = DoubleVar()
    LuminosityAPSE = DoubleVar()
    LuminositySTFE = DoubleVar()
    LuminositySTSE = DoubleVar()
    EccentricityFE = DoubleVar()
    EccentricitySE = DoubleVar()
    PerihilionFE = DoubleVar()
    PerihilionSE = DoubleVar()
    AphelionFE = DoubleVar()
    AphelionSE = DoubleVar()
    KEObjectFE = DoubleVar()
    KEObjectSE = DoubleVar()
    KEAtomFE = DoubleVar()
    KEAtomSE = DoubleVar()
    KEAtomBonusFE = DoubleVar()
    KEAtomBonusSE = DoubleVar()


    mainCanvas = tk.Frame(root, background="#CAEAE5")
    mainCanvas.place(relx=0.013, rely=0.016, relheight=0.97, relwidth=0.975)

    #Welcome labels
    lblWelcome = tk.Label(mainCanvas, background="#CAEAE5", foreground="#000000", text='''WELCOME TO CoMPiS!''', font = "-size 14 -weight bold")
    lblWelcome.place(relx=0.013, rely=0.082, height=46, width=732)


    lblGreeting1 = tk.Label(mainCanvas, background="#CAEAE5", foreground="#000000",text='''Computational Methods for Physics in Space''', font = "-size 11")
    lblGreeting1.place(relx=0.013, rely=0.147, height=46, width=732)

    lblGreeting2 = tk.Label(mainCanvas, background="#CAEAE5", foreground="#000000", text='''This program will help the user compute Physics formulas used in Space''', font = "-size 11")
    lblGreeting2.place(relx=0.013, rely=0.228, height=26, width=732)

    lblGreeting3 = tk.Label(mainCanvas, background="#CAEAE5", foreground="#000000", text='''Please choose from the formulas below:''', font = "-size 11")
    lblGreeting3.place(relx=0.013, rely=0.31, height=36, width=732)

    #buttons
    btnStellarProperties = tk.Button(mainCanvas, background="#F7BAB9", text='''Stellar Properties''', command=stellarPropertyOptionsGUI)
    btnStellarProperties.place(relx=0.159, rely=0.437, height=33, width=236)

    btnHubblesLaw = tk.Button(mainCanvas, background="#F7BAB9", text='''Hubble's Law''', command=HubbleLawGUI)
    btnHubblesLaw.place(relx=0.159, rely=0.518, height=33, width=236)

    btnEscapeVelocity = tk.Button(mainCanvas,background="#F7BAB9", text='''Escape Velocity''', command=escapeVelocityGUI)
    btnEscapeVelocity.place(relx=0.159, rely=0.60, height=33, width=236)

    btnKineticEnergy = tk.Button(mainCanvas, background="#F7BAB9", text='''Kinetic Energy''', command=KineticEnergyOptionGUI)
    btnKineticEnergy.place(relx=0.159, rely=0.681, height=33, width=236)

    btnKeplersEquation = tk.Button(mainCanvas, background="#F7BAB9", text='''Kepler's Equation (Law of Periods)''', command=keplerOptionsGUI)
    btnKeplersEquation.place(relx=0.159, rely=0.763, height=33, width=236)

    Use_of_Planck_Constant = tk.Button(mainCanvas, background="#F7BAB9", text='''Use of Planck Constant''', command=planckOptionsGUI)
    Use_of_Planck_Constant.place(relx=0.558, rely=0.437, height=33, width=236)

    btnSRadius = tk.Button(mainCanvas, background="#F7BAB9", text='''Schwarzschild Radius''', command=SRadiusGUI)
    btnSRadius.place(relx=0.558, rely=0.518, height=33, width=236)

    btnRelativity = tk.Button(mainCanvas, background="#F7BAB9", text='''Relativity''', command=relativityOptionsGUI)
    btnRelativity.place(relx=0.558, rely=0.60, height=33, width=236)

    btnEccentricity = tk.Button(mainCanvas, background="#F7BAB9", text='''Eccentricity''', command=eccentricityOptionsGUI)
    btnEccentricity.place(relx=0.558, rely=0.681, height=33, width=236)

    btnTelescopeRelated = tk.Button(mainCanvas, background="#F7BAB9", text='''Telescope Related''', command=telescopeOptionsGUI)
    btnTelescopeRelated.place(relx=0.558, rely=0.763, height=33, width=236)

    #for the Constant variables 
    lblPromptConstant = tk.Label(mainCanvas, background="#CAEAE5", foreground="#000000", text='''To check the Constant Variables that Astronomers use click the '*' button at the lower right of the screen.''', font= "-size 10" )
    lblPromptConstant.place(relx=0.013, rely=0.865, height=26, width=732)
    btnConstants = tk.Button(mainCanvas, background="#F7BAB9", text='''*''', command=constantFormulasGUI)   
    btnConstants.place(relx=0.93, rely=0.93, height=33, width=46)

    root.mainloop()
    
    
