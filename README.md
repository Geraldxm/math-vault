# math-vault

Curated, traceable snapshots of public mathematical reasoning datasets.

## 数据目录

| 数据 | 本地文件 | 行数 | 上游声明许可证 |
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
| MATH-500 | `source/math_500/test.jsonl` | 500 | 未声明 |
| Minerva-Math | `source/minerva_math/train.jsonl` | 272 | 未声明 |
| Omni-MATH | `source/omni_math/train.jsonl` | 4,428 | Apache-2.0 |
| OlympiadBench `OE_TO_maths_en_COMP` | `source/olympiad_bench/train.jsonl` | 674 | Apache-2.0 |
| DAPO-Math-17K | `source/dapo_math_17k/README.md` | 上游入口 | Apache-2.0 |
| math-eval canonical | `canonical/` | 32,228（另 17 个 issue 行） | 继承各父数据 |
| DAPO-Math-17K compact | `derived/dapo_math_17k_compact/train.jsonl` | 17,917 | Apache-2.0 |
| DAPO-Math-17K dedup | `derived/dapo_math_17k_dedup/train.jsonl` | 17,176 | Apache-2.0 |

每个数据目录的 README 是该对象的详细 provenance；表中的 "未声明" 表示所引用的上游数据页没有给出许可证，不表示数据属于公有领域。

## 目录约定

- `source/`：上游公开 artifact 的快照。允许 parquet → JSONL 这类不改变行、字段、顺序和内容的序列化转换。
- `derived/`：任何过滤、去重、去 prompt、冲突处理或采样后的版本。每个目录记录父数据、转换规则和重建脚本。
- `canonical/`：由 source/derived 机械转换、可由 math-eval 直接读取并经当前 parser 全量检查的 `id/problem/answer` 版本。

仓库只保存 JSONL。论文仓库副本、实验子集、实验用 prompt template 和 run manifest 不属于本仓库范围。

## 重建数据

DAPO dedup 版本只依赖 Python 标准库：

```bash
python derived/dapo_math_17k_dedup/build.py
```

math-eval canonical 数据同样只依赖 Python 标准库：

```bash
python canonical/build.py
```

## 引用与许可证

如果本仓库对你的研究有帮助，请引用 [`CITATION.cff`](CITATION.cff) 或直接复制以下 BibTeX：

```bibtex
@software{ge_math_vault_2026,
  author  = {Ge, Xinmu},
  title   = {math-vault: Curated, Traceable Snapshots of Public Mathematical Reasoning Datasets},
  year    = {2026},
  url     = {https://github.com/Geraldxm/math-vault},
  license = {MIT}
}
```

仓库中的整理代码和文档使用 [MIT License](LICENSE)。数据仍归各自上游作者或权利人所有，并遵循各数据目录所列的上游条款；本仓库的 MIT License 不对这些数据重新授权。使用或再分发数据前，请检查相应上游页面和许可证。
