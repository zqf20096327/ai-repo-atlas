# TheAuditorTool/Auditor

⭐ 549 · NOASSERTION · 推送 2026-07-23 · [GitHub](https://github.com/TheAuditorTool/Auditor) · [官网](https://blog.theauditortool.com) · 组织维护

**本地数据库优先的代码智能与多语言 SAST 平台（尚未发布）**

定位为面向 AI agent 与安全团队的代码智能工具：将代码库索引为确定性、可查询的结构化事实，供 agent 通过 CLI 与 MCP 接口查询符号、依赖、影响面、架构与安全问题，替代反复读取整个文件；同一份索引同时支持代码导航、变更影响分析与多语言安全发现。分析结果保留在本机并可离线运行。仓库仅为发布信息渠道，当前不含可分发软件，计划 2026 年 8 月初公开，软件为专有许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 代码库索引为确定性可查询事实，支持一次性索引后按查询取上下文
- 同一索引支持代码导航、变更影响分析与多语言 SAST 安全发现
- 提供 CLI 与 MCP 接口，返回有界的任务特定答案
- 本地化设计，分析结果留存本机并支持离线运行

## 适用场景

- AI agent 编码时按需查询代码符号、依赖与影响面，减少上下文消耗
- 安全团队在本地对多语言代码库做静态分析
- 为 MCP 客户端接入代码事实查询

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L5: TheAuditor is a local, database-first code intelligence and polyglot SAST platform. It turns a codebase into determi
> L18: - **Built for agents:** Focused CLI and MCP interfaces return bounded, task-specific answers.

## 星数曲线

```mermaid
xychart-beta
    title "TheAuditorTool/Auditor 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 548 --> 550
    line [549, 549]
```

2026-10-18 549 → 2026-10-28 549（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `8ce78d85b4f8` · [字段定义](../../DATASET.md)*
