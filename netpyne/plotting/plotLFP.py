# Generate plots of LFP (local field potentials) and related analyses

import matplotlib.patches as mpatches
from ..analysis.utils import exception #, loadData
from ..analysis.tools import loadData
from .plotter import LinesPlotter
import numpy as np


#@exception
def plotLFPTimeSeries(
    LFPData=None, 
    axis=None, 
    sim=None,
    timeRange=None,
    electrodes=['avg', 'all'], 
    pop=None,
    separation=1.0, 
    logy=False, 
    normSignal=False, 
    filtFreq=False, 
    filtOrder=3, 
    detrend=False, 
    returnPlotter=False,
    colorList=None,
    orderInverse=True,
    legend=True,
    scalebar=True,
    **kwargs):
    

    # If there is no input data, get the data from the NetPyNE sim object
    if LFPData is None:
        if 'sim' not in kwargs:
            from .. import sim
        else:
            sim = kwargs['sim']

        LFPData = sim.analysis.prepareLFP(
            sim=sim,
            timeRange=timeRange,
            electrodes=electrodes, 
            LFPData=LFPData, 
            logy=logy, 
            normSignal=normSignal, 
            filtFreq=filtFreq, 
            filtOrder=filtOrder, 
            detrend=detrend, 
            **kwargs
            )

    print('Plotting LFP time series...')

    # If input is a dictionary, pull the data out of it
    if type(LFPData) == dict:
    
        t = LFPData['t']
        lfps = LFPData['electrodes']['lfps']
        names = LFPData['electrodes']['names']
        locs = LFPData['electrodes']['locs']
        colors = LFPData.get('colors')
        linewidths = LFPData.get('linewidths')
        alphas = LFPData.get('alphas')
        axisArgs = LFPData.get('axisArgs')

    # Set up colors, linewidths, and alphas for the plots
    if not colors:
        if not colorList:
            from .plotter import colorList
        colors = colorList[0:len(lfps)]

    if not linewidths:
        linewidths = [1.0 for lfp in lfps]

    if not alphas:
        alphas = [1.0 for lfp in lfps]

    # Create a dictionary to hold axis inputs
    if not axisArgs:
        axisArgs = {}
        axisArgs['title'] = 'LFP Time Series Plot'
        axisArgs['xlabel'] = 'Time (ms)'
        axisArgs['ylabel'] = 'LFP Signal (uV)'

    # Link colors to traces, make avg plot black, add separation to traces
    plotColors = []
    legendLabels = []
    colorIndex = 0
    offset = np.absolute(lfps).max() * separation

    for index, (name, lfp) in enumerate(zip(names, lfps)):
        legendLabels.append(name)
        lfps[index] = index * offset + lfp
        if orderInverse:
            lfps[index] = index * offset - lfp
            axisArgs['invert_yaxis'] = True
        else:
            lfps[index] = index * offset + lfp
        if name == 'avg':
            plotColors.append('black')
        else:
            plotColors.append(colors[colorIndex])
            colorIndex += 1

    # Create a dictionary with the inputs for a line plot
    linesData = {}
    linesData['x'] = t
    linesData['y'] = lfps
    linesData['colors'] = plotColors
    linesData['markers'] = None
    linesData['markersizes'] = None
    linesData['linewidths'] = linewidths
    linesData['alphas'] = alphas
    linesData['label'] = legendLabels

    # If a kwarg matches a lines input key, use the kwarg value instead of the default
    for kwarg in kwargs:
        if kwarg in linesData:
            linesData[kwarg] = kwargs[kwarg]

    # create Plotter object
    linesPlotter = LinesPlotter(data=linesData, axis=axis, **axisArgs, **kwargs)
    linesPlotter.type = 'LFPTimeSeries'

    # remove the y-axis
    # linesPlotter.axis.get_yaxis().set_ticks([])
    # linesPlotter.axis.spines['top'].set_visible(False)
    # linesPlotter.axis.spines['right'].set_visible(False)
    # linesPlotter.axis.spines['left'].set_visible(False)

    # Set up the default legend settings
    legendKwargs = {}
    legendKwargs['title'] = 'Electrodes'
    #legendKwargs['bbox_to_anchor'] = (1.025, 1)
    #legendKwargs['loc'] = 2
    #legendKwargs['borderaxespad'] = 0.0
    #legendKwargs['handlelength'] = 0.5
    legendKwargs['fontsize'] = 'small'
    legendKwargs['title_fontsize'] = 'small'

    # If 'legendKwargs' is found in kwargs, use those values instead of the defaults
    if 'legendKwargs' in kwargs:
        legendKwargs_input = kwargs['legendKwargs']
        kwargs.pop('legendKwargs')
        for key, value in legendKwargs_input:
            if key in legendKwargs:
                legendKwargs[key] = value
    
    # add the legend
    if legend:
        axisArgs['legend'] = legendKwargs

    # add the scalebar
    if scalebar:
        axisArgs['scalebar'] = True

    # Generate the figure
    LFPTimeSeriesPlot = linesPlotter.plot(**axisArgs, **kwargs)

    # Default is to return the figure, but you can also return the plotter
    if returnPlotter:
        return linesPlotter
    else:
        return LFPTimeSeriesPlot




#@exception
def plotPSD(
    PSDData=None,
    sim=None,
    axis=None, 
    timeRange=None,
    electrodes=['avg', 'all'],
    pop=None, 
    separation=1.0,
    NFFT=256,
    noverlap=128, 
    nperseg=256,
    minFreq=1, 
    maxFreq=100, 
    stepFreq=1, 
    smooth=0,
    logx=False,
    logy=False, 
    normSignal=False,
    normPSD=False, 
    filtFreq=False, 
    filtOrder=3, 
    detrend=False, 
    transformMethod='morlet',
    returnPlotter=False,
    colorList=None,
    orderInverse=True,
    legend=True,
    **kwargs):
    

    # If there is no input data, get the data from the NetPyNE sim object
    if PSDData is None:
        if 'sim' not in kwargs:
            from .. import sim
        else:
            sim = kwargs['sim']

        PSDData = sim.analysis.preparePSD(
            PSDData=PSDData, 
            sim=sim,
            timeRange=timeRange,
            electrodes=electrodes,
            pop=pop,
            NFFT=NFFT,
            noverlap=noverlap, 
            nperseg=nperseg, 
            minFreq=minFreq, 
            maxFreq=maxFreq, 
            stepFreq=stepFreq, 
            smooth=smooth, 
            logx=logx,
            logy=logy, 
            normSignal=normSignal, 
            normPSD=normPSD, 
            filtFreq=filtFreq, 
            filtOrder=filtOrder, 
            detrend=detrend, 
            transformMethod=transformMethod,
            **kwargs
            )

    print('Plotting LFP power spectral density (PSD)...')

    # If input is a dictionary, pull the data out of it
    if type(PSDData) == dict:
    
        freqs = PSDData['psdFreqs']
        freq = freqs[0]
        psds = PSDData['psdSignal']
        names = PSDData['psdNames']
        colors = PSDData.get('colors')
        linewidths = PSDData.get('linewidths')
        alphas = PSDData.get('alphas')
        axisArgs = PSDData.get('axisArgs')

    # Set up colors, linewidths, and alphas for the plots
    if not colors:
        if not colorList:
            from .plotter import colorList
        colors = colorList[0:len(psds)]

    if not linewidths:
        linewidths = [1.0 for name in names]

    if not alphas:
        alphas = [1.0 for name in names]
    
    # Create a dictionary to hold axis inputs
    if not axisArgs:
        axisArgs = {}
        axisArgs['title'] = 'LFP Power Spectral Density'
        axisArgs['xlabel'] = 'Frequency (Hz)'
        axisArgs['ylabel'] = 'Power'

    # Link colors to traces, make avg plot black, add separation to traces
    plotColors = []
    legendLabels = []
    colorIndex = 0
    offset = np.absolute(psds).max() * separation
    
    for index, (name, psd) in enumerate(zip(names, psds)):
        legendLabels.append(name)
        if orderInverse:
            psds[index] = index * offset - psd
            axisArgs['invert_yaxis'] = True
        else:
            psds[index] = index * offset + psd
        if name == 'avg':
            plotColors.append('black')
        else:
            plotColors.append(colors[colorIndex])
            colorIndex += 1

    # Create a dictionary with the inputs for a line plot
    linesData = {}
    linesData['x'] = freq
    linesData['y'] = psds
    linesData['colors'] = plotColors
    linesData['markers'] = None
    linesData['markersizes'] = None
    linesData['linewidths'] = None
    linesData['alphas'] = None
    linesData['label'] = legendLabels

    # If a kwarg matches a lines input key, use the kwarg value instead of the default
    for kwarg in kwargs:
        if kwarg in linesData:
            linesData[kwarg] = kwargs[kwarg]

    # create Plotter object
    linesPlotter = LinesPlotter(data=linesData, axis=axis, **axisArgs, **kwargs)
    linesPlotter.type = 'PSD'

    # remove the y-axis
    linesPlotter.axis.get_yaxis().set_ticks([])

    # Set up the default legend settings
    legendKwargs = {}
    legendKwargs['title'] = 'Electrodes'
    #legendKwargs['bbox_to_anchor'] = (1.025, 1)
    #legendKwargs['loc'] = 2
    #legendKwargs['borderaxespad'] = 0.0
    #legendKwargs['handlelength'] = 0.5
    legendKwargs['fontsize'] = 'small'
    legendKwargs['title_fontsize'] = 'small'


    # If 'legendKwargs' is found in kwargs, use those values instead of the defaults
    if 'legendKwargs' in kwargs:
        legendKwargs_input = kwargs['legendKwargs']
        kwargs.pop('legendKwargs')
        for key, value in legendKwargs_input:
            if key in legendKwargs:
                legendKwargs[key] = value
    
    # add the legend
    if legend:
        axisArgs['legend'] = legendKwargs

    # Generate the figure
    PSDPlot = linesPlotter.plot(**axisArgs, **kwargs)

    # Default is to return the figure, but you can also return the plotter
    if returnPlotter:
        return linesPlotter
    else:
        return PSDPlot
