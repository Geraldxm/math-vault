# Minerva-Math

- 上游数据: [knoveleng/Minerva-Math](https://huggingface.co/datasets/knoveleng/Minerva-Math)
- 上游 revision: `93d86e1f779d84c7393587c2cdbf6c7511591f95`
- 上游 artifact: `data/train-00000-of-00001.parquet`
- 上游数据条数: 272
- 文件: `train.jsonl`（由上游 parquet 无损逐行转存）
- 本数据条数: 272
- 字段: `problem`, `solution`, `type`, `idx`
- 领域: MIT OpenCourseWare 定量题；`type` 覆盖 9 门大学 STEM 课程
- 难度: 大学课程题；上游未提供统一难度标签
- 答案格式: 答案位于 `solution` 末端的 LaTeX `\boxed{}` 中，包含数值、分数、表达式与单位
- 推荐解析方式: 使用支持嵌套 box、LaTeX 等价和单位处理的 parser。
- SHA256: `d78d04d5f80e73cd9970f3dc18079b4f7f95d2fb233d3f4b3f606a622a981dea`
- 上游声明许可证: 未声明

## 说明

该 benchmark 收录 Google Minerva 评测使用的 MIT OpenCourseWare 定量题。上游只发布名为 `train` 的单一 split，本目录保持该命名，不据此推断训练用途。
