#!/usr/bin/env python3
from datetime import datetime, timezone
import os, sys
try:
    from totp_utils import generate_totp_code
except Exception as e:
    print("IMPORT ERROR:", e, file=sys.stderr)
    sys.exit(1)
SEED_PATH = "/data/seed.txt"
def read_seed(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            s = f.read().strip()
        return s
    except FileNotFoundError:
        print(f"SEED FILE NOT FOUND: {path}", file=sys.stderr)
        return None
    except Exception as e:
        print("READ SEED ERROR:", e, file=sys.stderr)
        return None
def main():
    seed = read_seed(SEED_PATH)
    if not seed:
        return
    try:
        code = generate_totp_code(seed)
    except Exception as e:
        print("GENERATE TOTP ERROR:", e, file=sys.stderr)
        return
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    line = f"{ts} - 2FA Code: {code}"
    print(line)
if __name__ == "__main__":
    main()
