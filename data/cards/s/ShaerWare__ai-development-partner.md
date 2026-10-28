# ShaerWare/ai-development-partner

⭐ 19 · MIT · 推送 2026-01-20 · [GitHub](https://github.com/ShaerWare/ai-development-partner) · [官网](https://shaerware.github.io/) · 组织维护

**把 Claude/GPT 配置为全栈开发伙伴的系统提示词模板**

一套可复制的 Markdown 系统提示词（Full/Mini/Universal 三版本），将 Claude、ChatGPT 或本地 LLM 组合为系统分析师、技术负责人、项目经理与业务顾问角色；通过 /c、/tz、/plan、/cost、/review 等 slash 命令生成 CRUD 代码与测试、形成技术任务书、估算成本与 ROI、执行代码审查。默认面向 PHP/Laravel 栈，可修改技术栈段落适配 Node.js、Python 等。提供 Claude、ChatGPT、Open WebUI、VS Code(Continue) 四类平台的集成模板，安装方式即复制提示词文件并编辑项目上下文。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Full(~30KB)/Mini(~20KB)/Universal(~3KB) 三个版本的系统提示词
- slash 命令体系：/c 生成 15+ 文件的 CRUD、/tz 生成技术任务书、/cost 估算成本与 ROI
- 覆盖 Claude、ChatGPT、Open WebUI(本地 LLM)、VS Code(Continue) 的集成模板
- 技术栈通过编辑提示词中的 Context 段落适配（默认 Laravel，可改 Node.js/Python/Go）

## 适用场景

- 让 AI 助手按统一流程完成需求分析、架构与开发计划
- 通过 /c 一条命令生成带测试与文档的 Laravel CRUD
- 为项目生成技术任务书、成本与 ROI 估算
- 给本地 LLM 配备结构化的开发伙伴系统提示词

## 场景标签

`提示工程` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L21: **AI Development Partner** — это мощный системный промпт, превращающий Claude, GPT или локальные LLM в вашего **циф
> L119: * **Claude:** templates/claude/full.md
> L121: * **Open WebUI (локальные LLM):** templates/local-llm/openwebui.md

## 星数曲线

```mermaid
xychart-beta
    title "ShaerWare/ai-development-partner 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-28 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `52f50bffb2f6` · [字段定义](../../DATASET.md)*
