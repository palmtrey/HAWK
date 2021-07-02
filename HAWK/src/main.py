import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import os
import plotter
import startup.updater as updater


# HAWK entry point
if __name__ == '__main__':

    # Update the data in the project using updater.py
    updater.update()

    # Find waterfront properties in updated data
    plotter.findWaterfront('maranacook_lake', ['04364', '04355'], distance_from = 100)

    #plotter.findWaterfront('cobbossee_lake', ['04351'])

    # Plot waterfront properties
    plt.figure()
    ax = plt.axes(projection=ccrs.Orthographic())
    plotter.plotMaranacookLake(ax, 'blue', 'maranacook_lake')
    plotter.plotMaranacookIslands(ax, 'green', 'maranacook_lake')
    plotter.plotAddresses(ax, 'red', 'maranacook_lake')
    plt.show()
