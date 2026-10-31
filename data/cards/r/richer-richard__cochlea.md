# richer-richard/cochlea

⭐ 15 · Rust · Apache-2.0 · 推送 2026-09-19 · [GitHub](https://github.com/richer-richard/cochlea) · 个人维护

**面向 AI agent 的无头音频引擎：数据作曲、确定性渲染与数值听审**

Rust 编写的无音频设备音频引擎，供 agent 以“作曲→渲染→探测→验证”闭环处理音频：将乐谱（RON 或 Rust builder）离线渲染为字节可复现的 PCM，再用 JSON 报告输出响度、起音、音高、调性、节奏等特征，并用谱图（单次视觉调用）与内嵌断言验证结果。附带 stdio MCP 服务器（cochlea-mcp），暴露 12 个工具，支持目录沙箱与时间窗缩放；另提供 diff、digest、MIDI 导入等 CLI 命令。面向构建音频处理 agent 的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 确定性渲染：同一乐谱重渲染字节一致，整数 tick 时间、计数器 RNG
- probe 输出紧凑 JSON（响度/起音/音高/调性/节奏），digest 输出文本摘要
- cochlea-mcp 提供 12 个 MCP 工具，谱图以 base64 PNG 内联返回
- 支持 FLAC/mp3/ogg 读取与 MIDI 导入导出，无需 ffmpeg

## 适用场景

- 让 agent 用数据写乐谱并自动验证渲染结果
- 在 CI 中用 diff --tier2 拦截音频回归
- 通过 MCP 客户端对任意 WAV 做特征分析与谱图审阅

## 场景标签

 · 领域:音频/agent 工具

## 证据(README 行号)

> L8: **A headless audio engine for agents.** Write a score as data, render it
> L171: `cochlea-mcp` is a stdio MCP server built on the same libraries the CLI
> L182: claude mcp add cochlea -- cochlea-mcp

## 星数曲线

```mermaid
xychart-beta
    title "richer-richard/cochlea 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `1bb5b2543880` · [字段定义](../../DATASET.md)*
