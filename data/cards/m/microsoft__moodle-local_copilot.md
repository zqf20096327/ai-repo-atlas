# microsoft/moodle-local_copilot

⭐ 13 · PHP · GPL-3.0 · 推送 2026-10-28 · [GitHub](https://github.com/microsoft/moodle-local_copilot) · 组织维护

**将 Moodle 接入 Microsoft 365 Copilot 的插件与声明式 Agent 样例**

微软提供的 Moodle 本地插件（local_copilot）及 agent 样例，通过 OAuth 2.0 与 RESTful 端点将 Moodle 课程数据暴露给 M365 Copilot / Copilot Chat 中的两个声明式 agent：教师 agent 可列课程、查看作业与提交、创建作业、监控进度成绩；学生 agent 可查课程、作业详情、成绩并自助选课。安装需 Moodle 5.3+、PHP 8.3+、两个前置插件及 M365 租户与 A1/A3/A5 许可，经 Teams 开发者门户注册 OAuth 客户端并在 M365/Teams 管理中心部署 manifest。当前仅支持英语、每端点最多返回 10 条等限制。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 教师/学生两个声明式 agent，覆盖课程、作业、成绩等 Moodle 操作
- OAuth 2.0 流程连接 Moodle 与 Microsoft 365（经 Teams 开发者门户注册）
- 生成 manifest 包并可从 M365 Admin Center 或 Teams Admin Center 部署
- 插件实现教师/学生两组 RESTful 端点与 Adaptive Card 模板

## 适用场景

- 教师在 Word/Teams 等 M365 应用中通过 Copilot 查询课程与学生进度
- 学生通过 Copilot Chat 查作业截止时间、成绩并自助选课
- 基于样例定制连接自有 LMS 的声明式 agent

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L5: This repository contains Moodle plugin and agent samples for Education to be used with Microsoft 365 Copilot and Mic
> L7: The M365 Copilot plugin (local_copilot) enables Moodle to integrate with M365 Copilot and Copilot Chat by providing 
> L233: - OAuth 2.0 authentication flow between Moodle and Microsoft 365

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/moodle-local_copilot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `207b22e1dcf4` · [字段定义](../../DATASET.md)*
