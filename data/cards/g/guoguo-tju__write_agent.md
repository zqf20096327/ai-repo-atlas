# guoguo-tju/write_agent

⭐ 35 · Python · MIT · 推送 2026-05-05 · [GitHub](https://github.com/guoguo-tju/write_agent) · 个人维护 · 中文 README

**面向写作者的 AI 写作助手：改写、审校、封面与微信排版**

基于 FastAPI + React/Vite 的全栈 AI 写作应用：输入源文本后按选定风格改写（100-8000 字预设、流式输出），采用草稿-审校循环（后端限制重试次数 max_retries=1），并支持从素材库做 RAG 检索与引用展示；另含封面生成、主题化微信排版一键导出，以及 GitHub/Linux.do 热点聚合供选题。模型侧通过 OpenAI 兼容 API 与火山引擎 API 接入，可选 SiliconFlow 提供 RAG 嵌入。需配置 .env 密钥并分别启动前后端运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 风格约束改写 + 草稿/审校循环（后端限制重试次数）
- 写作时对素材库做 RAG 检索并在输出上下文展示引用材料
- 封面生成（多模式多比例）与微信排版一键导出
- GitHub/Linux.do 热点聚合可一键送入素材或改写流程

## 适用场景

- 按固定风格批量改写长文并逐级审校
- 从素材库检索引用、生成可溯源的写作内容
- 生成封面并排版成微信公众号可直接粘贴的版式

## 场景标签

`AI 写作` `图像生成` · 领域:内容生成

## 证据(README 行号)

> L5: A full-stack AI writing agent for style extraction, rewriting, review, cover generation, and publishing-ready WeChat
> L11: - Productize fragmented writing actions into one standardized loop: material retrieval, style-constrained rewriting
> L23: 1. **Rewrite**: input source text, pick style, set target length (`100-8000` preset options, default `500`), stream

## 星数曲线

```mermaid
xychart-beta
    title "guoguo-tju/write_agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 34 --> 36
    line [35, 35]
```

2026-10-18 35 → 2026-10-28 35（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `4eb654773109` · [字段定义](../../DATASET.md)*
