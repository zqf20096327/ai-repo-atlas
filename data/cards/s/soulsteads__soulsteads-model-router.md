# soulsteads/soulsteads-model-router

⭐ 5 · Rust · Apache-2.0 · 推送 2026-11-20 · [GitHub](https://github.com/soulsteads/soulsteads-model-router) · [官网](https://soulsteads.github.io/soulsteads) · 个人维护

**为本地推理服务器提供容量感知路由的 OpenAI 兼容网关**

Rust 编写的本地推理路由器，构建为 slotline 二进制：在多个自有推理服务器前提供统一 OpenAI 兼容端点与稳定模型别名。按后端能力（工具调用、结构化输出、内联图像、embeddings）与空闲槽位容量选路，共享物理后端限额；提供按客户端 key 的别名目录、凭据签发/轮换/吊销、有界重试与不落盘 prompt 文本的运维观测。不托管模型、不管理模型加载。要求 Linux/Unix 主机与既有本地推理服务器，默认监听 Tailnet IPv4。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 容量感知路由：优先空闲后端，按占用/空闲槽位排序，物理后端限额共享
- 能力检查：工具调用、结构化输出、内联图像、Responses、embeddings 只路由到合格后端
- 凭据生命周期：受保护 key 文件或 Argon2id 验证器存储，支持签发、轮换、吊销
- 不记录 prompt 文本的运维观测：健康、准入、亲和性、遥测、请求计时

## 适用场景

- 本地部署多个推理服务器时统一暴露一个 OpenAI 兼容端点
- 让 Agent 与兼容客户端无需感知后端分布与 GPU 容量
- 按客户端 key 限制可访问的模型别名与路由

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L4:  Route OpenAI-compatible requests across your own inference servers without overbooking them.
> L17: **Soulsteads Model Router** puts stable model aliases in front of your servers.
> L48: It does **not** host models, manage model loading, or provide cloud subscriptions.

## 星数曲线

```mermaid
xychart-beta
    title "soulsteads/soulsteads-model-router 星数(近 3 点)"
    x-axis ["2026-10-22", "2026-11-11", "2026-11-23"]
    y-axis "stars" 3 --> 6
    line [4, 5, 5]
```

2026-10-22 4 → 2026-11-23 5（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `68bbd880d3dd` · [字段定义](../../DATASET.md)*
