# dream-num/workbuddy-univer-office

⭐ 10 · TypeScript · Apache-2.0 · 推送 2026-09-11 · [GitHub](https://github.com/dream-num/workbuddy-univer-office) · [官网](https://univer.ai) · 组织维护 · 中文 README

**为 WorkBuddy 提供本地 Office 文档创建、预览与草稿审核的集成**

基于 Univer Office SDK 的开源集成：通过本地 MCP 服务器与 agent Skill，让 WorkBuddy 创建/修改本地表格、文档、幻灯片、Base 表与画布；agent 改动写入隔离草稿 worktree，用户查看只读实时预览并对比版本后手动确认合并或丢弃，五类内容均支持语义变更导航，并支持从已确认版本导出。要求 Node.js ≥22.12 与 pnpm 10.33.4，部分 SDK 功能需 Univer Pro 许可。目前为开发预览，非正式发布版。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 本地 MCP 服务器加一个 univer-office Skill 暴露五类内容操作
- agent 改动写入隔离 worktree，人工确认后才能合并
- 只读实时预览与固定版本对比，含语义变更导航
- 市场版采用 MCP+Skill 本地 stdio 进程，无需云账号或 Office API key

## 适用场景

- 让 WorkBuddy 助手自动创建或修改本地表格与文档
- 审核 agent 生成的文档草稿后再合并
- 从已确认版本导出文档格式

## 场景标签

 · 领域:办公/Agent 工具集成

## 证据(README 行号)

> L7: Create, inspect and review local spreadsheets, documents, slides, Base tables and Board canvases from WorkBuddy. Bui
> L19: Worktree View and Compare are always read-only, without a Ribbon. The current verified WorkBuddy 5.5.4 integration 

## 星数曲线

```mermaid
xychart-beta
    title "dream-num/workbuddy-univer-office 星数(近 2 点)"
    x-axis ["2026-11-16", "2026-11-28"]
    y-axis "stars" 9 --> 12
    line [11, 10]
```

2026-11-16 11 → 2026-11-28 10（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-18 · 置信度 high · 依据 README sha `c3cb692e9ac6` · [字段定义](../../DATASET.md)*
