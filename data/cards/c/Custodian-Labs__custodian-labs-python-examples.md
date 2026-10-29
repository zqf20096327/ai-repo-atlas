# Custodian-Labs/custodian-labs-python-examples

⭐ 18 · Python · 推送 2026-10-08 · [GitHub](https://github.com/Custodian-Labs/custodian-labs-python-examples) · [官网](https://www.custodianlabs.io/) · 组织维护

**用几行 Python 构建、托管 AI agent 的 SDK 示例集**

Custodian Labs Python SDK 的官方示例仓库：开发者以少量代码描述 agent，平台负责流水线构建、托管、对话记忆与 PII 处理，并生成可分享的聊天链接。支持单 agent、Builder 链式配置与多 agent 团队（CustodianSquad，三种路由模式），另含 GuardianLayer PII 遮盖服务与 FastAPI WebSocket 桥接示例。需 API key，Free 计划仅 1 个部署且固定 gpt-4o 模型，多 agent 团队为 Pro 功能。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 数行代码部署带 RAG 的 AI agent 并获得托管聊天链接
- CustodianSquad 多 agent 团队支持 single/workflow/chain 三种路由（Pro）
- GuardianLayer 独立服务可对文本/文件做 PII 遮盖
- 附法律合同助手、简历问答等应用示例与 WebSocket 桥接示例

## 适用场景

- 快速部署一个可分享链接的托管 AI 助手
- 把多个 agent 组成团队并控制消息路由
- 在自建应用中调用 PII 遮盖服务处理敏感文件

## 场景标签

`Agent 框架` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L5: Describe your agent in a few lines of Python. Custodian handles the pipeline, hosting, conversation memory and PIIs,
> L14: Your script describes an AI agent, and the Custodian platform builds, hosts and runs it.

## 星数曲线

```mermaid
xychart-beta
    title "Custodian-Labs/custodian-labs-python-examples 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `0e70c6a182c4` · [字段定义](../../DATASET.md)*
