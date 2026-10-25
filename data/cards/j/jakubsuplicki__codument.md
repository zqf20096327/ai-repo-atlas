# jakubsuplicki/codument

⭐ 48 · TypeScript · Apache-2.0 · 推送 2026-10-05 · [GitHub](https://github.com/jakubsuplicki/codument) · [官网](https://www.npmjs.com/package/codument) · 个人维护

**给 AI 编码代理变更加文档护栏的 CLI 安全层**

面向使用 Claude Code、Codex 等 AI 编码代理的开发者的 git 原生变更控制工具。由两部分组成：代理执行的文档驱动交付工作流（grill→plan→implement→review→commit，写入 AGENTS.md/CLAUDE.md 与 .claude/ 技能），以及用户运行的确定性本地 CLI 检查（doctor 文档覆盖率、review 变更波及与陈旧文档、watch 实时面板、scan/audit 漂移审计），检查不联网、不调用模型、输出可复现。另有计划与 diff 两个对抗门。核心数据结构为 docs/.registry.json 源文件到文档的归属映射。以 npm 包分发，通过 npx codument init 安装，支持 TypeScript/Python/Go/Rust/C#/Java/Kotlin 等语言按符号解析。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 确定性 CLI 检查（doctor/review/watch/scan/audit）：本地、无网络、无 AI 调用、可复现
- docs/.registry.json 源文件→文档归属映射，支持多语言按符号解析
- 计划与 diff 两个独立对抗门，由确定性判定规则裁决
- 为 Claude 与 Codex/AGENTS.md 代理安装可移植工作流档案

## 适用场景

- AI 代理改代码前用文档护栏约束计划与 diff 审查
- 量化仓库既有提交历史中的文档漂移（scan + audit）
- 实时查看代理工作面板与按特性归因的 token 开销

## 场景标签

 · 领域:开发者工具/AI 工作流治理

## 证据(README 行号)

> L148: - **A delivery workflow your agent runs.** Docs-backed planning, source-to-doc ownership, review discipline, and c
> L149: - **Deterministic CLI checks you run.** Local, no-network, no-AI commands that read the repo and report the facts:
> L11: Claude Code · native

## 星数曲线

```mermaid
xychart-beta
    title "jakubsuplicki/codument 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 47 --> 49
    line [48, 48]
```

2026-10-18 48 → 2026-10-25 48（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `e296bb34e9da` · [字段定义](../../DATASET.md)*
