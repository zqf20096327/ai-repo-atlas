# JiuNian3219/architext

⭐ 14 · TypeScript · MIT · 推送 2026-05-14 · [GitHub](https://github.com/JiuNian3219/architext) · 个人维护 · 中文 README

**文档驱动 AI 开发协议：先写 spec 与 plan，再让 AI 编码**

安装进仓库的 DDAD（Document-Driven AI Development）协议：CLI 层（npx archi）向项目部署 .architext 规则、提示词、技能与模板；AI 命令层（/archi.init、/archi.plan、/archi.code、/archi.change、/archi.review 等）在 IDE 对话中生成 vision/roadmap/spec/plan 等文档，并通过确认门让人先审文档再编码。支持 Cursor、Windsurf、Trae、VS Code、Claude Code、OpenCode，可采纳既有代码库。README 自声明处于早期开发阶段。面向中小应用、独立开发者或小团队。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- CLI 部署规则/提示词/技能 + AI 聊天命令驱动的两层结构
- init → plan → code → review 生命周期，spec/plan 文档先行并带确认门
- /archi.change 路由修复/编辑/全局修订，/archi.review 做任务审计与 map 同步
- 支持采纳既有代码库并注册 LEG-xx 任务

## 适用场景

- 在 AI 编码前先固化需求、边界与验收标准
- 让不同会话、队友和 AI 工具基于同一套文档继续开发
- 对既有代码库补建 spec 并纳入任务路线图

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L19: Architext is not an AI that makes product or architecture decisions for you, and it is not another code generator. 
> L31: |**CLI Tool Layer**|`npx archi <command>`|Deploy rule files, prompts, and skills into your project|
> L32: |**AI Command Layer**|`/archi.<command>` in AI chat|Generate documents, plan features, write code, audit|

## 星数曲线

```mermaid
xychart-beta
    title "JiuNian3219/architext 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `40248a9e77b0` · [字段定义](../../DATASET.md)*
