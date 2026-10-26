# AlanHuang168/AI-Project-Workflow

⭐ 29 · JavaScript · MIT · 推送 2026-07-22 · [GitHub](https://github.com/AlanHuang168/AI-Project-Workflow) · [官网](https://www.npmjs.com/package/@dayahs/ai-project-workflow) · 个人维护 · 中文 README

**面向多款 AI 编码助手的分阶段软件交付工作流框架**

为 Cursor、Claude Code、Codex、TRAE、CodeBuddy、CatPaw、Qoder 等 AI 编码助手提供统一的软件交付工作流：以 core/ 为唯一规范源，每个工具生成一层轻量适配（规则文件、入口文件、skills 目录），通过 .ai-workflow/state.json 跟踪阶段进度并设门禁，配套 apw CLI 负责安装、校验与同步。内置 init→prd→hld→sdd→impl→review→deploy→retro 八个阶段，可通过 project.yaml 自定义。约束基于提示词实现，CLI 校验文件与状态；要求 Node.js >= 20。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- core/ 单一规范源 + 各平台轻量适配层生成
- state.json 阶段状态跟踪与门禁，apw CLI 安装/校验/同步
- 内置八阶段流程，支持 project.yaml 自定义阶段
- 兼容 7 个已验证 AI 编码平台（Qoder 待验证）

## 适用场景

- 让 AI 编码助手按 PRD→架构→设计→实现→评审的分阶段流程交付项目
- 多工具团队在同一项目共享统一的 AI 工作流规范
- 通过 CLI 校验各阶段产出物与状态文件

## 场景标签

`提示工程` `工作流自动化` · 领域:Agent 开发

## 证据(README 行号)

> L9: 一套面向 Cursor、Claude Code、Codex、Qoder、CodeBuddy、CatPaw、TRAE 以及其他 AI 编码助手的通用 AI 原生软件交付工作流。一份规范的 `core/` 单一真相源、每个工具一层轻量适
> L44: 约束是基于提示词的:适配层指示 AI 先读当前阶段的 Skill、核对上游文档、更新状态文件,然后才能推进。CLI 负责校验文件(`apw validate`、`apw status`);AI 遵守契约是因为每个入口都这样要求它。
> L263: - 约束是基于提示词的:CLI 校验文件与状态,但让 AI 遵守流程的是工具侧的上下文(规则、入口文件)。偶尔需要人工把 AI 拉回流程。

## 星数曲线

```mermaid
xychart-beta
    title "AlanHuang168/AI-Project-Workflow 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-26 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `d844a896d61b` · [字段定义](../../DATASET.md)*
