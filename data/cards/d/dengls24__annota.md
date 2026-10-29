# dengls24/annota

⭐ 20 · Python · MIT · 推送 2026-04-17 · [GitHub](https://github.com/dengls24/annota) · [官网](https://modelcontextprotocol.io) · 个人维护 · 中文 README

**面向 Zotero 文献库的 AI 论文批注 MCP 服务器**

Annota 是一个用 Python 编写的 MCP Server，供 Claude Code 调用，读取 Zotero 文献库中的 PDF 并创建批注：高亮发现结果、解释公式、生成结构化阅读笔记、模拟审稿。提供 9 个 MCP 工具（文献检索、PDF 文本提取、创建高亮、添加笔记等）与 3 个 Claude Code 斜杠命令。采用两阶段工作流（先全文后坐标）与自动跳过参考文献以降低上下文消耗。批注通过直接写 Zotero SQLite 数据库实现，需先关闭 Zotero 并备份数据库；主要在 Windows 上测试。

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

- 9 个 MCP 工具：Zotero 检索、PDF 全文/坐标提取、批注创建、笔记添加
- 3 个 Claude Code 斜杠命令：智能批注、结构化笔记、模拟审稿
- 两阶段工作流降低 63–80% 上下文消耗，自动跳过参考文献节
- 语义化颜色约定：黄/绿/蓝/红/紫对应不同批注类型

## 适用场景

- 读论文时让 AI 高亮发现、方法、局限等关键内容
- 生成包含贡献、方法、结果、局限的结构化阅读笔记
- 让 AI 以审稿人视角输出带评分的评审意见
- 为公式和假设段落添加中文解释批注

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L1: # Annota — AI-Powered Paper Annotation Assistant
> L31: ### 9 MCP Tools
> L71: ### Step 2: Configure Claude Code

## 星数曲线

```mermaid
xychart-beta
    title "dengls24/annota 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-29 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `bd0638c4eadc` · [字段定义](../../DATASET.md)*
