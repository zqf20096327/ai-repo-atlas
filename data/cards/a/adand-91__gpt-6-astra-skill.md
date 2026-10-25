# adand-91/gpt-6-astra-skill

⭐ 124 · Python · MIT · 推送 2026-09-16 · [GitHub](https://github.com/adand-91/gpt-6-astra-skill) · 个人维护 · 中文 README

**面向 Codex 的项目接管与 Skill 适配插件工具**

面向 OpenAI Codex 的插件与 Python CLI 组合：插件层提供 Skill 工作流（项目接管、进度回顾、需求变更、阻塞诊断等六个项目管理场景的报告），CLI 层（requirement-ledger）提供证据绑定审计，包括源包生成、SHA-256 字节绑定与只读交接核验。插件本身无独立运行时、无网络客户端与遥测；CLI 仅使用 Python 标准库，不运行项目代码或修改工作树。通过 git clone 后以 codex plugin 命令安装，核心用 uv tool / pip 从本地安装。

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

- Codex 插件形式提供六个项目管理场景的决策报告（目标/阶段/阻塞/下一步）
- 证据绑定审计链：源包 + SHA-256 精确绑定 + 只读交接核验
- 插件为薄 Skill 分发层，无第二运行时/遥测/网络客户端
- CLI 仅依赖 Python 标准库，不运行项目代码或修改工作树

## 适用场景

- 长期 AI 辅助项目中恢复目标、阶段与阻塞并给出下一步行动
- 审查并最小化修改因模型行为变化而过时的 Skill 约束
- 生成可复现、可交接的项目审计报告

## 场景标签

 · 领域:开发者工具/Agent 工作流

## 证据(README 行号)

> L3: ### Adapt your Skills to GPT-6/Astra. Build toward Jarvis.
> L17: and CLI remain as compatibility entry points during migration. The current plugin is a thin Skill workflow;
> L158: - The plugin is a thin, skills-only Codex distribution layer. Deterministic schemas, privacy
> L179: The repository-local plugin is a thin Skill distribution layer with no second runtime, app, hook, plugin-owned

## 星数曲线

```mermaid
xychart-beta
    title "adand-91/gpt-6-astra-skill 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-25"]
    y-axis "stars" 122 --> 125
    line [123, 124, 124]
```

2026-10-18 123 → 2026-10-25 124（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `1dcb11a46580` · [字段定义](../../DATASET.md)*
