# DAPO-Math-17K Dedup

- 父数据: [`dapo_math_17k_compact`](../dapo_math_17k_compact/README.md)
- 父数据条数: 17,917
- 文件: `train.jsonl`, `conflicts.jsonl`, `build.py`
- 本数据条数: train 17,176；conflicts 12
- 字段: `train.jsonl`: `id`, `problem`, `answer`, `datasource`, `source`；`conflicts.jsonl`: `problem`, `ids`, `answers`, `source_rows`
- 领域: 数学推理题；继承 compact 版本的 DAPO-Math-17K 来源
- 难度: 父数据未提供统一难度标签
- 答案格式: `train.jsonl` 为有符号十进制整数字符串；冲突题的多个答案保存在 `conflicts.jsonl`
- 推荐解析方式: 从模型最后一个 `\boxed{}` 或明确的 final-answer 段提取有符号十进制整数，再按整数精确比较；不要把 `conflicts.jsonl` 用作单答案评测集。
- 继承上游许可证: Apache-2.0

## 说明

这是 compact 版本按空白归一化题面去重后的单答案评测版本。这里不做语义去重: 措辞不同但语义相同的题仍会保留。

## 处理方式

| 步骤 | 规则 | 结果 |
|---|---|---:|
| 输入 | compact JSONL | 17,917 行 |
| 题面分组 | 以 `" ".join(problem.split())` 为 key，只归一化空白 | 17,188 组 |
| 相同答案 | 同组答案完全相同时保留第一条原始题面和 UUID | — |
| 冲突答案 | 同组出现多个答案时整组移入 `conflicts.jsonl` | 删除 12 组 |
| 输出 | 唯一且无已知答案冲突的题目 | 17,176 行 |

## 文件与校验

| 文件 | 条数 | SHA256 |
|---|---:|---|
| `train.jsonl` | 17,176 | `7131540f334375c5fed33ac89b8728cdda851bde9ee95a755d74a33b201d8b25` |
| `conflicts.jsonl` | 12 | `67eb4b7cbacdedc5c6ad84e5667caa437cba9262a6babaa92571a04f05a5971d` |

## 重建

在仓库根目录运行:

```bash
python derived/dapo_math_17k_dedup/build.py
```

脚本只使用 Python 标准库，输出仅为 JSONL。
