import pandas as pd

def process_data(file_path: str) -> pd.DataFrame:
  if not file_path.endswith('csv'):
    raise ValueError("Invalid file format")
  df = pd.read_csv(file_path)
  return df


