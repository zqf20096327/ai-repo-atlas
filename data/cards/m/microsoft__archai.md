# microsoft/archai

⭐ 487 · Python · MIT · 推送 2026-10-05 · [GitHub](https://github.com/microsoft/archai) · [官网](https://microsoft.github.io/archai) · 组织维护

**微软开源的神经架构搜索（NAS）研究库，加速高效深度网络生成**

Archai 提供模块化、可复现的神经架构搜索（NAS）框架：定义搜索空间（如基于 GPT2 的 TransformerFlexSearchSpace）、配置搜索目标（参数量、ONNX 延迟与内存等）、运行 EvolutionParetoSearch 等算法产出帕累托最优架构，支持文本生成与人脸分割两类端到端任务。面向深度学习研究与 AutoML 开发者，要求 Python 3.8+ 与 PyTorch 1.7.0+，通过 pip 安装，由微软研究院团队维护。

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

- 离散搜索 API：自定义搜索空间、目标与算法
- 基于 ONNX 的延迟与内存评测目标
- 帕累托前沿多目标架构搜索（EvolutionParetoSearch）
- 提供文本生成与人脸分割端到端任务示例

## 适用场景

- 为 NLP 任务寻找帕累托最优的 Transformer 配置
- 按延迟/内存/参数量多目标压缩与优化模型
- 复用模块化 API 开展可复现的 NAS 研究

## 场景标签

 · 领域:机器学习/AutoML

## 证据(README 行号)

> L3:  Archai accelerates your Neural Architecture Search (NAS) through fast , reproducible and modular research, enabling
> L33: In this quickstart example, we will apply Archai in Natural Language Processing to find the optimal Pareto-frontier

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/archai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 486 --> 488
    line [487, 487]
```

2026-10-18 487 → 2026-10-22 487（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `0c59e524fce9` · [字段定义](../../DATASET.md)*
