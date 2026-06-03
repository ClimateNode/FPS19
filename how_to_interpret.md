<h1>How to interpret the Section 19 report map</h1>

<p>Section 19 reports are the reports which councils commission after flood events to investigate the causes of flooding and provide recommendations for how to prevent it in future. The Section 19 report map displays information on the impacts of flooding described in Section 19 reports in individual places.</p> 

<p>The map has been derived by extracting information using a Large Language Model (LLM). Relevant pages of each report were sent to the LLM along with instructions to return information on what happened in terms of impacts in the individual places described, and when these things happened. Coordinates matching place names were then derived used geocoding.</p> 

<h2>Points of interest</h2>

<p>It is important to note that the coordinates of each place <b>do not indicate the precise location of flood impacts</b> and should not be interpreted such. They are simply coordinates which indicate the general location of the place. Most coordinates have been derived from OpenStreetMap.</p>

<p>Lots of places in England have the same name &ndash; for example, there are thousands of High Streets  &ndash; and this can pose a challenge to identifying individual locations from text. Precise place name identification has been subject to rigorous human quality control and coordinates should in the vast majority of cases refer to the correct location.</p>

<h2>Sources of inaccuracy</h2>

<p>Most people who have used LLMs are aware that they can fabricate information ('hallucinate'). This possibility should have been reduced by asking the LLM very specific information about specific textual sources provided to it, rather than using its own internal knowledge. However the possibility remains there may be some hallucinations presented on the map. It is strongly recommnded that if users see information on the map which is important to them, for example information about flood events on their own street, or information which they are using for their own research, they <b>refer to the relevant passages in the underlying Section 19 report</b>. Links to the original reports and page numbers are provided to do this.</p>

<p>Section 19 reports themselves may contain inaccuracies. Typos around place names and dates are common, and have been corrected where spotted. The word <i>sic</i> is used to acknowledge that an inaccurate place name mentioned in a text differs to the one assumed to be the intended place name. <p/>

<p>Information extracted from <b>images, tables and lists overlapping pages should be viewed with caution</b>. It was noticed that images depicting flood flow routes in particular were liable to misinterpretation by the AI. Information contained in rows in large, complex tables can be misattributed to place names mentioned on other rows.</p>

<p>Another potential source of inaccuracy is the way the LLM has been instructed to return information in standardised formats, which may lead to shortcuts and inaccuracies when passages contain complex or nuanced information about multiple events. In paragraphs about multiple flood events it has not always been possible to disentangle information about which impacts relate to which events. For that reason, the same information is sometimes presented repeatedly for all events mentioned in a paragraph, though it may contain facts which are relevant only to a subset of those events. For this reasons <b>users should treat information from passages about multiple events with caution</b> (see below).</p> 

<p>The following data quality flags are used to inform users that a given piece of information may be subject to one of more of these problems:</p>

<ul style="list-style: none;">
<li><b>IMG:</b> information may have been extracted from an image
<li><b>TAB:</b> information may have been extracted from a table
<li><b>LST:</b> information may have been extracted from a list overlapping pages
<li><b>MUL:</b> information has been extracted from a sentence/paragraph about events on more than one date
<li><b>PAG:</b> information may have been extracted from text from a page other than the one indicated (see 'Page numbers' section below)
</ul>
  
<h2>Date information</h2>
Most flood impacts described in a given Section 19 report will be those which occurred during the event which is the subject of the report. However, many reports also provide a detailed flood history of the location and information about other recent flood events.

Information on when flooding occurred contained in text can be very specific, i.e. a precise date, or very vague, for example "winter 2013-14", "Easter 1998", etc., or sometimes just a year or decade. Precise dates or date ranges are given where they are available, but otherwise verbal descriptions of dates are used.

The term "ambiguous date" is used when:
<ul>
  <li>Information is about flooding in general rather then a precise event</li>
  <li>Information is about a precise event, but the LLM has failed to identify which one(s)</li>
</ul>

Where different date descriptions of the same event have been used in different documents, attempts have been made to harmonise these to avoid repetition. For example, Report A describes flooding which happened during Storm Babet between the 18th and 23rd of October 2023 in Borsetshire. Page 10 of Report B describes the same event, but states it happened in 'October 2023'. If there was no other notable flooding in Borsetshire in October 2023, these should both be listed under the date range '18-23 October 2023'. However, when users refer to p10 of Report B, they will find a reference to 'October 2023' and not the precise date range. Users may find that some multiple descriptions of the same event are displayed in the map sidebar.

In a number of cases, the LLM returned date information which related to the dates of investigations or remedial actions floowing the flooding rather than the event itself. Attempts have been made to correct these so they refer to the actual event, but it's possible some may still be displayed on the map sidebar.

<h2>Page numbers</h2>
<p>page numbers are counted from the cover page as page 1 and may differ from page numbering in the document (for example, where page numbering begins after the front matter).</p>

Overlapping context: a small amount of information from preceding and following pages is usually included in the context sent to the LLM for each page. Therefore information about a place or organisation may sometimes be on the following or preceding page to the one indicated.

Overlapping lists and tables: page numbers for information extracted from lists and tables overlapping pages may also not be accurate.
Images: if a figure is referred to on a previous page, this is included in the context sent to the LLM, along with the page the figure is actually on. Information used to interpret images may therefore be taken from pages other than the one indicated.
