# Jathurshan0330/TFM-Tokenizer

⭐ 38 · Python · MIT · 推送 2026-04-22 · [GitHub](https://github.com/Jathurshan0330/TFM-Tokenizer) · 个人维护

**科研用：单通道 EEG 时频 motif 离散化 tokenization 框架**

ICLR 2026 论文 "Tokenizing Single-Channel EEG with Time-Frequency Motif Learning" 的官方代码库。TFM-Tokenizer 从单通道 EEG 信号学习时频 motif 词表并编码为离散 token，采用带时频遮蔽的双路径架构；模型无关，可与轻量 transformer 及 BIOT、LaBraM 等基础模型配合用于下游任务。仓库提供 conda/pip 环境搭建、数据集处理脚本（TUEV/TUAB、CHB-MIT、EarEEG）、预训练/微调/推理脚本、预训练权重与 token 可视化 notebook。MIT 许可，面向复现与扩展研究的科研用户。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从单通道 EEG 学习时频 motif 词表并编码为离散 token
- 双路径架构 + 时频遮蔽，模型无关、可作为即插即用组件
- 提供预处理、预训练、微调、推理脚本与预训练权重
- 附带 token 可视化 notebook

## 适用场景

- 复现论文中异常检测/癫痫检测/睡眠分期实验
- 将 EEG tokenization 作为即插即用组件接入 BIOT、LaBraM 等基础模型
- 在 ear-EEG 等非 10-20 系统设备数据上做下游任务

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L14: Foundation models are reshaping EEG analysis, yet an important problem of EEG tokenization remains a challenge. Thi
> L15: Accuracy: Experiments on four diverse EEG benchmarks demonstrate consistent performance gains across both single- a

## 星数曲线

```mermaid
xychart-beta
    title "Jathurshan0330/TFM-Tokenizer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 37 --> 39
    line [38, 38]
```

2026-10-18 38 → 2026-10-29 38（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `81e503ce6c9a` · [字段定义](../../DATASET.md)*
