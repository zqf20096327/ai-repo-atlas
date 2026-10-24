# decisionintelligence/Aurora

⭐ 81 · Python · 推送 2026-04-29 · [GitHub](https://github.com/decisionintelligence/Aurora) · [官网](https://arxiv.org/pdf/2509.22295) · 组织维护

**多模态时间序列预测基础模型：生成式概率预测**

ICLR 2026 论文 Aurora 的官方代码仓库，提供预训练多模态时间序列基础模型。基于 Modality-Guided Multi-head Self-Attention 与 Prototype-Guided Flow Matching 机制，编码文本等模态注入领域知识，经 Flow Matching 生成概率预测。支持单模态与多模态零样本预测，可在自有时间序列语料上预训练；在 TimeMMD、TSFM-Bench、ProbTS、TFB、EPF 五个基准上提供复现脚本。通过 pip 发布，也可从源码运行并从 Hugging Face 下载检查点，Python 需 3.10 以上。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 预训练多模态时间序列基础模型，支持零样本概率预测
- 模态引导多头自注意力与原型引导 Flow Matching 两阶段架构
- 覆盖单模态与多模态预测两类调用接口
- 五个基准（TimeMMD/TSFM-Bench/ProbTS/TFB/EPF）复现脚本

## 适用场景

- 对时间序列做零样本概率预测，无需自训模型
- 结合文本等模态的领域知识提升预测效果
- 在自有时间序列语料上预训练定制模型
- 复现论文基准实验结果

## 场景标签

 · 领域:时间序列预测/深度学习

## 证据(README 行号)

> L9: Aurora is a highly capable multimodal time series foundation model. Based on the **Modality-Guided Multi-head Self-A
> L17: In this work, we pretrain Aurora in a cross-modality paradigm, which adopts Channel-Independence on time series dat

## 星数曲线

```mermaid
xychart-beta
    title "decisionintelligence/Aurora 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-24"]
    y-axis "stars" 79 --> 82
    line [80, 81, 81]
```

2026-10-18 80 → 2026-10-24 81（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `83b507ab71cb` · [字段定义](../../DATASET.md)*
