# LeeJuOh/claude-code-zero

⭐ 53 · Python · MIT · 推送 2026-10-13 · [GitHub](https://github.com/LeeJuOh/claude-code-zero) · 个人维护

**Claude Code 插件市场：9 个插件扩展 agent 技能与工作流**

面向 Claude Code 用户的插件市场，收录 9 个插件：codex-advisor 将代码与计划发给 Codex 做跨模型复核并对结果做事实核查、vision-powers 生成交互式 HTML/Markdown 分析报告、skill-creator-pro 提供技能起草-测试-优化循环与基准查看器、worktree-plus 改进 git worktree 的文件同步与安全移除，另有 NotebookLM 查询、终端分屏编排、密钥提取等工具。通过 Claude Code 插件市场命令或 npx skills CLI 安装，后者不含 hooks/agents/MCP servers，部分插件功能受限。

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

- codex-advisor 跨模型二次意见并对返回结果按 Agreed/Disputed/Nuanced 等分级核查
- vision-powers 将分析渲染为交互式 HTML 报告并在交付前回读图像检查布局
- skill-creator-pro 提供技能描述-触发优化与自动爬山优化
- 9 个插件经插件市场命令或 npx skills CLI 安装

## 适用场景

- 为 Claude Code 增加跨模型代码复核与报告生成能力
- 改进 Claude Code 的 worktree 工作流与本地文件同步
- 在 Claude Code 内直接查询 NotebookLM 笔记本

## 场景标签

`精选清单` · 领域:学习与行业

## 证据(README 行号)

> L5: > A plugin marketplace I built from what I needed while using Claude Code.
> L16: Full install: skills, hooks, agents, MCP servers, scripts — everything the plugin ships.
> L23: /plugin install <plugin-name>@claude-code-zero

## 星数曲线

```mermaid
xychart-beta
    title "LeeJuOh/claude-code-zero 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-31"]
    y-axis "stars" 51 --> 54
    line [52, 53, 53]
```

2026-10-18 52 → 2026-10-31 53（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `5d2273dba153` · [字段定义](../../DATASET.md)*
