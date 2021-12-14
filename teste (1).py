# import geopandas as gpd
# import folium
# import matplotlib.pyplot as plt
#
#
# def teste():
#
#     # Lê os dados
#     url = 'https://geoservicos.pbh.gov.br/geoserver/wfs?service=WFS&version=1.0.0&request=GetFeature&typeName=ide_bhgeo:BAIRRO&srsName=EPSG:31983&outputFormat=application%2Fjson'
#     gdf = gpd.read_file(url)
#
#     # Você pode agora ver os dados em formato df
#     gdf
#
#     # Verifica se os dados estão certos
#     fig, ax = plt.subplots(figsize=(10, 10))
#     gdf.plot(ax=ax)
#
#     # Converte para lat-long
#     gdf = gdf.to_crs(epsg=4326)
#
#     # Faz o mapa
#     bh = gdf[['id', 'geometry', 'NOME']]
#     x_map = bh.geometry.centroid.x.mean()
#     y_map = bh.geometry.centroid.y.mean()
#     mymap = folium.Map(location=[y_map, x_map], zoom_start=11, tiles='OpenStreetMap')
#
#     # Adiciona polígonos
#     folium.GeoJson(
#         gdf
#     ).add_to(mymap)
#
#     mymap
def teste():
    pass

