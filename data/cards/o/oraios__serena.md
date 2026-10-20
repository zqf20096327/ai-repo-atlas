# oraios/serena

⭐ 30,365 · Python · NOASSERTION · 推送 2026-10-15 · [GitHub](https://github.com/oraios/serena) · [官网](https://oraios.github.io/serena) · 组织维护

**给编码 Agent 提供符号级语义代码检索与编辑工具的 MCP 服务器**

Serena 以 MCP 服务器形式向编码 Agent 提供 IDE 式工具：符号级检索、重构、符号编辑与调试，并带跨会话记忆系统和多层 YAML 配置体系。语义能力有两种后端可选：默认的开源语言服务器（LSP，支持 40+ 语言）与付费的 JetBrains 插件（含独占的调试工具）。README 强调 agent-first 工具设计避免行号级低层操作；通过 uv 安装，可接入 Claude Code、Codex 等任何支持 MCP 的客户端。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 动量与使用信号

- 维护:`active` — 距上次 push 2.5 天,年发版 14,244 位贡献者
- 涨星:近 1 天 **+39**(自 20261016 起算)
- 平台:— · 协议:MCP

## 能力要点

- 符号级检索、重构与编辑工具，经 MCP 接入任意客户端
- LSP 后端支持 40+ 编程语言，可选 JetBrains 插件后端
- JetBrains 插件独占交互式调试（断点、变量检查、REPL）
- 跨会话/跨项目记忆系统与多层可组合配置

## 适用场景

- 让 Claude Code/Codex 等客户端里的 Agent 获得符号级代码理解与跨文件重构能力
- 在大型代码库中为 AI 编码工作流提供精准检索上下文
- 长期 Agent 工作流中跨会话共享项目知识

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L6: * Serena provides essential **semantic code retrieval, editing, refactoring and debugging tools** that are akin to a
> L58: Serena can extend the functionality of your existing AI client via the **model context protocol (MCP)**.
> L95: When using Serena's language server backend, we provide **support for over 40 programming languages**, including

---
*卡片 v1 · prompt 1.4 · 生成 2026-10-18 · 置信度 high · 依据 README sha `b0cd8f4b173d` · [字段定义](../../DATASET.md)*
