# norton77930/understanding-ai-outputs

⭐ — · [GitHub]() · 个人维护 · 中文 README

**面向 Claude Code 等 agent 的技能集：把 LLM 输出转为 STE 文本、图表、网页与讲解视频**

提供四个 agent 技能，按 Karpathy 提出的格式阶梯将 LLM 回答转换为四种形式：STE 简明文本（ste-writing）、Mermaid/SVG 图表（diagram-explainer）、自包含交互 HTML 页面（html-explainer）与带旁白字幕的 MP4 讲解视频（video-explainer）。每个技能仅在用户点名格式时启动；机制上由模型负责设计，脚本负责校验（长标签、渲染检查、字幕对齐），并以盲评方式持续测试，结果存于 evals 目录。支持 Claude Code 插件安装及通过 vercel-labs/skills 用于 Codex、Cursor。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四种输出格式各对应一个独立技能，按需单独安装
- 脚本化校验：标签检查、390px/1280px 与明暗模式渲染检查、字幕与旁白比对
- 每个技能通过 20 条查询的触发测试，盲评结果与损失记录公开
- 视频旁白支持离线英文（Kokoro）与繁体中文（edge-tts）

## 适用场景

- 让 agent 把冗长的技术回答改写为 STE 简明文本
- 为流程或概念自动生成可渲染的图表
- 把一个概念做成无需构建即可双击打开的交互讲解页
- 生成 3b1b 风格的短讲解视频并附字幕

## 场景标签

 · 领域:AI 生态/agent 技能

## 证据(README 行号)

> L11:  Four agent skills that follow the format ladder from Andrej Karpathy's
> L16:  Works with Claude Code, Codex, Cursor
> L63: **Claude Code** (all four skills):

## 星数曲线

```mermaid
xychart-beta
    title "norton77930/understanding-ai-outputs 星数(近 2 点)"
    x-axis ["2026-11-02", "2026-11-21"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-02 3 → 2026-11-21 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `ab14173746d9` · [字段定义](../../DATASET.md)*
