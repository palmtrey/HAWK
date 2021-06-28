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
    plotter.Plotter.findWaterfront()

    # Plot waterfront properties
    plt.figure()
    ax = plt.axes(projection=ccrs.Orthographic())
    plotter.Plotter.plotMaranacookLake(ax, 'blue')
    plotter.Plotter.plotMaranacookIslands(ax, 'green')
    plotter.Plotter.plotAddresses(ax, 'red')
    plt.show()
