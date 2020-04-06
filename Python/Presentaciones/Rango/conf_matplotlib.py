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