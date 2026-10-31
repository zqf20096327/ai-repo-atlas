# hackafterdark/context-sherpa

⭐ 27 · Go · MIT · 推送 2026-03-26 · [GitHub](https://github.com/hackafterdark/context-sherpa) · 个人维护

**面向 AI 编程 agent 的代码上下文工程平台（MCP server）**

以 Go+Wails 构建的单可执行程序，提供 GUI 与 headless MCP server 两种模式。通过 SCIP 索引与 ast-grep 结构分析向 AI 编程 agent 提供符号定义、引用与影响分析等信号，替代纯文本搜索，并称可降低 token 消耗。三层推理架构：确定性结构分析、本地模型（Ollama/LM Studio）蒸馏分流、前沿模型负责高层规划。集成 Cursor/Cline/Roo Code，含 Code Atlas 可视化、规则管理与 20+ MCP 工具。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- SCIP 索引 + ast-grep 结构分析提供符号级定义/引用/影响信号
- 三层推理：本地模型做蒸馏分流，前沿模型做高层规划
- 单一可执行文件，GUI 与 headless MCP 双模式
- Code Atlas 代码库关系可视化与 agent 规则管理

## 适用场景

- 为 Cursor/Cline/Roo Code 等 agent 接入精确的代码上下文
- 降低 agent 处理大型代码库时的 token 消耗
- 可视化检查代码库符号关系与依赖

## 场景标签

 · 领域:开发者工具/上下文工程

## 证据(README 行号)

> L29: - **Integrated Local Reasoning**: Connect to local providers (Ollama, LM Studio) to enable **Tiered Inference**. Th
> L30: - **Universal MCP Server**: A high-performance "headless" mode that integrates directly with tools like Cursor, Cli
> L98: ```json

## 星数曲线

```mermaid
xychart-beta
    title "hackafterdark/context-sherpa 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-31 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `69a16954c2c2` · [字段定义](../../DATASET.md)*
