# DAPO-Math-17K

- 上游数据: [BytedTsinghua-SIA/DAPO-Math-17k](https://huggingface.co/datasets/BytedTsinghua-SIA/DAPO-Math-17k)
- 论文: [DAPO: An Open-Source LLM Reinforcement Learning System at Scale](https://arxiv.org/abs/2503.14476)
- 上游 revision: `65877096c24ffa7abc4e4fa5edb95cf3413a5674`
- 上游 artifact: `data/dapo-math-17k.parquet`
- 上游数据条数: 1,791,700
- 文件: 无（仅登记上游入口）
- 本数据条数: 不适用
- 字段: 不适用（本目录不托管数据文件）
- 领域: 数学推理题；派生版本保留 `rule-lighteval/MATH_v2` 风格标记
- 难度: 上游未提供统一难度标签
- 答案格式: 官方 parquet 中题面外包固定 prompt，prompt 末行包含 `Answer:` 后的有符号十进制答案
- 推荐解析方式: 使用 [`derived/dapo_math_17k_compact`](../../derived/dapo_math_17k_compact/README.md) 或 [`derived/dapo_math_17k_dedup`](../../derived/dapo_math_17k_dedup/README.md)，不要直接把 100 次重复的官方 parquet 当作评测集。
- 上游声明许可证: Apache-2.0

## 说明

本目录只登记官方发布入口，不重新托管约 285 MB parquet。官方文件包含同一 17,917 行 block 的 100 次连续重复，并在题面外包有固定 prompt；去除存储重复和 prompt 的 JSONL 版本见 [`derived/dapo_math_17k_compact`](../../derived/dapo_math_17k_compact/README.md)。
