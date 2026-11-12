import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unittest
from main import find_duplicates

def row(tag, host, serial):
    return {"asset_tag": tag, "host": host, "serial": serial}

class TestAssetTagDuplicates(unittest.TestCase):
    def test_duplicate_found(self):
        d = find_duplicates([row("TAG-1", "PC-1", "SN-A"), row("TAG-1", "PC-2", "SN-B")])
        self.assertEqual(d, [("TAG-1", ["SN-A", "SN-B"], ["PC-1", "PC-2"])])
    def test_unique_tag_clean(self):
        self.assertEqual(find_duplicates([row("TAG-1", "PC-1", "SN-A")]), [])
    def test_same_serial_rescan_not_duplicate(self):
        self.assertEqual(find_duplicates([row("TAG-1", "PC-1", "SN-A"), row("TAG-1", "PC-1", "SN-A")]), [])
    def test_most_serials_first(self):
        d = find_duplicates([row("A", "H1", "S1"), row("A", "H2", "S2"),
                             row("B", "H1", "S1"), row("B", "H2", "S2"), row("B", "H3", "S3")])
        self.assertEqual(d[0][0], "B")
    def test_empty_input(self):
        self.assertEqual(find_duplicates([]), [])
