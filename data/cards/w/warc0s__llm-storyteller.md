# warc0s/llm-storyteller

⭐ 17 · Python · MIT · 推送 2026-06-18 · [GitHub](https://github.com/warc0s/llm-storyteller) · 个人维护

**面向写作者的三步式 LLM 故事生成 Streamlit 应用**

基于 Streamlit 的交互式 Web 应用，面向学生、写作者与爱好者生成故事。核心机制是将 LLM 提示拆为三步流水线：先生成结构化大纲，再据大纲撰写叙事，最后做语法与连贯性润化；每步可选不同模型。本地版要求两个 OpenAI 兼容模型运行于 localhost:7860，默认适配 Llama 1B / Qwen 1.5B 等 CPU 小模型；另有接入 OpenRouter 免费模型的在线版本部署于 Streamlit Cloud。支持温度、叙事风格（悬疑/科幻/爱情/奇幻/喜剧）、语言与长度等参数，故事可导出 txt。应用界面为西班牙语。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 大纲→写作→润化的三步引导式生成流程，针对小模型优化
- 本地 OpenAI 兼容端点（默认 localhost:7860）与 OpenRouter 在线版两种运行方式
- 可分步选择不同模型、调节温度、指定语言/风格/长度
- 生成结果一键下载为 txt 文件

## 适用场景

- 输入角色、地点、关键动作等要素快速生成完整故事
- 为大纲、写作、润化各步骤搭配不同模型获得更好的结果
- 无 GPU 环境下用 CPU 小模型本地生成故事

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L8: Welcome to **LLM StoryTeller**, an interactive web application that leverages Large Language Models (LLMs) to help y
> L26: LLM StoryTeller is a Streamlit-based application designed to assist users in creating engaging stories through the 
> L28: To ensure the application functions correctly, you need to have two OpenAI-compatible language models running local

## 星数曲线

```mermaid
xychart-beta
    title "warc0s/llm-storyteller 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-31 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `a45dc595f694` · [字段定义](../../DATASET.md)*
