# Green-PT/honey-for-devs

⭐ 342 · JavaScript · MIT · 推送 2026-10-18 · [GitHub](https://github.com/Green-PT/honey-for-devs) · [官网](https://github.com/Green-PT/honey-for-devs) · 个人维护

**压缩 AI 编程 agent 输出 token 的跨工具编码技能**

GreenPT 开发的跨工具编码技能（skill）：通过三条规则让 AI 编程 agent 输出更少代码（YAGNI 阶梯）、更少散文（先给答案）以及更紧凑的 agent 间交接格式，以降低 token 消耗与 API 成本。带自动强度分级（lite/full/ultra）、安全豁免清单（认证、迁移、删除等不压缩）与按需卫星技能。兼容 Claude Code、Cursor、Copilot、Codex、Gemini CLI 等约 18 种平台，基准报告称输出 token −40%、成本 −31%，并附外部任务集的保守数据。MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三条杠杆：更少代码、更少散文、更紧凑 agent 间交接格式
- 自动强度分级 lite/full/ultra，无需推理 token 决策
- 安全豁免：输入校验、错误处理、认证、迁移等不压缩
- 兼容约 18 种 AI 编程工具，含 Claude Code 插件市场安装

## 适用场景

- 降低 AI 编程 agent 的 token 用量与 API 账单
- 让 agent 间交接用紧凑格式而非冗长文档
- 在保持测试通过率的前提下压缩代码输出

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L7: cross-tool coding skill that cuts the output tokens AI coding agents spend —
> L9: with **Claude (claude.ai and the API), Claude Code, Cursor, GitHub Copilot, Codex, Gemini CLI, Windsurf, Cline,

## 星数曲线

```mermaid
xychart-beta
    title "Green-PT/honey-for-devs 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-23"]
    y-axis "stars" 336 --> 343
    line [337, 341, 342]
```

2026-10-18 337 → 2026-10-23 342（+5）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `05b672f2ef5e` · [字段定义](../../DATASET.md)*
