# MATH-500

- 上游数据: [HuggingFaceH4/MATH-500](https://huggingface.co/datasets/HuggingFaceH4/MATH-500)
- 上游 revision: `6e4ed1a2a79af7d8630a6b768ec859cb5af4d3be`
- 上游 artifact: `test.jsonl`
- 文件: `test.jsonl`
- 条数: 500
- 字段: `problem`, `solution`, `answer`, `subject`, `level`, `unique_id`
- 答案格式: 字符串；混合整数、十进制数、LaTeX 表达式、方程、区间/元组与文本答案
- 推荐提取方式: 评测 prompt 要求最终答案放入 `\boxed{}`；提取最后一个 box 并支持嵌套花括号，再根据 gold 类型分别解析数值、LaTeX、方程、集合/区间或文本并做等价判定。逗号也可能是元组、区间或千位分隔，不能直接切分。参考 [Hugging Face Math-Verify](https://github.com/huggingface/Math-Verify)
- 原始发布时间: 2021-03 (Hendrycks et al., MATH dataset)
- HF 发布: 2024-11 (HuggingFaceH4/MATH-500)
- SHA256: `35dc41080a3680858b27fa7e0533d2d547825316fc5dafe5d316f4ccc5a06132`
- 上游声明许可证: 未声明

## 背景

MATH-500 是 OpenAI 在 _Let's Verify Step by Step_ 论文中从 [MATH](https://github.com/hendrycks/math) benchmark 选取的 500 题子集，广泛用于数学推理评测。HuggingFaceH4 团队将其以 JSONL 格式重新发布。

## 数据分布

- 总计 500 题，按科目划分为 7 类
- 难度 1–5 级（5 最难），分布较均匀
- answer 为字符串类型，包含 LaTeX 表达式（如分数、根号、坐标等），**不是整数**

| 科目 | 数量 | 难度分布 |
|---|---|---|
| Algebra | 124 | 1:8, 2:20, 3:27, 4:37, 5:32 |
| Intermediate Algebra | 97 | 1:4, 2:15, 3:18, 4:24, 5:36 |
| Prealgebra | 82 | 1:17, 2:21, 3:18, 4:12, 5:14 |
| Number Theory | 62 | 1:6, 2:10, 3:15, 4:15, 5:16 |
| Precalculus | 56 | 1:4, 2:11, 3:16, 4:14, 5:11 |
| Geometry | 41 | 1:3, 2:9, 3:7, 4:10, 5:12 |
| Counting & Probability | 38 | 1:1, 2:4, 3:4, 4:16, 5:13 |
