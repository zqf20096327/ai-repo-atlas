# MK27MK/no-bs-skills

⭐ 15 · Python · MIT · 推送 2026-09-25 · [GitHub](https://github.com/MK27MK/no-bs-skills) · 个人维护

**面向实用主义程序员的 agent 技能集（7 个 Claude Code 技能）**

遵循 Agent Skills 格式的技能合集，每个技能是 skills/ 下的一个文件夹，可通过 npx skills CLI、Claude Code 插件市场或手工复制安装，兼容 Claude Code、Codex、Cursor、OpenCode 等读取技能目录的 agent。技能分三类：编码类（fill-the-gaps 半成品填空、add-didactic-comments 教学注释）、非编辑类（answer-as-type 按类型作答、no-bs-answer 直接答案）、行为类（just-do-it 只做被要求的事、back-your-claims 每条声明附链接）。其中三个技能带测试（共 204 次 headless Claude Code 运行），结果限于 Claude Code 与单一模型。

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

- 7 个技能覆盖半成品填空、按类型作答、计划生成与答案溯源等场景
- 支持 npx skills CLI、Claude Code 插件市场、手工复制三种安装方式
- 3 个技能附对照测试（34 任务 x 204 次运行），原始结果全部公开在 tests/

## 适用场景

- 写出函数签名与空类骨架，让 agent 补齐实现
- 问一个精确问题只要一个精确答案（如返回 int）
- 要求 agent 的每条结论附可靠来源链接

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L26: The skills follow the Agent Skills format. Each one is a folder
> L32: npx skills add MK27MK/no-bs-skills
> L57: |Claude Code|`.claude/skills/`|`~/.claude/skills/`|

## 星数曲线

```mermaid
xychart-beta
    title "MK27MK/no-bs-skills 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `7199040518ed` · [字段定义](../../DATASET.md)*
