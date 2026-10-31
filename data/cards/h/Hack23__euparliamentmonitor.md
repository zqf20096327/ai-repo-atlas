# Hack23/euparliamentmonitor

⭐ 14 · HTML · Apache-2.0 · 推送 2026-10-30 · [GitHub](https://github.com/Hack23/euparliamentmonitor) · [官网](https://euparliamentmonitor.com/) · 组织维护 · 中文 README

**AI 自动生成欧洲议会多语言新闻的开源新闻平台**

面向公众、记者与研究者的欧洲议会政治情报平台：通过 15 个 gh-aw agentic 工作流自动监测议会全体会议、委员会、动议与立法程序，产出结构化分析产物（每次运行 39/51 个模板），再由确定性聚合器渲染成 14 种语言的新闻文章并提交 PR 供人工审阅。数据经 European-Parliament-MCP-Server（60+ 工具）获取，EP API 不可用时有降级模式（USE_EP_MCP=false 可禁用 MCP）。方法论、模板与分析树全部公开可审计。以 npm/TypeScript 包形式提供，站点为纯静态部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 15 个 gh-aw agentic 工作流自动生成 14 种语言新闻文章
- 每次运行产出结构化分析产物，文章由确定性聚合器渲染、无 AI 生成 HTML 步骤
- 经 European-Parliament-MCP-Server v1.4.54 接入 60+ 欧洲议会数据工具
- 17 项方法论、170+ 每日分析运行全部公开链接可审计

## 适用场景

- 每日跟踪欧洲议会立法、委员会与投票动态的多语言新闻
- 记者/研究者核验文章背后的分析产物与方法论
- 研究 agentic 工作流驱动的自动化新闻生产管线

## 场景标签

`工作流自动化` `AI 写作` · 领域:效率与自动化

## 证据(README 行号)

> L38: This repository is the open-source platform behind **euparliamentmonitor.com**: an AI-driven newsroom that monitors
> L45: |🤖 **AI-Generated News**|14 unified gh-aw agentic workflows + 1 translation workflow run autonomously, produce stru

## 星数曲线

```mermaid
xychart-beta
    title "Hack23/euparliamentmonitor 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `3e6eb29bf1a3` · [字段定义](../../DATASET.md)*
