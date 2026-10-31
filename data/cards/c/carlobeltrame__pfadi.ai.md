# carlobeltrame/pfadi.ai

⭐ 13 · PHP · MIT · 推送 2026-10-22 · [GitHub](https://github.com/carlobeltrame/pfadi.ai) · [官网](https://pfadi.ai) · 个人维护

**瑞士童军 AI 工具集：生成活动方案与营地计划**

面向瑞士童军的 AI 用例与展示集合，含多个工具：pfadinamen.app 用浏览器内 tensorflow.js 运行 char-rnn 生成童军昵称；samstag/LS/LA/kursblock 是基于 GPT-4o 的 LLM 链，通过少样本示例与多次调用链生成周活动故事、营地计划与课程目标，kursblock 还结合检索增强生成；cudesch（当前不可用）为基于 Supabase 向量库的 PDF 语义搜索。工具仅支持瑞士德语。PHP 后端认证 OpenAI API key 并流式返回结果，可自托管于共享 PHP 主机。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- char-rnn 在浏览器内通过 tensorflow.js 运行，无托管与推理成本
- 基于 GPT-4o 的 LLM 链生成活动故事、营地计划与课程目标
- few-shot 示例 + 多次 LLM 调用链逐步生成内容，kursblock 采用 RAG
- cudesch：PDF 文本抽取→LLM 摘要→嵌入存入 Supabase 向量库的语义搜索

## 适用场景

- 为童军周活动生成故事与活动方案
- 为 J+S 营地生成 Lagersportblöcke 与 Lageraktivitäten 计划
- 在童军课程文献 PDF 中做语义检索
- 我想给童军起一个新颖的昵称并查看含义

## 场景标签

`RAG` `语义搜索` `AI 写作` · 领域:内容生成

## 证据(README 行号)

> L7: - **pfadinamen.app**, which is maintained in a separate repository, is a char-rnn trained on scout names, which can 
> L8: - **samstag** (code in `/samstag`) is an LLM chain (currently based on GPT-4o) for generating stories and programme 
> L28: These tools share a very similar architecture. They work by issuing a chat completion API call to the ChatGPT API (

## 星数曲线

```mermaid
xychart-beta
    title "carlobeltrame/pfadi.ai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `d9da4da1156b` · [字段定义](../../DATASET.md)*
