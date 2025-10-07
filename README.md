# Section 19 Report LLM Analysis

## Intro

This repository contains the outputs **to date** of an experimental *pro bono* project being undertaken by Helen Jackson (Director of [ClimateNode](https://www.climatenode.org)) for Flooded People using an LLM to extract information on flood impacts from Local Authority Section 19 reports.

It contains two types of outputs:

• maps (HTML files)

• readouts (markdown files)
(One of each per individual document)

## Interpretation notes

•  Outputs linked to individual Section 19 reports can be identified via the file name of each readout/map in the following format:<br>[_ISO code of the relevant local authority_](https://www.iso.org/obp/ui#iso:code:3166:GB) _ _index_ _ _start date of the event (YYYY-mm-dd)_ _ _file extension_

• Map coordinates of places are typically dervied from geocoding and do not indicate the precise locations of flood impacts – do not interpret them as such.

• Page numbers:

  * Counting: page numbers are counted from the cover page as page 1 and may differ from page numbering in the document (for example, where page numbering begins after the front matter).
  * Sources of inaccuracy:
    * Overlapping context: a small amount of information from preceding and following pages is usually included in the context sent to the LLM for each page. Therefore information about a place or organisation may sometimes be on the following or preceding page to the one indicated.
    * Overlapping lists and tables: page numbers for information extracted from lists and tables overlapping pages may also not be accurate.
    * Images: if a figure is referred to on a previous page, this is included in the context sent to the LLM, along with the page the figure is actually on. Information used to interpret images may therefore be taken from pages other than the one indicated.

• Information extracted from images and tables (particularly images) should be viewed with caution. 

• Quality flags for LLM outputs are as follows:
  * **IMG**: information may have been extracted from an image
  * **TAB**: information may have been extracted from a table
  * **LST**: information may have been extracted from a list overlapping pages 
  * **PAG**: information may have been extracted from text added to the context from a page other than the one indicated
  * **MUL**: information has been extracted from a sentence/paragraph about events on more than one date

• Maps show only information specific to the event which triggered the report, while readouts also contain any information in the report about historic flood events, or flooding in general, at a location.

•  Curly braces {} in readouts
  * If a piece of information has no curly braces it means that it relates to the main flood event described in the report
  * Curly braces surrounding date(s) indicate that the information is about events on the date(s) shown
  * `{general}` indicates that the information is about flooding in general, not specific events
