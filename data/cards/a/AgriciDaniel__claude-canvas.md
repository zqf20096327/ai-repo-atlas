# AgriciDaniel/claude-canvas

⭐ 302 · Python · MIT · 推送 2026-04-10 · [GitHub](https://github.com/AgriciDaniel/claude-canvas) · [官网](https://agricidaniel.com/blog/claude-canvas-ai-visual-production) · 个人维护

**Claude Code 驱动的 Obsidian Canvas 可视化生产技能插件**

面向 Claude Code CLI 的技能插件：通过 /canvas 命令让 Claude 在 Obsidian Canvas 中创建和填充可视化画布，覆盖演示文稿、流程图、知识图谱、看板等 12 种模板，支持图片/文本/PDF/Mermaid/SVG 等 12 类节点，提供 6 种自动布局算法（dagre、径向、力导向等）与 PNG/SVG/PDF 导出，并可从单句描述生成整块画布（配合 /banana 等 AI 图像技能）。依赖 Obsidian v1.1+ 与 Python 3.10+，演示功能推荐 Advanced Canvas 插件。

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

- 12 种画布模板与 12 类节点内容
- 6 种自动布局算法（含 auto-detect）
- /canvas generate 从单句描述生成完整画布
- 导出 PNG/SVG/PDF，支持 Advanced Canvas 演示模式

## 适用场景

- 让 Claude 帮我在 Obsidian 里搭演示文稿、流程图或知识图谱
- 把项目资料整理成看板、时间线或对比画布
- 为游戏/创意项目生成 mood board 与配图画廊

## 场景标签

`知识库管理` · 领域:知识与检索

## 证据(README 行号)

> L5: AI-orchestrated visual production for Obsidian Canvas. Create presentations, flowcharts, mood boards, knowledge grap
> L23: claude plugin install AgriciDaniel/claude-canvas
> L40: |You say|Claude does|

## 星数曲线

```mermaid
xychart-beta
    title "AgriciDaniel/claude-canvas 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 301 --> 303
    line [302, 302]
```

2026-10-18 302 → 2026-10-22 302（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `0c5022e63d11` · [字段定义](../../DATASET.md)*
