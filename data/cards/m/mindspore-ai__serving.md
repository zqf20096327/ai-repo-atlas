# mindspore-ai/serving

⭐ 41 · C++ · Apache-2.0 · 推送 2026-10-22 · [GitHub](https://github.com/mindspore-ai/serving) · [官网](https://gitee.com/mindspore/serving) · 组织维护 · 中文 README

**帮助 MindSpore 开发者部署在线推理服务的服务模块**

面向 MindSpore 开发者的推理服务部署模块：将训练后导出的 MindSpore 模型封装为在线推理服务。架构由 Client 与 Server 组成，Server 含 Main 节点与多个 Worker 节点，Servable 部署在 Worker 上，支持单模型与多模型组合，统一接口。Client 通过 gRPC 或 RESTful API 访问。推理后端为 MindSpore 时支持 Ascend 910 与 Nvidia GPU；后端为 MindSpore Lite 时支持 Ascend 310/310P、Nvidia GPU 与 CPU。提供批处理、前后处理与分布式推理。安装细节指向官网文档，README 未给出具体命令。

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

- Client/Server 架构，Main 节点管理 Worker 并分发请求
- gRPC 与 RESTful API，Client 不依赖特定硬件平台
- 多模型组合与单模型使用同一套接口
- 支持批处理、模型前后处理与分布式推理

## 适用场景

- 将训练完成的 MindSpore 模型上线为生产推理服务
- 在 Ascend 或 GPU 环境部署分布式推理
- 组合多个模型提供复杂推理服务

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L9: MindSpore Serving is a lightweight and high-performance service module that helps MindSpore developers efficiently
> L10: deploy online inference services in the production environment. After completing model training on MindSpore, you c

## 星数曲线

```mermaid
xychart-beta
    title "mindspore-ai/serving 星数(近 2 点)"
    x-axis ["2026-10-23", "2026-10-26"]
    y-axis "stars" 40 --> 42
    line [41, 41]
```

2026-10-23 41 → 2026-10-26 41（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `1ac74db7ec49` · [字段定义](../../DATASET.md)*
