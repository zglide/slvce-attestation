#!/usr/bin/env python3
"""Independent verifier for SLVCE's NAV attestation log.
Re-reads nav_log.csv, recomputes every per-day leaf hash from the published
numbers, re-walks the chain from genesis, and confirms the head. Trust nothing
here — this script only uses sha256 and the public CSV.

    python3 verify.py
"""
import csv
import hashlib
import json
import sys

ZERO = '0' * 64
FIELDS = ['date', 'nav', 'capital', 'strategy', 'red']


def leaf(rec):
    obj = {'date': rec['date'], 'nav': int(rec['nav']), 'capital': int(rec['capital']),
           'strategy': int(rec['strategy']), 'red': rec['red'] == 'true'}
    # An erratum is a later record for the same date that names the leaf it corrects.
    # Ordinary days have an empty `supersedes` and hash exactly as they always did.
    if rec.get('supersedes'):
        obj['supersedes'] = rec['supersedes']
    s = json.dumps(obj, separators=(',', ':'), ensure_ascii=False)
    return hashlib.sha256(s.encode('utf-8')).hexdigest()


def main(path='nav_log.csv'):
    prev = ZERO
    n = 0
    seen = {}
    errata = 0
    with open(path) as f:
        for row in csv.DictReader(f):
            if row.get('supersedes'):
                if seen.get(row['date']) != row['supersedes']:
                    print(f"ERRATUM at {row['date']} names leaf {row['supersedes'][:12]}… which is not that day's latest record")
                    return 1
                errata += 1
            lh = leaf(row)
            seen[row['date']] = lh
            if lh != row['leaf']:
                print(f"LEAF MISMATCH at {row['date']}: recomputed {lh} != {row['leaf']}")
                return 1
            ch = hashlib.sha256((prev + lh).encode()).hexdigest()
            if ch != row['chain']:
                print(f"CHAIN BREAK at {row['date']}: recomputed {ch} != {row['chain']}")
                return 1
            prev = ch
            n += 1
    print(f"OK — {n} records verified ({len(seen)} days, {errata} errata). head = {prev}")
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else 'nav_log.csv'))
