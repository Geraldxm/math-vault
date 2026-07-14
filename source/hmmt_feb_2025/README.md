# HMMT February 2025

- 上游数据: [MathArena/hmmt_feb_2025](https://huggingface.co/datasets/MathArena/hmmt_feb_2025)
- 上游 revision: `6fdc4277120810ff75aa22d2d5489b91f7a262a1`
- 上游 artifact: `data/train-00000-of-00001.parquet`
- 上游数据条数: 30
- 文件: `train.jsonl`（由上游 parquet 无损逐行转存）
- 本数据条数: 30
- 字段: `problem_idx`, `problem`, `answer`, `problem_type`
- 领域: Harvard-MIT Mathematics Tournament；本地 `problem_type` 覆盖 Algebra、Combinatorics、Geometry、Number Theory 及组合标签
- 难度: HMMT February 2025 竞赛题
- 答案格式: 字符串；14 题为整数，16 题为 LaTeX 数学表达式，其中 1 题为多答案
- 推荐解析方式: 评测 prompt 要求最终答案放入 `\boxed{}`；提取最后一个 `\boxed{}` / `\fbox{}`，支持嵌套花括号及同一末行的多个 box，再做数值或符号等价判定。不要直接按逗号切分。参考 [MathArena parser](https://github.com/eth-sri/matharena/blob/a11194deff8c67a232974a383795e8a2776b4c6f/src/matharena/parser.py)
- 原始发布时间: 2025-02 (HMMT February 2025 竞赛日)
- HF 发布: 2025-06 (MathArena/hmmt_feb_2025)
- SHA256: `d6483ddf5a456d5a65c814868c576183688f53d8431308070cb4e9aa89af2914`
- 上游声明许可证: CC BY-NC-SA 4.0
