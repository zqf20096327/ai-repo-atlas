# sup3x/claude-code-eco

⭐ 40 · JavaScript · MIT · 推送 2026-08-16 · [GitHub](https://github.com/sup3x/claude-code-eco) · 个人维护

**Claude Code 省 token 插件：减少冗余输出与成本**

面向 Claude Code 用户的插件（MIT 许可），通过节俭规则、输出风格与可选 hooks 降低输出 token 消耗。提供 /eco 与 /eco-max 命令、Eco 输出风格、/eco-audit 配置成本审计、/eco-report 会话 token 统计、只读 eco-scout 委派 agent，以及限制命令输出/全文件写入的 enforcement hooks。基准结果附 267 次原始运行记录与 CI 复算校验；README 同时发布负结果。通过插件市场命令或 install.sh/ps1 脚本安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四类组件：/eco 节俭命令、Eco 输出风格、审计/报告命令、opt-in enforcement hooks
- 基准数字由 verify.mjs 从原始 JSON 在 CI 中复算，含 267 次运行清单与负结果发布
- /eco-audit 读取 settings.json/CLAUDE.md/MCP 配置输出成本排序（只读）
- 支持插件市场安装、install.sh/ps1 脚本安装与项目级 skills 目录三种方式

## 适用场景

- 降低 Claude Code 日常使用中的 API 账单与 token 消耗
- 审计现有 Claude Code 配置中隐性的 token 开销
- 在例行小任务上用 /eco-max 进一步压缩输出

## 场景标签

 · 领域:LLM 开发者工具

## 证据(README 行号)

> L16: /plugin marketplace add sup3x/claude-code-eco
> L29: |**`/eco`**|Frugality rules with a non-negotiable quality floor. Full reasoning depth. One invocation covers the se

## 星数曲线

```mermaid
xychart-beta
    title "sup3x/claude-code-eco 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-27"]
    y-axis "stars" 38 --> 41
    line [39, 40, 40]
```

2026-10-18 39 → 2026-10-27 40（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `6f7ddc5754c5` · [字段定义](../../DATASET.md)*
