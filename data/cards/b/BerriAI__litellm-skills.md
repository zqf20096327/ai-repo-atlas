# BerriAI/litellm-skills

⭐ 100 · Python · MIT · 推送 2026-05-07 · [GitHub](https://github.com/BerriAI/litellm-skills) · [官网](https://github.com/BerriAI/litellm-skills) · 组织维护

**管理 LiteLLM 代理部署的 Agent Skills 集合**

BerriAI 维护的 Agent Skills 集合，用于管理运行中的 LiteLLM proxy 部署：通过 22 个技能覆盖用户、团队、API key、组织、模型、MCP 服务器、AI agent 及用量查询的增删改操作，技能调用依赖 curl 向代理 API 发起请求。安装方式为 curl 运行 install.sh 脚本；运行需本机已装 curl、一个运行中的 LiteLLM proxy 及代理管理员 key（非 llm_api_routes 范围的 virtual key）。以 MIT 许可发布。

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

- 覆盖用户/团队/key/组织/模型/MCP/agent 七类管理操作与用量查询
- 通过 install.sh 一键安装技能
- 运行要求：curl、运行中的 LiteLLM proxy 与管理员 key

## 适用场景

- 让 AI agent 代为在 LiteLLM proxy 上创建用户、团队与 API key
- 通过 agent 添加任意 LLM 提供商的模型并测试连通性
- 查询按用户/团队/组织/模型的日消费与 token 用量

## 场景标签

 · 领域:LLM 基础设施/网关管理

## 证据(README 行号)

> L3: Agent Skills for managing live LiteLLM proxy deployments. Requires `curl`.
> L69: - A running LiteLLM proxy

## 星数曲线

```mermaid
xychart-beta
    title "BerriAI/litellm-skills 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 98 --> 101
    line [99, 100]
```

2026-10-18 99 → 2026-10-24 100（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `9ebd36bb5d41` · [字段定义](../../DATASET.md)*
