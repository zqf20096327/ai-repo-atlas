# 1173591564/Dynamics-memory

⭐ 205 · TypeScript · 推送 2026-10-14 · [GitHub](https://github.com/1173591564/Dynamics-memory) · 个人维护 · 中文 README

**LLM agent 的有界自纠错长期记忆层，蒸馏项目交互日志**

面向 LLM agent（默认经 OpenCode CLI）的长期记忆 sidecar 服务：把连续、含矛盾的项目交互日志（L0 冷层）经 Hauler→Selector→Reviewer 三 Agent 协议蒸馏为有界记忆池，条目携带溯源与版本谱系，通过价值/置信动力学、滞回驱逐、矛盾人审队列与 SQLite 事务化任务机实现自更新与崩溃恢复。检索按相似度+压制+因果界过滤并按 token 预算注入。需自行配置 OpenCode 模型 provider，独立人工真实会话验收（PENDING-08）尚未完成。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Hauler→Selector→Reviewer 三 Agent 协议，冲突落入人审队列不静默改写
- 记忆池有界：价值×置信分离、滞回驱逐、容量背压 503 拒收
- 效果事务单一写入口，kill -9 崩溃后可恢复
- 与评测平台 TIDE 经 HTTP 分离，提供 passive 检索探针

## 适用场景

- 为编码 agent 提供跨会话项目记忆，新会话接续上次进度
- 避免全量日志或原文向量库导致的上下文膨胀与矛盾堆积
- 对 agent 记忆变更做溯源与人工冲突审核

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L6: **LLM agent 的有界长期记忆层**
> L25: python -m hybrid_memory.server --project <dir>   # 或被 opencode 插件自动拉起

## 星数曲线

```mermaid
xychart-beta
    title "1173591564/Dynamics-memory 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 204 --> 206
    line [205, 205]
```

2026-10-18 205 → 2026-10-22 205（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `8589ce7bb5c8` · [字段定义](../../DATASET.md)*
