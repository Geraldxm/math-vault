# DAPO-Math-17K Dedup

- 父数据：[`dapo_math_17k_compact`](../dapo_math_17k_compact/README.md)
- 文件：`train.jsonl`, `conflicts.jsonl`, `build.py`
- 条数：17,176
- 字段：`id`, `problem`, `answer`, `datasource`, `source`
- 继承上游许可证：Apache-2.0

## 处理方式

| 步骤 | 规则 | 结果 |
|---|---|---:|
| 输入 | compact JSONL | 17,917 行 |
| 题面分组 | 以 `" ".join(problem.split())` 为 key，只归一化空白 | 17,188 组 |
| 相同答案 | 同组答案完全相同时保留第一条原始题面和 UUID | — |
| 冲突答案 | 同组出现多个答案时整组移入 `conflicts.jsonl` | 删除 12 组 |
| 输出 | 唯一且无已知答案冲突的题目 | 17,176 行 |

这里不做语义去重：措辞不同但语义相同的题仍会保留。

| 文件 | 条数 | SHA256 |
|---|---:|---|
| `train.jsonl` | 17,176 | `7131540f334375c5fed33ac89b8728cdda851bde9ee95a755d74a33b201d8b25` |
| `conflicts.jsonl` | 12 | `67eb4b7cbacdedc5c6ad84e5667caa437cba9262a6babaa92571a04f05a5971d` |

在仓库根目录重建：

```bash
python derived/dapo_math_17k_dedup/build.py
```

脚本只使用 Python 标准库，输出仅为 JSONL。
