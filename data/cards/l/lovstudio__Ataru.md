# lovstudio/Ataru

⭐ 361 · Rust · Apache-2.0 · 推送 2026-08-24 · [GitHub](https://github.com/lovstudio/Ataru) · [官网](https://lovstudio.ai/app/ataru) · 组织维护 · 中文 README

**本地 AI 会话记忆检索工具：Rust 搜索内核加桌面 GUI**

面向使用 Claude、Codex 等 AI 编程代理的用户，把分散在本地会话文件（transcript）中的历史对话变成可检索的记忆层：通过来源适配器统一归一化格式，用 Tantivy+Jieba 建立中文友好的全文索引，支持 Turn/Run/Session/Project 四种粒度聚合与按稳定 ID 回读原始消息和行号。默认离线运行，语义检索为可选增强（OpenAI 兼容 Embeddings + SQLite 向量索引），未配置或超时降级到关键词。形态包括 Tauri 桌面应用、JSON CLI 与两个 Agent Skill；CLI 仅关键词模式，聚合查询有 limit 上限，实测大语料 turn 级查询约 48s。

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

- Claude/Codex 等本地会话统一索引，增量追赶无需全量重扫
- Tantivy+Jieba 中文/代码/错误串全文检索，混合召回可选
- Turn/Run/Session/Project 四粒度聚合，稳定 ID 深链回读原文与行号
- GUI、CLI、Agent Skill 共用同一套搜索契约（ensure_index→search→inspect）

## 适用场景

- 找回几周前某次故障排查或架构讨论的原始上下文
- 让 Agent 通过 Skill 检索我的历史会话作为工作记忆
- 按项目回看一段时间内的决策与演进

## 场景标签

`Agent 记忆` `语义搜索` · 领域:Agent 开发

## 证据(README 行号)

> L29: - 从 Claude、Codex 等本地会话来源建立统一索引。
> L98: GUI 只是 Ataru 的一个客户端。面向 Agent 的正确抽象是 Skill：把“确认索引可用、发起搜索、读取上下文”变成稳定动作，而不是让每个 Agent 自己理解 Tantivy、文件路径或来源格式。这套抽象已经落地为两
> L126: Skill 不拥有另一套索引，也不复制排序算法；它只是 `api/sdk` 契约的 Agent-facing adapter。独立 `SKILL.md` 包装层应复用这套 `ensure_index → search → ins

## 星数曲线

```mermaid
xychart-beta
    title "lovstudio/Ataru 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 360 --> 362
    line [361, 361]
```

2026-10-18 361 → 2026-10-24 361（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `46b618159281` · [字段定义](../../DATASET.md)*
