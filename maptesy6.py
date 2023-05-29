import pandas as pd
import folium
from geopy import distance
import requests

# URL to your CSV file in your GitHub repository
locations_url = 'https://raw.githubusercontent.com/testpythonhtmlcoder567/mapdata_test/main/locations.csv'
depth_url = 'https://raw.githubusercontent.com/testpythonhtmlcoder567/mapdata_test/main/depth.csv'

df_locations = pd.read_csv(locations_url)
df_depth = pd.read_csv(depth_url)

# create a list of location points from the latitude and longitude columns
locations = list(zip(df_locations['latitude'], df_locations['longitude']))
names = df_locations['name'].tolist()
depths = df_depth['depth'].tolist()

# create a map centered at the mean latitude and longitude
m = folium.Map(location=locations[0], zoom_start=10)

# plot the location points on the map
for i, location in enumerate(locations):
    # create a popup with the image, location, and depth information
    image_url = f'https://raw.githubusercontent.com/testpythonhtmlcoder567/pothole_images/main/images/image{i+1}.jpg'
    name = names[i]
    depth = depths[i]
    popup_html = f'<b>{name}</b><br>Latitude: {location[0]}<br>Longitude: {location[1]}<br>Depth: {depth}cm<br><img src="{image_url}" alt="{name}" width="300px">'
    popup = folium.Popup(popup_html)
    # create a marker at the location and add the popup to it
    folium.Marker(location, popup=popup).add_to(m)
    if i > 0:
        prev_location = locations[i-1]
        dist = round(distance.distance(prev_location, location).miles, 2)
        popup = f'<b>Distance from {names[i-1]} to {names[i]}:</b> {dist} miles'
        line = folium.PolyLine([prev_location, location], popup=popup, color='red', weight=5, opacity=1)
        line.add_to(m)
        midpoint = [(prev_location[0] + location[0])/2, (prev_location[1] + location[1])/2]
        marker = folium.Marker(midpoint, popup=f'{dist} miles', icon=folium.Icon(color='red')).add_to(m)

# save the map to an HTML file
m.save('map.html')

from github import Github

# authenticate with GitHub using a personal access token
g = Github("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")

# get the repository
repo = g.get_repo("testpythonhtmlcoder567/testpythonhtmlcoder567.github.io")

# get the file you want to update
file = repo.get_contents("map.html")

# update the contents of the file
with open("D:/sampleimg/pythonProject/map.html", "r") as f:
    file_contents = f.read()
repo.update_file(file.path, "Update map.html", file_contents, file.sha)