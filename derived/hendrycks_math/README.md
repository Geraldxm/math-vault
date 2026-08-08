# Hendrycks MATH normalized

- 父数据: [`source/hendrycks_math`](../../source/hendrycks_math/README.md)
- 文件: `train.jsonl`（7,500）与 `test.jsonl`（5,000）
- 处理: 保留所有原始题目与原始顺序；从每条 solution 的最后一个嵌套 `\\boxed{}` / `\\fbox{}`（兼容上游的无花括号写法）提取 answer；将 `Level N` 解析为整数，并生成稳定 ID
- 不做: 去重、难度筛选、题面改写、instruction 拼接或 test→train 混合

| 文件 | 行数 | SHA256 |
|---|---:|---|
| `train.jsonl` | 7,500 | `9079588d96e75288cbeb557cdd2212dcf8949629f346d3a1615dcf3632bc2ac5` |
| `test.jsonl` | 5,000 | `2f1dcffcee498358e67c5857332301bd0fca529409d3d41b4a1d0d18df64d1c9` |

本层为训练适配和审计提供 `id/problem/answer/answer_status/solution/subject/level/level_raw/source`；两条上游 `Level ?` 记录的 `level=null`、原值保留于 `level_raw`。上游有两条空 `\\boxed{}`，其 `answer=null`、`answer_status=missing_boxed_answer`，不由本层猜测补全。`build_eopd_json.py` 复用当前 DAPO EOPD pipeline 的 prompt suffix 与 `data_source/ability/reward_model/extra_info` 字段合同，生成 `eopd_train.json`（JSON，非 parquet）；`test.jsonl` 不得进入训练。
