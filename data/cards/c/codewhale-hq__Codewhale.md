# codewhale-hq/Codewhale

⭐ 41,102 · Rust · MIT · 推送 2026-10-18 · [GitHub](https://github.com/codewhale-hq/Codewhale) · [官网](https://codewhale.net/) · 组织维护 · 中文 README

**开源 Rust 编码 agent 引擎与终端客户端，任意模型可选**

Codewhale 提供本地运行的 Rust agent 引擎与终端客户端：读取项目、编辑文件、执行命令并自查工作，模型由用户自选（40+ 内置 provider 路由，含本地运行时）。核心机制包括 Plan/Work/Operate 三种模式、Ask/Auto-Review/Full Access 三种审批姿态、/undo 与 /restore 工作区恢复、/receipts 会话操作清单，以及 OS 沙箱（macOS Seatbelt、Linux bubblewrap）。安装覆盖 curl 脚本、winget、npm、cargo、Docker、Nix 等多条路线。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 动量与使用信号

- 维护:`active` — 距上次 push 0.7 天,年发版 100,209 位贡献者
- 涨星:近 1 天 **+1**(自 20261016 起算)
- 安装:npm 包 `codewhale` 月下载 23,668
- 平台:WINDOWS / MACOS / LINUX / ANDROID · 协议:OPENAI-API / MCP / OLLAMA

## 能力要点

- 40+ 内置 provider 路由，支持 OpenAI 兼容端点与 Ollama/vLLM/SGLang 本地模型
- Plan/Work/Operate 模式与审批姿态、/receipts 全量操作回执
- 子 agent 委派与受监督 agent 团队（含 pre-spend check）
- MCP 服务器、skills、plugins、hooks 扩展，并加载 Claude Code 插件

## 适用场景

- 在终端里用自选模型执行修测试、改代码等编码任务
- 脚本或 CI 中以 headless 方式运行编码 agent
- 本地模型场景下做审批可控的代码修改与 PR 评审

## 场景标签

`编码 Agent` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L3: **The open-source coding agent that works with any model.**
> L95: - **Any model, no lock-in.** Over 40 built-in provider routes — Anthropic,
> L77: Every client drives the same local Codewhale Engine, so

---
*卡片 v1 · prompt 1.4 · 生成 2026-10-18 · 置信度 high · 依据 README sha `890b8b777266` · [字段定义](../../DATASET.md)*
