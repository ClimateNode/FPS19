# Full geoJSON

Changes from the provisional full geoJSON structure:
* links have been updated so they link to a Google Drive
* An `llfa` of `null` is not allowed 
* `when_desc` strings have been standardised
* some repetitive information has been filtered out (using semantic similarity)
* `is_quant = True` information has been deleted
* Old LLFAs Cumbria and Somerset have been replaced by modern LLFAs due to 2023 local government changes
* UK, England, Wales and North Sea map features have been removed

Each `when_desc` format should confirm to one of the following permitted formats (using python date format notation):
* `%d %b %Y` a precise date 
* `%d %b %Y - %d %b %Y` a precise date range
* `%Y`  a year
* `%Ys` a decade
* `%Y - %Y`  a year range
* `%B %Y`  a month and year
* `%B - %B %Y`  a month range within the same year
* `%B %Y - %B %Y` a month range with different years  
* a season and year, e.g. "summer 2020"
* winter spanning two years e.g. "winter 2013 - 2014"
* Easter and year, e.g. "Easter 2010"
* "ambiguous date"

The geoJSON properties are structured as follows:

`"properties`" : {  
&nbsp;&nbsp;&nbsp;&nbsp;`"name"` : map feature name  
&nbsp;&nbsp;&nbsp;&nbsp;`"type"` : map feature type description. One of [`"settlement"`,`"administrative unit"`,`"hydrographic feature"`,`"physical feature"`,`"street"`,`"asset"`,`"other feature"`]   
&nbsp;&nbsp;&nbsp;&nbsp;`"llfa"` : Lead Local Flood Authority  
&nbsp;&nbsp;&nbsp;&nbsp;`"events"` : \[  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`"start_date"` : event start date (`null` if there is only a text description of when the event happened)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`"end_date"` : event end date (`null` if there is only a text description of when the event happened)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`"when_desc"` : text description of when the event happened  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`"info"` : \[  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`"text"` : information about what happened during the flood event in the place  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`"flags"`: quality control flags (see [README](https://github.com/ClimateNode/FPS19) on main page for possible values)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`"ref"` : report from which the information derives  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`"title"` : report title  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`"link"` : report URL (this is illustrative at the moment as we will need to set up a public repository for the reports)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`"page"` : page number (may not reflect nominal page numbering within the PDF – the front cover of every report is deemed page 1)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; \]  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}  
&nbsp;&nbsp;&nbsp;&nbsp;\]  
}

Example:  
`"properties`" : {  
&nbsp;&nbsp;&nbsp;&nbsp;`"name"`: "Barrington",  
&nbsp;&nbsp;&nbsp;&nbsp;`"type"`: "settlement",  
&nbsp;&nbsp;&nbsp;&nbsp;`"events"`: \[  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`"start_date"`: "2015-07-17",  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`"end_date"`: "2015-07-17",  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`"when_desc"`: "17 Jul 2015",   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`"info"`: \[  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`"text"`: "Formal flood incident recorded affecting various locations in Barrington on 17 July 2015 (Formal Flood Investigation reference FI/1/60). Risk Management Authorities recorded as Environment Agency and Cambridgeshire County Council.",  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`"flags"`: \[ "TAB" \],  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`"ref"` : 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`"title"` : "Flood Investigation Report: Barrington"  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`"link"` : "021_Cambridgeshire County/021_2014_Cambridgeshire County/Barrington flood investigation.pdf"
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`"page"`: 2  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;...  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\]  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}  
&nbsp;&nbsp;&nbsp;&nbsp;\]  
}
