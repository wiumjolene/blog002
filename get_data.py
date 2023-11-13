from xml.dom import minidom
from dash import html

import pandas as pd
from shapely.geometry import Point, Polygon


class ManageCoordinates:

    def get_coastline(self):
        data=open('RSACoast.gpx')
        xmldoc = minidom.parse(data)
        track = xmldoc.getElementsByTagName('trkpt')
        n_track=len(track)

        lon_list=[]
        lat_list=[]
        coords=[]
        coordsl=[]

        for s in range(n_track):
            lon,lat=track[s].attributes['lon'].value,track[s].attributes['lat'].value
            lat=float(lat)
            lon=float(lon)
            lat_list.append(lat)
            lon_list.append(lon)
            coords.append((lat,lon))
            coordsl.append([lon, lat])

        coastline={'lat_list':lat_list,
                'lon_list':lon_list,
                'coords':coords,
                'coords_list':coordsl}
        
        return coastline

    def check_point(self, point, coords):
        # Register a Shapely Point
        p = Point(point)

        # Create a RSA Coastline Bounds
        poly = Polygon(coords)
        
        # Return True/False
        return p.within(poly)

    def manage_vessels(self):
        # Dummy data
        visits = [['ON ROUTE', 'SANTA ISABEL', -27.8447100, 12.6333300, '2023-04-13'],
            ['CAPE TOWN', 'SANTA ISABEL', -33.9102200, 18.4481100, '2023-04-08'],
            ['CAPE TOWN ANCH', 'SANTA ISABEL', -33.8422800, 18.4062800, '2023-03-31'],
            ['DURBAN', 'SANTA ISABEL', -29.8803000, 31.0279100, '2023-03-25'],
            ['COEGA', 'SANTA ISABEL', -33.7983300, 25.6825600, '2023-03-22']]
        
        coords=self.get_coastline()['coords']
        data=[]

        for visit in visits:
            point=(visit[2],visit[3])
            
            inrsa=self.check_point(point, coords)
            if inrsa:
                colour='red'
            else:
                colour='green'

            if inrsa:
                status='Not Sailed'
                
            else:
                status='Sailed'

            visit.append(status)
            visit.append(colour)
            data.append(visit)

        columns = ['port', 'vessel_name', 'lat', 'lon', 'date', 'status', 'colours']
        df = pd.DataFrame(data=data, columns=columns)

        return df

    def get_text_for_dash(self):
        text = html.P([f"""
        This webapp compliments a blog post to illustrate the power of using Python to automate and enhance data quality. """,
        html.Br(),
        """
        The use case explained by the post is to determine if a vessel is in-or-outside an odly shaped geofenced area.""",
        html.Br(),
        html.Br(),
        """
        In the visual on the right, red markers indicate that a container vessel, the Santa Isabel, is still insde the demarketd geofence. """,
        html.Br(),
        """
        The green marker indicates that the vessel has departed the geofenced area and is now on route to Europe. """,
        html.Br(),
        html.Br(),
        """
        The source code to this post can be found on my """, html.A("GitHub", href='https://github.com/wiumjolene/blog002.git', target="_blank"),
        html.Br(),"""
        The blog post can be found on my """, html.A("Medium Articles", href='https://medium.com/@wiumjolene', target="_blank"),
        html.Br(),"""
        Feel free to reach out on my """, html.A("LinkedIn", href='https://www.linkedin.com/in/jolenewium/', target="_blank"),
        html.Br(),
        html.Br(),"""
        Happy Coding!
        """
        ])

        return text
