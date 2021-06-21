import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import os
import plotter
import updater


# HAWK entry point
if __name__ == '__main__':

    # Update the data in the project using updater.py
    updateHandler = updater.Updater()
    updateHandler.update()

    plotterHandler = plotter.Plotter()
    plotterHandler.findWaterfront()

    plt.figure()
    ax = plt.axes(projection=ccrs.Orthographic())
    plotterHandler.plotMaranacookLake(ax, 'blue')
    plotterHandler.plotMaranacookIslands(ax, 'green')
    plotterHandler.plotAddresses(ax, 'red')
    plt.show()


    # Next, compare the addresses to the coordinates using
    # waterfront_separator.py

    # Finally, plot the waterfront addresses for a map of addresses around
    # the lake.
