# The-Swarm-Corporation/swarms-tools

⭐ 39 · Python · MIT · 推送 2026-02-09 · [GitHub](https://github.com/The-Swarm-Corporation/swarms-tools) · [官网](https://docs.swarms.world) · 组织维护

**面向 agent 与多智能体系统的预构建工具库**

由 The Swarm Corporation 维护的 Python 工具函数库，为 agent、MCP 服务器与多智能体系统提供预构建工具：涵盖金融数据（HTX、Yahoo Finance、CoinGecko、DeFi TVL、Dex Screener）、网页抓取、Telegram/Twitter 消息、GitHub 仓库管理、代码执行等。基于 httpx 与 orjson 构建，提供工具链器（tool_chainer）支持顺序/并行执行，并定义了含类型提示与环境变量密钥管理的工具开发 schema。以 pip 包分发，面向使用 Swarms 编排平台的开发者。

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

- 金融/加密/DeFi/社交/GitHub 等领域的预构建工具函数
- tool_chainer 支持多工具顺序或并行编排执行
- 标准化工具开发 schema（类型提示、环境变量密钥管理）
- 基于 httpx/orjson 构建

## 适用场景

- 为多智能体系统快速接入金融与加密市场数据
- agent 中集成网页抓取、社交消息发送等能力
- 按统一 schema 编写并接入自定义工具

## 场景标签

`网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L7: **Swarms Tools** provides a vast array of pre-built tools for your agents, MCP servers, and multi-agent systems. It 
> L15: |**Multi-Agent System Compatibility**|Optimized for seamless integration into Swarms' distributed agent orchestrati

## 星数曲线

```mermaid
xychart-beta
    title "The-Swarm-Corporation/swarms-tools 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 38 --> 40
    line [39, 39]
```

2026-10-18 39 → 2026-10-30 39（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `fad46f0b4983` · [字段定义](../../DATASET.md)*
