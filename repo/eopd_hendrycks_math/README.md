# EOPD Hendrycks MATH training artifact

- 父数据: [`derived/hendrycks_math/train.jsonl`](../../derived/hendrycks_math/train.jsonl)
- 文件: `train.parquet`，7,500 条；Snappy Parquet，兼容 `EOPD/verl` 的 on-policy distillation dataset schema
- prompt: 单条 `user` message，内容为原始 `problem` 加现有 `repo/opd_dapo_math_17k_dedup` 同款 suffix：` Please reason step by step, and put your final answer within \boxed{{}}.`；无 system prompt、无 thinking prompt
- answer: `reward_model.ground_truth` 保存从官方 solution 提取的最终答案，仅作审计；两条上游空 `\\boxed{}` 保持为空字符串，不猜测补全。EOPD 的 on-policy distillation loss 不读取外部 reward
- schema: 与现有 `repo/opd_dapo_math_17k_dedup` 一致，包含 `data_source/prompt/ability/reward_model/extra_info`
- SHA256: `e517485f4479e442d3fae1e8dba719e691dd0d29b488a640874554e52ef4ce1b`

## 与论文的关系

论文未披露 MATH 训练时是否追加 instruction suffix。为与当前 DAPO EOPD pipeline 对齐，本 artifact 明确复用 DAPO 的 `\\boxed{}` suffix；因此它是 **论文数据 × 本地 DAPO prompt 合同**，而非声称逐字复刻未公开的原论文 prompt。

`soft_kd_entropy_threshold=.8`、top-k=16、EOPD/pure-FKL 的 loss 分支属于 EOPD runner 合同，不属于数据 artifact。

## 重建

```bash
python derived/hendrycks_math/build.py
python repo/eopd_hendrycks_math/build.py
```
