# MichaelKinsy/PiG

⭐ 903 · Go · MIT · 推送 2026-11-27 · [GitHub](https://github.com/MichaelKinsy/PiG) · [官网](https://pi-in-go.dev) · 个人维护

**给终端开发者的 Go 原生单二进制编码 Agent（上游 Pi 的移植）**

PiG 将 TypeScript 编写的终端编码 Agent Pi（1.6.1）按行为对等契约移植为 Go 单二进制，运行不需要 Node.js。提供 Agent 循环、TUI、providers/模型目录与认证、扩展 SDK（Go/Rust/Python/Common Lisp/TypeScript），支持将扩展、技能与提示打包成 Piglet 组合为可执行 Agent。当前为 0.x 预稳定版，用成对 parity 场景对照上游验证，Windows 支持为预览，0.8.0 起新增 Unix socket 的多会话 RPC 服务（无认证）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 上游行为为契约的等价移植，用 parity 场景与升级台账对照 Pi 1.6.1
- Go 原生单二进制，无需 Node.js；扩展可写 Go/Rust/Python/Common Lisp
- Piglet 机制可将扩展、技能、提示组合成独立可执行 Agent
- pig --mode rpc 通过 Unix socket 提供多会话 RPC 服务

## 适用场景

- 在终端用编码 Agent 辅助项目开发，无需 Node.js 环境
- 编写多语言扩展定制 Agent 行为并打包分享
- 通过 RPC socket 驱动多个并行 Agent 会话

## 场景标签

`编码 Agent` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L19: PiG is Pi, the minimal and extensible coding agent for the terminal, rebuilt in Go as one native binary. The binary
> L116: PiG's current package scope covers Pi's agent, AI, coding-agent, and TUI
> L140: |`coding/`|Public coding-agent SDK, extension contracts, Package support, and Piglet support.|

## 星数曲线

```mermaid
xychart-beta
    title "MichaelKinsy/PiG 星数(近 26 点)"
    x-axis ["2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-23", "2026-11-25", "2026-11-26", "2026-11-27", "2026-11-28"]
    y-axis "stars" 722 --> 919
    line [748, 751, 763, 770, 775, 783, 787, 789, 738, 826, 837, 847, 853, 858, 865, 867, 874, 879, 883, 886, 888, 892, 893, 898, 899, 903]
```

2026-10-26 748 → 2026-11-28 903（+155）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `9fb84c007fe3` · [字段定义](../../DATASET.md)*
