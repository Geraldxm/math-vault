# AIME 2024

- 上游数据: [HuggingFaceH4/aime_2024](https://huggingface.co/datasets/HuggingFaceH4/aime_2024)
- 上游 revision: `2fe88a2f1091d5048c0f36abc874fb997b3dd99a`
- 上游 artifact: `data/train-00000-of-00001.parquet`
- 上游数据条数: 30
- 文件: `train.jsonl`（由上游 parquet 无损逐行转存）
- 本数据条数: 30
- 字段: `id`, `problem`, `solution`, `answer`, `url`, `year`
- 领域: AIME 数学竞赛
- 难度: AIME 2024
- 答案格式: 三位十进制非负整数字符串（`000`–`999`，不足三位补前导零）
- 推荐解析方式: 原题未规定模型输出封装；建议评测 prompt 要求 `\boxed{}`，从最后一个 box 或明确的 final-answer 段提取一个十进制整数，校验 `0 ≤ n ≤ 999` 后按整数精确比较，因此 `023` 与 `23` 等价。参考 [MathArena parser](https://github.com/eth-sri/matharena/blob/a11194deff8c67a232974a383795e8a2776b4c6f/src/matharena/parser.py)
- 原始发布时间: 2024-02 (AIME I/II 考试)
- HF 发布: 2025-01 (HuggingFaceH4/aime_2024)
- SHA256: `66675268a74beba516b24e94426906b8730c38c3409f58ff683d252cf5aa2ce7`
- 上游声明许可证: 未声明

## 数据源对比

| 数据源 | 题目数 | 字段 | 许可 | 备注 |
|---|---:|---|---|---|
| [HuggingFaceH4/aime_2024](https://huggingface.co/datasets/HuggingFaceH4/aime_2024) | 30 | id, problem, solution, answer, url, year | — | 当前使用，AIME I+II 全量，含解答 |
| [Maxwell-Jia/AIME_2024](https://huggingface.co/datasets/Maxwell-Jia/AIME_2024) | 30 | ID, Problem, Solution, Answer | MIT | 同上 30 题，答案一致（H4 补零到 3 位，MJ 不补零） |
| [di-zhang-fdu/AIME_1983_2024](https://huggingface.co/datasets/di-zhang-fdu/AIME_1983_2024) | 933（1983–2024） | ID, Year, Question, Answer, Part | MIT | 2024 仅 14 题（AIME I），不含 AIME II，不全 |
| [werty1248/AIME-2024-Ko-Translated](https://huggingface.co/datasets/werty1248/AIME-2024-Ko-Translated) | 30 | +problem_ko | — | 韩语翻译版 |
