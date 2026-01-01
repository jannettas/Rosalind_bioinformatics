max_gc_id = ""
max_gc_ratio = 0.0

current_id = None
current_gc = 0
current_len = 0

with open("rosalind_gc.txt", "r") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        if line.startswith(">"):
            if current_id is not None: # if id is already set, we are at the end of sequence and can calculate GC ratio
                current_gc_ratio = (current_gc / current_len) * 100
                if current_gc_ratio > max_gc_ratio:
                    max_gc_ratio = current_gc_ratio
                    max_gc_id = current_id
            # if id is not set, we are at the new sequence start
            current_id = line[1:]
            current_gc = 0
            current_len = 0
        else:
            current_len += len(line)
            current_gc += line.count('G') + line.count('C')
# Process last sequence after which there is no ">"
if current_id is not None:
    current_gc_ratio = current_gc / current_len
    if current_gc_ratio > max_gc_ratio:
        max_gc_ratio = current_gc_ratio
        max_gc_id = current_id
print(max_gc_id)
print(f"{max_gc_ratio:.6f}")
