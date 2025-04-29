import gzip
import shutil

# Original file path
input_path = 'data_/similarity.pkl'

# Compressed output path
output_path = 'data_/similarity.pkl.gz'

# Compress the file
with open(input_path, 'rb') as f_in:
    with gzip.open(output_path, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

print(f"Compressed file saved to: {output_path}")
