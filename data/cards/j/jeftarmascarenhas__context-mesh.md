# jeftarmascarenhas/context-mesh

⭐ 39 · MIT · 推送 2026-01-27 · [GitHub](https://github.com/jeftarmascarenhas/context-mesh) · [官网](https://context-mesh.org) · 个人维护

**AI 辅助开发的三步上下文管理框架：Intent→Build→Learn**

一套以 Markdown 文件与提示词包形式提供的上下文管理框架，围绕 Intent（先写目标/原因/验收标准与决策记录 ADR）→ Build（AI 生成、人监督）→ Learn（交付后回写上下文）三步组织 AI 辅助开发流程。产物是存于仓库、随 Git 版本化的 context/ 目录与 AGENTS.md，通过复制粘贴 prompt-packs 中的提示词到 Cursor、Copilot、Claude 等 AI 编码助手中使用，框架本身与工具无关，无需安装软件。附带与 Scrum/Kanban 集成的说明文档及示例。

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

- Intent→Build→Learn 三步流程与最小结构（intent + 决策记录 ADR）
- prompt-packs 提示词包支持新项目与既有项目两种初始化路径
- 上下文以 Markdown 文件存于仓库，随 Git 版本化
- 声明与 Cursor、GitHub Copilot、Claude、ChatGPT 等任意 AI 编码助手配合使用

## 适用场景

- 在引入 AI 编码助手前为项目建立意图与决策记录
- 防止 AI 生成代码的背景理由随时间丢失，便于后续维护
- 为新成员入职与既有代码库生成活文档

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L25: Context Mesh is a simple 3-step framework that **standardizes AI-assisted development** by planning first and prese
> L111: 3. **Paste** into your AI assistant (Cursor, Copilot, Claude, etc.)
> L205: - ✅ Any AI coding assistant

## 星数曲线

```mermaid
xychart-beta
    title "jeftarmascarenhas/context-mesh 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 38 --> 40
    line [39, 39]
```

2026-10-18 39 → 2026-10-25 39（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `a1a9016f10c4` · [字段定义](../../DATASET.md)*
