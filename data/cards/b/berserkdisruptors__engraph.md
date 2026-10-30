# berserkdisruptors/engraph

⭐ 15 · TypeScript · MIT · 推送 2026-05-11 · [GitHub](https://github.com/berserkdisruptors/engraph) · 组织维护

**为 AI 编程 agent 构建持久化代码库专长上下文层的工具**

面向使用 AI 编程 agent（Claude Code、Pi、Codex 等）的开发者：在代码库旁建立由三部分组成并随仓库保存的上下文层——tree-sitter 生成的模块结构 codegraph、版本化 YAML 约定与验证文件、嵌入 git 提交的上下文化决策记录。通过五个以斜杠命令形式安装进 agent 的技能（context-search/extract/add/verify/commit）和五个确定性 CLI 命令来检索与维护。CLI 不调用 LLM、输出结构化 JSON。以 npm 全局包安装，MIT 许可。

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

- codegraph 由 tree-sitter AST 分析生成，engraph graph 秒级重建且不调用 LLM
- 五个技能 + 五个 CLI 命令的可组合原语，命令输出结构化 JSON
- 上下文提交以 intent/decision/rejected/constraint 等结构化行嵌入 git 历史，可 recall 查询
- 技能为通用 SKILL.md 文件夹，任何从 .agents/skills/ 读取技能的 agent 均可接入

## 适用场景

- 接手陌生模块或他人 PR 前获取约定与历史决策简报
- 改动前通过 codegraph 预判影响范围
- 提交 PR 前按模块级验证清单自查
- 查询某段代码设计背后的决策与被否决的备选方案

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L9: Engraph builds a persistent **context layer** alongside your codebase - structure, conventions, and the reasoning be
> L11: It works through **skills** that integrate directly into your AI coding agent, giving the agent curated codebase ex

## 星数曲线

```mermaid
xychart-beta
    title "berserkdisruptors/engraph 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `4ab72b72cf67` · [字段定义](../../DATASET.md)*
