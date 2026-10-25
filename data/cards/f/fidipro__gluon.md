# fidipro/gluon

⭐ 54 · TypeScript · Apache-2.0 · 推送 2026-10-24 · [GitHub](https://github.com/fidipro/gluon) · [官网](https://fidipro.github.io/gluon) · 组织维护

**编码代理控制平台：统一运行、选型与会话成本管理**

面向使用编码代理的开发者的控制平台：在一个终端帧内并行运行 Claude Code、Codex、Antigravity、Grok Build、OpenCode 与 Kimi Code，使用自己的 API key 或订阅。通过 intake agent 读取仓库并生成 spec，按可配置规则为每次会话路由 harness × model × effort 组合；提供会话管理、成本与上下文可观测性及分析。支持 Linux/macOS/Windows，安装脚本下载最新 release，Apache-2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单终端帧内并行运行 6 种编码代理（Claude Code、Codex 等）
- intake agent 读取仓库并提出 agent/模型/effort 的 spec 与路由
- 会话成本与上下文可观测性和分析
- 跨平台：Linux、macOS、Windows

## 适用场景

- 在同一终端里管理多个编码代理的会话
- 为每个会话挑选成本效益合适的 harness 与模型组合
- 跟踪编码代理的成本与上下文消耗

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L1: **Gluon** is a control platform for coding agents. It lets you:
> L5: 3. **Run Claude Code, Codex, Antigravity, Grok Build, OpenCode and Kimi Code** side by side in one terminal frame, o
> L46: Describe what the session is for. The intake agent reads your repo, asks a few questions and proposes an agent, mod

## 星数曲线

```mermaid
xychart-beta
    title "fidipro/gluon 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 53 --> 55
    line [54, 54]
```

2026-10-18 54 → 2026-10-25 54（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `37f4cb929fb3` · [字段定义](../../DATASET.md)*
