import os
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
ARTIFACT_DIR = os.path.join(ROOT_DIR, "artifacts")
os.makedirs(ARTIFACT_DIR, exist_ok=True)