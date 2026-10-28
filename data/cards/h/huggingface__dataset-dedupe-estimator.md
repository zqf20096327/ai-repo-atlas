# huggingface/dataset-dedupe-estimator

⭐ 27 · Jupyter Notebook · Apache-2.0 · 推送 2026-10-27 · [GitHub](https://github.com/huggingface/dataset-dedupe-estimator) · 组织维护

**估算 parquet 文件集内容定义分块去重收益的 CLI 工具**

由 Hugging Face 维护的 Rust/PyArrow 命令行工具（de），用于评估 Apache Parquet 上内容定义分块（CDC）的去重效果：对多个 parquet 文件统一分块并估算在内容寻址存储下可节省的空间。依赖未合入上游的 content-defined-chunking 分支实现（gearhash 分块器改变页面切分方式），通过 maturin 编译安装。提供 dedup、synthetic（生成合成数据并可视化）、revisions（检出 git 仓库中文件全部修订版）与 stats（目录级统计并绘图）四个命令，实验表格含 Vanilla Parquet/CDC Parquet/JSONLines/SQLite 对比框架。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 对多个 parquet 文件统一分块，估算内容寻址存储下的去重节省
- 基于未合入上游的 Arrow C++/PyArrow content-defined-chunking 分支（gearhash 分块器）
- 可检出 git 仓库中某文件的全部修订版用于多版本去重对比
- 生成合成数据（插入/删除/更新/追加变体）并可复现实验

## 适用场景

- 评估 parquet 数据集多版本存储在 CDC 下的去重潜力
- 对数据集目录生成去重统计与对比图表
- 复现不同行数与编辑数下的合成数据去重实验

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L3: This estimates the amount of chunk level dedupe available in a
> L9: This tool is primarily designed to evaluate the deduplication
> L32: This implementation introduces a gearhash-based chunker for each leaf column

## 星数曲线

```mermaid
xychart-beta
    title "huggingface/dataset-dedupe-estimator 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-28 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 low · 依据 README sha `7312b3384809` · [字段定义](../../DATASET.md)*
