# SLVCE — NAV attestation

An **append-only, tamper-evident** log of SLVCE's daily USD NAV record — the proof
behind *"no back-fill, no massaging up."* It commits the same numbers shown on
[slyce.xyz](https://slyce.xyz) and lets anyone verify, with nothing but `sha256`,
that a figure published on a given day has not been quietly rewritten since.

It reveals **only** date + dollar figures + hashes. No addresses, venues, sizes, or
positions.

## What's here

- **`nav_log.csv`** — one row per marked day: `date,nav,capital,strategy,red,leaf,chain`
- **`head.json`** — the current chain head (commits the entire history) + the recipe
- **`head.json.ots`** — an [OpenTimestamps](https://opentimestamps.org) proof anchoring
  the head into the Bitcoin blockchain (trustless "this existed before block N")

## How the chain works

For each day, in published order:

```
record = {"date","nav","capital","strategy","red"}          # the published row
leaf    = sha256( compact_json(record) )                     # per-day hash
chain   = sha256( prev_chain + leaf )                        # genesis prev = 64 × "0"
```

The latest `chain` (the **head**) commits the whole history: change any past number
and every chain hash from that day onward breaks.

## Verify it yourself

```bash
python3 verify.py        # re-walks nav_log.csv, recomputes every hash, checks the chain
```

Or by hand for a single day — recompute its `leaf`:

```python
import hashlib, json
rec = {"date":"2026-06-27","nav":7188591,"capital":5208409,"strategy":1980183,"red":True}
s = json.dumps(rec, separators=(",",":"), ensure_ascii=False)
print(hashlib.sha256(s.encode()).hexdigest())   # must equal that row's `leaf`
```

Verify the Bitcoin timestamp:

```bash
pip install opentimestamps-client
ots verify head.json.ots          # confirms head.json existed before a Bitcoin block
```

## Honest scope

The chain proves integrity **from genesis forward**. The genesis commit fixes the full
history-to-date so it can't change afterward, but pre-genesis days carry **no earlier
timestamp** — we do not claim they were stamped in the past. The record starts short
and honest, and grows one bitcoin-stamped day at a time.
