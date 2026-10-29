# dapr/proposals

⭐ 17 · Apache-2.0 · 推送 2026-10-07 · [GitHub](https://github.com/dapr/proposals) · [官网](https://docs.dapr.io/contributing) · 组织维护

**Dapr 新功能设计提案库：社区评审式的设计文档存档**

存储 Dapr 新特性（新构建块与 API）的设计提案，覆盖工作流、调度器、发布订阅、Actor、LLM Conversation API 与 MCP 服务器等方向。提案按 `YYYYMMDD-FLAGS-description.md` 命名，通过 PR 提交并由相应仓库维护者多数投票（>50%）决定是否接受合并；文档定义了 Alpha/Beta/Stable 三阶段功能生命周期要求与 RFC 2119 关键词语义。面向 Dapr 社区贡献者与维护者，用于设计讨论、历史记录与流程一致性。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提案按日期+标志位（B/C/I/P/R/S）命名，PR 评审后维护者多数投票接受
- 定义 Alpha/Beta/Stable 功能生命周期阶段要求
- 提供提案模板与撰写指南（templates/、guides/）
- 接受后需在 dapr/dapr 创建 issue 跟踪实现并指定发布版本

## 适用场景

- 为 Dapr 提交新构建块或 API 变更的设计提案
- 查阅 Dapr 历史设计决策与功能演进记录
- 了解提案评审与功能生命周期的流程规则

## 场景标签

 · 领域:云原生/分布式系统设计文档

## 证据(README 行号)

> L5: This repository stores proposals and designs for new features in Dapr (i.e not bug fixes or minor changes) with the 
> L11: * New Dapr building blocks


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `e68cab7aff31` · [字段定义](../../DATASET.md)*
