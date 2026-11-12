"""Find asset tags assigned to more than one serial number.

Usage: python3 main.py assets.csv
CSV columns: asset_tag,host,serial.
A tag is a DUPLICATE when it appears with two or more different
serial numbers — the same tag on two different machines. A tag
re-scanned with the same serial is not a duplicate. Most
serials first.
"""
import argparse, csv, sys
from collections import defaultdict

def find_duplicates(rows):
    by_tag = defaultdict(lambda: {"serials": set(), "hosts": set()})
    for row in rows:
        tag = row["asset_tag"].strip()
        by_tag[tag]["serials"].add(row["serial"].strip())
        by_tag[tag]["hosts"].add(row["host"].strip())
    out = []
    for tag in sorted(by_tag):
        info = by_tag[tag]
        if len(info["serials"]) > 1:
            out.append((tag, sorted(info["serials"]), sorted(info["hosts"])))
    return sorted(out, key=lambda r: (-len(r[1]), r[0]))

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path")
    args = parser.parse_args(argv)
    with open(args.path, newline="", encoding="utf-8") as f:
        duplicates = find_duplicates(list(csv.DictReader(f)))
    for tag, serials, hosts in duplicates:
        print(f"{tag}: DUPLICATE ({len(serials)} serials: {', '.join(serials)}; hosts: {', '.join(hosts)})")
    if not duplicates:
        print("No duplicate asset tags found.")
    else:
        print(f"{len(duplicates)} duplicate tag(s) found.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
