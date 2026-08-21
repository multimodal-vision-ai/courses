"""Sync the FMI course navigator and seven demos from Kaggle."""

from __future__ import annotations

import ast
import json
from pathlib import Path

from kaggle.api.kaggle_api_extended import ApiGetKernelRequest, KaggleApi


NOTEBOOKS = {
    "00-start-here.ipynb": (
        "guopingtan/fmi-course-kaggle-hands-on-lab-start-here"
    ),
    "demo1-traffic-classification.ipynb": "guopingtan/fmi-demo1-traffic-classification",
    "demo2-qoe-optimization.ipynb": "guopingtan/fmi-demo2-qoe-optimization",
    "demo3-quality-assessment.ipynb": "guopingtan/fmi-demo3-quality-assessment",
    "demo4-neural-compression.ipynb": "guopingtan/fmi-demo4-neural-compression",
    "demo5-semantic-communication.ipynb": "guopingtan/fmi-demo5-semantic-communication",
    "demo6-hd-video-impairments.ipynb": (
        "guopingtan/fmi-demo-6-network-impairments-on-hd-video"
    ),
    "demo7-vr-video-impairments.ipynb": (
        "guopingtan/fmi-demo-7-network-impairments-on-vr-360-video"
    ),
}


def validate_notebook(source: str, ref: str) -> dict:
    notebook = json.loads(source)
    if notebook.get("nbformat") != 4 or not isinstance(notebook.get("cells"), list):
        raise ValueError(f"{ref}: unsupported or invalid notebook structure")

    for index, cell in enumerate(notebook["cells"], start=1):
        if isinstance(cell.get("source"), str):
            cell["source"] = cell["source"].splitlines(keepends=True)
        if cell.get("cell_type") != "code":
            continue
        code = "".join(cell.get("source", []))
        if code.strip():
            ast.parse(code, filename=f"{ref}:cell-{index}")
    return notebook


def main() -> None:
    target_dir = Path(__file__).resolve().parent
    api = KaggleApi()
    api.authenticate()
    downloads: dict[Path, str] = {}

    with api.build_kaggle_client() as client:
        for filename, ref in NOTEBOOKS.items():
            owner, slug, version = api.parse_kernel_string(ref)
            request = ApiGetKernelRequest()
            request.user_name = owner
            request.kernel_slug = f"{slug}/{version}" if version else slug
            response = client.kernels.kernels_api_client.get_kernel(request)
            notebook = validate_notebook(response.blob.source, ref)
            downloads[target_dir / filename] = (
                json.dumps(notebook, ensure_ascii=False, indent=1) + "\n"
            )
            code_cells = sum(
                cell.get("cell_type") == "code" for cell in notebook["cells"]
            )
            print(f"validated {filename}: {len(notebook['cells'])} cells, {code_cells} code")

    for path, source in downloads.items():
        path.write_text(source, encoding="utf-8", newline="\n")
        print(f"updated {path.name}")


if __name__ == "__main__":
    main()
