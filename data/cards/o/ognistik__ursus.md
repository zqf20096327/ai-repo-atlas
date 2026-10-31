# ognistik/ursus

⭐ 19 · Swift · MIT · 推送 2026-08-05 · [GitHub](https://github.com/ognistik/ursus) · 个人维护

**macOS 本地 MCP 服务器与工具集，让 AI 应用读写 Bear 笔记**

面向 Bear 笔记用户的 macOS 桌面应用：作为本地 MCP 服务器向支持 MCP 的 AI 应用（Codex、Claude 等）暴露发现、笔记、标签、备份、导航五类工具。读取直接来自 Bear 本地数据库，写入通过 Bear 的 x-callback-url 路径，不直接改动数据库；编辑前自动快照备份以弥补 Bear 无版本历史的问题。支持当前选中笔记定位、模板感知的结构化编辑、批量操作，另提供 CLI 与自动化集成（Keyboard Maestro、Raycast 等）及可选的回环 HTTP 桥接（含 OAuth）。要求 macOS 14+ 且安装 Bear。

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

- 本地 MCP 服务器，stdio 与 HTTP 桥接两种连接方式
- 读 Bear 本地数据库、写走 x-callback-url，不直接改库
- 笔记编辑前自动快照备份，支持对比与恢复
- CLI 支持创建笔记、备份、恢复、模板应用，可接入自动化工具

## 适用场景

- 让 Claude/Codex 等 MCP 客户端直接读写我的 Bear 笔记
- 让 AI 总结或校对当前正在查看的笔记
- 通过命令行批量创建、备份、模板化 Bear 笔记

## 场景标签

`知识库管理` · 领域:知识与检索

## 证据(README 行号)

> L5:  Local MCP, CLI, and utilities for Bear · Overview Video
> L66: **Local MCP clients** (Codex, Claude, etc.) use stdio. The **Setup** tab detects supported apps on your Mac and let
> L78: **Remote or browser-based clients** use the optional HTTP bridge:

## 星数曲线

```mermaid
xychart-beta
    title "ognistik/ursus 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-31 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `8bc9e84b13a1` · [字段定义](../../DATASET.md)*
