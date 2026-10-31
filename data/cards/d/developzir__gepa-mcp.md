# developzir/gepa-mcp

⭐ 52 · Python · MIT · 推送 2025-11-10 · [GitHub](https://github.com/developzir/gepa-mcp) · 个人维护

**为 Claude Desktop 提供 GEPA 自动提示词优化的 MCP 服务器**

实现 GEPA（Genetic-Evolutionary Prompt Architecture）算法核心的 MCP 服务器，供 Claude Desktop 或其他 MCP 客户端调用，通过三个工具（optimize_prompt、quick_prompt_improve、conversational_optimize）对提示词做遗传进化式优化与快速改进。需要 Python 3.10+ 与 Gemini API key，优化引擎基于 Google Gemini。通过 git clone 加 install.sh 一键安装并合并 Claude Desktop 配置。README 开头自述实现可能不稳定，需借助模型辅助修复；本仓库为第三方实现，官方算法在 gepa-ai/gepa。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 三个 MCP 工具：完整 GEPA 优化、单轮快速改进、对话上下文感知优化
- 遗传进化式流程：种群生成、适应度评估、选择、交叉变异、收敛
- install.sh 自动装依赖并合并 Claude Desktop 配置，交互式输入 Gemini API key
- 基于 arXiv 2507.19457 论文的算法第三方实现

## 适用场景

- 在 Claude Desktop 中优化复杂提示词（带训练数据）
- 无训练数据时快速改进提示词
- 聊天过程中根据上下文调优提示词

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L25: A Model Context Protocol (MCP) server implementing the core GEPA (Genetic-Evolutionary Prompt Architecture) algorit
> L18: > **Genetic-Evolutionary Prompt Architecture** for Claude Desktop (or any MCP client)

## 星数曲线

```mermaid
xychart-beta
    title "developzir/gepa-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 51 --> 53
    line [52, 52]
```

2026-10-18 52 → 2026-10-31 52（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `f4eea2715bbc` · [字段定义](../../DATASET.md)*
