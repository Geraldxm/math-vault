# DAPO-Math-17K

- 上游数据：[BytedTsinghua-SIA/DAPO-Math-17k](https://huggingface.co/datasets/BytedTsinghua-SIA/DAPO-Math-17k)
- 上游 revision：`65877096c24ffa7abc4e4fa5edb95cf3413a5674`
- 上游 artifact：`data/dapo-math-17k.parquet`，1,791,700 行
- 论文：[DAPO: An Open-Source LLM Reinforcement Learning System at Scale](https://arxiv.org/abs/2503.14476)
- 上游声明许可证：Apache-2.0

本目录只登记官方发布入口，不重新托管 285 MB parquet。官方文件包含同一 17,917 行 block 的 100 次连续重复，并在题面外包有固定 prompt；去除存储重复和 prompt 的 JSONL 版本见 [`derived/dapo_math_17k_compact`](../../derived/dapo_math_17k_compact/README.md)。
