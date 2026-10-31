# siropkin/budi

⭐ 26 · Rust · MIT · 推送 2026-05-26 · [GitHub](https://github.com/siropkin/budi) · [官网](https://getbudi.dev) · 个人维护

**本地优先的 AI 编码 agent 成本分析工具：追踪 token 与花费去向**

Rust 编写的 CLI 与守护进程，通过实时 tailing 各 AI 编码 agent 已写入磁盘的转录文件（Claude Code、Codex CLI、Cursor、Copilot CLI、Copilot Chat 等），逐条归因 API 调用的成本与 token，按仓库/分支/工单/文件拆分，并检测上下文膨胀、缓存退化等会话健康指标。约 13 MB 二进制、零配置，数据默认全部留在本机；可选云同步仅上传聚合数值，提示词与代码不出本机。提供 Homebrew、shell 脚本、PowerShell 与源码编译安装，配套状态栏扩展与 JetBrains 插件生态。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 逐消息级成本与 token 归因，按仓库/分支/工单拆分
- 本地优先：守护进程读取磁盘转录文件，提示词与代码不外传
- Claude Code / Cursor / VS Code 内实时状态栏显示滚动花费
- 会话健康检测：上下文膨胀、缓存退化、成本加速

## 适用场景

- 查看各项目、分支、工单上的 AI 编码花费分布
- 在编辑器状态栏实时查看当日/近 7 天/30 天花费
- 团队通过云端仪表盘查看聚合成本指标（可选）
- 诊断 AI agent 会话的上下文膨胀与缓存退化问题

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L9: **Local-first cost analytics for AI coding agents.** See where your tokens and money go across Claude Code, Cursor, 
> L35: - **Tracks every AI coding agent** — Claude Code, Cursor, Codex CLI, Copilot CLI, and Copilot Chat (VS Code) in one
> L172: Budi is local-first. All data lives in `~/.local/share/budi/` (Unix) or `%LOCALAPPDATA%\budi` (Windows). The daemo

## 星数曲线

```mermaid
xychart-beta
    title "siropkin/budi 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-31 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `30a68bbda98d` · [字段定义](../../DATASET.md)*
