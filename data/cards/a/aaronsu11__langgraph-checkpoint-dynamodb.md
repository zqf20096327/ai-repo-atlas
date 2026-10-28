# aaronsu11/langgraph-checkpoint-dynamodb

⭐ 25 · Python · MIT · 推送 2025-11-01 · [GitHub](https://github.com/aaronsu11/langgraph-checkpoint-dynamodb) · [官网](https://deepwiki.com/aaronsu11/langgraph-checkpoint-dynamodb) · 个人维护

**LangGraph 的 DynamoDB 检查点存储实现**

实现 LangGraph checkpointer 接口的 Python 库，用单张 DynamoDB 表持久化图状态，支持 human-in-the-loop、记忆、时间回溯与容错等持久化特性。提供同步与异步方法，通过 DynamoDB KeyConditionExpression 查询；支持自定义表与客户端配置（计费模式、分区键等）。基础设施搭建提供三种途径：Saver 内建方法、CloudFormation 模板、AWS CDK（可选 infra 依赖）。默认配置需环境已配置 AWS 凭证；测试使用本地/模拟 AWS 服务。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单表 DynamoDB 实现 LangGraph checkpointer 接口
- 支持 human-in-the-loop、记忆、时间回溯、容错
- 同步与异步方法，KeyConditionExpression 查询
- 三种建表途径：Saver 方法 / CloudFormation / AWS CDK

## 适用场景

- 让 LangGraph 应用用 DynamoDB 持久化图状态
- AWS 环境下启用 LangGraph 的记忆与时间回溯
- 通过 CDK 管理检查点表的基础设施

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L3: A single table DynamoDB implementation of the LangGraph checkpointer interface for persisting graph state and enabli
> L127: The DynamoDB checkpointer enables all LangGraph persistence features:

## 星数曲线

```mermaid
xychart-beta
    title "aaronsu11/langgraph-checkpoint-dynamodb 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-28 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `515496414cc2` · [字段定义](../../DATASET.md)*
