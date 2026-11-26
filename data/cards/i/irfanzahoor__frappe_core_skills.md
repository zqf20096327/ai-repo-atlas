# irfanzahoor/frappe_core_skills

⭐ 9 · MIT · 推送 2026-11-25 · [GitHub](https://github.com/irfanzahoor/frappe_core_skills) · 个人维护

**为 Claude Code 提供 Frappe/ERPNext v14–v16 编码规范技能包**

将 Frappe 编码规范与 v14–v16 版本差异整理为 22 个按任务分支加载的 Markdown 技能，覆盖核心规范、Server Script 沙箱、报表、性能、升级、调试、测试与运维等。以 Claude Code 插件形式分发，包含 4 个 agent 与 3 个斜杠命令（仅 Claude Code 可用）；技能为纯 Markdown，不执行脚本、不联网、不收集数据，兼容手动复制到其他 AI 编码工具。声明技能仅起引导作用，不保证输出正确。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 22 个按任务分支加载的技能，会话开始仅加载 22 行描述以节省 token
- 4 个 agent（reviewer/migrator/builder/doctor）与 3 个斜杠命令，仅限 Claude Code 插件安装方式
- 提供 v14/v15/v16 功能兼容性对照表与升级检查命令
- 技能为纯 Markdown，可复制到 Codex/Cursor/Gemini/Copilot 使用

## 适用场景

- 让 AI 助手按 Frappe 规范写代码而非套用通用 Python 写法
- 规划或执行 Frappe v14 到 v15/v16 的版本升级
- 对 Frappe 项目做代码评审与安全审计
- 排查 Server Script 报错、慢查询与调度任务问题

## 场景标签

`编码 Agent` `代码审查` · 领域:编码与开发

## 证据(README 行号)

> L7: The best parts of **frappe-code-standards** (code placement, standard APIs) and
> L20: **Tokens:** at session start only 22 one-line descriptions load. A skill's body loads only when
> L156: The skills are plain Markdown. They run no scripts, make no network calls and collect no data.


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `9d73cad59690` · [字段定义](../../DATASET.md)*
