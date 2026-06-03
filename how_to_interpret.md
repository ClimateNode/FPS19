<h1>How to interpret the Section 19 report map</h1>

The Section 19 report map displays information on what has happened

The map has been derived by sending the pages of each report to an Large Language Model (LLM) and asking it to return information on places which have been flooded, what happened in terms of impacts, and when these things happened.

<h2>Points of interest</h2>
 Map coordinates of places are typically derived from geocoding and do not indicate the precise locations of flood impacts – do not interpret them as such.

<h2>Sources of inaccuracy</h2>

LLMs can hallucinate. By asking LLm to extract very specific information this possibility should have been reduced. If information is important to you <b>refer to the underlying source</b>.

Overlapping context: a small amount of information from preceding and following pages is usually included in the context sent to the LLM for each page. Therefore information about a place or organisation may sometimes be on the following or preceding page to the one indicated.
Overlapping lists and tables: page numbers for information extracted from lists and tables overlapping pages may also not be accurate.
Images: if a figure is referred to on a previous page, this is included in the context sent to the LLM, along with the page the figure is actually on. Information used to interpret images may therefore be taken from pages other than the one indicated.

Information extracted from images and tables (particularly images) should be viewed with caution.

In paragraphs about multiple flood events it has not always been possible to disentangle information about which impacts relate to which events. For that reason, the same information is sometimes presented repeatedly for all events mentioned in a paragraph, though it may contain facts which are relevant only to a subset of those events. <b>Users should treat information with the MUL data quality flag with caution</b> (see below). 

<h3>Data quality flags</h3>
The following data quality flags

IMG: information may have been extracted from an image
TAB: information may have been extracted from a table
LST: information may have been extracted from a list overlapping pages
PAG: information may have been extracted from text added to the context from a page other than the one indicated
MUL: information has been extracted from a sentence/paragraph about events on more than one date

<h2>Date information</h2>
Most flood impacts described in a given Section 19 report will be those which occurred during the event which is the subject of the report. However, many reports also provide a detailed flood history of the location and information about other recent flood events.

Information on when flooding occurred contained in text can be very specific, i.e. a precise date, or very vague, for example "winter 2013-14", "Easter 1998", etc., or sometimes just a year or decade. Precise dates or date ranges are given where they are available, but otherwise verbal descriptions of dates are used.

The term "ambiguous date" is used when:
<ul>
  <li>Information is about flooding in general rather then a precise event</li>
  <li>Information is about a precise event, but the LLM has failed to identify which one(s)</li>
</ul>

Where different date descriptions of the same event have been used in different documents, attempts have been made to harmonise these to avoid repetition. For example, Report A describes flooding which happened during Storm Babet between the 18th and 23rd of October 2023 in Borsetshire. Page 10 of Report B describes the same event, but states it happened in 'October 2023'. If there was no other notable flooding in Borsetshire in October 2023, these should both be listed under the date range '18-23 October 2023'. However, when users refer to p10 of Report B, they will find a reference to 'October 2023' and not the precise date range.

<h2>Page numbers</h2>
<p>Page numbers are cou</p>
