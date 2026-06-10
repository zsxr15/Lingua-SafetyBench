---
pretty_name: Lingua-SafetyBench
thumbnail: intro.png
---

<p align="center">
  <img src="intro.png" width="720">
</p>

# Lingua-SafetyBench

A Benchmark for Safety Evaluation of Multilingual Vision-Language Models.

The code and dataset will be progressively released here.

## Dataset

We provide our multilingual and multimodal dataset for safety evaluation.

Lingua-SafetyBench is a large-scale multilingual multimodal safety benchmark designed to evaluate the safety robustness of Vision-Language Large Models (VLLMs) under joint multilingual and multimodal inputs. Unlike prior benchmarks that mainly focus on either multilingual text-only safety or monolingual multimodal safety, Lingua-SafetyBench provides diverse image-text pairs across multiple languages and visual formats, enabling a more realistic evaluation of cross-lingual and cross-modal safety risks.

The benchmark contains 100,440 harmful image-text pairs covering 10 languages: Arabic, Chinese, English, Finnish, French, German, Japanese, Norwegian, Russian, and Spanish. To better analyze the source of safety risks, the dataset is explicitly divided into two subsets: image-dominant risks, where the unsafe intent is primarily conveyed through visual content, and text-dominant risks, where the harmful intent mainly comes from textual instructions. The image-dominant subset further includes pure visual, typographic, and mixed image types.

Lingua-SafetyBench covers eight major safety scenarios: Economic Harm, Fraud, Hate Speech, Illegal Activity, Malware Generation, Physical Harm, Privacy Violence, and Sex. This design allows researchers to systematically evaluate how VLLMs respond to harmful multimodal requests across different languages, scripts, resource levels, and risk-dominant modalities.

This dataset is strictly intended for academic research and AI safety evaluation purposes only, including model safety analysis, robustness assessment, and safety alignment research. It must not be used for any real-world harmful behavior, illegal activities, offensive system development, malicious content generation, safety bypassing, commercial misuse, or any other non-research purpose. Users are solely responsible for ensuring that their use of this dataset complies with applicable laws, ethical standards, access terms, and platform policies, and for any consequences arising from its use.

## Dataset Access

The dataset is available on Hugging Face:

[Hugging Face Dataset](https://huggingface.co/datasets/leaf-pear/Lingua-SafetyBench)

Users must follow the official access process before using the dataset. Redistribution of the dataset, in whole or in part, is not permitted without explicit authorization.

## Data Loading

Please refer to `load_data.py` in this repository for an example of how to load question-image pairs from Lingua-SafetyBench.

Example usage:

```bash
python load_data.py \
  --dataset_root ./dataset \
  --language English \
  --scenario "Physical Harm" \
  --risk_type Text-Dominant
```

The script loads the corresponding subset and returns question-image pairs for evaluation.

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

## Statement on Dual-Use Mitigation

Any form of unauthorized use is strictly prohibited, including but not limited to using the dataset without completing the official access process, redistributing the dataset in whole or in part to any third party without permission, or applying the dataset to research fields or practical scenarios beyond the stated AI safety research scope.

Access to the dataset may be reviewed to ensure compliance with the agreed terms and applicable regulations. If any violation is identified, access permission may be terminated without prior notice. Further action may be taken in accordance with the applicable agreements, laws, and regulations. The purpose of these restrictions is to promote the responsible and standardized use of the dataset.

## Citation

If you find Lingua-SafetyBench useful for your research, please cite our paper:

```bibtex
@article{shi2026lingua,
  title={Lingua-SafetyBench: A Benchmark for Safety Evaluation of Multilingual Vision-Language Models},
  author={Shi, Enyi and Shao, Pengyang and Zhang, Yanxin and Cui, Chenhang and Lyu, Jiayi and Xia, Xiaobo and Shen, Fei and Chua, Tat-Seng},
  journal={arXiv preprint arXiv:2601.22737},
  year={2026}
}
```

#### Terms of Use

This dataset is released for academic research and AI safety evaluation purposes only. Any use of the dataset must comply with the official access terms, applicable laws, ethical standards, and platform policies.
