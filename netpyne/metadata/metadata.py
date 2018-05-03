metadata = {
    "netParams": {
        "label": "Net Params",
        "suggestions": "",
        "help": "",
        "hintText": "",
        "children": {
            "popParams": {
                "label": "Population Params",
                "suggestions": "",
                "help": "",
                "hintText": "",
                "children": {
                    "cellType": {
                        "label": "Cell Type",
                        "suggestions": "",
                        "help": "Arbitrary cell type attribute/tag assigned to all cells in this population; can be used as condition to apply specific cell properties. e.g. 'Pyr' (for pyramidal neurons) or 'FS' (for fast-spiking interneurons)",
                        "hintText": "",
                        "type": "str"
                    },
                    "numCells": {
                        "label": "Population Dimensions",
                        "suggestions": "",
                        "help": "The total number of cells in this population, the density in neurons/mm3, or the fixed grid spacing (only one of the three is required). The volume occupied by each population can be customized (see xRange, yRange and zRange); otherwise the full network volume will be used (defined in netParams: sizeX, sizeY, sizeZ). density can be expressed as a function of normalized location (xnorm, ynorm or znorm), by providing a string with the variable and any common Python mathematical operators/functions. e.g. '1e5 * exp(-ynorm/2)'. gridSpacing is the spacing between cells (in um). The total number of cells will be determined based on spacing and sizeX, sizeY, sizeZ. e.g. 10.",
                        "hintText": "number of cells",
                        "type": "int"
                    },
                    "density": {
                        "label": "Density or Grid Spacing",
                        "suggestions": "",
                        "help": "The total number of cells in this population, the density in neurons/mm3, or the fixed grid spacing (only one of the three is required). The volume occupied by each population can be customized (see xRange, yRange and zRange); otherwise the full network volume will be used (defined in netParams: sizeX, sizeY, sizeZ). density can be expressed as a function of normalized location (xnorm, ynorm or znorm), by providing a string with the variable and any common Python mathematical operators/functions. e.g. '1e5 * exp(-ynorm/2)'. gridSpacing is the spacing between cells (in um). The total number of cells will be determined based on spacing and sizeX, sizeY, sizeZ. e.g. 10.",
                        "hintText": "density in neurons/mm3",
                        "type": "str"
                    },
                    "gridSpacing": {
                        "label": "Density or Grid Spacing",
                        "suggestions": "",
                        "help": "The total number of cells in this population, the density in neurons/mm3, or the fixed grid spacing (only one of the three is required). The volume occupied by each population can be customized (see xRange, yRange and zRange); otherwise the full network volume will be used (defined in netParams: sizeX, sizeY, sizeZ). density can be expressed as a function of normalized location (xnorm, ynorm or znorm), by providing a string with the variable and any common Python mathematical operators/functions. e.g. '1e5 * exp(-ynorm/2)'. gridSpacing is the spacing between cells (in um). The total number of cells will be determined based on spacing and sizeX, sizeY, sizeZ. e.g. 10.",
                        "hintText": "fixed grid spacing",
                        "type": "int"
                    },
                    "cellModel": {
                        "label": "Cell Model",
                        "help": "Arbitrary cell model attribute/tag assigned to all cells in this population; can be used as condition to apply specific cell properties. e.g. 'HH' (standard Hodkgin-Huxley type cell model) or 'Izhi2007' (Izhikevich2007 point neuron model).",
                        "suggestions": [
                            "VecStim",
                            "NetStim",
                            "IntFire1"
                        ],
                        "type": "str"
                    },
                    "xRange": {
                        "label": "X Range",
                        "help": "Range of neuron positions in x-axis (horizontal length), specified2-element list[min, max]. xRange for absolute value in um (e.g.[100, 200]), or xnormRange for normalized value between0 and1 as fraction of sizeX (e.g.[0.1, 0.2]).",
                        "suggestions": "",
                        "hintText": "",
                        "type": "list(float)"
                    },
                    "xnormRange": {
                        "label": "X Norm Range",
                        "help": "Range of neuron positions in x-axis (horizontal length), specified2-element list[min, max]. xRange for absolute value in um (e.g.[100, 200]), or xnormRange for normalized value between0 and1 as fraction of sizeX (e.g.[0.1,0.2]).",
                        "suggestions": "",
                        "hintText": "",
                        "default": [
                            0,
                            1
                        ],
                        "type": "list(float)"
                    },
                    "yRange": {
                        "label": "Y Range",
                        "help": "Range of neuron positions in y-axis (vertical height=cortical depth), specified2-element list[min, max].yRange for absolute value in um (e.g.[100,200]), or ynormRange for normalized value between0 and1 as fraction of sizeY (e.g.[0.1,0.2]).",
                        "suggestions": "",
                        "hintText": "",
                        "type": "list(float)"
                    },
                    "ynormRange": {
                        "label": "Y Norm Range",
                        "help": "Range of neuron positions in y-axis (vertical height=cortical depth), specified2-element list[min, max]. yRange for absolute value in um (e.g.[100,200]), or ynormRange for normalized value between0 and1 as fraction of sizeY (e.g.[0.1,0.2]).",
                        "suggestions": "",
                        "hintText": "",
                        "type": "list(float)"
                    },
                    "zRange": {
                        "label": "Z Range",
                        "help": "Range of neuron positions in z-axis (horizontal depth), specified2-element list[min, max]. zRange for absolute value in um (e.g.[100,200]), or znormRange for normalized value between0 and1 as fraction of sizeZ (e.g.[0.1,0.2]).",
                        "suggestions": "",
                        "hintText": "",
                        "type": "list(float)"
                    },
                    "znormRange": {
                        "label": "Z Norm Range",
                        "help": "Range of neuron positions in z-axis (horizontal depth), specified2-element list[min, max]. zRange for absolute value in um (e.g.[100,200]), or znormRange for normalized value between0 and1 as fraction of sizeZ (e.g.[0.1,0.2]).",
                        "suggestions": "",
                        "hintText": "",
                        "type": "list(float)"
                    },
                    "interval": {
                        "label": "Spike Interval",
                        "help": "Spike interval in ms.",
                        "suggestions": "",
                        "hintText": "",
                        "type": "list(float)"
                    },
                    "rate": {
                        "label": "Rate",
                        "help": "Firing rate in Hz (note this is the inverse of the NetStim interval property).",
                        "suggestions": "",
                        "hintText": "",
                        "type": "list(float)"
                    },
                    "noise": {
                        "label": "Noise",
                        "help": "Fraction of noise in NetStim (0 = deterministic; 1 = completely random).",
                        "suggestions": "",
                        "hintText": "",
                        "type": "list(float)"
                    },
                    "start": {
                        "label": "Start",
                        "help": "Time of first spike in ms (default = 0).",
                        "suggestions": "",
                        "hintText": "",
                        "type": "list(float)"
                    },
                    "number": {
                        "label": "Number",
                        "help": "Max number of spikes generated (default = 1e12).",
                        "suggestions": "",
                        "hintText": "",
                        "type": "list(float)"
                    },
                    "seed": {
                        "label": "Seed",
                        "help": " Seed for randomizer (optional; defaults to value set in simConfig.seeds['stim'])",
                        "suggestions": "",
                        "hintText": "",
                        "type": "list(float)"
                    },
                    "spkTimes": {
                        "label": "Spike Times",
                        "help": "Spike Times(only for 'VecStim') - List of spike times (e.g. [1, 10, 40, 50], range(1,500,10), or any variable containing a Python list).",
                        "suggestions": "",
                        "hintText": "",
                        "type": "list(float)"
                    },
                    "pulses": {
                        "label": "Pulses",
                        "help": "(only for 'VecStim') - List of spiking pulses; each item includes the start (ms), end (ms), rate (Hz), and noise (0 to 1) pulse parameters. ",
                        "suggestions": "",
                        "hintText": "",
                        "type": "list(float)"
                    }
                }
            },
            "cellParams": {
                "label": "Cell Params",
                "suggestions": "",
                "help": "",
                "hintText": "",
                "children": {
                    "conds": {
                        "label": "Conds",
                        "suggestions": "",
                        "help": "",
                        "hintText": "",
                        "children": {
                            "cellType": {
                                "label": "Cell Type",
                                "suggestions": "",
                                "help": "",
                                "hintText": ""
                            },
                            "cellModel": {
                                "label": "Cell Model",
                                "suggestions": "",
                                "help": "",
                                "hintText": ""
                            }
                        }
                    },
                    "secs": {
                        "label": "Secs",
                        "suggestions": "",
                        "help": "",
                        "hintText": "",
                        "children": {
                            "geom": {
                                "label": "Cell Type",
                                "suggestions": "",
                                "help": "",
                                "hintText": "",
                                "children": {
                                    "diam": {
                                        "label": "Diameter",
                                        "suggestions": "",
                                        "help": "",
                                        "hintText": "",
                                        "type": "float"
                                    },
                                    "L": {
                                        "label": "Length",
                                        "suggestions": "",
                                        "help": "",
                                        "hintText": "",
                                        "type": "float"
                                    },
                                    "Ra": {
                                        "label": "Ra",
                                        "suggestions": "",
                                        "help": "",
                                        "hintText": "",
                                        "type": "float"
                                    },
                                    "cm": {
                                        "label": "cm",
                                        "suggestions": "",
                                        "help": "",
                                        "hintText": "",
                                        "type": "float"
                                    },
                                    "pt3d": {
                                        "label": "pt3d",
                                        "suggestions": "",
                                        "help": "",
                                        "hintText": "",
                                        "type": "float"
                                    },
                                    "nseg": {
                                        "label": "nseg",
                                        "suggestions": "",
                                        "help": "",
                                        "hintText": "",
                                        "type": "float"
                                    }
                                },
                                "topol": {
                                    "label": "Topology",
                                    "help": "Dictionary with topology properties.Includes parentSec (label of parent section), parentX (parent location where to make connection) and childX (current section child location where to make connection).",
                                    "suggestions": "",
                                    "hintText": ""
                                },
                                "mechs": {
                                    "label": "Mechanisms",
                                    "help": "Dictionary of density/distributed mechanisms.The key contains the name of the mechanism (e.g. hh or pas) The value contains a dictionary with the properties of the mechanism (e.g. {'g': 0.003, 'e': -70}).",
                                    "suggestions": "",
                                    "hintText": ""
                                },
                                "ions": {
                                    "label": "Ions",
                                    "help": "Dictionary of ions.he key contains the name of the ion (e.g. na or k) The value contains a dictionary with the properties of the ion (e.g. {'e': -70}).",
                                    "suggestions": "",
                                    "hintText": ""
                                },
                                "pointps": {
                                    "label": "Point processes",
                                    "help": "Dictionary of point processes (excluding synaptic mechanisms). The key contains an arbitrary label (e.g. 'Izhi') The value contains a dictionary with the point process properties (e.g. {'mod':'Izhi2007a', 'a':0.03, 'b':-2, 'c':-50, 'd':100, 'celltype':1}).",
                                    "suggestions": "",
                                    "hintText": "",
                                    "children": {
                                        "mod": {
                                            "label": "mod",
                                            "help": "the name of the NEURON mechanism, e.g. 'Izhi2007a'",
                                            "suggestions": "",
                                            "hintText": "",
                                            "type": "float"
                                        },
                                        "loc": {
                                            "label": "Length",
                                            "help": "section location where to place synaptic mechanism, e.g. 1.0, default=0.5.",
                                            "suggestions": "",
                                            "hintText": "",
                                            "type": "float"
                                        },
                                        "vref": {
                                            "label": "vref (optional)",
                                            "help": "internal mechanism variable containing the cell membrane voltage, e.g. 'V'.",
                                            "suggestions": "",
                                            "hintText": "",
                                            "type": "float"
                                        },
                                        "synList": {
                                            "label": "synList (optional)",
                                            "help": "list of internal mechanism synaptic mechanism labels, e.g. ['AMPA', 'NMDA', 'GABAB'].",
                                            "suggestions": "",
                                            "hintText": "",
                                            "type": "float"
                                        }
                                    },
                                    "vinit": {
                                        "label": "vinit",
                                        "help": "(optional) Initial membrane voltage (in mV) of the section (default: -65).e.g. cellRule['secs']['soma']['vinit'] = -72",
                                        "suggestions": "",
                                        "hintText": ""
                                    },
                                    "spikeGenLoc": {
                                        "label": "spikeGenLoc",
                                        "help": "(optional) Indicates that this section is responsible for spike generation (instead of the default 'soma'), and provides the location (segment) where spikes are generated.e.g. cellRule['secs']['axon']['spikeGenLoc'] = 1.0.",
                                        "suggestions": "",
                                        "hintText": ""
                                    },
                                    "threshold": {
                                        "label": "threshold",
                                        "help": "(optional) Threshold voltage (in mV) used to detect a spike originating in this section of the cell. If omitted, defaults to netParams.defaultThreshold = 10.0.e.g. cellRule['secs']['soma']['threshold'] = 5.0.",
                                        "suggestions": "",
                                        "hintText": ""
                                    }
                                },
                                "secLists": {
                                    "label": "secLists - (optional) ",
                                    "help": "Dictionary of sections lists (e.g. {'all': ['soma', 'dend']})",
                                    "suggestions": "",
                                    "hintText": ""
                                }
                            }
                        }
                    }
                }
            },
            "synMechParams": {
                "label": "Syn Mech Params",
                "suggestions": "",
                "help": "",
                "hintText": "",
                "children": {
                    "mod": {
                        "label": "NMODL mechanism name",
                        "help": "the NMODL mechanism name (e.g. 'ExpSyn'); note this does not always coincide with the name of the mod file.",
                        "suggestions": "",
                        "hintText": ""
                    },
                    "selfNetCon": {
                        "label": "NMODL mechanism name",
                        "help": "Dict with parameters of NetCon between the cell voltage and the synapse, required by some synaptic mechanisms such as the homeostatic synapse (hsyn). e.g. 'selfNetCon': {'sec': 'soma' , threshold: -15, 'weight': -1, 'delay': 0} (by default the source section, 'sec' = 'soma').",
                        "suggestions": "",
                        "hintText": ""
                    },
                    "tau1": {
                        "label": "Time constant for Exponential 1 [mSec]",
                        "help": "Define the time constant for the first exponential.",
                        "suggestions": "",
                        "hintText": ""
                    },
                    "tau2": {
                        "label": "Time constant for Exponential 2 [mSec]",
                        "help": "Define the time constant for the first exponential.",
                        "suggestions": "",
                        "hintText": ""
                    },
                    "e": {
                        "label": "Reference Voltage [mV]",
                        "help": "Define the Voltage reference.",
                        "suggestions": "",
                        "hintText": ""
                    }
                }
            },
            "connParams": {
                "label": "Connectivity Params",
                "suggestions": "",
                "help": "",
                "hintText": "",
                "children": {
                    "preConds": {
                        "label": "Conditions for the presynaptic cells",
                        "help": "Defined as a dictionary with the attributes/tags of the presynaptic cell and the required values e.g. {'cellType': 'PYR'}. Values can be lists, e.g. {'pop': ['Exc1', 'Exc2']}. For location properties, the list values correspond to the min and max values, e.g. {'ynorm': [0.1, 0.6]}.",
                        "suggestions": "",
                        "hintText": "",
                        "children": {
                            "pop": {
                                "label": "Populations (multiple selection available)",
                                "suggestions": "",
                                "help": "",
                                "hintText": ""
                            },
                            "cellType": {
                                "label": "Cell Type (multiple selection available)",
                                "suggestions": "",
                                "help": "",
                                "hintText": ""
                            },
                            "cellModel": {
                                "label": "Cell Model (multiple selection available)",
                                "suggestions": "",
                                "help": "",
                                "hintText": ""
                            }
                        }
                    },
                    "postConds": {
                        "label": "Conditions for the postsynaptic cells",
                        "help": "Defined as a dictionary with the attributes/tags of the postsynaptic cell and the required values e.g. {'cellType': 'PYR'}. Values can be lists, e.g. {'pop': ['Exc1', 'Exc2']}. For location properties, the list values correspond to the min and max values, e.g. {'ynorm': [0.1, 0.6]}.",
                        "suggestions": "",
                        "hintText": "",
                        "children": {
                            "pop": {
                                "label": "Population (multiple selection available)",
                                "suggestions": "",
                                "help": "",
                                "hintText": ""
                            },
                            "cellType": {
                                "label": "Cell Type (multiple selection available)",
                                "suggestions": "",
                                "help": "",
                                "hintText": ""
                            },
                            "cellModel": {
                                "label": "Cell Model (multiple selection available)",
                                "suggestions": "",
                                "help": "",
                                "hintText": ""
                            }
                        }
                    },
                    "sec": {
                        "label": "Target section",
                        "help": "Name of target section on the postsynaptic neuron (e.g. 'soma'). If omitted, defaults to 'soma' if exists, otherwise to first section in the cell sections list. If synsPerConn > 1, a list of sections or sectionList can be specified, and synapses will be distributed uniformly along the specified section(s), taking into account the length of each section.",
                        "suggestions": "",
                        "hintText": ""
                    },
                    "loc": {
                        "label": "Target synaptic mechanism",
                        "help": "Location of target synaptic mechanism (e.g. 0.3). If omitted, defaults to 0.5. Can be single value, or list (if have synsPerConn > 1) or list of lists (If have both a list of synMechs and synsPerConn > 1).",
                        "suggestions": "",
                        "hintText": "",
                        "type": "list(list(float))"
                    },
                    "synMech": {
                        "label": "Target synaptic mechanism(s) on the postsynaptic neuron",
                        "help": "Label (or list of labels) of target synaptic mechanism on the postsynaptic neuron (e.g. 'AMPA' or ['AMPA', 'NMDA']). If omitted employs first synaptic mechanism in the cell synaptic mechanisms list. If have list, a separate connection is created to each synMech; and a list of weights, delays and or locs can be provided.",
                        "suggestions": "",
                        "hintText": ""
                    },
                    "synsPerConn": {
                        "label": "Number of individual synaptic connections",
                        "help": "Number of individual synaptic connections (synapses) per cell-to-cell connection (connection). Can be defined as a function (see Functions as strings). If omitted, defaults to 1.",
                        "suggestions": "",
                        "hintText": ""
                    },
                    "weight": {
                        "label": "Strength of synaptic connection",
                        "help": "Strength of synaptic connection (e.g. 0.01). Associated to a change in conductance, but has different meaning and scale depending on the synaptic mechanism and cell model. Can be defined as a function (see Functions as strings). If omitted, defaults to netParams.defaultWeight = 1.",
                        "suggestions": "",
                        "hintText": ""
                    },
                    "delay": {
                        "label": "Time (in ms) for the presynaptic spike to reach the postsynaptic neuron",
                        "help": "Time (in ms) for the presynaptic spike to reach the postsynaptic neuron. Can be defined as a function (see Functions as strings). If omitted, defaults to netParams.defaultDelay = 1.",
                        "suggestions": "",
                        "hintText": "",
                        "type": "list(float)"
                    },
                    "probability": {
                        "label": "Probability of connection between each pre and postsynaptic cell",
                        "help": "Probability of connection between each pre and postsynaptic cell (0 to 1). Can be defined as a function (see Functions as strings). Sets connFunc to probConn (internal probabilistic connectivity function). Overrides the convergence, divergence and fromList parameters.",
                        "suggestions": "",
                        "hintText": ""
                    },
                    "convergence": {
                        "label": "Number of pre-synaptic cells connected to each post-synaptic cell",
                        "help": "Number of pre-synaptic cells connected to each post-synaptic cell. Can be defined as a function (see Functions as strings).Sets connFunc to convConn (internal convergence connectivity function).",
                        "suggestions": "",
                        "hintText": ""
                    },
                    "divergence": {
                        "label": "Number of post-synaptic cells connected to each pre-synaptic cell",
                        "help": "Number of post-synaptic cells connected to each pre-synaptic cell. Can be defined as a function (see Functions as strings). Sets connFunc to divConn (internal divergence connectivity function).",
                        "suggestions": "",
                        "hintText": ""
                    },
                    "connList": {
                        "label": "Explicit list of connections between individual pre- and post-synaptic cells",
                        "help": "Each connection is indicated with relative ids of cell in pre and post populations, e.g. [[0,1],[3,1]] creates a connection between pre cell 0 and post cell 1; and pre cell 3 and post cell 1. Weights, delays and locs can also be specified as a list for each of the individual cell connection. These lists can be 2D or 3D if combined with multiple synMechs and synsPerConn > 1 (the outer dimension will correspond to the connList). Sets connFunc to fromList (explicit list connectivity function).",
                        "suggestions": "",
                        "hintText": ""
                    },
                    "connFunc": {
                        "label": "Internal connectivity function to use",
                        "help": "Its automatically set to probConn, convConn, divConn or fromList, when the probability, convergence, divergence or connList parameters are included, respectively. Otherwise defaults to fullConn, ie. all-to-all connectivity.",
                        "suggestions": "",
                        "hintText": ""
                    },
                    "shape": {
                        "label": "Modifies the conn weight dynamically during the simulation based on the specified pattern",
                        "help": "Contains a dictionary with the following fields: 'switchOnOff' - times at which to switch on and off the weight, 'pulseType' - type of pulse to generate; either 'square' or 'gaussian', 'pulsePeriod' - period (in ms) of the pulse, 'pulseWidth' - width (in ms) of the pulse.",
                        "suggestions": "",
                        "hintText": ""
                    },
                    "plasticity": {
                        "label": "Plasticity mechanism to use for this connections",
                        "help": "Requires 2 fields: mech to specifiy the name of the plasticity mechanism, and params containing a dictionary with the parameters of the mechanism, e.g. {'mech': 'STDP', 'params': {'hebbwt': 0.01, 'antiwt':-0.01, 'wmax': 50, 'RLon': 1 'tauhebb': 10}}.",
                        "suggestions": "",
                        "hintText": ""
                    }
                }
            },
            "stimSourceParams": {
                "label": "Stimulation Source Params",
                "suggestions": "",
                "help": "",
                "hintText": "",
                "children": {
                    "type": {
                        "label": "Point process used as stimulator",
                        "help": "Point process used as stimulator; allowed values: 'IClamp', 'VClamp', 'SEClamp', 'NetStim' and 'AlphaSynapse'. Note that NetStims can be added both using this method, or by creating a population of 'cellModel': 'NetStim' and adding the appropriate connections.",
                        "suggestions": "",
                        "hintText": ""
                    },
                    "stimParams": {
                        "label": "Stimulation parameters",
                        "help": "These will depend on the type of stimulator (e.g. for 'IClamp' will have 'delay', 'dur' and 'amp'). Can be defined as a function (see Functions as strings). Note for stims it only makes sense to use parameters of the postsynatic cell (e.g. 'post_ynorm').",
                        "suggestions": "",
                        "hintText": ""
                    },
                    "dur": {
                        "label": "Duration [msec]",
                        "help": "Clamp is on at time 0, and off at time dur[0]+dur[1]+dur[2]. When clamp is off the injected current is 0. Do not insert several instances of this model at the same location in order to make level changes. That is equivalent to independent clamps and they will have incompatible internal state values.",
                        "suggestions": "",
                        "hintText": "",
                        "type": "list(float)"
                    },
                    "amp": {
                        "label": "Stimulation Amplitud",
                        "help": "Clamp is on at time 0, and off at time dur[0]+dur[1]+dur[2]. When clamp is off the injected current is 0. Do not insert several instances of this model at the same location in order to make level changes. That is equivalent to independent clamps and they will have incompatible internal state values.",
                        "suggestions": "",
                        "hintText": "",
                        "type": "list(float)"
                    },
                    "del": {
                        "label": "Stimulation delay",
                        "help": "Define the stimulation delay.",
                        "suggestions": "",
                        "hintText": "",
                        "type": "list(float)"
                    },
                    "interval": {
                        "label": "Time between spikes",
                        "help": "Define the mean time interval between spike.",
                        "suggestions": "",
                        "hintText": ""
                    },
                    "rstim": {
                        "label": "Stimulation resistance",
                        "help": "Define the resistan to the cell.",
                        "suggestions": "",
                        "hintText": ""
                    },
                    "gain": {
                        "label": "Amplifier gain",
                        "help": "Define amplifier gain.",
                        "suggestions": "",
                        "hintText": ""
                    },
                    "number": {
                        "label": "Number of Spikes ",
                        "help": "Define the total number of spikes.",
                        "suggestions": "",
                        "hintText": ""
                    },
                    "start": {
                        "label": "Start time for the first spike ",
                        "help": "Define the start time for the first spike.",
                        "suggestions": "",
                        "hintText": ""
                    },
                    "noise": {
                        "label": "Noise level ",
                        "help": "Fractional noise, 0 <= noise <= 1, means that an interval between spikes consists of a fixed interval of duration (1 - noise)*interval plus a negexp interval of mean duration noise*interval. Note that the most likely negexp interval has duration 0.",
                        "suggestions": "",
                        "hintText": ""
                    },
                    "tau1": {
                        "label": "Time response for the read voltage.",
                        "help": "Set the time response for the voltage read from cell.",
                        "suggestions": "",
                        "hintText": ""
                    },
                    "tau2": {
                        "label": "Time response for the voltage inserted into the cell",
                        "help": ".",
                        "suggestions": "",
                        "hintText": ""
                    },
                    "i": {
                        "label": "Current [nA]",
                        "help": "Inyected current in nA.",
                        "suggestions": "",
                        "hintText": ""
                    },
                    "onset": {
                        "label": "Time delay for alpha conductance application ",
                        "help": ".",
                        "suggestions": "",
                        "hintText": ""
                    },
                    "tau": {
                        "label": "Alpha function time response",
                        "help": "Define time response for the Alpha function.",
                        "suggestions": "",
                        "hintText": ""
                    },
                    "gmax": {
                        "label": "Maximum Conductance",
                        "help": "Define the maximum conductance for the alpha function.",
                        "suggestions": "",
                        "hintText": ""
                    },
                    "e": {
                        "label": "Reference Voltage",
                        "help": "Define the reference voltage.",
                        "suggestions": "",
                        "hintText": ""
                    },
                    "rs": {
                        "label": "Resistance [MOhm]",
                        "help": "Define the resistance between the reference voltage and the cell.",
                        "suggestions": "",
                        "hintText": ""
                    },
                    "vc": {
                        "label": "Reference Voltage [mV]",
                        "help": "Define the reference Voltage.",
                        "suggestions": "",
                        "hintText": ""
                    }
                }
            },
            "stimTargetParams": {
                "label": "Stimulation Target Params",
                "suggestions": "",
                "help": "",
                "hintText": "",
                "children": {
                    "source": {
                        "label": "Label of the stimulation source",
                        "help": "Label of the stimulation source (e.g. 'electrode_current').",
                        "suggestions": "",
                        "hintText": ""
                    },
                    "conds": {
                        "label": "Conditions of cells where the stim will be applied",
                        "help": "Conditions of cells where the stim will be applied. Dictionary with conditions of cells where the stim will be applied. Can include a field 'cellList' with the relative cell indices within the subset of cells selected (e.g. 'conds': {'cellType':'PYR', 'y':[100,200], 'cellList': [1,2,3]}).",
                        "suggestions": "",
                        "hintText": "",
                        "children": {
                            "pop": {
                                "label": "Target Population",
                                "help": "Select the population targets e.g. {'pop': ['Exc1', 'Exc2']}",
                                "suggestions": "",
                                "hintText": "",
                                "type": "list(float)"
                            },
                            "cellType": {
                                "label": "Target Cell Type",
                                "suggestions": "",
                                "help": "Arbitrary cell type attribute/tag assigned to all cells in this population; can be used as condition to apply specific cell properties. e.g. 'Pyr' (for pyramidal neurons) or 'FS' (for fast-spiking interneurons)",
                                "hintText": "",
                                "type": "str"
                            }, 
                            "cellModel": {
                                "label": "Target Cell Model",
                                "help": "Arbitrary cell model attribute/tag assigned to all cells in this population; can be used as condition to apply specific cell properties. e.g. 'HH' (standard Hodkgin-Huxley type cell model) or 'Izhi2007' (Izhikevich2007 point neuron model).",
                                "suggestions": [
                                    "HH",
                                    "IntFire1"
                                ],
                                "type": "str"
                            },
                            "xRange": {
                                "label": "Target X Range",
                                "help": "Range of neuron positions in x-axis (horizontal length), specified2-element list[min, max]. xRange for absolute value in um (e.g.[100, 200]), or xnormRange for normalized value between0 and1 as fraction of sizeX (e.g.[0.1, 0.2]).",
                                "suggestions": "",
                                "hintText": "",
                                "type": "list(float)"
                            },
                            "xnormRange": {
                                "label": "Target X Norm Range",
                                "help": "Range of neuron positions in x-axis (horizontal length), specified2-element list[min, max]. xRange for absolute value in um (e.g.[100, 200]), or xnormRange for normalized value between0 and1 as fraction of sizeX (e.g.[0.1,0.2]).",
                                "suggestions": "",
                                "hintText": "",
                                "default": [
                                    0,
                                    1
                                ],
                                "type": "list(float)"
                            },
                            "yRange": {
                                "label": "Target Y Range",
                                "help": "Range of neuron positions in y-axis (vertical height=cortical depth), specified2-element list[min, max].yRange for absolute value in um (e.g.[100,200]), or ynormRange for normalized value between0 and1 as fraction of sizeY (e.g.[0.1,0.2]).",
                                "suggestions": "",
                                "hintText": "",
                                "type": "list(float)"
                            },
                            "ynormRange": {
                                "label": "Target Y Norm Range",
                                "help": "Range of neuron positions in y-axis (vertical height=cortical depth), specified2-element list[min, max]. yRange for absolute value in um (e.g.[100,200]), or ynormRange for normalized value between0 and1 as fraction of sizeY (e.g.[0.1,0.2]).",
                                "suggestions": "",
                                "hintText": "",
                                "type": "list(float)"
                            },
                            "zRange": {
                                "label": "Target Z Range",
                                "help": "Range of neuron positions in z-axis (horizontal depth), specified2-element list[min, max]. zRange for absolute value in um (e.g.[100,200]), or znormRange for normalized value between0 and1 as fraction of sizeZ (e.g.[0.1,0.2]).",
                                "suggestions": "",
                                "hintText": "",
                                "type": "list(float)"
                            },
                            "znormRange": {
                                "label": "Target Z Norm Range",
                                "help": "Range of neuron positions in z-axis (horizontal depth), specified2-element list[min, max]. zRange for absolute value in um (e.g.[100,200]), or znormRange for normalized value between0 and1 as fraction of sizeZ (e.g.[0.1,0.2]).",
                                "suggestions": "",
                                "hintText": "",
                                "type": "list(float)"
                            },
                            "cellList": {
                                "label": "Target Cell Index",
                                "help": "Indices of neuron to be included in the application of this stimulation. ([1, 8, 12])",
                                "suggestions": "",
                                "hintText": "",
                                "type": "list(float)"
                            },
                            
                        }
                    },
                    "sec": {
                        "label": "Target section",
                        "help": "Target section (default: 'soma').",
                        "suggestions": "",
                        "hintText": "",
                        "type": "str"
                    },
                    "loc": {
                        "label": "Target location ",
                        "help": "Target location (default: 0.5). Can be defined as a function (see Functions as strings).",
                        "suggestions": "",
                        "hintText": "",
                        "type": "float"
                    },
                    "synMech": {
                        "label": "Synaptic mechanism label to connect NetStim to",
                        "help": "Synaptic mechanism label to connect NetStim to. Optional; only for NetStims.",
                        "suggestions": "",
                        "hintText": ""
                    },
                    "weight": {
                        "label": "Weight of connection between NetStim and cell",
                        "help": "Weight of connection between NetStim and cell. Optional; only for NetStims. Can be defined as a function (see Functions as strings).",
                        "suggestions": "",
                        "hintText": ""
                    },
                    "delay": {
                        "label": "Delay of connection between NetStim and cell",
                        "help": "Delay of connection between NetStim and cell (default: 1). Optional; only for NetStims. Can be defined as a function (see Functions as strings).",
                        "suggestions": "",
                        "hintText": ""
                    },
                    "synsPerConn": {
                        "label": "Number of synapses of connection between NetStim and cell",
                        "help": "Number of synapses of connection between NetStim and cell (default: 1). Optional; only for NetStims. Can be defined as a function (see Functions as strings).",
                        "suggestions": "",
                        "hintText": ""
                    }
                }
            }
        }
    },
    "simConfig": {
        "label": "Sim Config",
        "suggestions": "",
        "help": "",
        "hintText": "",
        "children": {
            "simLabel": {
                "label": "Name of Simulation"
            },
            "duration": {
                "label": "Duration",
                "help": "simulation duration in ms (default: 1000)",
                "type": "float"
            },
            "dt": {
                "label": "Dt",
                "help": "simulation time step in ms (default: 0.1)",
                "type": "float"
            },
            "seeds": {
                "label": "Seeds",
                "help": "Dictionary with random seeds for connectivity, input stimulation, and cell locations (default: {'conn': 1, 'stim': 1, 'loc': 1}).",
                "type": "dict"
            },
            "addSynMechs": {
                "label": "Add Syn Mechs",
                "help": "Whether to add synaptich mechanisms or not (default: True).",
                "type": "bool"
            },
            "includeParamsLabel": {
                "label": "Include Params Label",
                "help": " Include label of param rule that created that cell, conn or stim (default: True).",
                "type": "bool"
            },
            "timing": {
                "label": "Timing",
                "help": "Show and record timing of each process (default: True).",
                "type": "bool"
            },
            "verbose": {
                "label": "Verbose",
                "help": "Show detailed messages (default: False).",
                "type": "bool"
            },
            "saveFolder": {
                "label": "Save Folder",
                "help": "Path where to save output data (default: '')",
                "type": "str"
            },
            "filename": {
                "label": "File Name",
                "help": "Name of file to save model output (default: 'model_output')",
                "type": "str"
            },
            "saveDataInclude": {
                "label": "Save Data Include",
                "help": "Data structures to save to file (default: ['netParams', 'netCells', 'netPops', 'simConfig', 'simData'])",
                "type": "list(str)"
            },
            "timestampFilename": {
                "label": "add timestamp to file name",
                "help": "Add timestamp to filename to avoid overwriting (default: False)",
                "type": "bool"
            },
            "savePickle": {
                "label": "Save Pickle",
                "help": "Save data to pickle file (default: False).",
                "type": "bool"
            },
            "saveJson": {
                "label": "Save Json",
                "help": "Save dat to json file (default: False).",
                "type": "bool"
            },
            "saveMat": {
                "label": "Save MAT",
                "help": " Save data to mat file (default: False).",
                "type": "bool"
            },
            "saveHDF5": {
                "label": "Save HDF5",
                "help": "Save data to save to HDF5 file (default: False).",
                "type": "bool"
            },
            "saveDpk": {
                "label": "Save DPK",
                "help": " Save data to .dpk pickled file (default: False).",
                "type": "bool"
            },
            "checkErrors": {
                "label": "Check Errors",
                "help": "check for errors (default: False).",
                "type": "bool"
            },
            "checkErrorsVerbose": {
                "label": "Check Errors Verbose",
                "help": "check errors vervose (default: False)",
                "type": "bool"
            },
            "backupCfgFile": {
                "label": "Copy config file to folder:",
                "help": "Copy cfg file to folder, eg. ['cfg.py', 'backupcfg/'] (default: []).",
                "type": "list(str)"
            },
            "recordCells": {
                "label": "record cells",
                "help": "List of cells from which to record traces. Can include cell gids (e.g. 5), population labels (e.g. 'S' to record from one cell of the 'S' population), or 'all', to record from all cells. NOTE: All cells selected in the include argument of simConfig.analysis['plotTraces'] will be automatically included in recordCells. (default: []).",
                "type": "list(list)"
            },
            "saveCSV": {
                "label": "save .cvs file",
                "help": "save cvs file (default: False)",
                "type": "bool"
            },
            "saveDat": {
                "label": "save .dat file",
                "help": "save .dat file (default: False)",
                "type": "bool"
            },
            "saveCellSecs": {
                "label": "save cell secs",
                "help": "save cell secs (default: True)",
                "type": "bool"
            },
            "saveCellConns": {
                "label": "save cell conns",
                "help": "save cell connections. (default: True)",
                "type": "bool"
            },
            "recordStim": {
                "label": "record spikes of cell stims",
                "help": "Record spikes of cell stims (default: False).",
                "type": "bool"
            },
            "recordTraces": {
                "label": "record traces",
                "help": "Dict of traces to record (default: {} ; example: {'V_soma': {'sec':'soma','loc':0.5,'var':'v'} }).",
                "type": "dict"
            },
            "recordLFP": {
                "label": "record LFP",
                "help": " 3D locations of local field potential (LFP) electrodes, e.g. [[50, 100, 50], [50, 200]] (default: False).",
                "type": "list(list(float))"
            },
            "saveLFPCells": {
                "label": "Store LFP",
                "help": "Store LFP generated individually by each cell in sim.allSimData['LFPCells'].",
                "type": "bool"
            },
            "recordStep": {
                "label": "step size for data recording",
                "help": "Step size in ms for data recording (default: 0.1).",
                "type": "float"
            },
            "printRunTime": { 
                "label": "print run time at intervals:",
                "help": "Print run time at interval (in sec) specified here (eg. 0.1) (default: False).",
                "type": "float"
            },
            "printSynsAfterRule": { 
                "label": "print total connections",
                "help": "Print total connections after each conn rule is applied.",
                "type": "bool"
            },
            "printPopAvgRates": {
                "label": "print pop average firing rates",
                "help": "Print population avg firing rates after run (default: False).",
                "type": "bool"
            },
            "connRandomSecFromList": {
                "label": "select sections at random",
                "help": "{Select random section (and location) from list even when synsPerConn=1 (default: True).",
                "type": "bool"
            },
            "compactConnFormat": {
                "label": "replace dict format with compact list for conns",
                "help": "Replace dict format with compact list format for conns (need to provide list of keys to include) (default: False).",
                "type": "bool"
            },
            "gatherOnlySimData": {
                "label": "gather only sim data",
                "help": "Omits gathering of net and cell data thus reducing gatherData time (default: False).",
                "type": "bool"
            },
            "createPyStruct": {
                "label": "create python structure",
                "help": "Create Python structure (simulator-independent) when instantiating network (default: True).",
                "type": "bool"
            },
            "createNEURONObj": {
                "label": "create NEURON object",
                "help": "Create runnable network in NEURON when instantiating netpyne network metadata (default: True).",
                "type": "bool"
            },
            "cvode_active": {
                "label": "use CVode",
                "help": "Use CVode variable time step (default: False).",
                "type": "bool"
            },
            "cache_efficient": {
                "label": "use CVode cache_efficient",
                "help": "Use CVode cache_efficient option to optimize load when running on many cores (default: False).",
                "type": "bool"
            },
            "hParams": {
                "label": "define temperature, initial voltage, etc",
                "help": "Dictionary with parameters of h module (default: {'celsius': 6.3, 'v_init': -65.0, 'clamp_resist': 0.001}).",
                "type": "dict"
            },
            "saveTxt": {
                "label": "Save txt",
                "help": "Save data to txt file (default: False)",
                "type": "bool"
            },
            "saveTiming": {
                "label": "Save timing to pickle file",
                "help": " Save timing data to pickle file (default: False).",
                "type": "bool"
            },
            "analysis": {
                "label": "Analysis",
                "suggestions": "",
                "help": "",
                "hintText": "",
                "children": {
                    "plotRaster": {
                        "label": "Raster Plot",
                        "suggestions": "",
                        "help": "Plot raster (spikes over time) of network cells.",
                        "hintText": "",
                        "children": {
                            "include": {
                                "label": "population (or cells by index) to raster",
                                "suggestions": "",
                                "help": "List of cells to include (['all'|,'allCells'|,'allNetStims'|,120|,'L4'|,('L2', 56)|,('L5',[4,5,6])])",
                                "hintText": "",
                                "type": "str"
                            },
                            "timeRange": {
                                "label": "time Range",
                                "suggestions": "",
                                "help": "Time range of spikes shown; if None shows all ([start,stop])",
                                "hintText": "",
                                "type": "list(int)"
                            },
                            "maxSpikes": {
                                "label": "maximum number of spikes",
                                "suggestions": "",
                                "help": "maximum number of spikes that will be plotted (int).",
                                "hintText": "",
                                "type": "float"
                            },
                            "orderBy": {
                                "label": "order by",
                                "suggestions": "",
                                "help": "Unique numeric cell property to order y-axis by, e.g. 'gid', 'ynorm', 'y' ('gid'|'y'|'ynorm'|...)",
                                "hintText": "",
                                "options": [
                                    "gid",
                                    "y",
                                    "ynorm"
                                ],
                                "type": "str"
                            },
                            "orderInverse": {
                                "label": "invert y-axis",
                                "suggestions": "",
                                "help": "Invert the y-axis order (True|False)",
                                "hintText": "",
                                "type": "bool"
                            },
                            "labels": {
                                "label": "labels",
                                "suggestions": "",
                                "help": "Show population labels in a legend or overlayed on one side of raster ('legend'|'overlay'))",
                                "hintText": "",
                                "type": "str"
                            },
                            "popRates": {
                                "label": "include rates",
                                "suggestions": "",
                                "help": "Include population rates ('legend'|'overlay')",
                                "hintText": "",
                                "options": [
                                    "legend",
                                    "overlay"
                                ],
                                "type": "str"
                            },
                            "spikeHist": {
                                "label": "overlay spike histogram",
                                "suggestions": "",
                                "help": "overlay line over raster showing spike histogram (spikes/bin) (None|'overlay'|'subplot')",
                                "hintText": "",
                                "options": [
                                    "None",
                                    "overlay",
                                    "subplot"
                                ],
                                "type": "str"
                            },
                            "spikeHistBin": {
                                "label": "bin size for histogram",
                                "suggestions": "",
                                "help": "Size of bin in ms to use for histogram (int)",
                                "hintText": "",
                                "type": "float"
                            },
                            "syncLines": {
                                "label": "synchronize lines",
                                "suggestions": "",
                                "help": "calculate synchorny measure and plot vertical lines for each spike to evidence synchrony (True|False)",
                                "hintText": "",
                                "type": "bool"
                            },
                            "figSize": {
                                "label": "Figure size",
                                "suggestions": "",
                                "help": "Size of figure ((width, height))",
                                "hintText": "",
                                "type": ""
                            },
                            "saveData": {
                                "label": "Save data",
                                "suggestions": "",
                                "help": "File name where to save the final data used to generate the figure (None|'fileName').",
                                "hintText": "",
                                "type": ""
                            },
                            "saveFig": {
                                "label": "Figure Name",
                                "suggestions": "",
                                "help": "File name where to save the figure (None|'fileName')",
                                "hintText": "",
                                "type": ""
                            },
                            "showFig": {
                                "label": "Show figure",
                                "suggestions": "",
                                "help": "Whether to show the figure or not (True|False).",
                                "hintText": "",
                                "type": ""
                            }
                        }
                    },
                    "plotSpikeHist": {
                        "label": "Plot Spike Histogram",
                        "suggestions": "",
                        "help": "Plot spike histogram.",
                        "hintText": "",
                        "children": {
                            "include": {
                                "label": "population (or cells by index) to histogram",
                                "suggestions": "",
                                "help": "List of cells to include (['all'|,'allCells'|,'allNetStims'|,120|,'L4'|,('L2', 56)|,('L5',[4,5,6])])",
                                "hintText": "",
                                "type": "list"
                            },
                            "timeRange": {
                                "label": "time Range",
                                "suggestions": "",
                                "help": "Time range of spikes shown; if None shows all ([start,stop])",
                                "hintText": "",
                                "type": "list(int)"
                            },
                            "binSize": {
                                "label": "bin size for histogram",
                                "suggestions": "",
                                "help": "Size of bin in ms to use for histogram (int)",
                                "hintText": "",
                                "type": "int"
                            },
                            "overlay": {
                                "label": "show overlay",
                                "suggestions": "",
                                "help": "Whether to overlay the data lines or plot in separate subplots (True|False)",
                                "hintText": "",
                                "type": "bool"
                            },
                            "graphType": {
                                "label": "type of Graph",
                                "suggestions": "",
                                "help": " Type of graph to use (line graph or bar plot) ('line'|'bar')",
                                "hintText": "",
                                "options": [
                                    "line",
                                    "bar"
                                ],
                                "type": "bool"
                            },
                            "yaxis": {
                                "label": "axis units",
                                "suggestions": "",
                                "help": "Units of y axis (firing rate in Hz, or spike count) ('rate'|'count')",
                                "hintText": "",
                                "options": [
                                    "rate",
                                    "count"
                                ],
                                "type": "str"
                            },
                            "figSize": {
                                "label": "Figure size",
                                "suggestions": "",
                                "help": "Size of figure ((width, height))",
                                "hintText": "",
                                "type": ""
                            },
                            "saveData": {
                                "label": "Save data",
                                "suggestions": "",
                                "help": "File name where to save the final data used to generate the figure (None|'fileName').",
                                "hintText": "",
                                "type": ""
                            },
                            "saveFig": {
                                "label": "Figure Name",
                                "suggestions": "",
                                "help": "File name where to save the figure (None|'fileName')",
                                "hintText": "",
                                "type": ""
                            },
                            "showFig": {
                                "label": "Show figure",
                                "suggestions": "",
                                "help": "Whether to show the figure or not (True|False).",
                                "hintText": "",
                                "type": ""
                            }
                        }
                    },
                    "plotRatePSD": {
                        "label": "Plot Rate PSD",
                        "suggestions": "",
                        "help": "Plot spikes power spectral density (PSD).",
                        "hintText": "",
                        "children": {
                            "include": {
                                "label": "population (or cell by index) to RatePSD",
                                "suggestions": "",
                                "help": "List of cells to include (['all'|,'allCells'|,'allNetStims'|,120|,'L4'|,('L2', 56)|,('L5',[4,5,6])])",
                                "hintText": "",
                                "type": "list"
                            },
                            "timeRange": {
                                "label": "Time Range",
                                "suggestions": "",
                                "help": "Time range of spikes shown; if None shows all ([start,stop])",
                                "hintText": "",
                                "type": "list(int)"
                            },
                            "binSize": {
                                "label": "Bin size",
                                "suggestions": "",
                                "help": "Size of bin in ms to use (int)",
                                "hintText": "",
                                "type": "int"
                            },
                            "maxFreq": {
                                "label": "maximum frequency",
                                "suggestions": "",
                                "help": " Maximum frequency to show in plot (float).",
                                "hintText": "",
                                "type": "float"
                            },
                            "NFFT": {
                                "label": "Number of point",
                                "suggestions": "",
                                "help": "The number of data points used in each block for the FFT (power of 2) (float)",
                                "hintText": "",
                                "type": ""
                            },
                            "noverlap": {
                                "label": "Number of overlap points",
                                "suggestions": "",
                                "help": "Number of points of overlap between segments (int, < nperseg).",
                                "hintText": "",
                                "type": ""
                            },
                            "smooth": {
                                "label": "Window size",
                                "suggestions": "",
                                "help": "Window size for smoothing; no smoothing if 0 (int).",
                                "hintText": "",
                                "type": ""
                            },
                            "overlay": {
                                "label": "Overlay data",
                                "suggestions": "",
                                "help": "Whether to overlay the data lines or plot in separate subplots (True|False).",
                                "hintText": "",
                                "type": "bool"
                            },
                            "figSize": {
                                "label": "Figure size",
                                "suggestions": "",
                                "help": "Size of figure ((width, height))",
                                "hintText": "",
                                "type": ""
                            },
                            "saveData": {
                                "label": "Save data",
                                "suggestions": "",
                                "help": "File name where to save the final data used to generate the figure (None|'fileName').",
                                "hintText": "",
                                "type": ""
                            },
                            "saveFig": {
                                "label": "Figure Name",
                                "suggestions": "",
                                "help": "File name where to save the figure (None|'fileName')",
                                "hintText": "",
                                "type": ""
                            },
                            "showFig": {
                                "label": "Show figure",
                                "suggestions": "",
                                "help": "Whether to show the figure or not (True|False).",
                                "hintText": "",
                                "type": ""
                            }
                        }
                    },
                    "plotSpikeStats": {
                        "label": "Plot Spike Statistics",
                        "suggestions": "",
                        "help": "Plot spike histogram.",
                        "hintText": "",
                        "children": {
                            "include": {
                                "label": "population (or cell by index) to SpikeStats",
                                "suggestions": "",
                                "help": "List of cells to include (['all'|,'allCells'|,'allNetStims'|,120|,'L4'|,('L2', 56)|,('L5',[4,5,6])])",
                                "hintText": "",
                                "type": "list"
                            },
                            "timeRange": {
                                "label": "time range",
                                "suggestions": "",
                                "help": "Time range of spikes shown; if None shows all ([start,stop])",
                                "hintText": "",
                                "type": "list(int)"
                            },
                            "graphType": {
                                "label": "type of graph",
                                "suggestions": "",
                                "help": "Type of graph to use ('boxplot').",
                                "hintText": "",
                                "options": [
                                    "boxplot"
                                ],
                                "type": "str"
                            },
                            "stats": {
                                "label": "meassure type to calculate stats",
                                "suggestions": "",
                                "help": "List of types measure to calculate stats over: cell firing rates, interspike interval coefficient of variation (ISI CV), pairwise synchrony, and/or overall synchrony (sync measures calculated using PySpike SPIKE-Synchrony measure) (['rate', |'isicv'| 'pairsync' |'sync'|]).",
                                "hintText": "",
                                "options": [
                                    "rate",
                                    "isicv",
                                    "pairsync",
                                    "sync"
                                ],
                                "type": "str"
                            },
                            "popColors": {
                                "label": "color for each population",
                                "suggestions": "",
                                "help": "Dictionary with color (value) used for each population/key.",
                                "hintText": "",
                                "type": "dict"
                            },
                            "figSize": {
                                "label": "figure size",
                                "suggestions": "",
                                "help": "Size of figure ((width, height)).",
                                "hintText": "",
                                "type": ""
                            },
                            "saveData": {
                                "label": "Save data",
                                "suggestions": "",
                                "help": "File name where to save the final data used to generate the figure (None|'fileName').",
                                "hintText": "",
                                "type": ""
                            },
                            "saveFig": {
                                "label": "Figure Name",
                                "suggestions": "",
                                "help": "File name where to save the figure (None|'fileName').",
                                "hintText": "",
                                "type": ""
                            },
                            "showFig": {
                                "label": "Show figure",
                                "suggestions": "",
                                "help": "Whether to show the figure or not (True|False).",
                                "hintText": "",
                                "type": ""
                            }
                        }
                    },
                    "plotTraces": {
                        "label": "Plot Traces",
                        "suggestions": "",
                        "help": "Plot recorded traces (specified in simConfig.recordTraces).",
                        "hintText": "",
                        "children": {
                            "include": {
                                "label": "trace ",
                                "suggestions": "",
                                "help": "List of cells to include (['all'|,'allCells'|,'allNetStims'|,120|,'L4'|,('L2', 56)|,('L5',[4,5,6])])",
                                "hintText": "",
                                "type": "list"
                            },
                            "timeRange": {
                                "label": "time Range",
                                "suggestions": "",
                                "help": "Time range for shown Traces ; if None shows all ([start,stop])",
                                "hintText": "",
                                "type": "list(int)"
                            },
                            "overlay": {
                                "label": "overlay data",
                                "suggestions": "",
                                "help": "Whether to overlay the data lines or plot in separate subplots (True|False).",
                                "hintText": "",
                                "type": "bool"
                            },
                            "oneFigPer": {
                                "label": "one figure per cell",
                                "suggestions": "",
                                "help": "Whether to plot one figure per cell or per trace (showing multiple cells) ('cell'|'trace').",
                                "hintText": "",
                                "options": [
                                    "cell",
                                    "traces"
                                ],
                                "type": "str"
                            },
                            "rerun": {
                                "label": "re-run simulation",
                                "suggestions": "",
                                "help": "rerun simulation so new set of cells gets recorded (True|False).",
                                "hintText": "",
                                "type": "bool"
                            },
                            "figSize": {
                                "label": "Figure size",
                                "suggestions": "",
                                "help": "Size of figure ((width, height))",
                                "hintText": "",
                                "type": ""
                            },
                            "saveData": {
                                "label": "Save data",
                                "suggestions": "",
                                "help": "File name where to save the final data used to generate the figure (None|'fileName').",
                                "hintText": "",
                                "type": ""
                            },
                            "saveFig": {
                                "label": "Figure Name",
                                "suggestions": "",
                                "help": "File name where to save the figure (None|'fileName')",
                                "hintText": "",
                                "type": ""
                            },
                            "showFig": {
                                "label": "Show figure",
                                "suggestions": "",
                                "help": "Whether to show the figure or not (True|False).",
                                "hintText": "",
                                "type": ""
                            }
                        }
                    },
                    "plotLFP": {
                        "label": "Plot LFP",
                        "suggestions": "",
                        "help": "Plot LFP / extracellular electrode recordings (time-resolved, power spectral density, time-frequency and 3D locations).",
                        "hintText": "",
                        "children": {
                            "electrodes": {
                                "label": "electrode",
                                "suggestions": "",
                                "help": " List of electrodes to include; 'avg'=avg of all electrodes; 'all'=each electrode separately (['avg', 'all', 0, 1, ...]).",
                                "hintText": "",
                                "type": "list"
                            },
                            "plots": {
                                "label": "plot types to show",
                                "suggestions": "",
                                "help": "list of plot types to show (['timeSeries', 'PSD', 'timeFreq', 'locations']).",
                                "hintText": "",
                                "options": [
                                    "timeSeries", 
                                    "PSD", 
                                    "timeFreq", 
                                    "location"
                                ],
                                "type": "str"
                            },
                            "timeRange": {
                                "label": "time Range",
                                "suggestions": "",
                                "help": "Time range for shown Traces ; if None shows all ([start,stop])",
                                "hintText": "",
                                "type": "list(int)"
                            },
                            "NFFT": {
                                "label": "number of point",
                                "suggestions": "",
                                "help": "The number of data points used in each block for the FFT (power of 2) (float)",
                                "hintText": "",
                                "type": "float"
                            },
                            "noverlap": {
                                "label": "number of overlap points",
                                "suggestions": "",
                                "help": "Number of points of overlap between segments (int, < nperseg).",
                                "hintText": "",
                                "type": ""
                            },
                            "maxFreq": {
                                "label": "maximum Frequency",
                                "suggestions": "",
                                "help": "Maximum frequency shown in plot for PSD and time-freq (float).",
                                "hintText": "",
                                "type": "float"
                            },
                            "nperseg": {
                                "label": "lenght per segment",
                                "suggestions": "",
                                "help": "Length of each segment for time-freq (int).",
                                "hintText": "",
                                "type": "int"
                            },
                            "smooth": {
                                "label": "window size",
                                "suggestions": "",
                                "help": "Window size for smoothing; no smoothing if 0 (int).",
                                "hintText": "",
                                "type": "int"
                            },
                            "separation": {
                                "label": "separation Factor",
                                "suggestions": "",
                                "help": "Separation factor between time-resolved LFP plots; multiplied by max LFP value (float).",
                                "hintText": "",
                                "type": "float"
                            },
                            "includeAxon": {
                                "label": "include Axon",
                                "suggestions": "",
                                "help": "Whether to show the axon in the location plot (boolean).",
                                "hintText": "",
                                "type": "bool"
                            },
                            "figSize": {
                                "label": "Figure size",
                                "suggestions": "",
                                "help": "Size of figure ((width, height))",
                                "hintText": "",
                                "type": ""
                            },
                            "saveData": {
                                "label": "Save data",
                                "suggestions": "",
                                "help": "File name where to save the final data used to generate the figure (None|'fileName').",
                                "hintText": "",
                                "type": ""
                            },
                            "saveFig": {
                                "label": "Figure Name",
                                "suggestions": "",
                                "help": "File name where to save the figure (None|'fileName')",
                                "hintText": "",
                                "type": ""
                            },
                            "showFig": {
                                "label": "Show figure",
                                "suggestions": "",
                                "help": "Whether to show the figure or not (True|False).",
                                "hintText": "",
                                "type": ""
                            }
                        }
                    },
                    "plotShape": {
                        "label": "Plot Shape",
                        "suggestions": "",
                        "help": "",
                        "hintText": "Plot 3D cell shape using Matplotlib or NEURON Interviews PlotShape.",
                        "children": {
                            "includePre": {
                                "label": "population (or cell by index) to presyn",
                                "suggestions": "",
                                "help": "List of cells to include (['all'|,'allCells'|,'allNetStims'|,120|,'L4'|,('L2', 56)|,('L5',[4,5,6])])",
                                "hintText": "",
                                "type": "list"
                            },
                            "includePost": {
                                "label": "population (or cell by index) to postsyn",
                                "suggestions": "",
                                "help": "List of cells to include (['all'|,'allCells'|,'allNetStims'|,120|,'L4'|,('L2', 56)|,('L5',[4,5,6])])",
                                "hintText": "",
                                "type": "list"
                            },
                            "synStyle": {
                                "label": "synaptic marker style",
                                "suggestions": "",
                                "help": "Style of marker to show synapses (Matplotlib markers).",
                                "hintText": "",
                                "type": "str"
                            },
                            "dist": {
                                "label": "3D distance",
                                "suggestions": "",
                                "help": "3D distance (like zoom).",
                                "hintText": "",
                                "type": "float"
                            },
                            "synSize": {
                                "label": "synapses marker size",
                                "suggestions": "",
                                "help": "Size of marker to show synapses.",
                                "hintText": "",
                                "type": "float"
                            },
                            "cvar": {
                                "label": "variable to represent in shape plot",
                                "suggestions": "",
                                "help": "Variable to represent in shape plot ('numSyns'|'weightNorm').",
                                "hintText": "",
                                "options": [
                                    "numSyns",
                                    "weightNorm"
                                ],
                                "type": "str"
                            },
                            "cvals": {
                                "label": "value to represent in shape plot",
                                "suggestions": "",
                                "help": "List of values to represent in shape plot; must be same as num segments (list of size num segments; ).",
                                "hintText": "",
                                "type": "list"
                            },
                            "iv": {
                                "label": "use NEURON iv",
                                "suggestions": "",
                                "help": "Use NEURON Interviews (instead of matplotlib) to show shape plot (True|False).",
                                "hintText": "",
                                "type": "bool"
                            },
                            "ivprops": {
                                "label": "properties for iv",
                                "suggestions": "",
                                "help": "Dict of properties to plot using Interviews (dict).",
                                "hintText": "",
                                "type": "dict"
                            },
                            "showSyns": {
                                "label": "show synaptic connections in 3D",
                                "suggestions": "",
                                "help": "Show synaptic connections in 3D (True|False).",
                                "hintText": "",
                                "type": "bool"
                            },
                            "bkgColor": {
                                "label": "background color",
                                "suggestions": "",
                                "help": "RGBA list/tuple with bakcground color eg. (0.5, 0.2, 0.1, 1.0) (list/tuple with 4 floats).",
                                "hintText": "",
                                "type": "list(float)"
                            },
                            "showElectrodes": {
                                "label": "show electrodes",
                                "suggestions": "",
                                "help": "Show electrodes in 3D (True|False).",
                                "hintText": "",
                                "type": "bool"
                            },
                            "includeAxon": {
                                "label": "include Axon in shape plot",
                                "suggestions": "",
                                "help": "Include axon in shape plot (True|False).",
                                "hintText": "",
                                "type": "bool"
                            },
                            "figSize": {
                                "label": "Figure size",
                                "suggestions": "",
                                "help": "Size of figure ((width, height))",
                                "hintText": "",
                                "type": ""
                            },
                            "saveData": {
                                "label": "Save data",
                                "suggestions": "",
                                "help": "File name where to save the final data used to generate the figure (None|'fileName').",
                                "hintText": "",
                                "type": ""
                            },
                            "saveFig": {
                                "label": "Figure Name",
                                "suggestions": "",
                                "help": "File name where to save the figure (None|'fileName')",
                                "hintText": "",
                                "type": ""
                            },
                            "showFig": {
                                "label": "Show figure",
                                "suggestions": "",
                                "help": "Whether to show the figure or not (True|False).",
                                "hintText": "",
                                "type": ""
                            }
                        }
                    },
                    "plot2Dnet": {
                        "label": "Plot 2D net",
                        "suggestions": "",
                        "help": "Plot 2D representation of network cell positions and connections.",
                        "hintText": "",
                        "children": {
                            "include": {
                                "label": "population (or cell by index) to 2Dnet",
                                "suggestions": "",
                                "help": "List of cells to show (['all'|,'allCells'|,'allNetStims'|,120|,'L4'|,('L2', 56)|,('L5',[4,5,6])]).",
                                "hintText": "",
                                "type": "list"
                            },
                            "showConns": {
                                "label": "show connections",
                                "suggestions": "",
                                "help": "Whether to show connections or not (True|False).",
                                "hintText": "",
                                "type": "bool"
                            },
                            "view": {
                                "label": "perspective view",
                                "suggestions": "",
                                "help": "Perspective view, either front ('xy') or top-down ('xz').",
                                "hintText": "",
                                "options": [
                                    "xy",
                                    "xz"
                                ],
                                "type": "str"
                            },
                            "figSize": {
                                "label": "Figure size",
                                "suggestions": "",
                                "help": "Size of figure ((width, height))",
                                "hintText": "",
                                "type": ""
                            },
                            "saveData": {
                                "label": "Save data",
                                "suggestions": "",
                                "help": "File name where to save the final data used to generate the figure (None|'fileName').",
                                "hintText": "",
                                "type": ""
                            },
                            "saveFig": {
                                "label": "Figure Name",
                                "suggestions": "",
                                "help": "File name where to save the figure (None|'fileName')",
                                "hintText": "",
                                "type": ""
                            },
                            "showFig": {
                                "label": "Show figure",
                                "suggestions": "",
                                "help": "Whether to show the figure or not (True|False).",
                                "hintText": "",
                                "type": ""
                            }
                        }
                    },
                    "plotConn": {
                        "label": "Plot Connectivity",
                        "suggestions": "",
                        "help": "Plot network connectivity.",
                        "hintText": "",
                        "children": {
                            "include": {
                                "label": "population (or cells by index) to connectivity",
                                "suggestions": "",
                                "help": "List of cells to show (['all'|,'allCells'|,'allNetStims'|,120|,'L4'|,('L2', 56)|,('L5',[4,5,6])]).",
                                "hintText": "",
                                "type": "list"
                            },
                            "feature": {
                                "label": "feature to show",
                                "suggestions": "",
                                "help": "Feature to show in connectivity matrix; the only features applicable to groupBy='cell' are 'weight', 'delay' and 'numConns'; 'strength' = weight * probability ('weight'|'delay'|'numConns'|'probability'|'strength'|'convergence'|'divergence')g.",
                                "hintText": "",
                                "options": [
                                    "weight",
                                    "delay",
                                    "numConns",
                                    "probability",
                                    "strength",
                                    "convergency",
                                    "divergency"
                                ],
                                "type": "str"
                            },
                            "groupBy": {
                                "label": "group by",
                                "suggestions": "",
                                "help": "Show matrix for individual cells or populations ('pop'|'cell').",
                                "hintText": "",
                                "options": [
                                    "pop", 
                                    "cell"
                                ],
                                "type": ""
                            },
                            "orderBy": {
                                "label": "order by",
                                "suggestions": "",
                                "help": "Unique numeric cell property to order x and y axes by, e.g. 'gid', 'ynorm', 'y' (requires groupBy='cells') ('gid'|'y'|'ynorm'|...).",
                                "hintText": "",
                                "options": [
                                    "gid", 
                                    "y", 
                                    "ynorm"
                                ],
                                "type": ""
                            },
                            "figSize": {
                                "label": "Figure size",
                                "suggestions": "",
                                "help": "Size of figure ((width, height))",
                                "hintText": "",
                                "type": ""
                            },
                            "saveData": {
                                "label": "Save data",
                                "suggestions": "",
                                "help": "File name where to save the final data used to generate the figure (None|'fileName').",
                                "hintText": "",
                                "type": ""
                            },
                            "saveFig": {
                                "label": "Figure Name",
                                "suggestions": "",
                                "help": "File name where to save the figure (None|'fileName')",
                                "hintText": "",
                                "type": ""
                            },
                            "showFig": {
                                "label": "Show figure",
                                "suggestions": "",
                                "help": "Whether to show the figure or not (True|False).",
                                "hintText": "",
                                "type": ""
                            }
                        }
                    },
                    "granger": {
                        "label": "Granger",
                        "suggestions": "",
                        "help": "Calculate and optionally plot Granger Causality.",
                        "hintText": "",
                        "children": {
                            "cells1": {
                                "label": "population (or cell by index) to subset 1",
                                "suggestions": "",
                                "help": "Subset of cells from which to obtain spike train 1 (['all',|'allCells','allNetStims',|,120,|,'E1'|,('L2', 56)|,('L5',[4,5,6])]).",
                                "hintText": "",
                                "type": "list"
                            },
                            "cells2": {
                                "label": "population (or cell by index cell) to subset 2",
                                "suggestions": "",
                                "help": "Subset of cells from which to obtain spike train 2 (['all',|'allCells','allNetStims',|,120,|,'E1'|,('L2', 56)|,('L5',[4,5,6])]).",
                                "hintText": "",
                                "type": "list"
                            },
                            "spks1": {
                                "label": "spike times to train 1",
                                "suggestions": "",
                                "help": "Spike train 1; list of spike times; if omitted then obtains spikes from cells1 (list).",
                                "hintText": "",
                                "type": "list"
                            },
                            "spks2": {
                                "label": "spike times to train 2",
                                "suggestions": "",
                                "help": "Spike train 2; list of spike times; if omitted then obtains spikes from cells1 (list).",
                                "hintText": "",
                                "type": "list"
                            },
                            "timeRange": {
                                "label": "time Range",
                                "suggestions": "",
                                "help": "Range of time to calculate nTE in ms ([min, max]).",
                                "hintText": "",
                                "type": "list(int)"
                            },
                            "binSize": {
                                "label": "bin size",
                                "suggestions": "",
                                "help": "Bin size used to convert spike times into histogram (int).",
                                "hintText": "",
                                "type": "int"
                            },
                            "label1": {
                                "label": "label for train 1",
                                "suggestions": "",
                                "help": "Label for spike train 1 to use in plot (string).",
                                "hintText": "",
                                "type": "str"
                            },
                            "label2": {
                                "label": "label for train 2",
                                "suggestions": "",
                                "help": "Label for spike train 2 to use in plot (string).",
                                "hintText": "",
                                "type": "str"
                            },
                            "figSize": {
                                "label": "Figure size",
                                "suggestions": "",
                                "help": "Size of figure ((width, height))",
                                "hintText": "",
                                "type": ""
                            },
                            "saveData": {
                                "label": "Save data",
                                "suggestions": "",
                                "help": "File name where to save the final data used to generate the figure (None|'fileName').",
                                "hintText": "",
                                "type": ""
                            },
                            "saveFig": {
                                "label": "Figure Name",
                                "suggestions": "",
                                "help": "File name where to save the figure (None|'fileName')",
                                "hintText": "",
                                "type": ""
                            },
                            "showFig": {
                                "label": "Show figure",
                                "suggestions": "",
                                "help": "Whether to show the figure or not (True|False).",
                                "hintText": "",
                                "type": ""
                            }
                        }
                    },
                    "nTE": {
                        "label": "Normalize Transfer Entropy",
                        "suggestions": "",
                        "help": "Calculate normalized transfer entropy.",
                        "hintText": "",
                        "children": {
                            "cell1": {
                                "label": "Cell Subset 1",
                                "suggestions": "",
                                "help": "Subset of cells from which to obtain spike train 1 (['all',|'allCells','allNetStims',|,120,|,'E1'|,('L2', 56)|,('L5',[4,5,6])]).",
                                "hintText": "",
                                "type": "list"
                            },
                            "cell2": {
                                "label": "Cell Subset 2",
                                "suggestions": "",
                                "help": "Subset of cells from which to obtain spike train 2 (['all',|'allCells','allNetStims',|,120,|,'E1'|,('L2', 56)|,('L5',[4,5,6])]).",
                                "hintText": "",
                                "type": "list"
                            },
                            "spks1": {
                                "label": "Spike train 1",
                                "suggestions": "",
                                "help": "Spike train 1; list of spike times; if omitted then obtains spikes from cells1 (list).",
                                "hintText": "",
                                "type": "list"
                            },
                            "spks2": {
                                "label": "Spike train 2",
                                "suggestions": "",
                                "help": "Spike train 2; list of spike times; if omitted then obtains spikes from cells1 (list).",
                                "hintText": "",
                                "type": "list"
                            },
                            "timeRange": {
                                "label": "Time Range",
                                "suggestions": "",
                                "help": "Range of time to calculate nTE in ms ([min, max]).",
                                "hintText": "",
                                "type": "list(int)"
                            },
                            "binSize": {
                                "label": "Bin size",
                                "suggestions": "",
                                "help": "Bin size used to convert spike times into histogram (int).",
                                "hintText": "",
                                "type": "int"
                            },
                            "numShuffle": {
                                "label": "Number of Shuffles",
                                "suggestions": "",
                                "help": "Number of times to shuffle spike train 1 to calculate TEshuffled; note: nTE = (TE - TEShuffled)/H(X2F|X2P) (int).",
                                "hintText": "",
                                "type": "int"
                            },
                            "figSize": {
                                "label": "Figure size",
                                "suggestions": "",
                                "help": "Size of figure ((width, height))",
                                "hintText": "",
                                "type": ""
                            },
                            "saveData": {
                                "label": "Save data",
                                "suggestions": "",
                                "help": "File name where to save the final data used to generate the figure (None|'fileName').",
                                "hintText": "",
                                "type": "str"
                            },
                            "saveFig": {
                                "label": "Figure Name",
                                "suggestions": "",
                                "help": "File name where to save the figure (None|'fileName')",
                                "hintText": "",
                                "type": "str"
                            },
                            "showFig": {
                                "label": "Show figure",
                                "suggestions": "",
                                "help": "Whether to show the figure or not (True|False).",
                                "hintText": "",
                                "type": "str"
                            }
                        }
                    }
                }
            }
        }
    }
}