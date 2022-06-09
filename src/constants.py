from pathlib import Path

ZKM_ROOT = Path("/home/bernardo/envs/decomposite-collections/")  # project's root dir
IMAGES_DIR = ZKM_ROOT / "artworks-images"
MOSAIC_DIR = ZKM_ROOT / "mosaico"
CAPTIONS_DIR = ZKM_ROOT / "captions"
RESIDUALS_DIR = ZKM_ROOT / "residuals"
SPLIT_TOKEN = "&"


CAPTIONS = {
    "fauna": "Fauna",
    "ceu": "Céu",
    "flora": "Flora",
    "artefatos_domesticos": "Artefatos domésticos",
    "homem_branco": "Homem Branco",
    "mulher_branca": "Mulher Branca",
    "homem_indigena": "Homem Indígena",
    "mulher_indigena": "Mulher Indígena",
    "homem_negro": "Homem Negro",
    "mulher_negra": "Mulher Negra",
    "trabalhadore_rural": "Trabalhador(a) rural",
    "trabalhadore_urbano": "Trabalhador(a) urbano",
    "paisagem_rural": "Paisagem rural",
    "paisagem_urbana": "paisagem_urbana",
    "res_abastada": "Residência (abastada)",
    "res_pobre": "Residência (pobre)",
    "igreja": "Igreja",
    "duv": "DUV",
}

CAPTIONS_REVERSE = {v: k for k, v in CAPTIONS.items()}

IMG_ID_COL = "tombo"
