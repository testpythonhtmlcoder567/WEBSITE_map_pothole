import pandas as pd
import folium
from geopy import distance

# URL to your CSV file in your GitHub repository
csv_url = 'https://raw.githubusercontent.com/testpythonhtmlcoder567/mapdata_test/main/locations.csv'
df = pd.read_csv(csv_url)

# create a list of location points from the latitude and longitude columns
locations = list(zip(df['latitude'], df['longitude']))
names = df['name'].tolist()

# create a map centered at the mean latitude and longitude
m = folium.Map(location=locations[0], zoom_start=10)

# plot the location points on the map
for i, location in enumerate(locations):
    folium.Marker(location, popup=names[i]).add_to(m)
    if i > 0:
        prev_location = locations[i-1]
        dist = round(distance.distance(prev_location, location).miles, 2)
        popup = f'<b>Distance from {names[i-1]} to {names[i]}:</b> {dist} miles'
        line = folium.PolyLine([prev_location, location], popup=popup, color='red', weight=5, opacity=1)
        line.add_to(m)
        midpoint = [(prev_location[0] + location[0])/2, (prev_location[1] + location[1])/2]
        marker = folium.Marker(midpoint, popup=f'{dist} miles', icon=folium.Icon(color='red')).add_to(m)


marker_count = len(df)
print(marker_count)
# plot the location points on the map
for location in locations:
    lat, lon = location
    popup_text = f"Latitude: {lat}, Longitude: {lon}"
    folium.Marker(location, popup=popup_text).add_to(m)
for i, location in enumerate(locations):
    # create a popup with the image and location information
    image_url = f'https://raw.githubusercontent.com/testpythonhtmlcoder567/pothole_images/main/images/image{i+1}.jpg'
    name = names[i]
    popup_html = f'<b>{name}</b><br>Latitude: {location[0]}<br>Longitude: {location[1]}<br><img src="{image_url}" alt="{name}" width="300px">'
    popup = folium.Popup(popup_html)
    # create a marker at the location and add the popup to it
    folium.Marker(location, popup=popup).add_to(m)





# save the map to an HTML file
m.save('map.html')



