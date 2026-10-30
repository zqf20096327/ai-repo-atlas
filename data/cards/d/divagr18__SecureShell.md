# divagr18/SecureShell

⭐ 24 · Python · MIT · 推送 2026-01-29 · [GitHub](https://github.com/divagr18/SecureShell) · 个人维护

**LLM Agent 的 shell 命令安全拦截层**

作为代理与终端之间的插入式门禁，在每条 shell 命令执行前进行评估：GREEN/YELLOW/RED 三级风险分类、沙箱路径校验、平台兼容检查，YELLOW/RED 命令交由独立 LLM 门禁结合上下文裁决，拒绝时返回详细反馈供代理自我修正。提供 TypeScript 与 Python 双实现，内置 Paranoid/Production/Development/CI-CD 四种安全模板，支持接入 OpenAI、Anthropic、Gemini、DeepSeek、Groq、Ollama、llama.cpp 等提供商，并提供 LangChain/LangGraph/MCP 集成工具。面向需要给 LLM 代理开放 shell 权限的开发者。

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

- GREEN/YELLOW/RED 三级风险分类与零信任 LLM 门禁裁决
- 平台感知：自动拦截与 OS 不兼容的命令（如 Windows 下的 rm/ls）
- 四种安全模板（Paranoid/Production/Development/CI-CD）免配置切换
- TypeScript 与 Python 双实现，LangChain/LangGraph/MCP 插入式集成

## 适用场景

- 给 AI DevOps 代理加安全护栏后执行部署与运维命令
- 让代码助手在受控范围内执行文件与 git 操作
- 为 Claude Desktop 等 MCP 客户端提供安全的 shell 访问
- CI/CD 流水线中安全执行构建与测试命令

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L13: SecureShell acts as "sudo for LLMs" - a drop-in zero-trust gatekeeper that evaluates every shell command before exe
> L23: - **Drop-in Integration** - Plug into LangChain, LangGraph, MCP, or use standalone

## 星数曲线

```mermaid
xychart-beta
    title "divagr18/SecureShell 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-30 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `162f5de7971d` · [字段定义](../../DATASET.md)*
