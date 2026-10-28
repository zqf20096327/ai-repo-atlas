# hoangsonww/DocuThinker-AI-App

⭐ 48 · JavaScript · NOASSERTION · 推送 2026-09-27 · [GitHub](https://github.com/hoangsonww/DocuThinker-AI-App) · [官网](https://docuthinker.vercel.app) · 个人维护

**AI 文档分析与摘要应用：上传文档得摘要、洞察与对话**

基于 FERN 技术栈（Firebase、Express、React、Node.js）的全栈文档分析应用。用户上传 PDF、Word、Markdown、HTML、CSV、代码等数十种格式，浏览器端完成文本抽取，原始文件经签名 URL 直传 Supabase 私有桶；后端调用 Google Gemini 生成摘要、要点、讨论问题，并支持基于文档上下文的 AI 聊天、语音对话、情感分析、改写、多语言摘要等。含 Firebase 认证、Passkeys 免密登录、文档库、分析面板；部署于 Vercel/AWS，提供 Docker/K8s 与蓝绿/金丝雀部署配置。限制：依赖外部服务（Firebase、Supabase、Gemini）方能运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 数十种格式上传，浏览器端（pdf.js/mammoth）抽取纯文本供 AI 处理
- AI 功能由 Google Gemini 提供：摘要、要点、文档上下文聊天、语音对话、情感分析
- Passkeys/WebAuthn 免密登录与每用户 Firestore 文档库
- Docker/K8s 容器化与 AWS 蓝绿/金丝雀零停机部署脚本

## 适用场景

- 快速读完长文档：拿摘要、要点和讨论问题
- 针对上传的文档内容与 AI 追问澄清
- 对文档做情感分析、改写、分类与可读性分析

## 场景标签

`聊天机器人` `文档问答` · 领域:对话与助手

## 证据(README 行号)

> L15: The **DocuThinker** app is designed to provide users with a simple, AI-powered document management tool. Users can 
> L17: **DocuThinker** is built on the **FERN-Stack** architecture — **Firebase, Express, React, and Node.js**. The backen

## 星数曲线

```mermaid
xychart-beta
    title "hoangsonww/DocuThinker-AI-App 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 47 --> 49
    line [48, 48]
```

2026-10-18 48 → 2026-10-28 48（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `0159403d2159` · [字段定义](../../DATASET.md)*
