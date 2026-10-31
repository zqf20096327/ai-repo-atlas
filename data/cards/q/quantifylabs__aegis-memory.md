# quantifylabs/aegis-memory

⭐ 27 · Python · Apache-2.0 · 推送 2026-08-20 · [GitHub](https://github.com/quantifylabs/aegis-memory) · [官网](https://www.aegismemory.com/) · 组织维护

**面向 AI agent 的安全记忆与上下文层：写入前拦截注入与泄密**

为 AI agent 提供带内容安全审查的记忆与上下文层。三种用法：aegis_memory.guard 作为离线写入门可包裹任意存储（LangGraph、向量库等）；aegis inspect 静态扫描 agent 代码中的不安全写入点；Aegis server 为 FastAPI + PostgreSQL/pgvector 服务，提供排序检索、多 agent 访问控制、Context Hub 与审计日志。每次写入经 4 阶段内容安全流水线（校验→密钥/PII 检测→注入正则→可选 LLM 分类器），HMAC-SHA256 完整性哈希防篡改，OWASP 4 级信任层级与作用域 ACL。限制：正则阶段无法覆盖语义级注入、未绑定 key 无 agent 级隔离、单实例限流需 Redis 扩展。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 4 阶段内容安全流水线审查每次记忆写入，投毒写入被拒绝
- HMAC-SHA256 完整性签名覆盖内容、作用域与信任级别，读取时重验
- OWASP 4 级信任层级 + 作用域 ACL + API key 绑定 agent 身份
- Context Hub 单次调用加载 prompts/memory/skills/subagents 四类工件

## 适用场景

- 多 agent 系统中防止被污染的记忆成为其他 agent 的指令
- 为共享记忆库拦截密钥、PII 与提示注入内容
- 审计 agent 记忆的来源、策略判定与篡改情况

## 场景标签

`Agent 记忆` `网络安全` · 领域:Agent 开发

## 证据(README 行号)

> L30: **Aegis Memory is a secure memory and context layer for AI agents.** It does what a memory
> L41: - **The Aegis server** — a full FastAPI service with PostgreSQL + pgvector: ranked retrieval,

## 星数曲线

```mermaid
xychart-beta
    title "quantifylabs/aegis-memory 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-31 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `b1d605ad9d8f` · [字段定义](../../DATASET.md)*
