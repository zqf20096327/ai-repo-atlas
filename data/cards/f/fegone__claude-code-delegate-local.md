# fegone/claude-code-delegate-local

⭐ 18 · Python · MIT · 推送 2026-10-26 · [GitHub](https://github.com/fegone/claude-code-delegate-local) · 个人维护

**将 Claude Code 子代理委派给本地/第三方模型后端的 MCP 服务器**

面向保留 Anthropic 主会话（Max 套餐或 API）做编排、同时把部分子代理卸载到其他后端的用户：通过一个 MCP 服务器暴露多个工具，把 .md 定义的子代理任务路由到本地模型（LM Studio、llama.cpp、Ollama、vLLM、LiteLLM）、DeepSeek、MiniMax M3、GLM Coding Plan、AWS Bedrock 或任意 OpenAI/Anthropic 兼容端点。支持双格式端点自动转换、完整工具调用（read_file/write_file/run_bash）、按模型前缀分桶的并发池与跨模型故障转移链（本地模型固定不外转）；另可将任务委派给 Codex CLI 并提供批派发、轮询与取消。安装需 uv 与 Claude Code，git clone 后 uv sync。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按模型前缀自动路由 Anthropic/OpenAI 双格式端点
- 每模型 6 并发槽位（flock 文件实现）与等价模型故障转移链
- 本地模型与 Codex 固定不参与云端故障转移
- 委派子代理具备 read_file/write_file/run_bash 工具调用与批量并行派发（最多 4 任务）

## 适用场景

- 把安全或敏感数据子代理放到本地模型，数据不出本机
- 将大任务子代理路由到其他云端后端以节省 Max 套餐额度
- 通过 ChatGPT 订阅免 API key 委派 Codex CLI 自主完成任务

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L9: **MCP server that delegates Claude Code subagents to alternative backends** — local models (LM Studio, llama.cpp, Ol
> L23: That's what `delegate-local` does. It's an MCP server you install once that exposes tools the orchestrator can invo
> L57: See docs/CONFIGURATION.md for full details and example setups with LiteLLM, llama.cpp, Ollama, DeepSeek direct, and

## 星数曲线

```mermaid
xychart-beta
    title "fegone/claude-code-delegate-local 星数(近 5 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22", "2026-10-27", "2026-10-29"]
    y-axis "stars" 14 --> 19
    line [15, 16, 17, 18, 18]
```

2026-10-18 15 → 2026-10-29 18（+3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `55a3b6c75b75` · [字段定义](../../DATASET.md)*
