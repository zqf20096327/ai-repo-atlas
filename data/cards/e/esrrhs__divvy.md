# esrrhs/divvy

⭐ 62 · Go · MIT · 推送 2026-10-29 · [GitHub](https://github.com/esrrhs/divvy) · 个人维护 · 中文 README

**面向小参数廉价模型的自动化编程 Agent：任务树拆解+真实验收**

Go 编写的命令行自动化编码 Agent，面向弱模型（小参数、低算力、廉价模型）：把目标拆成带契约和验收命令的任务树，每个叶子在隔离上下文里用 9 个基础工具执行，靠编译/测试与根目标端到端验收（真实运行交付物）判定完成，而非长会话记忆。支持任意 OpenAI 兼容接口（含 Ollama/vLLM/本地网关），提供批处理、交互式 REPL、人在回路引导式工作流与 Web 界面，自动识别 Go/Node/Rust/Python 等技术栈生成验收命令，可选联网搜索、headless 浏览器与网络隔离安全约束。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 目标拆解为带契约与验收命令的任务树，叶子在隔离上下文执行
- 根目标端到端验收：真实运行交付物（启动服务、curl 接口）而非仅编译
- 多语言技术栈自动识别并生成默认验收命令（Go/Node/Rust/Python/Makefile）
- Ollama/vLLM 等任意 OpenAI 兼容接口均可接入，含成本与 token 预算控制

## 适用场景

- 用本地或廉价小模型自动完成中小型编码任务
- 先只拆解任务树人工审查，再执行（-plan/-resume，CI 可用 -strict 把关）
- 引导式工作流中评审计划、中途加需求或让 agent 提问
- 通过 Web 界面审批计划、逐叶子审查 diff 与续跑会话

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L5: *An automated coding agent for small, cheap LLMs: split big goals into contract-driven task trees, execute each leaf
> L18: 任意 **OpenAI 兼容** 接口都可以，包括 OpenAI、vLLM、Ollama、本地网关。本地 Ollama 实战配置见 docs/qwen3.8-local.md、docs/debug-local-ollama.md；

## 星数曲线

```mermaid
xychart-beta
    title "esrrhs/divvy 星数(近 2 点)"
    x-axis ["2026-10-26", "2026-10-30"]
    y-axis "stars" 61 --> 63
    line [62, 62]
```

2026-10-26 62 → 2026-10-30 62（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `867173adae43` · [字段定义](../../DATASET.md)*
