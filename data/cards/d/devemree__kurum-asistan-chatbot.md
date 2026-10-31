# devemree/kurum-asistan-chatbot

⭐ 14 · Python · 推送 2026-08-09 · [GitHub](https://github.com/devemree/kurum-asistan-chatbot) · 个人维护

**企业内部 Flask 聊天助手：知识库问答、工单与文档问答**

Flask 编写的内部助理聊天应用：集成内部知识库问答、支持工单创建与仪表盘跟踪、PDF/DOCX 文档上传、摘要与向量检索问答。通过 OpenAI 兼容 API（如 LM Studio）提供对话与嵌入，可用 Ollama 作聊天提供方，按用户会话选择模型，切换提供方后需重建向量库。安装方式为源码运行：创建虚拟环境、pip 安装依赖、配置 .env 后启动 app.py。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 内部知识库问答与文档向量检索（PDF/DOCX 上传、摘要、搜索）
- 支持工单创建与仪表盘跟踪
- LM Studio / Ollama 双提供方，嵌入模型随提供方切换
- 按用户会话选择活动模型

## 适用场景

- 团队内部搭建知识库问答助手
- 在对话中创建并跟踪支持工单
- 上传公司文档做问答与摘要

## 场景标签

`聊天机器人` `文档问答` · 领域:对话与助手

## 证据(README 行号)

> L3: This Flask project brings together internal knowledge base lookups, support ticket creation, and document question-a
> L7: - Answer questions from the internal knowledge base
> L9: - Upload, summarize, and search PDF and DOCX files

## 星数曲线

```mermaid
xychart-beta
    title "devemree/kurum-asistan-chatbot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `aaf7ba6ee4fa` · [字段定义](../../DATASET.md)*
