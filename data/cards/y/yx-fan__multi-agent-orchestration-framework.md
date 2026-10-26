# yx-fan/multi-agent-orchestration-framework

⭐ 28 · Python · MIT · 推送 2025-11-10 · [GitHub](https://github.com/yx-fan/multi-agent-orchestration-framework) · 个人维护

**给开发者的 YAML 声明式多智能体编排框架**

基于 LangGraph 与 FastAPI 的多智能体编排框架，面向构建领域定制 AI 系统的开发者。通过 intents.yaml 与 workflow.yaml 声明式定义意图与工作流，运行时由 LangGraphBuilder 解析 YAML 构建可执行图，AgentRouter 按意图路由，StateManager 与 Redis 后端管理会话状态与短期记忆。分执行/核心/编排三层，节点、智能体、工具、提供者均可插拔扩展；内置 /chat FastAPI 端点，默认提供 AzureOpenAI 提供者，更换其他提供者需修改代码。安装为 git clone 源码方式，需 Python 3.12+ 并自行配置 Redis 与 Azure OpenAI 环境变量。

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

- YAML 声明式定义意图与多域工作流，无需编写编排代码
- LangGraph 驱动的异步运行时与节点-智能体两级结构
- Redis 后端短期记忆与统一 MemoryInterface 抽象
- 内置 FastAPI /chat 端点，可将智能体作为微服务部署

## 适用场景

- 用 YAML 快速搭建领域专属的多智能体对话系统
- 为智能体服务提供带会话记忆的 API 后端
- 按域（如学校、金融、客服）组织并路由多个智能体工作流

## 场景标签

 · 领域:LLM 基础设施/智能体编排

## 证据(README 行号)

> L20: is a **developer-oriented orchestration framework** for building **multi-agent, multi-domain AI systems** powered b
> L29: Together, they form **intelligent conversational workflows** defined declaratively via YAML —

## 星数曲线

```mermaid
xychart-beta
    title "yx-fan/multi-agent-orchestration-framework 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-26 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `43b16c3dec55` · [字段定义](../../DATASET.md)*
