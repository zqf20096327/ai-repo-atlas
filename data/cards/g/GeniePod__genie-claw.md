# GeniePod/genie-claw

⭐ 47 · Rust · AGPL-3.0 · 推送 2026-07-30 · [GitHub](https://github.com/GeniePod/genie-claw) · [官网](https://genieclaw.org) · 组织维护

**面向 Jetson 家庭设备的本地 AI agent 运行层**

Rust 编写的私有家庭 agent 层，面向 NVIDIA Jetson Orin Nano 8GB，以 4096-token 上下文为基线。仓库负责 prompt 组装、SQLite 会话与家庭记忆、工具路由、Home Assistant 适配（含确认、限流、审计）、安全策略与本地 HTTP API/CLI。LLM 后端可选 genie-ai-runtime 或 llama.cpp，通过确定性设备状态接地而非模型规模提升工具调用准确率，用 BFCL 评分度量。当前版本 v1.0.0-rc.1，releases/latest 尚无稳定构建，需固定版本号安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 4096-token Jetson 基线的 agent harness 契约与 BFCL 工具调用评分
- Home Assistant 适配含确认、限流与审计日志
- LLM 后端可选 genie-ai-runtime 或 llama.cpp
- 一行脚本安装预编译二进制（Linux aarch64/x86_64），含 KV 前缀缓存优化路径

## 适用场景

- 在 Jetson Orin Nano 上运行不联网的家庭语音/对话 agent
- 通过 Home Assistant 安全控制家中设备并留审计记录
- 在低显存预算下评测本地小模型的工具调用准确率

## 场景标签

`Agent 框架` `模型评测` · 领域:Agent 开发

## 证据(README 行号)

> L10: GenieClaw is the Rust agent layer native to NVIDIA Jetson Orin 8GB. It is built
> L12: This repo owns prompt assembly, memory, tool routing, smart-home intent, safety
> L59: - LLM backend facade for `genie-ai-runtime` and selectable `llama.cpp`

## 星数曲线

```mermaid
xychart-beta
    title "GeniePod/genie-claw 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 46 --> 48
    line [47, 47]
```

2026-10-18 47 → 2026-10-31 47（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `136d0403caf9` · [字段定义](../../DATASET.md)*
