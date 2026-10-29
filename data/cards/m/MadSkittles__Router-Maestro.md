# MadSkittles/Router-Maestro

⭐ 18 · Python · MIT · 推送 2026-10-27 · [GitHub](https://github.com/MadSkittles/Router-Maestro) · 个人维护

**本地/自托管 LLM 网关：让各类客户端用 Copilot 等多家模型**

Python 编写的本地或自托管模型网关与代理，将客户端协议（Anthropic Messages、OpenAI Chat/Responses、Gemini generateContent）与上游模型传输解耦：GitHub Copilot（OAuth 设备流）、OpenAI、Anthropic、DeepSeek 及自定义 OpenAI 兼容提供商均可作为后端，供 Claude Code、Codex、Gemini CLI、DeepSeek Harness 及 API 客户端调用。提供协议匹配直通与跨协议翻译、Auto 虚拟模型路由（任务分类/优先级链）、CLI 向导与本地 Web 配置门户、Prometheus 指标；支持本地、Docker、HTTPS 部署。限制：Copilot 模型需有效订阅，跨协议不支持的字段会显式报错；Python 3.14 要求。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单一 Copilot 订阅向多协议客户端暴露完整模型目录（GPT/Claude/Gemini/Grok/MAI）
- Auto 虚拟模型按任务分类（fast/general/coding/deep_reasoning）路由并做上下文窗口安全过滤
- 四类接入协议（Anthropic Messages、Chat、Responses、Gemini）经统一分发器，按需协议翻译与流式转发
- CLI 向导与 loopback Web 门户配置客户端；Prometheus 指标、审计追踪支持自托管运维

## 适用场景

- 用一份 GitHub Copilot 订阅在 Claude Code、Codex、Gemini CLI 中调用各家模型
- 自建 LLM 网关做多提供商路由与自动回退，不经第三方托管门户
- 按任务类型（编码/深度推理）自动选择模型并控制上下文预算

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L10: Router-Maestro is a local or self-hosted model gateway. It separates the client
> L23: - **Protocol-independent routing.** Anthropic Messages, OpenAI Chat
> L59: |Provider|Authentication|Upstream transports|

## 星数曲线

```mermaid
xychart-beta
    title "MadSkittles/Router-Maestro 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `36020e7611ec` · [字段定义](../../DATASET.md)*
