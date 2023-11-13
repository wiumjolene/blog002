import pandas as pd

from visuals import MakeVisualisation
from get_data import ManageCoordinates

mv = MakeVisualisation()
mc = ManageCoordinates()

df=mc.manage_vessels()
coastline=mc.get_coastline()


fig = mv.make_mapboxplot(df, coastline)
fig.show()

fig = mv.make_mapboxplot_geofenceonly(df, coastline)
fig.show()

fig = mv.make_mapboxplot_markersonly(df, coastline)
fig.show()



