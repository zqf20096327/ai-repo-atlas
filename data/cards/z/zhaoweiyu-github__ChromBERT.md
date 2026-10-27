# zhaoweiyu-github/ChromBERT

⭐ 22 · Python · 推送 2026-03-24 · [GitHub](https://github.com/zhaoweiyu-github/ChromBERT) · [官网](https://chrombert.readthedocs.io/) · 组织维护

**面向转录调控网络解读的基因组预训练基础模型**

ChromBERT 是一个在约一千个转录调控因子的全基因组共关联数据（Cistrome 人类/小鼠数据集，1-kb 分辨率）上预训练的深度学习基础模型，用于学习情境特异性转录调控网络（TRN）的可解释表示，可通过迁移学习微调到不同生物学下游任务。配套 ChromBERT-tools 提供 CLI 与 Python API；推荐用 Singularity 镜像直接使用或从源码安装，需 Python 3.8+、PyTorch 2.0+ 与 FlashAttention-2，预训练权重从 Hugging Face 下载。论文发表于 Cell Genomics。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 捕获约一千个转录调控因子的全基因组共关联模式
- 支持迁移学习微调到不同生物学情境的下游任务
- 提供 Human-6K 与 Mouse-5K 预训练模型及多分辨率 checkpoint
- 提供 Singularity 预构建镜像与 chrombert_prepare_env 环境准备命令

## 适用场景

- 微调基础模型做情境特异性转录调控网络分析
- 研究生成式预测、位点特异性与细胞动态的 TRN 任务
- 在标准化容器环境中复现基因组调控建模流程

## 场景标签

`微调` `模型训练` · 领域:训练与推理

## 证据(README 行号)

> L8: **ChromBERT** is a pre-trained deep learning model designed to capture the genome-wide co-association patterns of ap
> L101: ChromBERT has been initially trained on the human Cistrome-Human-6K dataset at 1-kb resolution. Currently availabl

## 星数曲线

```mermaid
xychart-beta
    title "zhaoweiyu-github/ChromBERT 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-27 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `f06e8c29238c` · [字段定义](../../DATASET.md)*
