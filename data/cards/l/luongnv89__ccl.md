# luongnv89/ccl

⭐ 39 · Python · MIT · 推送 2026-09-08 · [GitHub](https://github.com/luongnv89/ccl) · [官网](https://luongnv.com/ccl) · 个人维护

**把 Claude Code/Codex/Pi 切换到本地模型运行的 CLI 工具**

CCL（claude-codex-local）为使用 Claude Code、Codex CLI 或 Pi 终端编码工具的开发者提供向导式切换：生成 cc/cx/ccp 别名，把 harness 接到本地推理引擎（Ollama、LM Studio、llama.cpp、vLLM）或云端路由（9router、OpenRouter），已有 skills、agents、MCP servers 配置保持不动。含 llmfit 硬件分析与量化选择、跨 harness 会话上下文桥接（cwd 限定、7 天时效、密钥脱敏）、远程引擎端点配置。限制：需 macOS/Linux、Python 3.11+，LM Studio 与 Claude Code 组合存在已知 400 错误。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 向导生成别名，将 Claude Code/Codex/Pi 指向本地模型，原配置不动
- 支持 Ollama/LM Studio/llama.cpp/vLLM/9router/OpenRouter 六种引擎适配
- llmfit 扫描硬件并挑选合适的量化模型
- 跨 harness 会话上下文桥接（cwd 限定、7 天上限、密钥脱敏、幂等去重）

## 适用场景

- 配额用尽时把 Claude Code 会话切到本地模型继续工作
- 代码不出本机的离线编码工作流
- 在 Claude Code/Codex/Pi 之间中途交接任务上下文
- 连接另一台机器上的 Ollama/llama.cpp/vLLM 服务

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L13: One alias. Claude Code, Codex, or Pi on a local model. Skills, agents, MCP servers — all intact.
> L169: Supported engine packages are `ollama`, `lmstudio`, `llamacpp`, `vllm`,
> L245: - At least one engine: Ollama (recommended), LM Studio, vLLM, llama.cpp, 9router (local cloud-routing proxy), or O

## 星数曲线

```mermaid
xychart-beta
    title "luongnv89/ccl 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 38 --> 40
    line [39, 39]
```

2026-10-18 39 → 2026-10-25 39（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `81ecf6b5297c` · [字段定义](../../DATASET.md)*
