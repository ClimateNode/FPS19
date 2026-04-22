# Sample geoJSON

There are two geoJSON samples:

`small_geoJSON_sample_GB-CAM_2`: This is a really small, simple sample best used just for viewing the data structure: two map features, a single flood event and all information taken from just one Section 19 report about flooding in Barrington, Cambridgeshire
`large_geoJSON_sample_GB-KEN_all`: This is a more complex sample generated using (nearly) all the Kent Section 19 reports, resulting in 400+ map features. It is quite a bit more complex as individual map features may have experienced more than one event, and have information taken from more than one Section 19 report.

The geoJSON properties are structured as follows:

`"properties`" : {  
    `"name"` : map feature name  
}

