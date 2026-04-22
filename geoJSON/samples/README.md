# Sample geoJSON

There are two geoJSON samples:

`small_geoJSON_sample_GB-CAM_2`: This is a really small, simple sample best used just for viewing the data structure: two map features, a single flood event and all information taken from just one Section 19 report about flooding in Barrington, Cambridgeshire
`large_geoJSON_sample_GB-KEN_all`: This is a more complex sample generated using (nearly) all the Kent Section 19 reports, resulting in 400+ map features. It is quite a bit more complex as individual map features may have experienced more than one event, and have information taken from more than one Section 19 report.

The geoJSON properties are structured as follows:

`"properties`" : {  
&nbsp;&nbsp;&nbsp;&nbsp;`"name"` : map feature name  
&nbsp;&nbsp;&nbsp;&nbsp;`"gross_type"` : category denoting the rough level of granularity of the feature, with three main levels: `admin` (administrative unit, e.g. County), `settlement` (city, town, village, parish or ward), `asset_or_street`. There are also `hydro` (for hydrological features) and `other` categories (e.g. other physical features or local toponyms) at the moment – we can decide what to do with these later.   
&nbsp;&nbsp;&nbsp;&nbsp;`"medium_type"` : name of the class of the place name record in the original database in snake case  
&nbsp;&nbsp;&nbsp;&nbsp;`"fine_type"` : OpenStreetMap [map feature type](https://wiki.openstreetmap.org/wiki/Map_features), where available (not all map features in the dataset are present in OpenStreetMap, and not all coordinates are derived from it)  
&nbsp;&nbsp;&nbsp;&nbsp;`"events"` : \[  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`"start_date"` : event start date (`null` if there is only a text description of when the event happened)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`"end_date"` : event end date (`null` if there is only a text description of when the event happened)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`"when_desc"` : text description of when the event happened  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`"info"` : \[  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`"text"` : information about what happened during the flood event in the place  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`"is_quant"` : is intended to capture quantitative information  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`"link"` : report URL (this is illustrative at the moment as we will need to set up a public repository for the reports)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`"page"` : page number (may not reflect nominal page numbering within the PDF – the front cover of every report is deemed page 1)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; \]  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}  
&nbsp;&nbsp;&nbsp;&nbsp;\]  
}

Example:  
`"properties`" : {  
&nbsp;&nbsp;&nbsp;&nbsp;`"name"`: "Barrington",  
&nbsp;&nbsp;&nbsp;&nbsp;`"gross_type"`: "settlement",  
&nbsp;&nbsp;&nbsp;&nbsp;`"medium_type"`: "urban",  
&nbsp;&nbsp;&nbsp;&nbsp;`"fine_type"`: "administrative",  
&nbsp;&nbsp;&nbsp;&nbsp;`"events"`: \[  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`"start_date"`: "2015-07-17",  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`"end_date"`: "2015-07-17",  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`"when_desc"`: "17 Jul 2015",   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`"info"`: \[  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`"text"`: "Formal flood incident recorded affecting various locations in Barrington on 17 July 2015 (Formal Flood Investigation reference FI/1/60). Risk Management Authorities recorded as Environment Agency and Cambridgeshire County Council.",  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`"is_quant"`: false,  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `"link"`: "021_Cambridgeshire County/021_2014_Cambridgeshire County/Barrington flood investigation.pdf",  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`"page"`: 2  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;...  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\]  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}  
&nbsp;&nbsp;&nbsp;&nbsp;\]  
}
