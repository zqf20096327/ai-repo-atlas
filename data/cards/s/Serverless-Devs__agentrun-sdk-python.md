# Serverless-Devs/agentrun-sdk-python

⭐ 33 · Python · Apache-2.0 · 推送 2026-10-20 · [GitHub](https://github.com/Serverless-Devs/agentrun-sdk-python) · [官网](https://docs.agent.run) · 组织维护 · 中文 README

**阿里云 AgentRun 服务的 Python SDK：构建、部署与管理 AI Agent**

面向阿里云 AgentRun 服务的 Python 客户端库，提供同步/异步 API 管理 AI Agent 运行时环境：沙箱执行、Browser Sandbox、MCP ToolSet，以及为 LangChain、AgentScope、CrewAI、Google ADK、PydanticAI 等框架提供集成层，可快速创建框架可识别的模型与工具。部署流程依赖 Serverless Devs 工具（s build/s deploy），本地构建依赖 docker，通过 s.yaml 配置 CPU/内存规格与日志投递，认证支持 Access Key、STS Token。要求 Python 3.10+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 同步与异步双接口，完整类型注解
- LangChain/AgentScope/CrewAI/Google ADK/PydanticAI 多框架集成层
- 沙箱执行、Browser Sandbox 与 MCP ToolSet
- 基于 Serverless Devs 的模板创建与云端部署流程

## 适用场景

- 用熟悉的 Agent 框架开发并部署到阿里云 AgentRun
- 通过 OpenAI 兼容接口线上调用部署好的 Agent
- 为 Agent 提供 sandbox 与 MCP 工具执行环境

## 场景标签

 · 领域:AI Agent 基础设施/云服务

## 证据(README 行号)

> L9: AgentRun Python SDK 是阿里云 AgentRun 服务的 Python 客户端库，提供简洁易用的 API 来管理 AI Agent 运行时环境。
> L83: 使用 `from agentrun.integration.langchain import model, sandbox_toolset` 导入 langchain 的集成能力，这里默认提供了 `model`、`sandbox_

## 星数曲线

```mermaid
xychart-beta
    title "Serverless-Devs/agentrun-sdk-python 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-27 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `133e69091a6b` · [字段定义](../../DATASET.md)*
