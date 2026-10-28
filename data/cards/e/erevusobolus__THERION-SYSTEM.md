# erevusobolus/THERION-SYSTEM

⭐ 30 · AGPL-3.0 · 推送 2026-06-09 · [GitHub](https://github.com/erevusobolus/THERION-SYSTEM) · [官网](https://erevus.space) · 个人维护

**67 专家角色的 AI 行为规则文件集，供任意 AI 编辑器加载**

由 SOUL.md、AGENTS.md、USER.md、MEMORY.md 四个纯文本文件组成的行为系统：放入项目根目录后，VS Code、Cursor、Windsurf、Claude Code 等 AI 编辑器可自动检测并加载。核心机制为关键词扫描→领域匹配→按需加载单个专家文件的路由方式，宣称包含 67 个跨 12 个领域的专家角色、11 条行为规则与跨会话记忆。通过 git clone 获取，以 'WAKE UP THERION' 一句话激活；AGPL 许可，无付费组件。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四个纯文本文件（SOUL/AGENTS/USER/MEMORY）构成，无任何可执行代码
- 关键词扫描→领域匹配→按需加载单个领域文件的路由机制
- 宣称 67 个专家角色、12 个领域、100+ 内置技能与工具
- 声明兼容任意模型与平台（Claude、Gemini、Mistral、Llama 等）

## 适用场景

- 在 Cursor/VS Code 等 AI 编辑器中加载专家角色与行为规则
- 减少 AI 回复中的冗长前言与碎片化输出
- 跨会话保持用户偏好与项目上下文

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L42: **2. Drop** — Place the THERION files at the root of any project folder. Open it in any AI-powered editor — VS Code
> L148: - **Any AI Tool** — Claude, Gemini, Mistral, Llama — any model. VS Code, Cursor, Windsurf, Claude Code — any platf
> L199: |**AGENTS.md**|Expertise. 67 specialists across 12 fields. Your AI detects what you need and activates the right k

## 星数曲线

```mermaid
xychart-beta
    title "erevusobolus/THERION-SYSTEM 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-28 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 low · 依据 README sha `3b1dab0d5c8b` · [字段定义](../../DATASET.md)*
