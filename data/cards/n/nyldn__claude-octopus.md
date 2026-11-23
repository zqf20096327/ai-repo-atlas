# nyldn/claude-octopus

⭐ 4,485 · Shell · MIT · 推送 2026-11-19 · [GitHub](https://github.com/nyldn/claude-octopus) · [官网](https://reddit.com/r/ClaudeOctopus/) · 个人维护

**Claude Code 多模型协同插件：并行多模型审查并标记分歧**

以 Claude Code 插件形式安装的多模型编排工具，也支持作为 Codex 插件与 Cursor 的 MCP server 运行。接入最多 12 个外部模型提供方，对同一研究、设计或编码任务获取多个模型意见，用 75% 共识门标记发布前的分歧。包含 31 个角色化 persona、56 个命令、64 个技能；默认休眠，仅显式 /octo:* 调用。要求 Claude Code v2.1.14+，支持 Linux/macOS 原生，Windows 经 WSL 或 SSH。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 接入 12 个外部提供方并内置 Claude Code 宿主，零外部提供方即可启动
- 75% 共识门在发布前标记多模型分歧
- 31 personas / 56 命令 / 64 技能，默认休眠需显式调用
- 同时支持 Claude Code 插件、Codex 插件与 Cursor MCP server 三种接入形态

## 适用场景

- 发布前让多个模型交叉审查代码改动并暴露分歧
- 以规格输入驱动从研究到交付的自动化流水线，人工只审产出
- 在 Claude Code、Codex 或 Cursor 中复用同一套多模型工作流

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L3: Every AI model has blind spots. Claude Octopus supports twelve external provider integrations — Codex, Antigravity C
> L17: 🐙 **Research, build, review, and ship — with twelve external providers checking the host's work.** Claude-native ha

## 星数曲线

```mermaid
xychart-beta
    title "nyldn/claude-octopus 星数(近 28 点)"
    x-axis ["2026-10-21", "2026-10-22", "2026-10-23", "2026-10-24", "2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23"]
    y-axis "stars" 4242 --> 4507
    line [4264, 4271, 4281, 4291, 4300, 4302, 4309, 4316, 4325, 4330, 4336, 4346, 4350, 4300, 4413, 4429, 4433, 4436, 4441, 4442, 4445, 4452, 4464, 4471, 4473, 4482, 4484, 4485]
```

2026-10-21 4,264 → 2026-11-23 4,485（+221）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `af0238700529` · [字段定义](../../DATASET.md)*
