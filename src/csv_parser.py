"""
Módule responsible to organize Dataset
"""
import shutil
import re
import io
import os
import requests
import urllib
from pathlib import Path
from PIL import Image

from constants import (
    CAPTIONS,
    IMAGES_DIR,
    SPLIT_TOKEN,
    MOSAIC_DIR, IMG_ID_COL,
)


def process_image(data, image_path):
    """
    Extract individual images per caption
    """
    results = {}
    for caption in CAPTIONS:
        coords = data[caption]
        if not coords:
            continue

        caption_dir = MOSAIC_DIR / caption
        if not caption_dir.exists():
            os.mkdir(caption_dir.resolve())

        item_id = data[IMG_ID_COL]
        image = Image.open(image_path)
        results[caption] = []

        for i, area in enumerate(coords):
            out_img = caption_dir / f"{item_id}-{caption}-{i:0>2d}.jpg"

            results[caption].append({
                'area': area,
                'image': out_img,
            })
            if out_img.exists():
                continue

            crop = image.crop(area)
            crop.save(
                out_img,
                quality="maximum",
                icc_profile=image.info.get("icc_profile"),
            )

        image.close()

    return results


def clean_row(row):
    """
    Clean and organize input data
    """
    errors_list = []

    entry = row._asdict()
    img_id = entry[IMG_ID_COL].replace(".", "_") + ".jpg"

    img_path = IMAGES_DIR / Path(img_id)
    if not img_path.exists():
        errors_list.append(f"Image {img_path} does not exist.")

    entry["img_id"] = img_id
    entry["img_path"] = img_path
    for caption in CAPTIONS:
        # parse coordinates string and organises them as a list of tuples
        try:
            entry[caption] = [
                [int(n) for n in c.strip().split(",")]
                for c in (entry[caption] or "").strip().split(SPLIT_TOKEN)
                if c.strip()
            ]
        except ValueError:
            entry[caption] = []
            errors_list.append(
                f"Caption {caption} with bad formatted data (line breaks, non-numeric chars, bad separator...)"
            )

    # garante que todas as coordenadas possuem somente 4 valores
    for caption in CAPTIONS:
        invalid_coords = []
        coords = entry[caption]
        if not coords:
            continue
        for coord in coords:
            # cada tupla de coordenada deve ter somente 4 valores
            invalid = False
            if len(coord) > 4:
                errors_list.append(f"Caption {caption} with bounding box are with more than 4 pts.")
                invalid = True
            if len(coord) < 4:
                errors_list.append(f"Caption {caption} with bounding box are with more than 4 pts.")
                invalid = True

            if invalid:
                invalid_coords.append(coord)
            else:
                # garante ordenação no eixo X (primeira coordenada deve ser x e a outra é x + diff)
                if coord[0] > coord[2]:
                    coord[0], coord[2] = coord[2], coord[0]
                # garante ordenação no eixo Y (primeira coordenada deve ser y e a outra é y + diff)
                if coord[1] > coord[3]:
                    coord[1], coord[3] = coord[3], coord[1]

        for invalid in invalid_coords:
            entry[caption].remove(invalid)

    should_skip = False
    return entry, errors_list, should_skip
