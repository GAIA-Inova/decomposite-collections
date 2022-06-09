#!/usr/bin/env python3
import csv
import click
import rows
from pathlib import Path
from tqdm import tqdm
from collections import OrderedDict, defaultdict
from PIL import Image

from constants import CAPTIONS, MOSAIC_DIR, CAPTIONS_REVERSE, IMG_ID_COL, ZKM_ROOT
import csv_parser


@click.group()
def command_line_entrypoint():
    """
    Ferramenta para explorar imagens do Museu Paulista e MAC-USP para o projeto Decomposite Collections
    """
    pass


@command_line_entrypoint.command("bbox")
@click.argument("filename", type=click.Path(exists=True))
def crop_bboxes(filename):
    analisys = rows.import_from_csv(filename)
    output_rows = []
    for line, row in tqdm(enumerate(analisys, start=1), desc="Processing captions..."):
        entry, errors, skip_row = csv_parser.clean_row(row)
        if errors:
            print(f"{entry[IMG_ID_COL]} - ERROR - line {line}:")
            print("\t" + "\n\t".join(errors))
            if skip_row:
                continue

        image_path = entry["img_path"]
        tags_result = csv_parser.process_image(entry, image_path)

        for caption, outputs in tags_result.items():
            for tag_img in outputs:
                out_row = OrderedDict()
                out_row["Tombo"] = entry[IMG_ID_COL]
                out_row["Categoria"] = CAPTIONS[caption]
                out_row["Área"] = ','.join([str(i) for i in tag_img['area']])
                out_row["Títulos do objeto"] = entry["titulos_do_objeto"]
                out_row["Autor"] = entry["autor"]
                out_row["Data"] = entry["data"]
                out_row["Técnica"] = entry["tecnica"]
                out_row["Dimensões"] = entry["dimensoes"]
                out_row["Categoria Id"] = caption
                out_row["Imagem Id"] = entry["img_id"]
                out_row["Imagem"] = tag_img['image'].relative_to(MOSAIC_DIR / caption)
                # TODO
                # adicionar todos os campos do relatório a partir do obj entry
                output_rows.append(out_row)

    with open("output.csv", 'w', newline='') as fd:
        writer = csv.DictWriter(fd, fieldnames=output_rows[0].keys())
        writer.writeheader()
        writer.writerows(output_rows)

    print(f"Output CSV captions at 'output.csv'")


if __name__ == '__main__':
    command_line_entrypoint()
