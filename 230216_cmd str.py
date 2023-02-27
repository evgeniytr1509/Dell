# командная строка
import sys
from pathlib import Path

print(sys.argv)
path = Path(sys.argv[1])
print(path.exist())