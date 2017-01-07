def graficar(xs, ys, tam=(9, 6), tls=True):
    #%matplotlib notebook
    from matplotlib.pyplot import figure
    from matplotlib import rc
    #rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
    ## for Palatino and other serif fonts use:
    rc('font',**{'family':'serif','serif':['Palatino'], 'size':14.0})
    #rc('font', **{'family':'cursive', 'cursive':['Zapf Chancery'], 'size':14.0})
    #rc('font', **{'family':'fantasy', 'fantasy':['Humor Sans'], 'size':14.0})
    rc('text', usetex=True)
    
    fig = figure(figsize=tam)
    ax = fig.gca()

    #ax.axes.get_xaxis().set_visible(False)
    #ax.axes.get_yaxis().set_visible(False)

    ax.axes.spines["top"].set_color("none")
    ax.axes.spines["right"].set_color("none")
    ax.tick_params(top="off", right="off")

    ax.axes.spines["left"].set_position("zero")
    ax.axes.spines["bottom"].set_position("zero")
    ax.spines["left"].set_linewidth(2)
    ax.spines["bottom"].set_linewidth(2)

    ax.plot(xs, ys, 'k')
    ax.axes.set_xlim(-0.1, max(xs) + 0.1)
    ax.axes.set_ylim(min(ys)-0.1, max(ys)+0.1)
    fig.canvas.draw()
    
    if tls == False:
        ax.axes.get_xaxis().set_ticks([])
        ax.axes.get_yaxis().set_ticks([])

    labels = ax.xaxis.get_ticklabels()
    #ticklabels[0].set_visible(False)
    for label in labels:
        if label.get_text() == r'$0$' or label.get_text() == r'$0.0$':
            label.set_visible(False)

    labels = ax.yaxis.get_ticklabels()
    #ticklabels[0].set_visible(False)
    for label in labels:
        if label.get_text() == r'$0$' or label.get_text() == r'$0.0$':
            label.set_visible(False)
            
    return ax