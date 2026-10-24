# GET-Foundation/get_model

⭐ 114 · Jupyter Notebook · 推送 2026-04-07 · [GitHub](https://github.com/GET-Foundation/get_model) · 组织维护

**跨人类细胞类型转录调控基础模型（General Expression Transformer）**

论文配套的官方实现：基于 Transformer 的模块化框架，包含 Region Embedding、Transformer Encoder 与任务专属头（表达预测、ATAC 预测等），支持微调、继续预训练与结果解释；配置管理采用 Hydra，通过 YAML 与命令行覆盖运行实验。面向基因组学/单细胞方向的研究者，提供 pip、conda、Docker/Singularity 三种安装途径与教程数据。因果分析依赖需手动安装的 R 包 pcalg；许可为 CC BY-NC 4.0，商用需联系作者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Transformer 架构的转录调控基础模型，含表达/ATAC 等任务头
- 支持微调、继续预训练与 motif→ATAC 预测教程
- Hydra 配置管理与命令行训练脚本
- 提供 pip/conda/Docker/Singularity 多种安装方式

## 适用场景

- 在我的细胞类型数据上微调并解释转录调控模型
- 预测 ATAC 信号或基因表达
- 基于预训练数据继续预训练定制模型

## 场景标签

`微调` `科研工具` · 领域:学习与行业

## 证据(README 行号)

> L3: A foundation model of transcription across human cell types.
> L120: GET uses a transformer-based architecture with several key components:
> L121: - Region Embedding

## 星数曲线

```mermaid
xychart-beta
    title "GET-Foundation/get_model 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 113 --> 115
    line [114, 114]
```

2026-10-18 114 → 2026-10-24 114（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `ceb9c7082c65` · [字段定义](../../DATASET.md)*
