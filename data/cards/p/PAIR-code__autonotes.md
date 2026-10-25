# PAIR-code/autonotes

⭐ 45 · TypeScript · Apache-2.0 · 推送 2026-06-19 · [GitHub](https://github.com/PAIR-code/autonotes) · [官网](https://pair-code.github.io/autonotes/) · 组织维护

**AI 笔记应用原型：自动打标签、摘要与对话式问答**

PAIR-code（Google）发布的实验性 AI 笔记应用原型：支持导入/新建 Markdown 笔记并通过 Gemini API 自动打标签、生成标签摘要与 Highlights 回顾，提供基于笔记的 Chat 问答（可查看引用笔记、保存回答为新笔记）。可导入 Obsidian Markdown 与 Google Keep JSON。纯客户端实现，数据存于浏览器本地存储，AI 功能需自备 AI Studio Gemini API key（仅限部分地区可用）。提供在线试用与本地 npm 运行方式，Apache 2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Gemini 驱动的笔记自动打标签与摘要生成
- Chat with your notes：回答可查看引用笔记并可保存为新笔记
- 支持导入 Obsidian Markdown 与 Google Keep JSON
- 客户端本地存储，官方声明数据不上传服务器

## 适用场景

- 整理个人笔记并自动生成层级标签与摘要
- 对自己的笔记提问并追溯回答出处
- 导入 Obsidian/Google Keep 既有笔记做 AI 归纳

## 场景标签

`知识库管理` `文档问答` · 领域:知识与检索

## 证据(README 行号)

> L3: AutoNotes is a experimental prototype for AI-powered notetaking.
> L101: AutoNotes uses Gemini Pro via the AI Studio Gemini API to tag notes, respond
> L117: AutoNotes is a client-side experiment: any data you save is kept in local

## 星数曲线

```mermaid
xychart-beta
    title "PAIR-code/autonotes 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 44 --> 46
    line [45, 45]
```

2026-10-18 45 → 2026-10-25 45（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `9d9216512fcb` · [字段定义](../../DATASET.md)*
