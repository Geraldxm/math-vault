# OlympiadBench: OE_TO_maths_en_COMP

- 上游数据：[Hothan/OlympiadBench](https://huggingface.co/datasets/Hothan/OlympiadBench)
- 官方项目：[OpenBMB/OlympiadBench](https://github.com/OpenBMB/OlympiadBench)
- 上游 revision：`91184b52131e7fc9455fef848035173aea8cc01a`
- 上游 artifact：`OlympiadBench/OE_TO_maths_en_COMP/OE_TO_maths_en_COMP.parquet`
- 文件：`train.jsonl`（由上游 parquet 无损逐行转存）
- 条数：674
- SHA256：`8398e5c9c5fe5761ca8998f28d27519c15a6a9126c2a0cb68a27e5f963b5c923`
- 上游声明许可证：Apache-2.0

这是 OlympiadBench 的一个公开 configuration：open-ended、text-only、mathematics、English、competition。完整 benchmark 还包含中文、物理、多模态与证明题，本目录不镜像其他 configuration。

字段：`id`, `question`, `solution`, `final_answer`, `context`, `image_1`–`image_9`, `modality`, `difficulty`, `is_multiple_answer`, `unit`, `answer_type`, `error`, `question_type`, `subfield`, `subject`, `language`。

| answer type | 数量 |
|---|---:|
| Numerical | 572 |
| Expression | 63 |
| Tuple | 33 |
| Interval | 6 |

`final_answer` 是答案列表，并可能带 LaTeX 或单位。评测时应按 `answer_type` 使用数值、符号、tuple 或 interval 等价判定；多答案题比较集合而不是原始字符串。

