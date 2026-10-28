# MohitGoyal09/AgentForge

⭐ 62 · Python · MIT · 推送 2026-10-21 · [GitHub](https://github.com/MohitGoyal09/AgentForge) · [官网](https://pypi.org/project/agentforge-harness/) · 个人维护

**面向学习者的终端 AI 编码 agent 框架，研究 agent 循环与安全机制**

Python 编写的终端 AI coding-agent harness，定位为学习现代编码 agent 结构的实验场。围绕 agent 循环、schema 优先的工具注册表、MCP 工具接入、子代理委托、上下文压缩、持久化快照与事件日志等核心机制组织代码。安全层面提供密钥脱敏（默认开启）、输出清洗、提示注入边界标记与六种审批模式。支持 OpenRouter、OpenAI、Anthropic 及自定义 OpenAI 兼容模型提供商。通过 PyPI 安装，带 Rich 终端 UI；文档明言脱敏层非沙箱，注入防护非完整策略引擎。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Hybrid ReAct/function-calling agent 循环，含流式输出与类型化工具调用
- 默认开启的集中式密钥脱敏与提示注入边界标记（untrusted_content 包裹）
- 六种审批模式（on-request/on-failure/auto/auto-edit/never/yolo）
- 快照、事件日志、检查点、JSON/HTML/markdown 会话导出与 resume/restore

## 适用场景

- 学习编码 agent 的 harness 工程结构（循环、工具、上下文、安全）
- 在终端中运行带审批门与脱敏的 AI 编码助手
- 通过 MCP 接入外部工具服务器进行实验
- 用子代理做有边界的只读任务委托

## 场景标签

`Agent 框架` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L10: AgentForge is a terminal-based AI coding-agent harness built in Python for learning how modern coding agents are st
> L34: The project currently supports OpenRouter, OpenAI, Anthropic, and custom OpenAI-compatible model providers, plus st
> L38: This repository is intended as a learning lab for AI harness engineering.

## 星数曲线

```mermaid
xychart-beta
    title "MohitGoyal09/AgentForge 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 61 --> 63
    line [62, 62]
```

2026-10-18 62 → 2026-10-28 62（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `e9e40410a85c` · [字段定义](../../DATASET.md)*
