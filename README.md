# math-vault

[![Code and docs: MIT](https://img.shields.io/badge/code%20%26%20docs-MIT-green)](LICENSE)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21411213.svg)](https://doi.org/10.5281/zenodo.21411213)

Curated, traceable snapshots of public mathematical reasoning datasets. All datasets normalized to `id/problem/answer` canonical JSONL with per-source provenance records. Designed to feed [math-eval](https://github.com/Geraldxm/math-eval) directly.

这是一个持续维护、可扩展的数据仓库：下表描述当前快照；后续版本可以继续纳入新的数学数据集，并沿用同一套 provenance、canonical schema 和 parser audit 流程。

## 当前数据快照

Zenodo `v0.1.0` 冻结版包含 15 个 evaluation subsets、32,226 条 parser-valid evaluation rows；另有 19 条 Omni-MATH 记录隔离在 `canonical/omni_math/issues.jsonl` 供审计，不进入评测。

| 数据 | 本地文件 | 行数 | 上游许可证 |
|---|---|---:|---|
| AIME 2024 | `source/aime_2024/train.jsonl` | 30 | 未声明 |
| AIME 2025 | `source/aime_2025/train.jsonl` | 30 | CC BY-NC-SA 4.0 |
| AIME 2026 | `source/aime_2026/train.jsonl` | 30 | CC BY-NC-SA 4.0 |
| AIMO validation AIME | `source/aimo_validation_aime/train.jsonl` | 90 | Apache-2.0 |
| AIMO validation AMC | `source/aimo_validation_amc/train.jsonl` | 83 | Apache-2.0 |
| AMC 2023 | `source/amc_2023/test.jsonl` | 40 | 未声明 |
| BrUMO 2025 | `source/brumo_2025/train.jsonl` | 30 | CC BY-NC-SA 4.0 |
| CMIMC 2025 | `source/cmimc_2025/train.jsonl` | 40 | CC BY-NC-SA 4.0 |
| GSM8K | `source/gsm8k/{train,test}.jsonl` | 7,473 / 1,319 | MIT |
| HMMT February 2025 | `source/hmmt_feb_2025/train.jsonl` | 30 | CC BY-NC-SA 4.0 |
| Hendrycks MATH | `source/hendrycks_math/{train,test}.jsonl` | 7,500 / 5,000 | MIT |
| MATH-500 | `source/math_500/test.jsonl` | 500 | 未声明 |
| Minerva-Math | `source/minerva_math/train.jsonl` | 272 | 未声明 |
| Omni-MATH | `source/omni_math/train.jsonl` | 4,428 | Apache-2.0 |
| OlympiadBench `OE_TO_maths_en_COMP` | `source/olympiad_bench/train.jsonl` | 674 | Apache-2.0 |
| DAPO-Math-17K | `source/dapo_math_17k/README.md` | 上游入口 | Apache-2.0 |
| math-eval canonical | `canonical/` | 32,226 | 继承各父数据 |
| DAPO-Math-17K compact | `derived/dapo_math_17k_compact/train.jsonl` | 17,917 | Apache-2.0 |
| DAPO-Math-17K dedup | `derived/dapo_math_17k_dedup/train.jsonl` | 17,176 | Apache-2.0 |
| Hendrycks MATH normalized | `derived/hendrycks_math/{train,test}.jsonl` | 7,500 / 5,000 | MIT |
| OPD DAPO-Math-17K dedup | `repo/opd_dapo_math_17k_dedup/train.parquet` | 17,176 | Apache-2.0 |
| EOPD Hendrycks MATH | `repo/eopd_hendrycks_math/train.parquet` | 7,500 | MIT |

每个数据目录的 README 记录该对象的完整 provenance。"未声明" 表示上游未给出许可证，不代表公有领域。

## 目录约定

- `source/`：上游 artifact 快照。仅允许不改变行、字段、顺序和内容的序列化转换（如 parquet → JSONL）。
- `derived/`：过滤、去重、去 prompt 或采样后的版本。每个目录记录父数据、转换规则和重建脚本。
- `canonical/`：由 source/derived 机械转换、可直接被 math-eval 读取的 `id/problem/answer` 版本。
- `repo/`：绑定具体代码仓库、checkpoint 或训练 setting 的数据适配，例如特定 prompt 和训练框架 schema；不得作为 source/derived/canonical 的父数据。

source/derived/canonical 只保存 JSONL。repo 可保存带完整 provenance 和重建脚本的训练格式；论文仓库副本、临时实验子集和 run manifest 仍不属于本仓库范围。

## 重建

DAPO dedup：

```bash
python derived/dapo_math_17k_dedup/build.py
```

math-eval canonical：

```bash
python canonical/build.py
```

均只依赖 Python 标准库。

## 引用

```bibtex
@dataset{ge_math_vault_2026,
  author  = {Ge, Xinmu},
  title   = {math-vault: Curated, Traceable Snapshots of Public Mathematical Reasoning Datasets},
  year    = {2026},
  version = {v0.1.0},
  doi     = {10.5281/zenodo.21411214},
  url     = {https://doi.org/10.5281/zenodo.21411214}
}
```

代码与文档使用 [MIT License](LICENSE)。数据归各自上游权利人所有，遵循各数据目录所列的上游条款；本仓库的 MIT License 不对数据重新授权。
