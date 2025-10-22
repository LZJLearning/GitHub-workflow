# dedupe.py
from collections import defaultdict
from typing import List

def dedupe_header(columns: List[str]) -> List[str]:
    """
    Make header column names unique by appending numeric suffixes to duplicates.
    Rules:
    - The first occurrence of a name is kept as-is.
    - The 2nd, 3rd, ... occurrences of the same name get ".1", ".2", ...
      appended.
    - Order is preserved exactly as given.
    - Input is a list of strings (column names); output is a same-length list.
    Example:
    ["id", "name", "id", "name", "name"] -> ["id", "name", "id.1", "name.1", "name.2"]
    """
    seen_counts = defaultdict(int)
    result: List[str] = []
    for col in columns:
        count = seen_counts[col]
        if count == 0:
            result.append(col)
        else:
            result.append(f"{col}.{count}")
        # increment count for this column
        seen_counts[col] += 1
    return result
