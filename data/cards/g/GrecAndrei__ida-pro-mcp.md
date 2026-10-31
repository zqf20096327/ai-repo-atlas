# GrecAndrei/ida-pro-mcp

⭐ 15 · Python · NOASSERTION · 推送 2026-10-26 · [GitHub](https://github.com/GrecAndrei/ida-pro-mcp) · [官网](https://glama.ai/mcp/servers/GrecAndrei/ida-pro-mcp) · 个人维护

**已归档的 IDA Pro MCP 服务器：让 AI agent 做确定性二进制逆向分析**

本地运行的 MCP 服务器，把 IDA Pro/Home 的二进制分析能力以 102 个（归档说明称 109 个）严格 schema 的 ida_* 操作暴露给 MCP 客户端，覆盖反编译、反汇编、交叉引用、查找、结构/类型编辑等；每个会话默认启动独立 IDA headless 进程，主机与 IDA 运行时通过 token 保护的回环桥通信。IDB 变更类操作由确定性策略门控，workspace findings 独立于 IDB 保存并记录证据与来源。项目已被官方 Hex-Rays IDA MCP 服务器取代并停止维护（停留在 1.0.0a4），README 明示不再推荐使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 102 个严格 schema 的 ida_* 操作，支持 tools/list 与 ida_help 实时发现
- 本地优先架构：token 保护回环桥，分析路径中无隐藏 LLM 服务
- findings 保存证据、置信度、生命周期与审计历史，独立于 IDB
- IDB 变更操作由确定性策略与风险确认门控

## 适用场景

- 让 Claude Code/Cursor 等 MCP 客户端读取 IDB 做逆向分析
- 以带证据记录的 findings 流程管理分析发现
- 在策略控制下由 agent 写回 IDB 注释与重命名

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L21: IDA Pro MCP is a local Model Context Protocol server for IDA Pro. It lets an
> L29: - **Deterministic agent surface:** 102 strict-schema `ida_*` operations with

## 星数曲线

```mermaid
xychart-beta
    title "GrecAndrei/ida-pro-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `5e0009473293` · [字段定义](../../DATASET.md)*
