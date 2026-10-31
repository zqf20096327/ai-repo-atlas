# Fewinfos/LayerLens

⭐ 17 · Python · MIT · 推送 2026-01-31 · [GitHub](https://github.com/Fewinfos/LayerLens) · [官网](https://pypi.org/project/layerlens/) · 个人维护

**深度学习模型逐层可解释性库：生成代理模型解释各层行为**

Python 可解释性库（Python 3.7+，MIT）：为深度学习模型的每一层生成代理模型以解释该层行为，可将各层解释拼接为层级化的整体理解，提供交互式 dashboard 探索模型行为，并支持对已部署模型做漂移检测与故障定位。框架无关，可搭配 PyTorch、TensorFlow 等。安装以源码克隆为主，pip 安装标注为“发布后可用”，需额外安装至少一个 ML 框架。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 逐层生成代理模型解释各层行为
- 各层解释可拼接为层级化整体洞察
- 交互式 dashboard 与生产环境漂移检测/故障定位
- 框架无关：支持 PyTorch、TensorFlow 等主要框架

## 适用场景

- 分析深度学习模型各层如何影响决策
- 部署后监控模型漂移并定位故障层
- 通过 dashboard 交互探索模型行为

## 场景标签

`模型评测` `MLOps` · 领域:评测与运维

## 证据(README 行号)

> L11: - **Layer-wise Explanation**: Generate surrogate models for each layer to explain its behavior
> L14: - **Production Monitoring**: Detect drift and localize failures in deployed models

## 星数曲线

```mermaid
xychart-beta
    title "Fewinfos/LayerLens 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-31 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `a4312ce666b4` · [字段定义](../../DATASET.md)*
