# zhangl1001/civil-ai

⭐ 41 · TypeScript · MIT · 推送 2026-10-25 · [GitHub](https://github.com/zhangl1001/civil-ai) · [官网](https://github.com/zhangl1001/civil-ai/releases/latest) · 个人维护 · 中文 README

**面向 iOS/Web 的本地优先自适应教育 Agent 基础框架**

用 TypeScript/Vue 3 实现的可复用教育 Agent 基础层：提供供应商中立的 Agent 运行时（循环、工具/技能注册、检查点、恢复、取消）、学习者证据、掌握度投影、自适应规划、结构化内容生成与 SQLite/IndexedDB 本地持久化。附带中国公考应用作为端到端参考适配，另含教师招聘考试包验证课程与评分以数据形式装载。构建门禁含 39 项检查；跨学习域的可移植性尚未验证，部分契约仍带考试域标识符。给维护者和构建者使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 供应商中立的 Agent 运行时（检查点、租约、取消、恢复、并发控制）
- 学习者证据、掌握度投影与自适应规划契约
- SQLite/IndexedDB 本地优先持久化，含 43 个校验迁移
- 公考与教师招聘两个考试包以数据而非代码形式装载

## 适用场景

- 在 iOS/Web 上构建基于学习证据的自适应辅导 Agent
- 替换模型供应商同时保持确定性校验与持久化
- 通过版本化课程、能力图与评分策略添加学习域

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L10: Civil AI is a reusable, local-first foundation for building adaptive education Agents on iOS and Web. It separates 
> L39: - build an education Agent that acts on durable learning evidence instead of chat history alone;
> L65: |Portable Agent runtime|Agent loop, provider gateway, Tool/Skill registries, context assembly, cancellation, recove

## 星数曲线

```mermaid
xychart-beta
    title "zhangl1001/civil-ai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 40 --> 42
    line [41, 41]
```

2026-10-18 41 → 2026-10-28 41（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `7f83aa74eb25` · [字段定义](../../DATASET.md)*
