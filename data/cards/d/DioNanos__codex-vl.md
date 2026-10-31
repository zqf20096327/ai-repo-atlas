# DioNanos/codex-vl

⭐ 17 · Rust · Apache-2.0 · 推送 2026-10-29 · [GitHub](https://github.com/DioNanos/codex-vl) · [官网](https://www.npmjs.com/package/@mmmbuto/codex-vl) · 个人维护

**OpenAI Codex CLI 社区分支：增加循环任务与 Vivling 陪伴层**

Codex VL 是 OpenAI Codex CLI 的社区 fork，以 codex-vl 命令与官方 codex 并存安装，保留上游运行时模型并追加实验性工作流功能：/loop 会话级周期检查任务、/vivling 本地陪伴与编排层（生长/生命周期/可选 brain 配置）、/vl 直接对话、/remote-control 守护进程控制与 ChatGPT 移动端配对、/mcp reload 免重启加载 MCP 配置，以及基于 WebRTC 的 /voice 实时语音（macOS 与 glibc Linux，Termux 不可用）。提供 npm 安装：Linux/Android 为预编译二进制，macOS arm64 需本地 Cargo 源码构建（首次 10-30 分钟）。Vivling 行为仍为实验性。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- fork 官方 Codex CLI，以 codex-vl 命令并存安装不覆盖原命令
- /loop 周期任务与 /vivling 本地陪伴层（实验性）
- /mcp reload 免重启应用 MCP 配置变更
- 基于 WebRTC 与内置 GStreamer 运行时的 /voice 实时语音

## 适用场景

- 在 Linux/树莓派/Termux 上运行带附加工作流功能的 Codex CLI
- 用周期循环任务做状态检查与长任务监督
- 通过 ChatGPT 移动端配对远程控制 Codex 守护进程

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L9: Codex VL is a fork of OpenAI Codex that
> L12: The fork keeps the upstream Codex runtime model and adds a small set of

## 星数曲线

```mermaid
xychart-beta
    title "DioNanos/codex-vl 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-31 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `c05e5d358a59` · [字段定义](../../DATASET.md)*
