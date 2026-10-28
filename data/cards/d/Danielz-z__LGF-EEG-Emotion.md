# Danielz-z/LGF-EEG-Emotion

⭐ 27 · Python · MIT · 推送 2026-10-10 · [GitHub](https://github.com/Danielz-z/LGF-EEG-Emotion) · 组织维护 · 中文 README

**跨被试 EEG 情绪识别的局部-全局特征融合 PyTorch 实现**

面向科研用户的 EEG 情绪识别研究代码：以 Transformer 架构融合通道级局部特征、图连接性全局特征与多重分形辅助特征，在 LOSO（留一被试）协议下训练与评估跨被试泛化性能。提供特征提取、训练、评估的完整 PyTorch 流水线及基线模型对比脚本。仓库不含原始 EEG 数据、特征、标签或预训练模型，用户需自行获取（如 SEED-VII 等数据集）并预处理。配套论文已被 IEEE EMBC 接收为口头报告，预印本在 arXiv。

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

- Transformer 融合通道级 EEG、图连接性与多重分形三类特征
- 严格遵循 LOSO 被试无关评估协议
- 含基线模型训练与混淆矩阵/指标聚合评估脚本
- 仓库不含数据与预训练模型，需自行获取预处理

## 适用场景

- 在 SEED-VII 等多被试 EEG 数据集上复现跨被试情绪识别实验
- 对比局部-全局融合方法与基线模型的 LOSO 性能
- 研究 EEG 跨被试泛化与特征融合方法

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L5: **LGF-EEG-Emotion** is a PyTorch implementation of a **local–global feature fusion framework**
> L35: - **Local–global feature fusion**: combines channel-wise EEG, graph-based connectivity, and multifractal features.

## 星数曲线

```mermaid
xychart-beta
    title "Danielz-z/LGF-EEG-Emotion 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-28 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `20472ecf7b37` · [字段定义](../../DATASET.md)*
