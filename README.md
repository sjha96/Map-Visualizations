# Map-Visualizations
Python based application that uses the Folium library to generate a world map. 

The map contains a polygon layer and a point layer on top of the base map layer with the functionality to toggle both on and off.

The point layer marks out all the volcanoes in the United States and is based off the Volcanoes_USA file in the repository. The points are color coded based on elevation. Green if under 1000m, orange if between 1000m and 3000m and red otherwise.

The polygon layer color codes the population distribution throughout the world. The polygons are also color-coded to represent the concentration of the populations. Yellow if population less than 10 million, orange if between 10 and 20 million and red otherwise. 

The final output map is available as ```Map1.html```
