# Omni-MATH

- 上游数据: [KbsdJames/Omni-MATH](https://huggingface.co/datasets/KbsdJames/Omni-MATH)
- 论文: [Omni-MATH: A Universal Olympiad Level Mathematic Benchmark For Large Language Models](https://arxiv.org/abs/2410.07985)
- 上游 revision: `40ba231d8f16e29ecd40e6407e2c8640145a8f62`
- 上游 artifact: `data/test-00000-of-00001.parquet`
- 上游数据条数: 4,428
- 文件: `train.jsonl`（由上游 parquet 无损逐行转存）
- 本数据条数: 4,428
- 字段: `domain` (List[string] 多级学科标签), `difficulty` (float64, 1.0–9.5), `problem`, `solution`, `answer`, `source`
- 领域: 33+ 子领域，覆盖代数、几何、数论、组合、概率统计、离散数学等
- 难度: `difficulty` 1.0–9.5，均值 5.0，中位约 5
- 答案格式: 不统一，以文本描述和 LaTeX 数学表达式为主
- 推荐解析方式: 评测 prompt 要求最终答案放入 `\boxed{}`；根据答案内容做数值、LaTeX 符号、集合或文本等价判定，不能只做原始字符串比较。
- HF 发布: 2024-10
- SHA256: `7c87be8ee41ac7c7a597ef5a5500e84bd2b639a85a06db3da7f69bf9a32ef168`
- 上游声明许可证: Apache-2.0

## 说明

题目来源覆盖各国家队选拔考试、IMO 相关赛事和国际竞赛。本地文件名使用 `train.jsonl`，但上游 artifact 名称为 `test-00000-of-00001.parquet`。
