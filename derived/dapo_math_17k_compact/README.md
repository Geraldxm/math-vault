# DAPO-Math-17K Compact

- 父数据: [官方 DAPO-Math-17K](../../source/dapo_math_17k/README.md)
- 父数据条数: 1,791,700
- 文件: `train.jsonl`
- 本数据条数: 17,917
- 字段: `id`, `problem`, `answer`, `style`
- 领域: 数学推理题；`style` 全部为 `rule-lighteval/MATH_v2`
- 难度: 父数据未提供统一难度标签
- 答案格式: 有符号十进制整数字符串；超出有符号 64 位范围的答案仍以字符串保存
- 推荐解析方式: 从模型最后一个 `\boxed{}` 或明确的 final-answer 段提取有符号十进制整数，再按整数精确比较。
- SHA256: `018a9cc4f977b085684b8804da0eeb3e5de6d11bf6bcbfff28b2e9f2270b1265`
- 继承上游许可证: Apache-2.0

## 说明

这是官方 DAPO-Math-17K 去除 100 次存储重复和固定 prompt 后的 JSONL 版本；不改变第一个 block 内部的重复、顺序、答案或 UUID。

进一步的一题一答案版本见 [`dapo_math_17k_dedup`](../dapo_math_17k_dedup/README.md)。

## 处理方式

1. 确认官方 parquet 由同一个 17,917 行 block 连续重复 100 次。
2. 只保留第一个 block，不改变其内部重复、顺序、答案或 UUID。
3. 移除固定 DAPO prompt，仅保留题面，并从 prompt 末行 `Answer:` 提取有符号十进制答案。
4. 逐行写为 JSONL；超出有符号 64 位范围的答案仍以字符串保存。

固定 DAPO prompt:

```text
Solve the following math problem step by step. The last line of your response should be of the form Answer: $Answer (without quotes) where $Answer is the answer to the problem.

{question}

Remember to put your answer on its own line after "Answer:".
```

## 统计

| 统计项 | 数量 |
|---|---:|
| 总行数 | 17,917 |
| raw 唯一题面 | 17,398 |
| 空白归一化唯一题面 | 17,188 |
| 多答案冲突题面 | 12 |
