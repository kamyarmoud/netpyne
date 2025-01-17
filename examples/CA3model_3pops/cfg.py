from netpyne import specs

cfg = specs.SimConfig()

cfg.duration = 1500
cfg.dt = 0.1
cfg.params = {'v_init': -65.0}
cfg.verbose = False
cfg.recordTraces = {'V_soma':{'sec':'soma','loc':0.5,'var':'v'}}  # Dict with traces to record
cfg.recordStim = True
cfg.recordStep = 0.1            # Step size in ms to save data (eg. V traces, LFP, etc)
cfg.filename = '00'         # Set file output name
cfg.savePickle = False        # Save params, network and sim output to pickle file
cfg.saveDat = False
cfg.recordLFP = [[50, 50, 50]]

cfg.analysis['plotLFP'] = {'includeAxon': False, 'figSize': (6,10), 'timeRange': [250,1250], 'saveFig': True} 
cfg.analysis['plotRaster'] = {'saveFig': True}
cfg.analysis['plotTraces'] = {'include': [0, 1, 800, 801, 1000, 1001], 'saveFig': True}  # Plot recorded traces for this list of cells
#cfg.analysis['plotShape'] = {'includePre': ['all'],'includePost': [0,800,1000],'cvar':'numSyns','dist':0.7, 'saveFig': True}
