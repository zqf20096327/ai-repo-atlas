# aristoapp/openclaw-membase

⭐ 39 · TypeScript · MIT · 推送 2026-06-26 · [GitHub](https://github.com/aristoapp/openclaw-membase) · [官网](https://docs.membase.so/connectors/openclaw) · 组织维护

**为 OpenClaw agent 提供跨会话持久记忆的插件**

OpenClaw 框架的记忆插件，接入 Membase 云服务（可指向自托管实例）：用混合向量检索加知识图谱存储实体、关系与事实。机制上通过两个钩子工作：AI 轮次前自动召回相关记忆注入上下文（受 maxRecallChars 预算限制），对话后缓冲并自动保存转录到 Wiki；同时注册 9 个 AI 工具（搜索、存储、遗忘、Wiki 增删改查等）。认证用 OAuth 2.0 PKCE，无需 API key。面向使用 OpenClaw 的开发者，需注册 app.membase.so 账号，MIT 许可。

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

- 混合向量检索 + 知识图谱存储实体、关系与事实
- Auto-Recall / Auto-Capture 两个钩子自动注入与保存上下文
- 9 个 AI 工具：membase_search / store / forget / Wiki 增删改查等
- OAuth 2.0 PKCE 认证，token 自动轮换缓存

## 适用场景

- 让 OpenClaw agent 在会话间记住我的偏好与目标
- 把对话转录沉淀为可检索的 Wiki 文档
- 通过语义搜索和日期/来源过滤查找历史记忆

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L5:  Persistent long-term memory for OpenClaw using hybrid vector search and a knowledge graph.
> L133: - OpenClaw — AI agent framework

## 星数曲线

```mermaid
xychart-beta
    title "aristoapp/openclaw-membase 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 38 --> 40
    line [39, 39]
```

2026-10-18 39 → 2026-10-25 39（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `82ffce659e6c` · [字段定义](../../DATASET.md)*
