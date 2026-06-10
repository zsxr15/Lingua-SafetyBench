# Lingua-SafetyBench

A Benchmark for Safety Evaluation of Multilingual Vision-Language Models.


## Dataset

We provide our multilingual and multimodal dataset for safety evaluation here.

Lingua-SafetyBench is a large-scale multilingual multimodal safety benchmark designed to evaluate the safety robustness of Vision-Language Large Models (VLLMs) under joint multilingual and multimodal inputs. Unlike prior benchmarks that mainly focus on either multilingual text-only safety or monolingual multimodal safety, Lingua-SafetyBench provides diverse image-text pairs across multiple languages and visual formats, enabling a more realistic evaluation of cross-lingual and cross-modal safety risks.

The benchmark contains 100,440 harmful image-text pairs covering 10 languages: Arabic, Chinese, English, French, German, Japanese, Norwegian, Finnish, Russian, and Spanish. To better analyze the source of safety risks, the dataset is explicitly divided into two subsets: image-dominant risks, where the unsafe intent is primarily conveyed through visual content, and text-dominant risks, where the harmful intent mainly comes from textual instructions. The image-dominant subset further includes pure visual, typographic, and mixed image types.

Lingua-SafetyBench covers eight major safety scenarios: economic harm, fraud, hate speech, illegal activity, malware generation, physical harm, privacy violations, and sexual content. This design allows researchers to systematically evaluate how VLLMs respond to harmful multimodal requests across different languages, scripts, resource levels, and risk-dominant modalities.

This dataset is strictly intended for academic research and AI safety evaluation purposes only, including model safety analysis, robustness assessment, and safety alignment research. It must not be used for any real-world harmful behavior, illegal activities, offensive system development, malicious content generation, safety bypassing, commercial misuse, or any other non-research purpose. Users are solely responsible for ensuring that their use of this dataset complies with applicable laws, ethical standards, and platform policies, and for any consequences arising from its use.

## Statement on Dual-Use Mitigation

Any form of unauthorized use, including but not limited to using the dataset without going through the official access process, redistributing the dataset in whole or in part to any third party without permission, or applying the dataset to research fields or practical scenarios beyond the stated safety-related research scope, is strictly prohibited. In addition, all access activities and usage behaviors related to the dataset are subject to full-cycle and real-time auditing to ensure that every operation complies with the agreed terms and relevant regulations. If any violations are found, the access permission will be terminated immediately without prior notice, and corresponding legal enforcement actions will be taken in accordance with the agreements and relevant laws, with the ultimate aim of promoting the responsible and standardized use of the dataset.
