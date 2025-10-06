# Section 19 Report LLM Analysis

## Intro

This repository contains the outputs to date of an experimental project being undertaken by Helen Jackson for Flooded People using an LLM to extract information on flood impacts from Setion 19 reports.

It contains two types of outputs:

• maps (HTML files)

• readouts (markdown files)
(One of each per individual document)

## Interpretation notes

•  Outputs linked to individual Section 19 reports can be identified via the file name of each readout/map in the following format:<br>[_ISO code of the relevant local authority_](https://www.iso.org/obp/ui#iso:code:3166:GB) _ _index_ _ _start date of the event (YYYY-mm-dd)_ _ _file extension_

•  Map coordinates of places are typically dervied from geocoding and do not indicate the precise locations of flood impacts – do not interpret them as such.

•  Quality flags for LLM outputs are as follows:
  * **IMG**: information may have been extracted from an image
  * **TAB**: information may have been extracted from a table
  * **LST**: information may have been extracted from a list overlapping pages 
  * **PAG**: information may have been extracted from the preceding or following page rather than the page number shown
  * **MUL**: information has been extracted from a sentence/paragraph about events on more than one date
 
 In general, page numbers for information extracted from lists and tables overlapping pages may not be accurate

•  Curley braces {} in readouts
  * If a piece of information has no curly braces it means that it relates to the main flood event described in the report
  * Curly braces surrounding date(s) indicate that the information is about events on the date(s) shown
  * `{general}` indicates that the information is about flooding in general, not specific events
