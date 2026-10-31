# tabularis-ai/be_great

⭐ 372 · Python · MIT · 推送 2026-08-16 · [GitHub](https://github.com/tabularis-ai/be_great) · 组织维护

**用预训练 LLM 生成合成表格数据的 Python 框架**

GReaT（be-great）是基于预训练 Transformer 语言模型的表格数据合成框架：对真实数据微调 LLM 后采样生成新表格行，支持缺失值填补、条件约束采样（age >= 30 等逻辑条件在 token 生成时强制生效）、基于声明式 schema 的无训练 mock 数据生成、LoRA 参数高效微调及训练中质量监控。内置统计、保真/效用与隐私三类指标（含 k 匿名、成员推断攻击模拟等）。需 Python >= 3.9，pip 安装，有论文支撑（ICLR 2023）。

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

- 微调 LLM 采样生成合成表格数据，支持缺失值填补
- 条件约束采样在 token 生成时强制生效（支持 >=/<=/==/!= 等操作符）
- 声明式 schema 的 mock 数据生成，无需训练数据
- 内置统计、保真/效用、隐私三类评估指标
- 支持 LoRA 高效微调与训练中质量实时监控

## 适用场景

- 为机器学习开发或测试生成隐私安全的合成表格数据
- 填补数据集中任意组合的缺失值
- 在指定条件约束下生成满足业务规则的样本
- 评估合成数据的统计保真度与隐私风险

## 场景标签

 · 领域:合成数据生成/表格机器学习

## 证据(README 行号)

> L19: Our GReaT framework leverages the power of advanced pretrained Transformer language models to produce high-quality 
> L34: In the example below, we show how the GReaT approach is used to generate synthetic tabular data for the California 

## 星数曲线

```mermaid
xychart-beta
    title "tabularis-ai/be_great 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-31"]
    y-axis "stars" 370 --> 373
    line [371, 372, 372]
```

2026-10-18 371 → 2026-10-31 372（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `e6fd27b81be0` · [字段定义](../../DATASET.md)*
