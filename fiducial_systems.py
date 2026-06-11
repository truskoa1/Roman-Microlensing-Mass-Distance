'''
This script defines the 3 fiducial systems that we will use for our analysis. 
With the source star at a fixed 8kpc, we will only vary the lens mass and 
lens-source distance here to see how different system setups affect our results.

'''

systems = {
    "0p2Msun_3kpc": {
        "M_L": 0.2,
        "D_L": 3.0,
        "D_S": 8.0
    },
    "0p8Msun_7kpc": {
        "M_L": 0.8,
        "D_L": 7.0,
        "D_S": 8.0
    },
    "0p5Msun_7kpc": {
        "M_L": 0.5,
        "D_L": 7.0,
        "D_S": 8.0
    }
}
