# ADT109119/ChatPDF-LineBot

⭐ 17 · Python · Apache-2.0 · 推送 2026-10-19 · [GitHub](https://github.com/ADT109119/ChatPDF-LineBot) · [官网](https://adt109119.github.io/ChatPDF-LineBot-Docs/) · 个人维护 · 中文 README

**上傳 PDF 並問答的 Line Bot（LangChain+FastAPI+Vue）**

面向 LINE 用戶的 PDF 問答機器人：透過 LIFF 網頁上傳 PDF/CSV/TXT 文件，自動 Embedding 後以自然語言問答。後端用 FastAPI 與 LangChain 構建，前端為 Vue.js，對接 LINE Messaging API 與 LIFF。模型透過 OpenAI 相容 API 接入（預設 Groq 與 OpenAI），Embedding 預設使用 sentence-transformers 模型，可選 CUDA 設備。支援 Docker 部署與 Hugging Face 一鍵部署（免費方案檔案不持久），需設定多項 LINE 憑證與 API Key 環境變數方可運行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LIFF 網頁上傳 PDF，Embedding 後問答
- 多模型可配置，經 OpenAI 相容 BASE_URL 接入 Groq 等
- Docker 與 Hugging Face 一鍵部署，支援 CloudFlare Tunnel
- 每用戶空間配額與上傳檔案類型/大小限制可配置

## 适用场景

- 在 LINE 上傳文件並直接提問獲得回答
- 為社群建立基於自家 PDF 資料的問答機器人
- 以 Docker 或 Hugging Face 快速自架文件問答服務

## 场景标签

`文档问答` `聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L3: 這是一個使用 LangChain、FastAPI 和 Vue 構建的 Line Bot，可以透過 Line Liff 網頁上傳 PDF 文件並回答相關問題。
> L19: - [x] 自然語言處理，從 PDF 中提取相關內容回答問題
> L21: - [x] 使用 Line Bot 進行互動

## 星数曲线

```mermaid
xychart-beta
    title "ADT109119/ChatPDF-LineBot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-30 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `7284dcbe8639` · [字段定义](../../DATASET.md)*
