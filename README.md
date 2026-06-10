# Lingua-SafetyBench

A Benchmark for Safety Evaluation of Multilingual Vision-Language Models.

The code and dataset will be progressively released here.

## Dataset

We provide our multilingual and multimodal dataset for safety evaluation here.

Lingua-SafetyBench is a large-scale multilingual multimodal safety benchmark designed to evaluate the safety robustness of Vision-Language Large Models (VLLMs) under joint multilingual and multimodal inputs. Unlike prior benchmarks that mainly focus on either multilingual text-only safety or monolingual multimodal safety, Lingua-SafetyBench provides diverse image-text pairs across multiple languages and visual formats, enabling a more realistic evaluation of cross-lingual and cross-modal safety risks.

The benchmark contains 100,440 harmful image-text pairs covering 10 languages: Arabic, Chinese, English, French, German, Japanese, Norwegian, Finnish, Russian, and Spanish. To better analyze the source of safety risks, the dataset is explicitly divided into two subsets: image-dominant risks, where the unsafe intent is primarily conveyed through visual content, and text-dominant risks, where the harmful intent mainly comes from textual instructions. The image-dominant subset further includes pure visual, typographic, and mixed image types.

Lingua-SafetyBench covers eight major safety scenarios: economic harm, fraud, hate speech, illegal activity, malware generation, physical harm, privacy violations, and sexual content. This design allows researchers to systematically evaluate how VLLMs respond to harmful multimodal requests across different languages, scripts, resource levels, and risk-dominant modalities.

This dataset is strictly intended for academic research and AI safety evaluation purposes only, including model safety analysis, robustness assessment, and safety alignment research. It must not be used for any real-world harmful behavior, illegal activities, offensive system development, malicious content generation, safety bypassing, commercial misuse, or any other non-research purpose. Users are solely responsible for ensuring that their use of this dataset complies with applicable laws, ethical standards, and platform policies, and for any consequences arising from its use.

## Dataset Access

The dataset is available on Hugging Face:

```text
https://huggingface.co/datasets/leaf-pear/Lingua-SafetyBench
```

Users must follow the official access process before using the dataset. Redistribution of the dataset, in whole or in part, is not permitted without authorization.

## Data Structure

Lingua-SafetyBench is organized according to risk attribution type, language, and safety scenario.

The dataset contains two major risk categories:

```text
1-Image-Dominant Risk
2-Text-Dominant Risk
```

The image-dominant risk subset is further divided into three image types:

```text
Visual
Typography
Mixed
```

A typical directory structure is as follows:

```text
dataset/
├── 1-Image-Dominant Risk/
│   ├── Visual/
│   │   └── English/
│   │       └── Physical Harm.json
│   ├── Typography/
│   │   └── English/
│   │       └── Physical Harm.json
│   └── Mixed/
│       └── English/
│           └── Physical Harm.json
├── 2-Text-Dominant Risk/
│   └── English/
│       └── Physical Harm.json
└── bundle_data/
    └── ...
```

Each JSON file contains samples with a textual question and a corresponding image path. The image files are stored under the `bundle_data` directory.

## Data Loading Example

We provide a simple script, `load_data.py`, to load question-image pairs from Lingua-SafetyBench.

Example usage:

```bash
python load_data.py \
  --dataset_root ./dataset \
  --language English \
  --scenario "Physical Harm" \
  --risk_type Text-Dominant
```

The script loads the corresponding JSON file and returns a list of `(question, image_path)` pairs. The image paths are automatically resolved under the `bundle_data` directory.

## Supported Arguments

### `--dataset_root`

Path to the root directory of the downloaded dataset.

Example:

```bash
--dataset_root ./dataset
```

### `--language`

The language of the subset to load. Supported values are:

```text
Arabic
Chinese
English
Finnish
French
German
Japanese
Norwegian
Russian
Spanish
```

### `--scenario`

The safety scenario to load. Supported values are:

```text
Economic Harm
Fraud
Hate Speech
Illegal Activity
Malware Generation
Physical Harm
Privacy Violence
Sex
```

When the scenario name contains spaces, please wrap it with quotation marks.

Example:

```bash
--scenario "Physical Harm"
```

### `--risk_type`

The risk attribution type to load. Supported values are:

```text
Image-Dominant-Visual
Image-Dominant-Typography
Image-Dominant-Mixed
Text-Dominant
```

The four risk types correspond to the following dataset subsets:

```text
Image-Dominant-Visual      -> 1-Image-Dominant Risk / Visual
Image-Dominant-Typography  -> 1-Image-Dominant Risk / Typography
Image-Dominant-Mixed       -> 1-Image-Dominant Risk / Mixed
Text-Dominant              -> 2-Text-Dominant Risk
```

## Example Script

```python
import os
import json
import argparse
from typing import List, Tuple


LANGUAGES = [
    "Arabic", "Chinese", "English", "Finnish", "French",
    "German", "Japanese", "Norwegian", "Russian", "Spanish"
]

SCENARIOS = [
    "Economic Harm", "Fraud", "Hate Speech", "Illegal Activity",
    "Malware Generation", "Physical Harm", "Privacy Violence", "Sex"
]

RISK_ATTRIBUTION = [
    "Image-Dominant-Visual",
    "Image-Dominant-Typography",
    "Image-Dominant-Mixed",
    "Text-Dominant"
]


def get_json_path(dataset_root: str, language: str, scenario: str, risk_type: str) -> str:
    json_name = f"{scenario}.json"

    path_map = {
        "Image-Dominant-Visual": os.path.join(
            dataset_root, "1-Image-Dominant Risk", "Visual", language, json_name
        ),
        "Image-Dominant-Typography": os.path.join(
            dataset_root, "1-Image-Dominant Risk", "Typography", language, json_name
        ),
        "Image-Dominant-Mixed": os.path.join(
            dataset_root, "1-Image-Dominant Risk", "Mixed", language, json_name
        ),
        "Text-Dominant": os.path.join(
            dataset_root, "2-Text-Dominant Risk", language, json_name
        ),
    }

    return path_map[risk_type]


def load_question_image_pairs(
    dataset_root: str,
    language: str,
    scenario: str,
    risk_type: str
) -> List[Tuple[str, str]]:

    if language not in LANGUAGES:
        raise ValueError(f"Unsupported language: {language}")
    if scenario not in SCENARIOS:
        raise ValueError(f"Unsupported scenario: {scenario}")
    if risk_type not in RISK_ATTRIBUTION:
        raise ValueError(f"Unsupported risk_type: {risk_type}")

    json_path = get_json_path(dataset_root, language, scenario, risk_type)

    if not os.path.exists(json_path):
        raise FileNotFoundError(f"JSON file not found: {json_path}")

    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    img_root = os.path.join(dataset_root, "bundle_data")

    pairs = []
    for item in data:
        question = item.get("question", "")
        rel_img_path = item.get("image_path", "")
        img_path = os.path.normpath(os.path.join(img_root, rel_img_path))

        pairs.append((question, img_path))

    return pairs


def build_parser():
    parser = argparse.ArgumentParser(description="Load question-image pairs")

    parser.add_argument("--dataset_root", type=str, required=True)
    parser.add_argument("--language", type=str, required=True)
    parser.add_argument("--scenario", type=str, required=True)
    parser.add_argument("--risk_type", type=str, required=True)

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    pairs = load_question_image_pairs(
        dataset_root=args.dataset_root,
        language=args.language,
        scenario=args.scenario,
        risk_type=args.risk_type
    )

    print(f"{args.language} | {args.risk_type} | {args.scenario} loaded successfully")
    print(f"Loaded {len(pairs)} question-image pairs")


if __name__ == "__main__":
    main()
```

## Running Example

```bash
python load_data.py \
  --dataset_root ./dataset \
  --language English \
  --scenario "Physical Harm" \
  --risk_type Text-Dominant
```

Expected output:

```text
English | Text-Dominant | Physical Harm loaded successfully
Loaded XXXX question-image pairs
```

## Statement on Dual-Use Mitigation

Any form of unauthorized use, including but not limited to using the dataset without going through the official access process, redistributing the dataset in whole or in part to any third party without permission, or applying the dataset to research fields or practical scenarios beyond the stated safety-related research scope, is strictly prohibited.

In addition, all access activities and usage behaviors related to the dataset are subject to full-cycle and real-time auditing to ensure that every operation complies with the agreed terms and relevant regulations. If any violations are found, the access permission will be terminated immediately without prior notice, and corresponding legal enforcement actions will be taken in accordance with the agreements and relevant laws, with the ultimate aim of promoting the responsible and standardized use of the dataset.

## Citation

If you find Lingua-SafetyBench useful for your research, please cite our paper:

```bibtex
@article{linguasafetybench,
  title={Lingua-SafetyBench: A Benchmark for Safety Evaluation of Multilingual Vision-Language Models},
  author={},
  journal={arXiv preprint arXiv:2601.22737},
  year={2026}
}
```

## License

This dataset is released for academic research and AI safety evaluation purposes only. Any use of the dataset must comply with the access terms, applicable laws, ethical standards, and platform policies.
