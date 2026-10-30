# orhun/ratcode

⭐ 25 · Rust · MIT · 推送 2026-09-04 · [GitHub](https://github.com/orhun/ratcode) · [官网](https://www.youtube.com/live/hhw741JrQeQ&t=1611) · 个人维护

**极简终端编码 agent：400 行 Rust 实现 Codex 风格编码助手**

用 Rig 与 Ratatui 构建的终端编码 agent，约 400 行 Rust 代码。演示 Rig 的 agent builder 与 OpenAI provider、带类型的工具实现（读文件、写文件、shell 命令）、自动多轮工具循环，并支持流式文本输出、工具事件展示、对话历史与 token 用量统计。面向希望参考最小实现学习 agent 构建方式的 Rust 开发者。MIT 许可证，README 未给出安装命令，附带 YouTube 代码讲解视频。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 约 400 行 Rust 的极简实现
- 基于 Rig 的 agent builder 与 OpenAI provider
- 读/写/shell 三类带类型工具与自动多轮工具循环
- 流式输出、工具事件、对话历史与 token 用量展示

## 适用场景

- 学习如何用 Rig 构建编码 agent
- 作为终端 coding agent 的最小参考实现
- 了解多轮工具循环与流式输出的实现方式

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L3: A deliberately small Codex-style terminal coding agent built with Rig and
> L11: - typed Tool implementations for reading, writing, and shell commands

## 星数曲线

```mermaid
xychart-beta
    title "orhun/ratcode 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-30 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `fe80a4946406` · [字段定义](../../DATASET.md)*
