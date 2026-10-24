# mai-yyy/multi-llm-mcp

⭐ 117 · Python · MIT · 推送 2026-05-30 · [GitHub](https://github.com/mai-yyy/multi-llm-mcp) · 个人维护 · 中文 README

**让 Claude Code 调度 Codex CLI 并行调用多模型的 MCP 工具**

基于 FastMCP 开发的 MCP 服务，供 Claude Code 接入后使用两类能力：通过 ask_codex/wait_codex 把编码任务交给本机 Codex CLI 执行（支持 read-only、workspace-write、danger-full-access 三档沙盒），以及 ask_many/review 将同一问题并行发送给 GPT、Kimi、DeepSeek、Qwen、Claude 等多个模型做对比参考。长任务用 job_id + wait_* 轮询避免超时，ask 支持多轮会话。模型密钥经环境变量配置在 PROVIDERS 中；ask_codex 依赖本机已登录的 Codex CLI。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- MCP 调度 Codex CLI 执行编码任务，三级沙盒模式
- 同一问题并行发送多个模型并支持多轮会话
- job_id + wait_* 轮询机制处理长任务超时
- health_check 检查环境、Codex CLI 与 API Key 配置状态

## 适用场景

- 在 Claude Code 里把任务委派给 Codex CLI 执行
- 同一问题发给多个模型对比、补充答案
- 用多个模型同时审查同一段代码或方案

## 场景标签

`编码 Agent` `模型网关` `代码审查` · 领域:Agent 开发

## 证据(README 行号)

> L3: 一个用于 Claude Code 的 MCP 工具，支持通过 MCP 调用 Codex CLI 执行任务，并支持多个模型（GPT、Kimi、DeepSeek、Qwen 等）并行调用。
> L5: 本项目基于 FastMCP 开发，主要解决两个问题：

## 星数曲线

```mermaid
xychart-beta
    title "mai-yyy/multi-llm-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 116 --> 118
    line [117, 117]
```

2026-10-18 117 → 2026-10-24 117（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `fb2d13ae8242` · [字段定义](../../DATASET.md)*
