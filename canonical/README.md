# math-eval canonical datasets

## 范围与 schema

`canonical/` 将 math-vault 的 source/derived 数据确定性转换为 math-eval 输入。评测文件为 JSONL，每行至少包含非空且唯一的字符串 `id`，以及非空的 `problem`、`answer`。

`solution`、`source`、`metadata` 仅保留用于审计。

`issues.jsonl` 保存不能由当前 parser 可靠处理的原始行，不是 math-eval 输入。数据许可与 provenance 以各父目录 README 为准。

## 数据

| 数据集 | 评测文件 | 评测行数 | 转换 |
|---|---|---:|---|
| AIME 2024 | `aime_2024/train.jsonl` | 30 | 字段映射 |
| AIME 2025 | `aime_2025/train.jsonl` | 30 | 字段映射 |
| AIME 2026 | `aime_2026/train.jsonl` | 30 | 字段映射 |
| AIMO Validation AIME | `aimo_validation_aime/train.jsonl` | 90 | 字段映射 |
| AIMO Validation AMC | `aimo_validation_amc/train.jsonl` | 83 | 以上游 URL 作为唯一 ID |
| AMC 2023 | `amc_2023/test.jsonl` | 40 | 字段映射 |
| BrUMO 2025 | `brumo_2025/train.jsonl` | 30 | 字段映射 |
| CMIMC 2025 | `cmimc_2025/train.jsonl` | 40 | 字段映射 |
| DAPO-Math-17K dedup | `dapo_math_17k_dedup/train.jsonl` | 17,176 | 复用去重且排除冲突的版本 |
| GSM8K | `gsm8k/{train,test}.jsonl` | 7,473 / 1,319 | 提取 `####` 后的最终答案 |
| HMMT February 2025 | `hmmt_feb_2025/train.jsonl` | 30 | 字段映射 |
| MATH-500 | `math_500/test.jsonl` | 500 | 字段映射 |
| Minerva-Math | `minerva_math/train.jsonl` | 272 | 提取 solution 中最后一个完整 box |
| Omni-MATH | `omni_math/train.jsonl` | 4,411 | 17 个问题行转存至 `omni_math/issues.jsonl` |
| OlympiadBench `OE_TO_maths_en_COMP` | `olympiad_bench/train.jsonl` | 674 | 提取唯一 `final_answer` |

Omni-MATH 的 4,428 个父数据行均被保留：4,411 行进入评测文件，17 行进入审计文件。

| issue | 行数 | 含义 |
|---|---:|---|
| `empty_answer` | 9 | answer 为空 |
| `malformed_latex` | 5 | LaTeX 括号不完整 |
| `piecewise_text` | 1 | 当前 parser 不支持该分段文本格式 |
| `verification_error` | 1 | Math-Verify 触发 `PrecisionExhausted` |
| `multiple_boxed_answers` | 1 | 单个 gold 含多个 boxed 函数族 |

## 重建

`build.py` 是数据物化脚本，不参与模型生成或判分。它从固定父文件重建全部 canonical JSONL，检查行数、ID 唯一性和必需字段，并将父文件与输出文件的 SHA256 写入 `manifest.json`。

```bash
python canonical/build.py
```

## 验证

`check_answers.py` 先核对 manifest checksum，再使用 math-eval 当前 parser 检查每个 gold。

```bash
/path/to/math-eval/.venv/bin/python canonical/check_answers.py /path/to/math-eval
```

审计基线（2026-07-15）：math-eval `math-v3`、Math-Verify 0.9.0，32,228 / 32,228 个评测答案通过，失败数为 0。
