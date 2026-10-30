# Tahirpathan-AiLab/Athena_RAG_Intelligence

⭐ 22 · JavaScript · MIT · 推送 2026-10-18 · [GitHub](https://github.com/Tahirpathan-AiLab/Athena_RAG_Intelligence) · [官网](https://mrtahirpathan.netlify.app/) · 个人维护

**基于 RAG 的文档智能问答平台，含语音助手与分析面板**

面向终端用户的文档智能平台：用户上传 PDF 后系统自动切分语义块、生成向量嵌入并索引；提问时先做语义相似度检索，再将上下文发送给 Grok 语言模型生成回答，每条回答附带来源引用与相似度分数。另提供知识库浏览、带 FluidGlob 动画的语音助手、分析面板（文档/嵌入/存储/查询趋势/响应性能）、持久化聊天记录与深浅色主题。前端 React+Vite，后端 FastAPI。README 未给出安装与运行命令，API 需自行配置。

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

- PDF 上传→语义分块→向量嵌入→检索的 RAG 流水线
- 回答附带来源引用与相似度分数
- 语音助手（FluidGlob 动画界面）与分析面板
- React+Vite 前端与 FastAPI REST 后端

## 适用场景

- 上传自己的 PDF 文档并进行带出处的问答
- 管理和浏览已索引的文档知识库
- 通过仪表盘查看文档、嵌入与查询使用情况

## 场景标签

`文档问答` · 领域:知识与检索

## 证据(README 行号)

> L3: This project is an **AI-powered document intelligence platform** built using **Retrieval-Augmented Generation (RAG)*
> L9: The chat interface enables users to ask questions in natural language. Instead of relying only on the language model

## 星数曲线

```mermaid
xychart-beta
    title "Tahirpathan-AiLab/Athena_RAG_Intelligence 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-29", "2026-10-30"]
    y-axis "stars" 20 --> 23
    line [21, 22, 22]
```

2026-10-18 21 → 2026-10-30 22（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `7784ea2899e5` · [字段定义](../../DATASET.md)*
