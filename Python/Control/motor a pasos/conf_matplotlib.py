def conf_matplotlib_oscuro():
    from matplotlib.pyplot import style, rcParams

    style.use("dark_background")

    rcParams["figure.facecolor"] = (43/256, 43/256, 43/256)
    rcParams["axes.facecolor"]   = (43/256, 43/256, 43/256)
    rcParams["legend.facecolor"] = (43/256, 43/256, 43/256)
    
    rcParams["legend.edgecolor"] = (43*4/256, 43*4/256, 43*4/256, 0.5)
    rcParams["axes.edgecolor"]   = (43*3/256, 43*3/256, 43*3/256, 0.5)
    
    rcParams["axes.grid"]        = True
    
    rcParams["grid.color"]       = (43*4/256, 43*4/256, 43*4/256, 0.5)
    
    rcParams["xtick.color"]      = (43*4/256, 43*4/256, 43*4/256, 0.8)
    rcParams["ytick.color"]      = (43*4/256, 43*4/256, 43*4/256, 0.8)
    
    rcParams["lines.linewidth"]  = 5
    rcParams["grid.linewidth"]   = 0.5

def conf_matplotlib_horizon():
    from matplotlib.pyplot import style, rcParams
    
    c_fondo = (36/256, 36/256, 48/256)
    c_texto = (149/256, 153/256, 166/256)

    style.use("dark_background")

    rcParams["figure.facecolor"] = c_fondo
    rcParams["axes.facecolor"]   = c_fondo
    rcParams["legend.facecolor"] = c_fondo
    
    rcParams["legend.edgecolor"] = c_texto
    rcParams["axes.edgecolor"]   = c_texto
    
    rcParams["axes.grid"]        = True
    
    rcParams["grid.color"]       = c_texto
    
    rcParams["xtick.color"]      = c_texto
    rcParams["ytick.color"]      = c_texto
    
    rcParams["lines.linewidth"]  = 5
    rcParams["grid.linewidth"]   = 0.5
    
def conf_matplotlib_claro():
    from matplotlib.pyplot import style, rcParams

    style.use("ggplot")

    #rcParams["figure.facecolor"] = (43/256, 43/256, 43/256)
    #rcParams["axes.facecolor"]   = (43/256, 43/256, 43/256)
    #rcParams["legend.facecolor"] = (43/256, 43/256, 43/256)
    
    #rcParams["legend.edgecolor"] = (43*4/256, 43*4/256, 43*4/256, 0.5)
    #rcParams["axes.edgecolor"]   = (43*3/256, 43*3/256, 43*3/256, 0.5)
    
    rcParams["axes.grid"]        = True
    
    #rcParams["grid.color"]       = (43*4/256, 43*4/256, 43*4/256, 0.5)
    
    #rcParams["xtick.color"]      = (43*4/256, 43*4/256, 43*4/256, 0.8)
    #rcParams["ytick.color"]      = (43*4/256, 43*4/256, 43*4/256, 0.8)
    
    rcParams["lines.linewidth"]  = 2
    rcParams["grid.linewidth"]   = 1