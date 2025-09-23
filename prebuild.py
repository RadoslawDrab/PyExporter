from pathlib import Path
import os

for item in Path('./dist').glob('**/*'):
	os.remove(item)