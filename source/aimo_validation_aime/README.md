# AIMO Validation AIME

- 上游数据: [AI-MO/aimo-validation-aime](https://huggingface.co/datasets/AI-MO/aimo-validation-aime)
- 上游 revision: `13f9e12f613e720c2a2b2f345dd04b998a29494d`
- 上游 artifact: `data/train-00000-of-00001.parquet`
- 上游数据条数: 90
- 文件: `train.jsonl`（由上游 parquet 无损逐行转存）
- 本数据条数: 90
- 字段: `id`, `problem`, `solution`, `answer`, `url`
- 领域: AIME 数学竞赛
- 难度: AIME 2022–2024
- 答案格式: 三位十进制非负整数字符串（`000`–`999`，不足三位补前导零）
- 推荐解析方式: 原题未规定模型输出封装；建议评测 prompt 要求 `\boxed{}`，从最后一个 box 或明确的 final-answer 段提取一个十进制整数，校验 `0 ≤ n ≤ 999` 后按整数精确比较，因此 `004` 与 `4` 等价。参考 [MathArena parser](https://github.com/eth-sri/matharena/blob/a11194deff8c67a232974a383795e8a2776b4c6f/src/matharena/parser.py)
- SHA256: `fa42838c9d643be2fa83671fb7960a31bae75d5fe73b902cca9f21cbf70607ee`
- 上游声明许可证: Apache-2.0

## 说明

内容为 AIME 2022–2024，每年 AIME I/II 共 30 题。题目和解答来自 AoPS Wiki；这是 AI-MO 团队参加 AIMO Progress Prize 时使用的内部验证集。
