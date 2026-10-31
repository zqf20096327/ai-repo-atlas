# imran-siddique/agentic-architecture

⭐ 16 · Python · MIT · 推送 2026-09-25 · [GitHub](https://github.com/imran-siddique/agentic-architecture) · [官网](https://imransiddique.com) · 个人维护

**可约束、可观测、可验证的 agent 系统设计模式指南**

一个文档化仓库，编目四种 agent 系统架构模式：路由先于推理、接地上下文、静默执行、强制与证据。每个模式按问题、机制、不变式、测试、不适用场景、参考实现的模板展开，并附带依赖无关的 Python 示例与 36 个可执行单元测试（标准库实现、不调用模型）。示例为参考实现而非生产组件，数字为示意模拟非基准结果。另含 Cognitive Systems Architect 角色说明、设计检查清单与开发者/架构师两类快速开始路径。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四个模式各声明一个可失败的不变式并附测试（36 个检查）
- 示例仅用 Python 标准库，不调用任何模型
- 区分不变式/度量/设计目标三类陈述并要求可复现 PR 证据
- 提供开发者与架构师两套快速开始与设计检查清单

## 适用场景

- 设计多 agent 系统时参考约束与验证机制
- 评估现有 agent 系统的推理占比与幻觉风险
- 为策略执行与证据留痕建立可测试的不变式

## 场景标签

`精选清单` · 领域:学习与行业

## 证据(README 行号)

> L9: A guide to agentic system design patterns, with dependency-free examples and executable checks. The patterns emphasi
> L15: This repository documents architectural patterns for building agent systems that are easier to constrain, observe, 

## 星数曲线

```mermaid
xychart-beta
    title "imran-siddique/agentic-architecture 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `5519c43f60ff` · [字段定义](../../DATASET.md)*
