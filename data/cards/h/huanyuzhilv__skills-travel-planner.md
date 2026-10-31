# huanyuzhilv/skills-travel-planner

⭐ 16 · HTML · MIT · 推送 2026-06-01 · [GitHub](https://github.com/huanyuzhilv/skills-travel-planner) · [官网](https://huanyuzhilv.github.io/skills-travel-planner/) · 个人维护 · 中文 README

**面向定制游顾问与 Agent 的 AI 路书/行程单生成 Skill**

以 Cursor / Claude Code / Codex Agent Skill 形式提供的路书生成工具：读取 txt/docx 简版行程，转为结构化 tripData.json，再经 deliver_roadbook_v2.py 一键生成客户可交付的 HTML 路书（可导出 PDF/长图）。配图通过 TikHub 小红书搜索、飞猪 FlyAI 与 Wikimedia 兜底；每日正文与亮点文案可用 OpenAI 或 DeepSeek LLM 润色（可选）。需要 .env 配置 API key，MIT 开源可 fork。

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

- txt/docx 行程 → tripData.json → 交付级 HTML/PDF 路书的一键流水线
- 小红书（TikHub）+ 飞猪 FlyAI + Wikimedia 自动配图，strict https 校验
- 可选 OpenAI / DeepSeek LLM 文案润色
- install.sh 安装为 Claude Code / Codex 的 Agent Skill

## 适用场景

- 定制游顾问把简版行程表快速做成客户可交付路书
- 在 Cursor / Claude Code 中以 Agent Skill 方式生成行程文档
- 为路书自动配小红书图片与酒店简介

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L7: 面向定制游顾问与 **AI Agent（Cursor / Claude Code / Codex）** 的专业 **路书（Roadbook）生成 Skill**。
> L21: |**Agent 集成**|Cursor / Claude Skill 原生|无 Skill 规范|无|无|

## 星数曲线

```mermaid
xychart-beta
    title "huanyuzhilv/skills-travel-planner 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `26ca091054c6` · [字段定义](../../DATASET.md)*
