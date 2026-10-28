# Eljot19/runic

⭐ 58 · HTML · 推送 2026-10-28 · [GitHub](https://github.com/Eljot19/runic) · 个人维护

**macOS 菜单栏应用：本地追踪多家 AI 服务的用量、成本与配额**

面向同时使用多个 AI 订阅的开发者的本地优先 macOS 菜单栏工具：从 Claude、Codex、opencode 等本地 CLI 日志、浏览器会话与 provider API 读取用量、成本估算、配额信号、重置窗口与 token 历史，逐字段标注来源（reported/estimated/declared）。历史存于本地 JSONL，首跑自动回填，可显式重建。凭据存 macOS Keychain，无遥测。凭 Python 3 运行时打包于应用内，GitHub Releases 或 Homebrew Cask 安装；要求 macOS 14+。附带 runic CLI 与只读 MCP 工具。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多 provider 独立追踪：Claude、Codex、opencode 及 API 配置的 provider
- 每个字段带来源标注，不暴露的字段保持缺失而非填 0
- 本地 JSONL 历史：首跑回填、显式重建、数据不离开 Mac
- 热重载 config.json、CSV/JSON 导出、runic CLI 与只读 MCP 工具

## 适用场景

- 在一个菜单栏里看多个 AI 订阅的用量与剩余配额
- 自建滚动预算窗口监控成本
- 导出带来源标签的用量快照供脚本分析

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L5: Runic is a macOS menu bar app that shows AI usage, cost estimates, quota signals, reset windows, and token history a
> L23: - Tracks each enabled provider independently: Claude, Codex, opencode, and API-linked providers you configure.

## 星数曲线

```mermaid
xychart-beta
    title "Eljot19/runic 星数(近 2 点)"
    x-axis ["2026-10-26", "2026-10-28"]
    y-axis "stars" 57 --> 59
    line [58, 58]
```

2026-10-26 58 → 2026-10-28 58（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `fcbb87afbe0a` · [字段定义](../../DATASET.md)*
