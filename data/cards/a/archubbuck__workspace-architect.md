# archubbuck/workspace-architect

⭐ 19 · Python · ISC · 推送 2026-10-26 · [GitHub](https://github.com/archubbuck/workspace-architect) · 个人维护

**为 GitHub Copilot 等 AI 助手分发 400+ 专业 agent/指令/提示词的 CLI**

以 npx 直接运行的 npm CLI 工具，提供 400+ 精选的 agents、instructions、prompts、skills、hooks、plugins 与 collections 七类资产，下载为 Markdown 文件到 .github/ 目录，供 GitHub Copilot、Claude 等 AI 编码助手使用。资产集合通过同步脚本从 github/awesome-copilot 与 anthropics/skills 等上游仓库自动同步，并用 TF-IDF/余弦相似度做策展筛选。面向不想从零编写自定义指令的开发者，ISC 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | ISC |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 七类资产（agents/instructions/prompts/skills/hooks/plugins/collections）按类型下载到项目
- npx 零安装直接使用，附 wsa 短别名
- 从 github/awesome-copilot 与 anthropics/skills 上游自动同步资产
- TF-IDF/余弦相似度策展引擎维护集合相关性

## 适用场景

- 为特定技术栈快速下载现成的 Copilot agent 与指令配置
- 为 Claude/Copilot 项目添加 Skills、Hooks 等标准化资产
- 浏览并获取社区维护的领域化 prompt 与插件集合

## 场景标签

`提示工程` `精选清单` · 领域:Agent 开发

## 证据(README 行号)

> L11: Workspace Architect is a zero-friction CLI tool that provides curated collections of specialized agents, instructio
> L121: |**Skills**|Claude Skills with templates, scripts, and resources|`.github/skills/`|
> L128: **Skills** are an emerging standard for packaging AI agent capabilities. Compatible with Claude, GitHub Copilot, a

## 星数曲线

```mermaid
xychart-beta
    title "archubbuck/workspace-architect 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-28 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `b2337ea6cffb` · [字段定义](../../DATASET.md)*
