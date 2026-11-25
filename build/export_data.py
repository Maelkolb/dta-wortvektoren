"""DTA word2vec model (dta_all) -> top words as int8 unit vectors for the explorer page."""
import base64, json
from pathlib import Path
import numpy as np

MODEL = Path("C:/Users/totom/Downloads/S06_Wortvektoren_Projektideen_v3/build/w2v/models/dta_all")
OUT = Path(__file__).parent / "data"
WORDS = 40000

words, counts = [], []
for line in open(MODEL / "vocab.txt", encoding="utf-8"):
    w, c = line.rstrip("\n").split("\t")
    words.append(w)
    counts.append(int(c))
words, counts = words[:WORDS], counts[:WORDS]
unit = np.load(MODEL / "vectors.npy")[:WORDS].astype(np.float32)
unit /= np.linalg.norm(unit, axis=1, keepdims=True)
quantized = np.round(unit * (127 / np.abs(unit).max(axis=1))[:, None]).astype(np.int8)

OUT.mkdir(exist_ok=True)
meta = {"words": words, "counts": counts, "dims": int(unit.shape[1]), "minCount": counts[-1]}
(OUT / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
(OUT / "vectors.b64").write_text(base64.b64encode(quantized.tobytes()).decode("ascii"))
