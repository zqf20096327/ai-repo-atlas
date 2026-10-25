# yasserfarouk/negmas

⭐ 101 · Jupyter Notebook · NOASSERTION · 推送 2026-10-22 · [GitHub](https://github.com/yasserfarouk/negmas) · 个人维护

**构建自主谈判智能体的 Python 库，支持多边谈判与仿真**

用于开发嵌入仿真环境的自主谈判 agent 的 Python 库：提供双边/多边谈判、多种协议（SAO 交替出价、单文本、拍卖及自定义协议）、线性/非线性/概率型效用函数、内置多种谈判策略智能体，并支持并发谈判与 World 世界仿真（如供应链 SCML）。可通过 Genius 桥接运行 Java 版 Genius 智能体（可选依赖），提供 negotiate CLI、内置绘图与 BOA 组件式构建方式。以 pip 安装的库形式交付。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 双边与多边谈判，支持 SAO/单文本/拍卖及自定义协议
- 并发谈判与多智能体世界仿真（situated 模块）
- BOA 组件式智能体构建与 MetaNegotiator 集成方法
- 通过 Genius 桥接运行 Java 版 Genius 智能体

## 适用场景

- 研究和实验自动谈判策略与协议
- 构建含多场相互关联谈判的多智能体仿真
- 复用 Genius 生态中的智能体组件做策略对比

## 场景标签

`多智能体` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L46: NegMAS is a Python library for developing autonomous negotiation agents embedded in simulation
> L224: - **Multiple Protocols**: SAO (Alternating Offers), Single-Text, Auctions, and custom protocols

## 星数曲线

```mermaid
xychart-beta
    title "yasserfarouk/negmas 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 100 --> 102
    line [101, 101]
```

2026-10-18 101 → 2026-10-25 101（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `07a6a0a507d2` · [字段定义](../../DATASET.md)*
