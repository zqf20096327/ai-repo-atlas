# imxcstar/sharpclaw

⭐ 25 · C · MIT · 推送 2026-03-30 · [GitHub](https://github.com/imxcstar/sharpclaw) · 个人维护 · 中文 README

**基于 .NET 10 的自主 AI agent，带跨会话长期记忆与 WASM 沙箱**

构建在 .NET 10 上的自主 AI agent 框架，用户通过 TUI、Web 界面或 QQ 机器人与 MainAgent 对话。核心机制包括三层记忆管线（工作记忆→近期记忆→主记忆）、后台 MemorySaver agent 自主决定保存/更新/删除记忆、基于 SQLite 向量库的记忆检索与 DashScope 重排；可执行文件操作、进程管理与系统命令。Python 代码在 RustPython WASM 沙箱（Wasmtime/Wasmer）中隔离执行，文件访问限制于 /workspace 且有强制超时。通过 Microsoft.Extensions.AI 抽象层接入 Anthropic、OpenAI、Gemini；需 .NET 10 SDK 从源码构建运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三层长期记忆管线（Working→Recent→Primary）加向量检索与语义去重
- Python 代码在 RustPython WASM 沙箱执行，文件系统隔离与强制超时（默认 180s）
- TUI / Web / QQ 机器人三种前端共享同一 MainAgent 逻辑
- 凭据以 AES-256-GCM 加密存储于系统凭据管理器

## 适用场景

- 通过终端、网页或 QQ 与带长期记忆的 AI 助手持续对话
- 让 agent 在隔离沙箱中安全执行生成的 Python 代码
- 作为可扩展的 agent 框架加载自定义技能执行系统操作

## 场景标签

`Agent 框架` `Agent 记忆` `AI 助手` · 领域:Agent 开发

## 证据(README 行号)

> L5: Sharpclaw is an advanced, highly capable **autonomous AI agent framework** built on **.NET 10**. Its core distinctiv
> L7: By leveraging the `Microsoft.Extensions.AI` abstraction layer, Sharpclaw seamlessly integrates with multiple LLM pro

## 星数曲线

```mermaid
xychart-beta
    title "imxcstar/sharpclaw 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-27 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `c3c7f86feb2c` · [字段定义](../../DATASET.md)*
