# Deep-CodeAI/Agents.KT

⭐ 16 · Kotlin · MIT · 推送 2026-10-06 · [GitHub](https://github.com/Deep-CodeAI/Agents.KT) · [官网](https://deep-code.ai) · 组织维护

**面向 JVM 的强类型 Kotlin AI agent 框架：编译期边界与审计**

Typed Kotlin DSL 的 JVM agent 运行时：每个 agent 为 Agent<IN, OUT> 类型契约，类型不匹配在编译期报错，非法组合在构造时快速失败。提供六种组合原语（管道/并行/分支/师生/论坛/分诊交接）、技能级工具白名单授权、权限清单与 JSONL 审计导出、MCP 客户端/服务端、OTel/LangSmith/Langfuse 适配器。支持 Ollama 本地与 Anthropic/OpenAI/DeepSeek/Kimi/OpenRouter/Perplexity/Gemini 八种模型提供方。明确声明不做 OS 沙箱、不做合规产品、不限制 MCP 入口速率。面向需要明确 AI 系统边界的开发团队，以 Gradle 依赖或源码构建安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Agent<IN, OUT> 类型契约与六种组合原语，编译期强制边界
- 技能级工具白名单：运行时拒绝白名单外调用
- 权限清单、manifestHash 关联与 JSONL 审计导出、防篡改 ToolAuditLedger
- MCP 客户端/服务端支持与八种模型提供方统一 ModelClient 接口

## 适用场景

- 在 JVM 上构建有编译期类型保证的多 agent 工作流
- 为受监管部署生成权限清单与审计证据
- 本地 Ollama 优先运行 agent 并按需切换云端模型

## 场景标签

`Agent 框架` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L17: Agents.KT is built for teams that need to know exactly what an AI system is allowed to do. Every agent is `Agent<IN
> L137: - **Eight model providers** — `model { ollama(...) }` for local/cloud Ollama, `model { claude("claude-opus-4-7"); 

## 星数曲线

```mermaid
xychart-beta
    title "Deep-CodeAI/Agents.KT 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `dd88b3f17e1e` · [字段定义](../../DATASET.md)*
