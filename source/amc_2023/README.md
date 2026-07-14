# AMC 2023

- 上游数据：[math-ai/amc23](https://huggingface.co/datasets/math-ai/amc23)
- 上游 revision：`80815d37005feb82cd7f8fbc6901d5d3eff43057`
- 上游 artifact：`test-00000-of-00001.parquet`
- 文件：`test.jsonl`（由上游 parquet 无损逐行转存）
- 条数：40
- 字段：`id`, `answer`, `url`, `question`
- SHA256：`02ae54425741562778916b5fa8f6ff07749689cfcd7a53e65e1d88a89e5065f9`
- 上游声明许可证：未声明

该数据包含 2023 AMC 12A 的 22 道题和 12B 的 18 道题。原始 AMC 是五选一选择题；该上游为了使用数值 verifier，对题面和答案做了整数输出改写，因此它不是未经修改的官方试卷文本。

`answer` 在上游为 float，但 40 个值均为整数，范围为 `-1`–`3159`。评测时可从模型最后一个 `\boxed{}` 或明确的 final-answer 段提取有符号十进制整数，再做整数精确比较。
