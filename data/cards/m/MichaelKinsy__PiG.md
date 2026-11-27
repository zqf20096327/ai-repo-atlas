# MichaelKinsy/PiG

⭐ 899 · Go · MIT · 推送 2026-11-26 · [GitHub](https://github.com/MichaelKinsy/PiG) · [官网](https://pi-in-go.dev) · 个人维护

**终端编程代理 Pi 的 Go 原生单二进制移植版**

PiG 是上游 TypeScript 项目 Pi（终端编程代理）的对等移植，用 Go 构建为无需 Node.js 的原生二进制，行为以钉定的 Pi 1.6.0 为契约，用成对 parity 场景核验。支持通过兼容运行时运行 Pi 的 TypeScript 扩展，也可用 Go/Rust/Python/Common Lisp 写扩展，并将扩展、技能、提示打包为可分享或可编译执行的 Piglet。当前为 0.x 预稳定版，Windows 支持为预览，不实现 Pi 的实验性远程 Session 与独立遥测/评测包，且非官方发布、上游维护者不作背书。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 以 Pi 1.6.0 为行为契约的 parity 核验（coverage.md 与升级台账）
- TypeScript 扩展经兼容运行时运行，另支持 Go/Rust/Python/Common Lisp 扩展
- Piglet 机制：把扩展、技能与提示打包为可分享的具名代理或独立可执行文件
- RPC 模式在 Unix socket 上按连接提供多会话服务

## 适用场景

- 在没有 Node.js 的环境用单二进制运行 Pi 兼容的终端编程代理
- 用 Go/Rust/Python 等语言编写代理扩展
- 把扩展与技能组合打包成 Piglet 分享或独立部署
- 通过 RPC socket 在多个会话间复用同一代理服务

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L19: PiG is Pi, the minimal and extensible coding agent for the terminal, rebuilt in Go as one native binary. The binary
> L116: PiG's current package scope covers Pi's agent, AI, coding-agent, and TUI
> L140: |`coding/`|Public coding-agent SDK, extension contracts, Package support, and Piglet support.|

## 星数曲线

```mermaid
xychart-beta
    title "MichaelKinsy/PiG 星数(近 26 点)"
    x-axis ["2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-23", "2026-11-25", "2026-11-26", "2026-11-27"]
    y-axis "stars" 722 --> 915
    line [738, 748, 751, 763, 770, 775, 783, 787, 789, 738, 826, 837, 847, 853, 858, 865, 867, 874, 879, 883, 886, 888, 892, 893, 898, 899]
```

2026-10-25 738 → 2026-11-27 899（+161）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `45a1433efe0e` · [字段定义](../../DATASET.md)*
