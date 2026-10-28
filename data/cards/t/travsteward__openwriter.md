# travsteward/openwriter

⭐ 36 · TypeScript · MIT · 推送 2026-10-27 · [GitHub](https://github.com/travsteward/openwriter) · [官网](https://openwriter.io) · 个人维护

**面向 AI agent 协作的 Markdown 编辑器，人工审批 agent 改动**

Markdown 原生的富文本编辑器，定位为人类与编码类 agent（Claude Code、Cursor、Codex 等 MCP 兼容 agent）并肩写作的界面：agent 通过 MCP server 的 24 个工具读写文档，改动以彩色标记形式呈现，用户逐条接受或拒绝。文档为磁盘上的纯 .md 文件，无数据库与专有格式。提供工作区、版本历史、Git 同步与导出（Markdown/HTML/Word/PDF）。通过 npx 安装 skill 与 MCP server，或 npm 全局安装单独运行于 localhost:5050。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- MCP 协作的 24 个文档编辑工具，兼容任意 MCP agent
- pending-change 逐条审批（绿增/蓝改/红删，快捷键接受或拒绝）
- 文档为磁盘纯 .md 文件，无数据库与专有格式
- 右键写作动作（Enhance/Shrink/Expand）使用自有 Claude API key 并学习个人文风

## 适用场景

- 让 Claude Code 等 agent 代写文档，自己逐条审阅改动
- 在无锁定的纯 Markdown 文件上组织多文档写作项目
- 编辑器内直接推送文档到 GitHub 并保留版本历史

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L7: OpenWriter is a markdown-native rich text editor built for humans and agents working side by side. Your agent writes
> L15: Every writing tool is racing to bolt on its own weak agent. They have it backwards. The strongest agents already ex

## 星数曲线

```mermaid
xychart-beta
    title "travsteward/openwriter 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-28"]
    y-axis "stars" 34 --> 37
    line [35, 36, 36]
```

2026-10-18 35 → 2026-10-28 36（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `b248b5653c4e` · [字段定义](../../DATASET.md)*
