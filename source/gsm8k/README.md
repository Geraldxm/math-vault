# GSM8K

- 上游数据: [openai/gsm8k](https://huggingface.co/datasets/openai/gsm8k)，`main` config
- 上游 revision: `740312add88f781978c0658806c59bc2815b9866`
- 上游 artifact: `main/train-00000-of-00001.parquet`, `main/test-00000-of-00001.parquet`
- 上游数据条数: train 7,473；test 1,319
- 文件: `train.jsonl`, `test.jsonl`（由上游 parquet 无损逐行转存）
- 本数据条数: train 7,473；test 1,319
- 字段: `question`, `answer`
- 领域: 小学数学文字题
- 难度: Grade-school math
- 答案格式: `answer` 同时含人工书写的推导和末行 `#### <integer>` gold；本快照所有 gold 为整数
- 推荐解析方式: 要求模型把最终数值置于 `\boxed{}`，或从其末个明确 final-answer 位置取有符号十进制整数；以整数精确比较。评测时不要把题内推导中的中间数误当答案。
- 论文发布: 2021-10（Cobbe et al.）
- 上游声明许可证: MIT

## 文件与校验

| 文件 | 上游 split | 行数 | SHA256 |
|---|---|---:|---|
| `train.jsonl` | `main/train` | 7,473 | `0d52e684c6aba18d811188810b1264099e890882cdb460ba50e94367a3f8fd87` |
| `test.jsonl` | `main/test` | 1,319 | `5f9c0d85d3174547c8960de1fd96c3e777d9a40298771eecd4b0eef9b2f6acd6` |

## 说明

这里保留上游 `main` config 的原始 train/test split，不包含 `socratic` config。
