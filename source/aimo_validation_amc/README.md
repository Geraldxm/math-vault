# AIMo Validation AMC

- 上游数据: [AI-MO/aimo-validation-amc](https://huggingface.co/datasets/AI-MO/aimo-validation-amc)
- 上游 revision: `69d78a4a2c840e82d69af6bc742bda09005f6316`
- 上游 artifact: `data/train-00000-of-00001.parquet`
- 文件: `train.jsonl`（由上游 parquet 无损逐行转存）
- 条数: 83
- 字段: `id`, `problem`, `answer`, `url`
- 答案格式: 整数（含负数；本地范围 `-4`–`8178`）
- 推荐提取方式: 原题未规定模型输出封装；建议评测 prompt 要求 `\boxed{}`，从最后一个 box 或明确的 final-answer 段提取一个有符号十进制整数，再按整数精确比较。参考 [Math-Verify `ExprExtractionConfig`](https://github.com/huggingface/Math-Verify)
- 内容: AMC 12 2022–2023 独立题（2022 12A 22 题 + 2022 12B 21 题 + 2023 12A 22 题 + 2023 12B 18 题）
- 原始发布时间: 2022-11 (AMC 12 2022) ~ 2023-11 (AMC 12 2023)
- HF 发布: 2024-07 (AI-MO/aimo-validation-amc)
- SHA256: `ce1a63706f20e9d5c51cd369a5bb38fcba9d2fa914f4a63ed8270f0c3b5080a6`
- 上游声明许可证: Apache-2.0

## 命名与背景

AIMO = AI Mathematical Olympiad（AIMO Progress Prize 竞赛）。本数据集是 AI-MO 团队参赛时使用的内部验证集（validation set），并非官方 AMC 题目。

## 题目已被改写

原始 AMC 12 为五选一选择题，本数据集将可数值化的题目改写为整数填空题以匹配 AIMO 竞赛格式。无法自然改写为数值答案的题目已被剔除，因此每套 25 题最终剩余约 20 题。**题目文本不是未经修改的 AMC 原题**。

## 与 amc_2023 的关系

本数据集的 2023 部分（40 题）与 `amc_2023` 完全一致，多出 2022 年份的 43 题。

## ID 设计

`id` 范围 0–49，但跨年份不唯一；它不能作为整个文件的题目唯一标识。
