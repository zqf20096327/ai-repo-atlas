# strands-labs/benchmark-harnesses

⭐ 65 · Python · Apache-2.0 · 推送 2026-09-21 · [GitHub](https://github.com/strands-labs/benchmark-harnesses) · [官网](https://strandsagents.com) · 组织维护

**基于 Strands 的 agentic 基准测试 agent 与 harness 集合**

strands-labs 维护的 uv workspace 仓库，收录面向 agentic 基准的 agent 与 harness。核心成员 Simple Strands Agent（SSA）将前沿 LLM 与 bash/文件编辑工具配对，在隔离 Docker 环境中分析代码、修复 bug、生成补丁，内置 SWE-Bench Verified/Pro 与 Terminal Bench 2 运行脚本；另一成员为 ARC-AGI-3 agent，基于 Strands SDK 与 Amazon Bedrock，通过 append-only 日志与自写脚本从交互游戏中学习。要求 Python 3.12+ 与 Docker，含 shell 访问安全提示。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- SSA 支持 Anthropic/OpenAI/Google/xAI/Bedrock 及 OpenAI 兼容端点的模型适配器
- Docker 沙箱隔离环境与 Hydra 配置（命令行可覆盖全部参数）
- 内置 SWE-Bench Verified/Pro、Terminal Bench 2 基准脚本
- ARC-AGI-3 agent 通过日志与自写脚本进行长程环境学习

## 适用场景

- 在 SWE-Bench 等软件工程基准上评测不同 LLM 的 agent 表现
- 快速更换模型/提示词/工具做 agent 实验
- 复现或改造 SSA 与 ARC-AGI-3 agent 的基准运行结果

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L9: A repository for Strands-based agents and harnesses for agentic benchmarks. It is a
> L29: Simple Strands Agent (SSA) is a minimal, hackable harness for autonomous software engineering. It pairs frontier LL
> L39: - **Built-in benchmarking** — turnkey scripts for SWE-Bench Verified, SWE-Bench Pro, and Terminal Bench 2, includin

## 星数曲线

```mermaid
xychart-beta
    title "strands-labs/benchmark-harnesses 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 64 --> 66
    line [65, 65]
```

2026-10-18 65 → 2026-10-25 65（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `c0e9340fb3b7` · [字段定义](../../DATASET.md)*
