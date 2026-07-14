# AIME 2026

- 上游数据: [MathArena/aime_2026](https://huggingface.co/datasets/MathArena/aime_2026)
- 上游 revision: `d2de22f3c656b4f56cf8981212186377d1e23bc3`
- 上游 artifact: `data/train-00000-of-00001.parquet`
- 上游数据条数: 30
- 文件: `train.jsonl`（由上游 parquet 无损逐行转存）
- 本数据条数: 30
- 字段: `problem_idx`, `answer`, `problem`
- 领域: AIME 数学竞赛
- 难度: AIME 2026
- 答案格式: 整数（`0`–`999`；本地 gold 为整数类型，不保留前导零）
- 推荐解析方式: 原题未规定模型输出封装；建议评测 prompt 要求 `\boxed{}`，从最后一个 box 或明确的 final-answer 段提取一个十进制整数，校验 `0 ≤ n ≤ 999` 后按整数精确比较，忽略前导零。参考 [MathArena parser](https://github.com/eth-sri/matharena/blob/a11194deff8c67a232974a383795e8a2776b4c6f/src/matharena/parser.py)
- 原始发布时间: 2026-02 (AIME I/II 考试)
- HF 发布: 2026-02 (MathArena/aime_2026)
- SHA256: `3c03a0a42d8f844a099f78a5ae636b8f657dc07cd35c9ccb30846aa5e9e21259`
- 上游声明许可证: CC BY-NC-SA 4.0

## 数据源对比

| 数据源 | 题目数 | 字段 | 许可 | 备注 |
|---|---:|---|---|---|
| [MathArena/aime_2026](https://huggingface.co/datasets/MathArena/aime_2026) | 30 | problem_idx, answer, problem | CC BY-NC-SA 4.0 | 当前使用，AIME I+II 全量 |
| [math-ai/aime26](https://huggingface.co/datasets/math-ai/aime26) | 30 | id, problem, answer | Apache 2.0 | 答案与 MathArena 完全一致，字段略有不同 |
| [MathArena/aime_2026_I](https://huggingface.co/datasets/MathArena/aime_2026_I) | 15 | problem_idx, answer, problem | CC BY-NC-SA 4.0 | 仅 AIME I，答案全部包含在上述 30 题中 |
| [LumiOpen/mAIME2026](https://huggingface.co/datasets/LumiOpen/mAIME2026) | 30 | id, question, solution, url, language | — | 丹麦语/芬兰语翻译版 |
