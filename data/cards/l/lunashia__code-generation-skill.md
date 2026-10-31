# lunashia/code-generation-skill

⭐ 17 · PowerShell · 推送 2026-06-19 · [GitHub](https://github.com/lunashia/code-generation-skill) · 个人维护 · 中文 README

**供 Codex/Claude 共用的代码生成工作流约束 skill**

一套双份维护的 agent skill：为 Codex 提供 SKILL.md 入口与按需加载的 References 参考文件，为 Claude 提供 CLAUDE.md 项目级说明与 .claude/skills/generate-code/ 入口，内容为代码生成的工作流约束与提示词。附 PowerShell 同步检查脚本，用于校验两套文件是否漂移。使用者需自行保证四份入口文件同步，且不得提交密钥或本机路径。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Codex 与 Claude 双入口（SKILL.md / CLAUDE.md + .claude/skills）
- References/ 目录供 Codex 按需加载参考文件
- check-sync.ps1 检查双份 skill 文件是否漂移

## 适用场景

- 让 Codex 按统一工作流约束生成代码
- 在 Claude 项目中复用同一套代码生成规范
- 校验两套平台 skill 文件的一致性

## 场景标签

`代码生成` `提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L3: 是一套供 Codex 和 Claude 共用的代码生成工作流约束 skill 😂
> L20: 给 Codex 使用时，直接把这个仓库作为 skill 来源，并读取 `SKILL.md`。

## 星数曲线

```mermaid
xychart-beta
    title "lunashia/code-generation-skill 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-30", "2026-10-31"]
    y-axis "stars" 15 --> 18
    line [16, 17, 17]
```

2026-10-18 16 → 2026-10-31 17（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `49e9b7e2f4f6` · [字段定义](../../DATASET.md)*
