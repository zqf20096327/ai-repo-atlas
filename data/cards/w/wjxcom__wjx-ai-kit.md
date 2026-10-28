# wjxcom/wjx-ai-kit

⭐ 22 · JavaScript · MIT · 推送 2026-10-28 · [GitHub](https://github.com/wjxcom/wjx-ai-kit) · [官网](https://www.npmjs.com/package/wjx-mcp-server) · 组织维护 · 中文 README

**问卷星 OpenAPI 工具包：TypeScript SDK + CLI + MCP Server**

问卷星官方开源的全栈工具包，三部分共享业务基础层：CLI 为默认入口，供 AI Agent、自动化脚本与终端使用；MCP Server 面向 Claude Desktop/Code、Cursor 等 MCP 客户端，处于 secondary/maintenance-mode 定位，只覆盖核心业务子集；SDK 用于 Node.js/TypeScript 程序化集成。支持通过 API Key 初始化、私有化部署（--base-url）、JSONL 与 XML DSL 两条问卷创建路径、答卷报告与查询，另含 skill 安装与诊断命令。

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

- CLI/MCP/SDK 三层共享业务基础层，能力矩阵界定差异
- 支持私有化部署（--base-url）与 API Key 初始化
- JSONL 与完整 XML DSL 两条问卷创建路径
- 提供 AI 助手可执行的自动安装与验收流程

## 适用场景

- 在终端或 CI 中创建问卷并拉取答卷报告
- 让 Claude Desktop 或 Cursor 通过 MCP 操作问卷星
- 在 Node.js/TypeScript 程序中集成问卷星 API

## 场景标签

 · 领域:调查问卷/AI 工具集成

## 证据(README 行号)

> L3: 问卷星官方开源 AI 工具包：SDK 提供共享业务基础层，CLI 是完整的主入口，MCP Server 提供面向原生 MCP 客户端的核心业务子集。
> L15: CLI 是默认入口：它不要求客户端支持 MCP，适合 AI Agent、自动化脚本和人工终端操作。MCP 处于 secondary / maintenance-mode 定位，只覆盖核心业务子集；初始化、诊断、profile、补全

## 星数曲线

```mermaid
xychart-beta
    title "wjxcom/wjx-ai-kit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-28 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `832257ec29f1` · [字段定义](../../DATASET.md)*
