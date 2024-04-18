import json

import pandas as pd

with open('datas/public_bath.json', 'r') as file:
    data = json.load(file)
    public_baths = pd.json_normalize(data['features'])

public_baths['lon'] = public_baths['geometry.coordinates'].apply(lambda coordinates: coordinates[0])
public_baths['lat'] = public_baths['geometry.coordinates'].apply(lambda coordinates: coordinates[1])


public_baths.fillna('', inplace=True)
public_baths.drop(columns=['properties.@id', 'id', 'type', 'properties.amenity', 'geometry.type', 'properties.description:hu'], inplace=True)
print(public_baths)

data = {
    'public_baths': public_baths,
}
