import json

import pandas as pd


# Make a dataframe and prepare it from path
def prepare_dataframe_from_geojson(path: str) -> pd.DataFrame:
    with open(path, 'r') as file:
        data = json.load(file)
        df = pd.json_normalize(data['features'])

    df['lon'] = df['geometry.coordinates'].apply(lambda coordinates: coordinates[0])
    df['lat'] = df['geometry.coordinates'].apply(lambda coordinates: coordinates[1])


    df.fillna('', inplace=True)
    df.drop(columns=['properties.@id', 'id', 'type', 'properties.amenity', 'geometry.type'], inplace=True)

    return df
