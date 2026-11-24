# langchain-ai/langchain-plugins

⭐ 10 · MIT · 推送 2026-09-21 · [GitHub](https://github.com/langchain-ai/langchain-plugins) · [官网](https://docs.langchain.com/oss/python/deepagents/code/plugins) · 组织维护

**编码 agent 的 LangChain 生态插件市场：装技能与 MCP 服务器**

LangChain 官方维护的插件市场，面向 dcode、Claude Code、OpenAI Codex 三种编码 agent CLI。收录 4 个插件：LangChain/LangGraph/Deep Agents 构建技能、LangSmith 追踪与评测技能、LangChain 文档与 API 参考 MCP 服务器、LangSmith MCP 服务器（OAuth 登录，支持区域主机）。通过 marketplace add 一次性接入后按需安装插件，技能按请求自动激活，插件随上游 LangChain 版本自动刷新。需要已支持的 agent CLI；LangSmith 插件还需 LangSmith 账号。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 4 个插件：langchain-skills、langsmith-skills、langchain-mcp、langsmith-mcp
- 提供 LangChain 实时文档与 API 参考 MCP 服务器
- LangSmith MCP 通过 OAuth 登录，支持 EU/APAC/AWS 区域主机
- 技能随上游 LangChain 发布自动刷新

## 适用场景

- 在编码 agent 里查找并加载 LangChain/LangGraph 开发技能
- 让 agent 查询最新 LangChain 文档与 API 签名
- 在 agent 中读取 LangSmith 的追踪、数据集与实验数据
- 为 LangChain 应用搭建 LangSmith 评测流程

## 场景标签

 · 领域:开发工具/agent 插件生态

## 证据(README 行号)

> L3: The official marketplace of **LangChain ecosystem plugins** for your coding agent.
> L8: Works with **[dcode]**, **Claude Code**, and **OpenAI Codex**.
> L96: - A supported agent CLI: [dcode], Claude Code, or OpenAI Codex.

## 星数曲线

```mermaid
xychart-beta
    title "langchain-ai/langchain-plugins 星数(近 2 点)"
    x-axis ["2026-11-23", "2026-11-24"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-11-23 10 → 2026-11-24 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-23 · 置信度 high · 依据 README sha `efcfc9150e6d` · [字段定义](../../DATASET.md)*
