# fikrilal/burnly

⭐ 29 · Rust · 推送 2026-10-12 · [GitHub](https://github.com/fikrilal/burnly) · [官网](https://burnly.dev/) · 个人维护

**本地托盘应用：追踪 AI 编程工具的 token 用量与成本**

面向使用多种 AI 编程工具（Claude Code、Codex、OpenCode 等）的开发者的本地托盘应用：从各工具的本地使用数据（SQLite、JSONL 等）读取 token 消耗，存储于本机 SQLite，提供托盘日常汇总、来源与模型分解及成本估算（来自 provider 上报、ccusage 计算或内嵌 models.dev 定价快照）。支持 4 个稳定来源与 9 个实验性来源，Cursor/Windsurf 等在路线图上。以 Tauri 构建，提供 Linux AppImage、Windows x64 与 macOS（Apple Silicon/Intel）安装包；macOS 与 Windows 预览版未签名。不读取提示词、回复或源码。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 托盘式日常 token 用量汇总与本地 SQLite 历史
- 13 种 AI 编程工具来源（4 个 Supported、9 个 Experimental）
- 三级成本估算：provider 上报 / ccusage 计算 / 内嵌 models.dev 定价快照
- 本地优先：无需账号，不收集提示词、回复、源码或文件内容

## 适用场景

- 我想随时在托盘看到今天 Claude Code/Codex 等工具烧了多少 token
- 按来源和模型分解多个 AI 编程工具的用量
- 估算没有上报成本的来源（如 Grok、Antigravity）的花费

## 场景标签

 · 领域:开发者工具/AI 用量监控

## 证据(README 行号)

> L3: Burnly is a local tray app for tracking AI coding-tool token usage.
> L13: - Estimated cost: provider-reported where available, ccusage-calculated for
> L23: Burnly reads local usage from supported AI coding tools. Support levels are

## 星数曲线

```mermaid
xychart-beta
    title "fikrilal/burnly 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-30 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `c8031c759c86` · [字段定义](../../DATASET.md)*
