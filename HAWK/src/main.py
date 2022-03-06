import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import os
import plotter
import startup.updater as updater
import startup.lake_extractor as extractor

# HAWK entry point
if __name__ == '__main__':
    """
    Some description of my function goes here
    """


    # Update the data in the project using updater.py
    #updater.update()

    #extractor.extractPolygons('../data/lake/apple_valley_lake')


    # Find waterfront properties in updated data
    plotter.findWaterfront('lower_narrows_pond', ['04364'], distance_from = 100)

    #plotter.findWaterfront('annabessacook_lake', ['04259', '04265', '04364'], distance_from = 100)

    # Plot waterfront properties
    
    # plt.figure()
    # ax = plt.axes(projection=ccrs.Orthographic())
    # plotter.plotMaranacookLake(ax, 'blue', 'maranacook_lake')
    # plotter.plotMaranacookIslands(ax, 'green', 'maranacook_lake')
    # plotter.plotAddresses(ax, 'red', 'maranacook_lake')
    # plt.show()
    
