# redpanda-data/agent

⭐ 67 · Python · Apache-2.0 · 推送 2026-03-11 · [GitHub](https://github.com/redpanda-data/agent) · [官网](https://ai.redpanda.com) · 组织维护

**Redpanda 维护的企业级 agent 开发框架**

Redpanda Data 维护的 agent 开发体验项目，README 仅给出定位口号与路线图：已完成与 Redpanda MCP server、Redpanda broker/ACL/认证的集成、Starlark 声明式配置（Python 语法替代 YAML）、gRPC Python agent 插件、OTel 指标（Redpanda Connect 管道与 Python 进程）、项目初始化模板引擎与进程内多 agent；待办包括审计日志发送到 Redpanda/Kafka broker 与持久化 promise 执行。面向构建企业 agent 的开发者，公开文档见 GitHub Pages。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 与 Redpanda MCP server 及 broker/ACL/认证集成
- Starlark 声明式配置替代 YAML
- gRPC 插件支持 Python agent
- OTel 指标覆盖 Redpanda Connect 管道与 Python 进程

## 适用场景

- 基于 Redpanda 生态构建多 agent 系统
- 用 Python 语法编写 agent 的声明式配置
- 为 agent 管道接入 OTel 可观测性

## 场景标签

`Agent 框架` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L3: unreasonably good developer experience for enterprise agents
> L19: - ✅ integration with redpanda broker/acls/auth{z,n}/etc for multi agents

## 星数曲线

```mermaid
xychart-beta
    title "redpanda-data/agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 66 --> 68
    line [67, 67]
```

2026-10-18 67 → 2026-10-28 67（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 low · 依据 README sha `2c1f29e25d2b` · [字段定义](../../DATASET.md)*
