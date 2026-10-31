# iiishop/StratumCode

⭐ 16 · Python · 推送 2026-10-24 · [GitHub](https://github.com/iiishop/StratumCode) · 个人维护 · 中文 README

**本地优先的透明软件工程 agent，每步可审计、补丁需授权**

面向开发者的本地优先 AI 编码 agent 桌面应用（pywebview + Vue 3）。以显式状态机驱动任务流程：任务分析、代码调查（LSP/MCP/Web 工具）、设计、补丁计划、事务化编辑、独立验证，产出可追溯、可回滚的变更。安全约束在运行时层面强制执行（范围授权、Plan Hash、文件快照、原子提交、回滚、证据门控），支持 OpenAI 兼容端点与实验性 Codex OAuth。当前为 Alpha（v0.0.17），格式与传输可能随提交变化，需在版本控制仓库中使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 状态机驱动的六阶段流程，各阶段职责与转移规则分离
- 运行时硬约束：补丁范围授权、Plan Hash、原子提交与回滚
- 跨会话工程记忆系统（图结构、压缩、新鲜度、选择器）
- pywebview 桌面 UI：时间线、记忆面板、用量统计、自更新

## 适用场景

- 在本地以可审计流程让 AI 完成功能、修复或重构
- 要求每个补丁先经计划与授权再落地，避免静默扩散变更
- 保留跨会话的项目知识记忆以便持续开发

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L9:  A local-first software engineering agent. It does not jump from your instruction straight to editing code —
> L45: > **The model proposes. The runtime validates, authorizes, records, and routes.**
> L66: User request → Task Analysis → Investigation → Design → Patch Planning → Implementation → Validation

## 星数曲线

```mermaid
xychart-beta
    title "iiishop/StratumCode 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `be9c480c0542` · [字段定义](../../DATASET.md)*
