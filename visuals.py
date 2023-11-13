import os

#import matplotlib.pyplot as plt 
import plotly.graph_objects as go
#from plotly.subplots import make_subplots
from dotenv import find_dotenv, load_dotenv


class MakeVisualisation:
    load_dotenv(find_dotenv())

    def make_mapboxplot(self, df, coastline):
        mapbox_center_lon = 24.386058
        mapbox_center_lat = -32.2
        mapbox_zoom = 4.5
        mapbox_access_token = os.environ.get('MAPBOXTOKEN')

        color = df['colours']
        category = df['status']
        cats = {k: str(v) for k, v in zip(set(color), set(category))}

        fig = go.Figure(
            go.Scattermapbox(
            mode = "lines+markers+text",
            )
        )

        fig.update_layout(
            mapbox = {
                'style': "light",
                'accesstoken': mapbox_access_token,
                'center': { 'lon': mapbox_center_lon, 'lat': mapbox_center_lat},
                'zoom': mapbox_zoom,       
                'layers': [{
                    'source': {
                        'type': "FeatureCollection",
                        'features': [
                            {
                                'type': "Feature",
                                'geometry': {
                                'type': "MultiPolygon",
                                'coordinates': [[coastline['coords_list']]]
                            }
                        }]
                    },
                    'type': "line", 'below': "traces", 'color': "silver"}]},
            margin = {'l':0, 'r':0, 'b':0, 't':0},
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=0.96,
                xanchor="right",
                x=1
            ),
        )

        for col in df['colours'].unique():
            df_color = df[df['colours'] == col].reset_index(drop=True)
            vessels = list(df_color['vessel_name'])
            dates = list(df_color['date'])
            ports = list(df_color['port'])
            text = []

            for (a, b, p) in zip(vessels, dates, ports):
                text.append(f'{a}<br>{p}: {b}')

            fig.add_trace(go.Scattermapbox(
                mode='markers+text',
                lat=df_color['lat'],
                lon=df_color['lon'],
                text=text,
                textposition = "bottom right",
                name=df_color['status'][0],
                #name=cats[col],
                marker=dict(color=col, size=16), 
                customdata=df_color['vessel_name'],
                hovertemplate='<b>%{customdata}</b>'
                )
            )

        return fig

    def make_mapboxplot_markersonly(self, df, coastline):
        mapbox_center_lon = 24.386058
        mapbox_center_lat = -32.2
        mapbox_zoom = 4.5
        mapbox_access_token = os.environ.get('MAPBOXTOKEN')

        color = df['colours']
        category = df['status']
        cats = {k: str(v) for k, v in zip(set(color), set(category))}

        fig = go.Figure(
            go.Scattermapbox(
            mode = "lines+markers+text",
            )
        )

        fig.update_layout(
            mapbox = {
                'style': "light",
                'accesstoken': mapbox_access_token,
                'center': { 'lon': mapbox_center_lon, 'lat': mapbox_center_lat},
                'zoom': mapbox_zoom, },
            margin = {'l':0, 'r':0, 'b':0, 't':0},
            legend=dict(
                orientation="h",
                #entrywidth=70,
                yanchor="bottom",
                y=0.96,
                xanchor="right",
                x=1
            ),
        )

        df['colours'] ='navy'
        for c in df['colours'].unique():
            df_color = df[df['colours'] == c].reset_index(drop=True)
            vessels = list(df_color['vessel_name'])
            dates = list(df_color['date'])
            ports = list(df_color['port'])
            text = []

            for (a, b, p) in zip(vessels, dates, ports):
                text.append(f'{a}<br>{p}: {b}')

            fig.add_trace(go.Scattermapbox(
                mode='markers+text',
                lat=df_color['lat'],
                lon=df_color['lon'],
                text=text,
                textposition = "bottom right",
                #name=cats[c],
                marker=dict(color=c, size=12), 
                customdata=df_color['vessel_name'],
                hovertemplate='<b>%{customdata}</b>'
                )
            )

        return fig

    def make_mapboxplot_geofenceonly(self, df, coastline):
        mapbox_center_lon = 24.386058
        mapbox_center_lat = -32.2
        mapbox_zoom = 4.5
        mapbox_access_token = os.environ.get('MAPBOXTOKEN')
        print(mapbox_access_token)

        fig = go.Figure(
            go.Scattermapbox(
            mode = "lines+markers+text",
            )
        )

        fig.update_layout(
            mapbox = {
                'style': "light",
                'accesstoken': mapbox_access_token,
                'center': { 'lon': mapbox_center_lon, 'lat': mapbox_center_lat},
                'zoom': mapbox_zoom,       
                'layers': [{
                    'source': {
                        'type': "FeatureCollection",
                        'features': [
                            {
                                'type': "Feature",
                                'geometry': {
                                'type': "MultiPolygon",
                                'coordinates': [[coastline['coords_list']]]
                            }
                        }]
                    },
                    'type': "line", 'below': "traces", 'color': "navy"}]},
            margin = {'l':0, 'r':0, 'b':0, 't':0},
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=0.96,
                xanchor="right",
                x=1
            ),
        )


        return fig
