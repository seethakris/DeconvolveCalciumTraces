"""config.py: 

"""
    
__author__           = "Dilawar Singh"
__copyright__        = "Copyright 2015, Dilawar Singh and NCBS Bangalore"
__credits__          = ["NCBS Bangalore"]
__license__          = "GNU GPL"
__version__          = "1.0.0"
__maintainer__       = "Dilawar Singh"
__email__            = "dilawars@ncbs.res.in"
__status__           = "Development"

args_ = None

# NOTE: All units are S.I.

# Average firing rate of neuron in LHB, In Hz.
firing_rate_in_lhb = 50.0
blue_light_on = 5
blue_light_off = 5

# Average time interval of spike in network.
# This variable is used to sample spikes from spike rates generated by
# deconvolving fluroscence data.
spike_dt = 0.020
