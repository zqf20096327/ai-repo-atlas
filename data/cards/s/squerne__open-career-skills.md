# squerne/open-career-skills

⭐ 26 · MIT · 推送 2026-08-07 · [GitHub](https://github.com/squerne/open-career-skills) · [官网](https://jobmentis.com/?ref=oss-prompts) · 组织维护

**求职场景的 8 个 Claude 技能与提示词集合，拒绝编造个人事实**

由 JobMentis 开源的求职提示词架构：8 个技能覆盖 CV 优化、STAR 故事库、LinkedIn 规划、求职信、模拟面试、职位搜索、git 证据挖掘与 ATS 识别，共同约束是不编造用户事实——缺数据时向用户提问而非估算。提供三种使用方式：作为 Claude Code 工作区 git clone 运行（含 /apply 端到端流水线与独立审查子代理）、复制单个技能目录、或在任意聊天模型中粘贴 prompts/ 版本。个人数据默认 git-ignore 本地存储。同时对比其托管产品 JobMentis 的功能边界。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 8 个求职技能，核心约束为不编造用户事实、缺失数据时提问
- /apply 流水线含独立 reviewer 子代理审计每条声明的出处
- 支持 Claude Code 工作区、单技能安装与任意聊天模型粘贴三种用法
- 个人数据（简历/故事/日历）通过 .gitignore 保持在本地

## 适用场景

- 在 Claude Code 中按 JD 定制 CV 并做全流程求职管理
- 把 git 提交历史整理为有出处的成就故事库
- 在不依赖特定订阅的聊天模型里粘贴提示词完成求职文书写作

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L5: **The prompt architecture behind JobMentis, open-sourced as installable Claude skills.**
> L16: |Skill|What it does|The rule that makes it different|
> L73: The five writing skills have self-contained paste-able versions in `prompts/`. Paste one as your first message and 

## 星数曲线

```mermaid
xychart-beta
    title "squerne/open-career-skills 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-27"]
    y-axis "stars" 24 --> 27
    line [25, 26, 26]
```

2026-10-18 25 → 2026-10-27 26（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `6683e145e682` · [字段定义](../../DATASET.md)*
