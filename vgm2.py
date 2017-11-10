from googlemaps import Client
gmaps = Client('')
address = "HRBR layout,2nd block,kalyan nagar,bangalore"
destination = "apple fitness, kalyan nagar,bangalore,karnataka,india"
directions = gmaps.directions(address, destination)
for step in directions['Directions']['Routes'][0]['Steps']:
    print step['descriptionHtml']
