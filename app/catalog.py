"""The station list from stations.yaml, with each station's place, map position and map
label filled in. Used by the server and by build_static.py so both see the same data."""

from pathlib import Path

import yaml


def load(path: Path) -> dict:
    data = yaml.safe_load(path.read_text())
    places = data.get("places", {})
    zones = data.get("timezones", {})
    codes = data.get("codes", {})
    for g in data["groups"]:
        for st in g["stations"]:
            st.setdefault("place", g.get("place", ""))
            if st["place"] in zones:
                st.setdefault("tz", zones[st["place"]])
            p = st.get("map") or places.get(st["place"])
            if p:
                st["geo"] = [p[0], p[1]]
                st["city"] = p[2] if len(p) > 2 else st["place"]
            city = st.get("city") or st["place"]
            st["code"] = codes.get(city) or "".join(ch for ch in city if ch.isalpha())[:3].upper()
    return data
