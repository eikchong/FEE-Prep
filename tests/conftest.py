import os
import sys
import tempfile
from pathlib import Path

# isolate user data before config is imported anywhere
_tmp = Path(tempfile.mkdtemp(prefix="fee-test-"))
os.environ["FEE_DATA_DIR"] = str(_tmp / "data")
os.environ["FEE_MATERIALS_DIR"] = str(_tmp / "materials")
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
