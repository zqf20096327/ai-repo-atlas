# anchorco/anchor-sdk

⭐ 14 · Python · Apache-2.0 · 推送 2026-04-07 · [GitHub](https://github.com/anchorco/anchor-sdk) · [官网](https://www.getanchor.dev/) · 组织维护

**Anchor API 官方 SDK：管控 AI agent 数据存储与审计**

Anchor 平台的官方 Python 与 TypeScript SDK。通过 anchor.agents、anchor.config、anchor.data、anchor.checkpoints、anchor.audit 等命名空间提供 agent 管理、配置版本与回滚、带策略执行的数据读写、状态快照恢复及哈希链审计日志的查询/导出/校验。使用前需在 getanchor.dev 注册获取 API Key。以 pip 与 npm 包形式分发，依赖 Anchor 云端 API 服务。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Python 与 TypeScript 双语言 SDK（pip/npm 安装）
- 数据写入时的策略执行（policy enforcement）
- 状态快照（checkpoint）创建与恢复
- 哈希链审计日志的查询、校验与导出

## 适用场景

- 在 AI agent 存储数据前执行策略拦截
- 为 agent 操作留存可校验的审计轨迹
- agent 出错时回滚配置或恢复状态快照

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L9: **Control what your AI agents store. Audit everything.**
> L55: |`anchor.data`|Store data with policy enforcement|write, read, read full, delete, delete prefix, list, search|

## 星数曲线

```mermaid
xychart-beta
    title "anchorco/anchor-sdk 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `5a48ca0e2405` · [字段定义](../../DATASET.md)*
