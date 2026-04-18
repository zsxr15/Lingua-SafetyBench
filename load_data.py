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

if __name__ == "__main__":
    main()