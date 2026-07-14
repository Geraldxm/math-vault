# HMMT February 2025

- 上游数据: [MathArena/hmmt_feb_2025](https://huggingface.co/datasets/MathArena/hmmt_feb_2025)
- 上游 revision: `6fdc4277120810ff75aa22d2d5489b91f7a262a1`
- 上游 artifact: `data/train-00000-of-00001.parquet`
- 竞赛: Harvard-MIT Mathematics Tournament February 2025
- 文件: `train.jsonl`（由上游 parquet 无损逐行转存）
- 条数: 30
- 字段: `problem_idx`, `problem`, `answer`, `problem_type`
- 答案格式: 字符串；14 题为整数，16 题为 LaTeX 数学表达式，其中 1 题为多答案
- 推荐提取方式: 评测 prompt 要求最终答案放入 `\boxed{}`；提取最后一个 `\boxed{}` / `\fbox{}`，支持嵌套花括号及同一末行的多个 box，再做数值或符号等价判定。不要直接按逗号切分。参考 [MathArena parser](https://github.com/eth-sri/matharena/blob/a11194deff8c67a232974a383795e8a2776b4c6f/src/matharena/parser.py)
- SHA256: `d6483ddf5a456d5a65c814868c576183688f53d8431308070cb4e9aa89af2914`
- 上游声明许可证: CC BY-NC-SA 4.0
- 原始发布时间: 2025-02 (HMMT February 2025 竞赛日)
- HF 发布: 2025-06 (MathArena/hmmt_feb_2025)
