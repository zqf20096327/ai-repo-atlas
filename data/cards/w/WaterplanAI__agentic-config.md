# WaterplanAI/agentic-config

⭐ 31 · Python · MIT · 推送 2026-07-23 · [GitHub](https://github.com/WaterplanAI/agentic-config) · 组织维护

**项目无关的组合式 AI 工作流配置：pi 包与 Claude Code 插件**

以 pi 包和 Claude Code 插件形式分发的集中式配置系统，提供 7 个插件共 42 个技能，覆盖 spec 工作流与 pimux 编排、Git 自动化、QA/E2E 测试、工具集成、元提示、安全防护与审计日志。技能之间可互相调用形成组合自动化，宣称可在任意代码库不作修改地使用。安装通过 pi install git ref 或 claude plugin marketplace 完成，npm 发布为未来计划；计划扩展到 Cursor、Codex CLI 等更多工具。MUX 工作流建议以跳过权限方式运行 Claude Code。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 7 个插件、42 个技能，覆盖工作流/Git/QA/安全/审计
- 技能可互相调用，形成组合式自动化
- pi 包与 Claude Code 插件双分发渠道
- pimux tmux 控制平面支持 scout/planner/worker 编排

## 适用场景

- 在任意代码库中统一部署 AI 编码代理的工作流配置
- 团队通过固定 git tag 的 .pi/settings.json 做可复现的配置分发
- 为 Claude Code 代理增加 Git 自动化、QA 测试与安全防护技能

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L3: Project-agnostic, composable AI workflow automation via pi packages and Claude Code plugins.
> L70: A centralized configuration system shipped as pi packages and Claude Code plugins.
> L78: 3. **Native distribution surfaces** -- pi via `pi install`; Claude Code via `claude plugin install`

## 星数曲线

```mermaid
xychart-beta
    title "WaterplanAI/agentic-config 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-26 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `19594b476e56` · [字段定义](../../DATASET.md)*
