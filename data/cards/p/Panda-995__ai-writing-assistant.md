# Panda-995/ai-writing-assistant

⭐ 33 · TypeScript · AGPL-3.0 · 推送 2026-10-17 · [GitHub](https://github.com/Panda-995/ai-writing-assistant) · 个人维护 · 中文 README

**面向创作者的 AI 写作助手：纠错润色、评分与全文重写**

基于 React 18 + TypeScript + Vite 构建的 Web 写作辅助应用：接入 Google Gemini（默认，@google/genai SDK）或 OpenAI 兼容接口，提供五维量化评分（总分/可读性/逻辑性/情感共鸣/创意度）、错别字与语法纠错润色、D3.js 逻辑结构树状图、标题传播潜质分析与替代标题生成、保留原意的全文重写，并支持导出 Word 文档。API Key 可在界面配置或经环境变量注入；提供 Dockerfile + Nginx 一键容器化部署。AGPL-3.0 协议。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 五维量化评分体系与智能纠错润色
- D3.js 生成文章逻辑树状图
- 爆款标题分析与替代标题生成
- 支持 Gemini/OpenAI 切换并可自定义 Base URL 与模型名称

## 适用场景

- 写作后对文章做多维度评分与纠错润色
- 查看文章论点与论据的逻辑层次结构
- 生成候选标题并获得全文优化版本

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L3: **妙笔生花** 是一款基于 Google Gemini 和 OpenAI 技术的现代化智能写作辅助工具。它能够深度分析文章内容，提供从基础纠错到逻辑重构的全方位建议，帮助创作者打磨出更优质的内容。
> L13: * **全方位评分体系**：从总分、可读性、逻辑性、情感共鸣、创意度五个维度对文章进行量化评估。
> L18: * **多模型支持**：默认支持 **Google Gemini (Flash/Pro)**，兼容 **OpenAI (GPT-4o)** 及其他兼容接口。

## 星数曲线

```mermaid
xychart-beta
    title "Panda-995/ai-writing-assistant 星数(近 2 点)"
    x-axis ["2026-10-19", "2026-10-30"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-19 33 → 2026-10-30 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `8cfedea292cf` · [字段定义](../../DATASET.md)*
