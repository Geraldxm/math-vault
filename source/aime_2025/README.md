# AIME 2025

- 上游数据: [MathArena/aime_2025](https://huggingface.co/datasets/MathArena/aime_2025)
- 上游 revision: `c94da77eb22bbd6439e62a323bec18493a421302`
- 上游 artifact: `data/train-00000-of-00001.parquet`
- 上游数据条数: 30
- 文件: `train.jsonl`（由上游 parquet 无损逐行转存）
- 本数据条数: 30
- 字段: `problem_idx`, `problem`, `answer`, `problem_type`
- 领域: AIME 数学竞赛；本地 `problem_type` 覆盖 Algebra、Combinatorics、Geometry、Number Theory 及组合标签
- 难度: AIME 2025
- 答案格式: 整数（`0`–`999`；本地 gold 为整数类型，不保留前导零）
- 推荐解析方式: 原题未规定模型输出封装；建议评测 prompt 要求 `\boxed{}`，从最后一个 box 或明确的 final-answer 段提取一个十进制整数，校验 `0 ≤ n ≤ 999` 后按整数精确比较，忽略前导零。参考 [MathArena parser](https://github.com/eth-sri/matharena/blob/a11194deff8c67a232974a383795e8a2776b4c6f/src/matharena/parser.py)
- 原始发布时间: 2025-02 (AIME I/II 考试)
- HF 发布: 2025-05 (MathArena/aime_2025)
- SHA256: `15a0cdfb6ad94ccca14604702fc26126c92ec73ac4125d85e692fa16637b9359`
- 上游声明许可证: CC BY-NC-SA 4.0

## 数据源对比

| 数据源 | 题目数 | 字段 | 许可 | 备注 |
|---|---:|---|---|---|
| [MathArena/aime_2025](https://huggingface.co/datasets/MathArena/aime_2025) | 30 | problem_idx, problem, answer, problem_type | CC BY-NC-SA 4.0 | 当前使用，AIME I+II 全量 |
| [yentinglin/aime_2025](https://huggingface.co/datasets/yentinglin/aime_2025) | 30 | id, problem, answer, solution, url, year | — | 答案与 MathArena 完全一致，字段更全（含解答） |
| [opencompass/AIME2025](https://huggingface.co/datasets/opencompass/AIME2025) | 30 | question, answer | — | 分为 I/II 两个文件；答案一致，仅一道 `336^\circ` vs `336` 格式差异 |
| [allganize/AIME2025-ko](https://huggingface.co/datasets/allganize/AIME2025-ko) | 30 | +problem_ko | — | 韩语翻译版，人工校验 |
