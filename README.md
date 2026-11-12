# asset-tag-duplicate-finder

Find asset tags assigned to more than one serial number from a CSV: a tag appearing with two or more different serials is a DUPLICATE — most serials first. A re-scan with the same serial is not a duplicate.

## How to run

```sh
python3 main.py assets.csv
```

## Example output

```
TAG-1042: DUPLICATE (2 serials: SN-A101, SN-B207; hosts: PC-12, PC-19)
1 duplicate tag(s) found.
```

Standard library only. Run the tests with `python3 -m unittest discover`.
