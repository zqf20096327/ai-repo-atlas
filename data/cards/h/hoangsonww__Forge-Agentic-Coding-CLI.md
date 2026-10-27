# hoangsonww/Forge-Agentic-Coding-CLI

⭐ 26 · TypeScript · MIT · 推送 2026-09-27 · [GitHub](https://github.com/hoangsonww/Forge-Agentic-Coding-CLI) · [官网](https://hoangsonww.github.io/Forge-Agentic-Coding-CLI/) · 个人维护

**本地优先的多智能体软件工程运行时（CLI/REPL/UI）**

以 npm 包或 Docker 镜像分发的 agentic 编码运行时：自带调度器、沙箱、权限系统、任务状态机、四层记忆与插件生态，内置 6 个角色 agent 与 18 个工具，任务经规划→执行→校验的闭环处理。模型由用户自选托管：自动探测 Ollama、LM Studio、vLLM、llama.cpp 本地端点，云 API（Anthropic/OpenAI 兼容）为可选。提供 9 种带预算上限的运行模式、VS Code 扩展与 Web UI 仪表盘。限制：小模型在多轮工具调用场景下易失败，README 给出各任务的模型规模下限。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自带调度器、沙箱、权限系统、任务状态机与四层记忆的运行时
- 内置 6 个角色 agent（planner/architect/executor/reviewer/debugger/memory）与 18 个沙箱化工具
- 自动探测 Ollama/LM Studio/vLLM/llama.cpp 本地端点，41 个模型家族按角色路由
- 9 种模式带可执行的预算上限（执行轮数、校验重试、变更许可）

## 适用场景

- 在本地跑多 agent 编码工作流并审批每一步操作
- 用自有本地模型替代云端托管式编码助手
- 在终端、VS Code 或 Web 仪表盘中跟踪与回放 agent 任务

## 场景标签

`多智能体` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L18: Forge is a local-first, plan-first, multi-agent, and programmable software-engineering runtime. Unlike Claude Code 
> L26: |🔌 **Model providers** (auto-detected)|**6**|ollama · lmstudio · vllm · llama.cpp · openai-compat · anthropic|
> L138: - **Local-first.** Forge auto-detects Ollama, LM Studio, vLLM, and

## 星数曲线

```mermaid
xychart-beta
    title "hoangsonww/Forge-Agentic-Coding-CLI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-27 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `66f91a7419b3` · [字段定义](../../DATASET.md)*
