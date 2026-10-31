# Santosh-Prasad-Verma/ClaudeGate

⭐ 32 · Python · MIT · 推送 2026-09-13 · [GitHub](https://github.com/Santosh-Prasad-Verma/ClaudeGate) · 个人维护

**本地代理网关：让 Claude Code 等 CLI 编码助手接入任意 OpenAI 兼容模型**

基于 FastAPI 的本地桥接代理，运行于 8082 端口，将 Claude Code CLI、OpenAI Codex CLI、OpenCode、Aider 等编码代理的请求实时转换为 OpenAI 格式，转发到 DeepSeek、Ollama、Gemini、Groq、OpenRouter 等 28+ 预设提供商并流式回传。提供自动故障转移、密钥脱敏、上下文溢出压缩、实时 Web 监控面板与 --doctor 诊断（探测 Ollama/LM Studio/vLLM 本地引擎）。安装方式为 git clone 源码运行 Python 脚本，可选 Docker；需 Python 3.9+。

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

- 28+ 提供商预设，一条命令切换模型
- 自动故障转移（429/503 时切换备用提供商）
- 密钥脱敏防止 AWS/GitHub/SSH 凭证外泄
- 实时 Web 面板：延迟、token、请求日志与飞行记录仪

## 适用场景

- 用 Ollama 本地模型零成本驱动 Claude Code CLI
- 编码代理在多 AI 提供商之间切换或做故障备份
- 本地监控编码代理的请求、延迟与 token 消耗

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L6:  A fast, lightweight local gateway that connects your favorite coding agents to DeepSeek, Ollama, OpenAI, Gemini, Gr
> L20: **ClaudeGate is a local bridge for your machine.** It sits quietly in the background on port `8082`. When your codi

## 星数曲线

```mermaid
xychart-beta
    title "Santosh-Prasad-Verma/ClaudeGate 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-31 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `1197a32a335f` · [字段定义](../../DATASET.md)*
