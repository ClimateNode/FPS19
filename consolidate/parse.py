# %%
import os
from bs4 import BeautifulSoup
import re
import pandas as pd


def load_la_mapping():
    la_df = pd.read_csv("la_codes.csv")
    la_df["code"] = la_df["code"].str.replace("*", "", regex=False).str.strip()
    la_df["name"] = la_df["name"].replace(r"\[.+\]", "", regex=True).str.strip()

    local_authority_mapping = la_df.set_index("code")["name"].to_dict()

    la_df["parent"] = la_df["parent"].map(local_authority_mapping)
    parent_mapping = la_df.set_index("code")["parent"].to_dict()

    return local_authority_mapping, parent_mapping, la_df


LOCAL_AUTHORITY_MAPPING, PARENT_MAPPING, la_df = load_la_mapping()


def parse_popup_html(html):
    """Parses html from pop-up to extract clean body-text, location

    Args:
        html (str):
    """

    soup = BeautifulSoup(html, "html.parser")
    heading = soup.find("h1")
    heading = heading.text.strip() if heading else ""

    bodies = soup.select("div.nugget-popup:not([class*=' '])")
    body = "\n".join([b.text.strip() for b in bodies]) if bodies else ""

    impacts = (
        "\n".join(
            [i.text.strip() for i in soup.find_all("div", class_="nugget-popup quant")]
        )
        if soup.find_all("div", class_="nugget-popup quant")
        else ""
    )

    return heading, body, impacts


def parse_file_name(file_path):
    """Parse file name to extract metadata.

    Args:
        file_path (str): Path to the HTML file.

    Returns:
        dict: Metadata extracted from the file name.
    """
    base_name = os.path.basename(file_path)

    loc, doc_id, date = base_name.replace(".html", "").split("_")[:3]

    return {
        "authority_code": loc,
        "doc_id": doc_id,
        "date": date,
    }


def extract_md_data(markdown_file):
    with open(markdown_file, "r") as f:
        content = f.readlines()

    # Get heading
    heading_line = next((line for line in content if line.startswith("# ")), None)
    if not heading_line:
        raise ValueError("No heading found in markdown file.")
    heading = heading_line.replace("# ", "").strip()

    # Get document reference
    reference_line = next(
        (line for line in content if line.startswith("Reference document:")), None
    )
    if not reference_line:
        print(content)
        raise ValueError("No reference document found in markdown file.")
    reference_line = reference_line.replace("Reference document:", "").strip()
    _, doc, reference = reference_line.split("<br>")

    return heading, doc, reference


def extract_map_data(html_file):
    """Extract markers and their data from an HTML map file."""
    with open(html_file, "r") as f:
        content = f.read()

    # Extract all markers

    # Extract all markers
    markers = []
    marker_pattern = r"var marker_[^=]+= L\.marker\(\s*\[([^\]]+)\]"
    marker_matches = re.findall(marker_pattern, content)

    # Extract popup content for each marker
    popup_pattern = r"var html_[^=]+= \$\(`([^`]+)`\)"
    popup_matches = re.findall(popup_pattern, content)

    # Match markers with their popups (they appear in the same order)
    for i, marker_coords in enumerate(marker_matches):
        coords = marker_coords.split(",")
        lat, lng = float(coords[0].strip()), float(coords[1].strip())

        popup_content = ""
        if i < len(popup_matches):
            # Clean up the popup content
            popup_content = popup_matches[i].replace("\\n", "").replace('\\"', '"')

        heading, body, impacts = parse_popup_html(popup_content)

        d = parse_file_name(html_file)
        la_name = LOCAL_AUTHORITY_MAPPING.get(d["authority_code"], "Unknown Authority")
        country = PARENT_MAPPING.get(d["authority_code"], "Unknown Country")

        d.update(
            {
                "lat": lat,
                "lng": lng,
                "html": popup_content,
                "local_authority": la_name,
                "location": heading,
                "country": country,
                "body": body,
                "impacts": impacts,
                "source_html": os.path.basename(html_file),
                "source_id": os.path.basename(html_file).replace(".html", ""),
            }
        )

        try:
            heading, doc, reference = extract_md_data(
                f"../readouts/{d['source_id']}.md"
            )
            d.update(
                {
                    "readout_title": heading,
                    "report_document": doc,
                    "report_reference": reference.replace("\\_", "/"),
                }
            )
        except FileNotFoundError as e:
            print(f"Markdown file not found for {d['source_id']}: {e}")

        markers.append(d)

    return markers


def main():
    html_path = "../maps/"
    all_data = []
    html_files = [
        f
        for f in os.listdir(html_path)
        if os.path.isfile(os.path.join(html_path, f))
        and f.endswith(".html")
        and not f.startswith("index")
    ]

    for html_file in html_files:
        file_data = extract_map_data(os.path.join(html_path, html_file))
        all_data.extend(file_data)

    df = pd.DataFrame(all_data)
    df.to_csv("consolidated_data.csv", index=False)
    print("Data consolidated into consolidated_data.csv")


if __name__ == "__main__":
    main()
