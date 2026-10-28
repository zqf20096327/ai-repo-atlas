# wagtail/wagtail-ai

⭐ 205 · Python · MIT · 推送 2026-08-12 · [GitHub](https://github.com/wagtail/wagtail-ai) · [官网](https://wagtail-ai.readthedocs.io/latest) · 组织维护

**给 Wagtail CMS 用户的 AI 内容辅助插件**

面向 Wagtail（基于 Django 的 CMS）的集成插件，通过 LLM API 协助内容编辑：生成页面标题与 meta 描述建议、为图片生成标题/描述/alt 文本、提供内容改进反馈、拼写语法纠正、文本续写，并基于向量嵌入建议相关页面。默认接入 OpenAI 模型（gpt-3.5-turbo，需 API key，README 给出 token 成本估算），也支持本地模型、Mistral、Claude 等多种 LLM 提供方，允许自定义提示词。要求 Wagtail 7.1+、Django 5.2+、Python 3.11+。

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

- 生成页面标题/meta 描述与图片标题/描述/alt 文本建议
- 提供内容定性反馈与拼写语法纠正、文本续写
- 基于向量嵌入按语义相似度建议相关页面
- 支持多 LLM 提供方（OpenAI、Mistral、Claude、本地模型）及自定义提示词

## 适用场景

- 在 Wagtail 后台编辑页面时生成 SEO 标题与描述
- 为上传图片批量生成 alt 文本
- 让 AI 检查并纠正内容的拼写与语法

## 场景标签

`AI 写作` `语义搜索` · 领域:内容生成

## 证据(README 行号)

> L11: Wagtail AI integrates Wagtail with AI's APIs (think ChatGPT) to help you write and correct your content.
> L20: * Work with multiple LLM providers including local models, OpenAI, Mistral, Claude and many others
> L79: * Wagtail 7.1+

## 星数曲线

```mermaid
xychart-beta
    title "wagtail/wagtail-ai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 204 --> 206
    line [205, 205]
```

2026-10-18 205 → 2026-10-28 205（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `a653c3809540` · [字段定义](../../DATASET.md)*
