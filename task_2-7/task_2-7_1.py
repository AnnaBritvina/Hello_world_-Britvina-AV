files = ["seq1", "seq2", "seq3", "seq4"]
date = "2024-03-15"
for name in files:

   new_name = f"{name}_{date}.fasta"

   print(f"{new_name}")