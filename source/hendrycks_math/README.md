# Hendrycks MATH

- 上游数据: [EleutherAI/hendrycks_math](https://huggingface.co/datasets/EleutherAI/hendrycks_math)，MATH 官方 GitHub 仓库的公开镜像
- 上游 revision: `21a5633873b6a120296cce3e2df9d5550074f4a3`
- 上游 artifact: 七个 subject 各自的 `train-00000-of-00001.parquet` 与 `test-00000-of-00001.parquet`
- 上游声明许可证: MIT
- 文件: `train.jsonl`、`test.jsonl`；由上述 parquet 无损逐行转存，并按 subject 固定顺序合并
- 本数据条数: train 7,500；test 5,000
- 字段: 保留上游 `problem`、`solution`、`level`、`type` 等字段，不添加 prompt 或答案解析字段

| 文件 | 上游 split | 行数 | SHA256 |
|---|---:|---:|---|
| `train.jsonl` | 7 个 subject 的 train | 7,500 | `505a29f3461da54981f8f4d26b89ef4077aaf14dc8d1611b29d96ab1a28a13d1` |
| `test.jsonl` | 7 个 subject 的 test | 5,000 | `36fe05b2aa3f100458f123e59dedf6efe772b930119e353b208b24788fd45174` |

## 重建

```bash
tmp_dir="$(mktemp -d)"
hf download EleutherAI/hendrycks_math --type dataset \
  --revision 21a5633873b6a120296cce3e2df9d5550074f4a3 \
  --local-dir "$tmp_dir" --quiet
python source/hendrycks_math/build.py "$tmp_dir"
rm -rf "$tmp_dir"
```

训练实验必须单独把本数据适配为目标训练框架的 schema，并在实验步骤中冻结 prompt、chat template 与答案格式；本目录不携带这些 setting。
