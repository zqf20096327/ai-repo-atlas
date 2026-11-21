# Dirgha-AI/dirgha

⭐ 16 · TypeScript · Apache-2.0 · 推送 2026-11-20 · [GitHub](https://github.com/Dirgha-AI/dirgha) · [官网](https://dirgha.ai) · 组织维护

**本地运行的终端 AI 编码 agent，带安全门与审计**

在终端中运行编码 agent 的开源 harness：TypeScript agent 处理对话、工具与 provider，Rust 内核提供 WebAssembly 安全门、签名的 hash-chain 审计账本、本地 cockpit 与 24 个 MCP 工具。支持交互、单次任务、headless 与 NDJSON 输出，可通过 git worktree 并行运行子 agent，另含 MuJoCo 机器人仿真评估。键、记忆与日志保留在本地机器，默认无遥测。2.0 为面向开发者与试点的早期发布，机器人与硬件工具为演示，未经独立安全审查。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 每个工具调用先经 WebAssembly 安全门检查，S2 物理动作需人工 Ed25519 签名批准
- 14 个托管 provider 家族加任意 OpenAI 兼容端点，或经 Ollama/llama.cpp 完全本地运行
- MCP 双向支持：连接 MCP 服务器，Rust 内核自身提供 24 个 MCP 工具
- 追加式本地日志与可验证的签名账本记录每次门控决策

## 适用场景

- 在本地终端用自选模型执行编码任务，保留完整操作记录
- 团队让 agent 遵循书面规则：可触碰哪些文件、哪些命令需人工批准
- 在 MuJoCo 仿真中评估 agent 行为并前置安全门
- 脚本中以 headless 模式与 NDJSON 事件输出集成 agent

## 场景标签

`编码 Agent` `模型评测` · 领域:编码与开发

## 证据(README 行号)

> L10: AI agents now open files, run commands, send messages and, increasingly, move machines. Dirgha is a harness for tho
> L36: |**Your choice of model**|14 hosted provider families plus any OpenAI-compatible endpoint, or fully local models th
> L53: The TypeScript agent handles conversation, tools and providers. The Rust kernel handles the gate, the ledger, the M


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 mid · 依据 README sha `de32fe9e8ad2` · [字段定义](../../DATASET.md)*
