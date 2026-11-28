# FeatherHunter/dsh-mattpocock-skills-deck

⭐ 423 · TypeScript · MIT · 推送 2026-11-27 · [GitHub](https://github.com/FeatherHunter/dsh-mattpocock-skills-deck) · [官网](https://featherhunter.github.io/dsh-mattpocock-skills-deck/architecture/MattSkills-architecture.html) · 个人维护 · 中文 README

**DSH 插件：将 mattpocock/skills 化为任务面板管理 issue**

面向 DSH CLI 的插件，安装即内置 mattpocock/skills v1.3.2 的 27 个技能，无需手动安装。将技能工作流呈现为游戏风格任务面板：支持 GitHub 与 GitLab 的 issue 管理（本地 Markdown 为预览版），提供任务拆分与多会话并发执行、单票详情、胶囊状态栏、需求引导流程、后端切换与环境自检、版本管理页面及标签配色设置。安装依赖 npm 全局安装 DSH CLI；GitHub 后端需本机 gh 已登录账号具备 push/triage 权限。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 内置 mattpocock/skills v1.3.2 的 27 个技能并提供原文查看
- GitHub/GitLab issue 后端与本地 Markdown 预览版
- 技能任务拆分支持多工作区多会话并发处理
- 六步初始化流程与环境逐项自检

## 适用场景

- 在 DSH 中用任务面板管理 GitHub/GitLab issue 开发流程
- 任务拆分后多会话并发执行开发任务
- 学习 mattpocock/skills 原始技能内容

## 场景标签

 · 领域:开发者工具/AI 编码辅助

## 证据(README 行号)

> L6: 让 mattpocock/skills 在 DSH 里化作游戏系统的任务面板。
> L61: 根据办公环境不同提供多样后端：GitHub、本地 Markdown、GitLab。

## 星数曲线

```mermaid
xychart-beta
    title "FeatherHunter/dsh-mattpocock-skills-deck 星数(近 27 点)"
    x-axis ["2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26", "2026-11-27", "2026-11-28"]
    y-axis "stars" 205 --> 442
    line [232, 237, 245, 251, 262, 265, 269, 274, 224, 320, 338, 343, 350, 359, 363, 369, 373, 380, 383, 391, 398, 401, 403, 412, 421, 420, 423]
```

2026-10-26 232 → 2026-11-28 423（+191）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 mid · 依据 README sha `132300cade91` · [字段定义](../../DATASET.md)*
