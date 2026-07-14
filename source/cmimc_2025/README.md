# CMIMC 2025

- 上游数据: [MathArena/cmimc_2025](https://huggingface.co/datasets/MathArena/cmimc_2025)
- 上游 revision: `8f27517ce4ad1d05e023c0e7eca4344754ba2a04`
- 上游 artifact: `data/train-00000-of-00001.parquet`
- 竞赛: Carnegie Mellon Informatics and Mathematics Competition 2025
- 文件: `train.jsonl`（由上游 parquet 无损逐行转存）
- 条数: 40
- 字段: `problem_idx`, `problem`, `answer`, `problem_type`
- 答案格式: 字符串；16 题为整数，其余为 LaTeX 数学表达式或十进制数
- 推荐提取方式: 评测 prompt 要求最终答案放入 `\boxed{}`；提取最后一个 `\boxed{}` / `\fbox{}` 并支持嵌套花括号，再做数值或符号等价判定；十进制答案不要经二进制浮点做严格相等比较。参考 [MathArena parser](https://github.com/eth-sri/matharena/blob/a11194deff8c67a232974a383795e8a2776b4c6f/src/matharena/parser.py)
- SHA256: `6f50851fc59f7c8109f3314ab1494e0138d89e4af0c70647f69a07093e50c1bf`
- 上游声明许可证: CC BY-NC-SA 4.0
- 原始发布时间: 2025-03 (CMIMC 竞赛日: 2025-03-15)
- HF 发布: 2025-06 (MathArena/cmimc_2025)
