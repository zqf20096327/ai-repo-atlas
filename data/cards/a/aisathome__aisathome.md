# aisathome/aisathome

⭐ 3 · Go · Apache-2.0 · 推送 2026-11-21 · [GitHub](https://github.com/aisathome/aisathome) · [官网](https://aisathome.org) · 组织维护

**志愿者 GPU 分发式服务开源模型的网关与节点**

由两个 Go 组件组成的分布式推理网络：志愿者在自己 GPU 上运行 node，节点向外连接网关（不开端口）；网关提供 OpenAI 兼容 API 与聊天入口，负责路由、排队与故障转移、账户与计量。隐私机制包括剥离身份、不存储提示与回答、仅暂存被拦截片段 14 天。项目自称处于试点阶段，非生产就绪；附带 Python harness 以 agent 方式在可机器验证的外部任务（如 Lean 证明）上运行模型。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- OpenAI 兼容 API（api.aisathome.org/v1）与聊天入口，路由含排队与故障转移
- 节点仅向外连接网关，无需开放端口
- 隐私设计：网关剥离身份、不存储提示与回答，被拦截片段仅存 14 天
- harness 可将 open 模型接入外部可验证任务（Lean 证明）

## 适用场景

- 在志愿者 GPU 上运行节点参与分布式推理
- 通过 OpenAI 兼容 API 接入 deep/agent 模型
- 自建网关为社区提供服务
- 将模型作为 agent 运行在机器可校验的科学任务上

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L4: company's data centre. Volunteers run a node on their own GPU; a gateway (the project
> L5: server) takes requests from the chat and the OpenAI-compatible API and routes them to
> L32: |`gateway/`|`aisathome-gateway`: the OpenAI-compatible API, routing with queueing and failover, accounts and sign-i


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `3c7bd4e05d69` · [字段定义](../../DATASET.md)*
