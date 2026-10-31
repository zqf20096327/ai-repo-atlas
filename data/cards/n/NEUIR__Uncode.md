# NEUIR/Uncode

⭐ 46 · Python · MIT · 推送 2026-10-24 · [GitHub](https://github.com/NEUIR/Uncode) · [官网](https://passionate11.github.io/Uncode-project-page/) · 组织维护 · 中文 README

**掩码扩散语言模型的免训练解码校准方法（ACL 2026 论文代码）**

UNCODE（曾名 PC-Sampler）是针对 LLaDA、Dream 等掩码扩散语言模型（MDM）的免训练解码校准框架：通过位置感知加权（指数衰减控制解码顺序）与基于参考语料频率的置信度校准，修正不确定性采样器的刚性边界偏置与平凡 token 偏置，无需微调或改架构。在 3 个 MDM 骨干与 7 个推理/规划基准上评测，提供评估脚本、基线解码方法对比脚本与解码轨迹热图生成工具。东北大学团队，论文被 ACL 2026 主会接收。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 位置感知指数加权控制解码生成顺序，消除 U 形轨迹
- 基于参考语料频率分布的置信度校准抑制平凡 token 过早生成
- 免训练、仅解码侧改动，即插即用
- 集成 ReMDM、Fast-dLLM、Semi-AR 等多种基线采样策略的统一评估脚本

## 适用场景

- 对 LLaDA/Dream 等扩散 LLM 做解码策略评测与对比
- 提升扩散语言模型在数学推理、代码生成任务上的准确率
- 可视化分析不同解码方法的 token 生成轨迹

## 场景标签

`代码生成` `模型评测` · 领域:编码与开发

## 证据(README 行号)

> L38: **UNCODE** (**UN**masking **C**alibration for Dec**O**ding **DE**biasing) is a *training-free* decoding-calibration
> L57: - **2026-04-07**: Our paper has been **accepted to ACL 2026 (Main Conference)**! 🎉

## 星数曲线

```mermaid
xychart-beta
    title "NEUIR/Uncode 星数(近 3 点)"
    x-axis ["2026-10-19", "2026-10-23", "2026-10-31"]
    y-axis "stars" 44 --> 47
    line [45, 46, 46]
```

2026-10-19 45 → 2026-10-31 46（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `4e9df550c0f6` · [字段定义](../../DATASET.md)*
