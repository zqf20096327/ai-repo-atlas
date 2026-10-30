# maxmilian/loop-engineering

⭐ 29 · Python · MIT · 推送 2026-06-24 · [GitHub](https://github.com/maxmilian/loop-engineering) · 个人维护 · 中文 README

**设计与审查自主 agent 循环的技能包（SKILL.md）**

以单个 SKILL.md 文件（YAML frontmatter + Markdown）加 references 目录形式交付的 agent 技能：为 Claude Code、Codex、Copilot CLI、Gemini CLI 等编码 agent 提供自主/半自主循环的设计模式与审查清单，内容为从 12 个公开来源提炼的七条原则（可机检的完成条件、确定性验证、退出条件预定义、上下文裁剪、文件系统作记忆、人工门控等）。安装方式为 git clone 到各工具的 skills 目录，或粘贴进任意 LLM 上下文。附 evals 目录含 11 个测试用例与结果，基准流程可复现。MIT 许可。

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

- 七条循环设计原则：触发/检查/行动/验证 + 成功/失败/预算退出与人工门控
- SKILL.md 文件夹形式，可被 Claude Code/Codex/Copilot/Gemini 自动发现加载
- 附 11 个 held-out 测试用例（evals/evals.json）与可复现的基准流程
- 对无技能加载器的工具（Cursor/Windsurf 等）提供 instructions 文件引用方式

## 适用场景

- 让编码 agent 按框架设计新的自主运行 agent 或后台任务
- 在上线前审查现有循环的停止条件、护栏与升级路径
- 诊断 token 消耗过高、无法结束的 agent 循环问题

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L54: ├── SKILL.md                          # the skill itself (frontmatter + instructions)
> L59: A skill is just a folder with a `SKILL.md` (YAML frontmatter + Markdown). That
> L161: Distilled from public writing on loop engineering, agent loops, and context

## 星数曲线

```mermaid
xychart-beta
    title "maxmilian/loop-engineering 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-30 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `059ad22f433f` · [字段定义](../../DATASET.md)*
