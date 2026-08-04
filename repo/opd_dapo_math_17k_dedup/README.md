# OPD DAPO-Math-17K Dedup

- 作用域: OPD/Verl 仓库级训练 setting，不是通用 canonical 数据
- 父数据: [`derived/dapo_math_17k_dedup`](../../derived/dapo_math_17k_dedup/README.md)
- 父数据 SHA256: `7131540f334375c5fed33ac89b8728cdda851bde9ee95a755d74a33b201d8b25`
- 文件: `train.parquet`
- Artifact SHA256: `8dffce2de713177fab35d44efe39dec20908ad18b0efd529b70051e32a5993b0`
- 条数: 17,176
- 格式: Snappy Parquet，兼容 Verl RL dataset schema
- 继承上游许可证: Apache-2.0

## 冻结的训练合同

| 字段 | 值或来源 |
|---|---|
| `data_source` | `math_dapo` |
| `prompt` | 单条 `user` message，内容为 dedup `problem` 加固定后缀 |
| prompt 后缀 | ` Please reason step by step, and put your final answer within \boxed{{}}.` |
| `ability` | `MATH` |
| `reward_model.ground_truth` | dedup `answer`，字符串 |
| `reward_model.style` | `rule-lighteval/MATH_v2` |
| `extra_info.index` | dedup `id` |

该合同复用 `/Repos/OPD/dapo-math-17k-processed.parquet` 的字段、类型和 prompt setting，但题面以本仓库 dedup JSONL 为唯一事实源。相比 17,917 行 processed 数据，本版本删除 717 条干净重复记录和 12 个答案冲突组的 24 行。

## 相对父数据的适配变更

- **题面和答案**：继承 `derived/dapo_math_17k_dedup/train.jsonl` 的 17,176 条记录；不重新改写题面、答案或 `id`。
- **user prompt**：将原始 `problem` 后追加固定后缀
  ` Please reason step by step, and put your final answer within \boxed{{}}.`，作为唯一的 `user` message。
- **system prompt**：不添加 system message；`prompt` 列中只有一个 `role: user` 元素，没有 `role: system`。
- **字段适配**：将 JSONL 的 `id` / `answer` 映射为 `extra_info.index` / `reward_model.ground_truth`，并补充 Verl 所需的 `data_source=math_dapo`、`ability=MATH` 和 `reward_model.style=rule-lighteval/MATH_v2`。
- **格式转换**：仅从 JSONL 转为 Snappy Parquet 及 Verl 嵌套 schema；不复制原始 solutions，也不把 `conflicts.jsonl` 纳入训练集。

## 处理方式

`build.py` 校验父数据 hash 和空白归一化后的题面唯一性，然后构造上述嵌套字段并写为 Snappy Parquet。需要 Python 和 PyArrow；在 math-vault 根目录运行:

```bash
python repo/opd_dapo_math_17k_dedup/build.py
```

当前 artifact 使用 PyArrow 25.0.0 构建。输出必须为 17,176 行，且 schema 与本页冻结合同一致。
