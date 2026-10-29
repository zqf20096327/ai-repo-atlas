# mthines/lorekit

⭐ 20 · TypeScript · MIT · 推送 2026-10-28 · [GitHub](https://github.com/mthines/lorekit) · [官网](https://lorekit.io) · 个人维护

**为 AI 编程 agent 提供本地/远程持久记忆的 MCP 工具**

面向 Claude Code、Cursor、Codex 等 AI 编程 agent 的持久记忆系统：通过生命周期钩子监测会话中的失败与重复命令，提示 agent 写下经验教训（markdown 格式），下次失败时按工具名与错误文本检索并注入匹配教训；按 branch/repo/project/global 四级作用域组织，按复发计数晋升为规则、按使用率归档。提供 CLI（install/doctor/search/dedupe 等）、Claude Code 插件、配套技能与仪表盘。支持本地离线模式、托管服务与自部署（Supabase/Vercel），MIT 许可。Codex 支持处于实验阶段；项目自述仍在快速开发期。

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

- 生命周期钩子自动捕获 agent 失败经验并写成 markdown 教训
- 错误文本匹配检索，失败重试前注入最多三条匹配教训
- branch/repo/project/global 四级作用域，按复发晋升规则、按使用率归档
- 本地离线、托管与自部署三种运行模式，全栈 MIT 开源自部署

## 适用场景

- 让我的编程 agent 记住踩过的坑，下次直接拿到解法
- 团队共享同一套 repo 级经验教训，CI 以只读 token 读取
- 从代码评审评论中沉淀候选经验教训

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L22: Works with **Claude Code** and **Cursor**, Codex (experimental), and any MCP
> L31: It stores lessons in scopes (`branch::`, `repo::`, `project::`, `global`; the
> L174: |**Claude Code**|Marketplace plugin or CLI: skills + 4 lifecycle hooks + MCP|Supported|

## 星数曲线

```mermaid
xychart-beta
    title "mthines/lorekit 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-29"]
    y-axis "stars" 18 --> 21
    line [19, 20, 20]
```

2026-10-18 19 → 2026-10-29 20（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `e6b7c69f2c36` · [字段定义](../../DATASET.md)*
