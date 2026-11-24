# speak2jerome/llmdyno

⭐ 3 · Python · MIT · 推送 2026-11-22 · [GitHub](https://github.com/speak2jerome/llmdyno) · [官网](https://zynxtech.in/projects/llmdyno/) · 个人维护

**为开发者提供本地与云端 LLM 编码代理基准测试工具**

LLMDyno 是一个以编码代理身份运行本地与云端 LLM 的基准测试工具：用户选择模型（本机 GPU 上的 GGUF/llama.cpp，或 OpenAI、Anthropic、Gemini、DeepSeek 等 API）与 agent harness（Pi、OpenCode、Codex CLI、Aider 等），在离线 Docker 沙箱中运行多文件编码任务，由隐藏测试评分、LLM 盲评审查，并在仪表盘中比较正确性、代码质量、速度、VRAM 与成本。支持 SWE-bench 与 Aider polyglot 基准，提供 Python API、CLI、npm 客户端与 Web 仪表盘四种驱动方式。依赖 Docker 与 Python 3.11+，本地模型推荐 GPU。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- VRAM 拟合检查：仅从 GGUF 头部投影显存占用，运行前给出溢出与上下文告警
- 七种 agent harness 在离线 Docker 沙箱中跑相同任务，支持自定义 harness
- 盲评 LLM 评审：可编辑评分标准、多评委一致性报告与厂商偏向检测
- Web 仪表盘、Python API、CLI 与 TypeScript 客户端共享同一引擎与数据

## 适用场景

- 在自有硬件和设置上测试本地 GGUF 模型能否胜任编码代理任务
- 对比本地模型与付费 API 在每任务上的成本与质量
- 接入 SWE-bench 与 Aider polyglot 官方基准进行回归测试

## 场景标签

`编码 Agent` `模型评测` · 领域:编码与开发

## 证据(README 行号)

> L16: **LLMDyno is an open-source benchmark for running local and cloud LLMs as coding agents.** You pick models (GGUF fi
> L19: multi-file coding tasks in offline Docker sandboxes. Hidden tests grade the result, LLM judges can review the code
> L92: **Plans**: profiles × harnesses × benchmarks × iterations. Preflight checks compatibility, memory and budget; local


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `15cf7c1c6601` · [字段定义](../../DATASET.md)*
