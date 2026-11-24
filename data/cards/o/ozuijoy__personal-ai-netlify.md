# ozuijoy/personal-ai-netlify

⭐ 4 · JavaScript · MIT · 推送 2026-11-18 · [GitHub](https://github.com/ozuijoy/personal-ai-netlify) · 个人维护 · 中文 README

**部署在 Netlify+Neon 的私人單使用者 AI 聊天工作區**

由 scupro/personal-ai（Cloudflare Workers+D1）移植到 Netlify Functions/Edge Functions+Neon Postgres 的私人聊天工作台。不內建任何供應商，透過設定面板或 PROVIDER_N_* 環境變數接入任意 OpenAI 相容服務（允許空 Key 的自架模型）。功能含知識庫（PDF/DOCX 上傳、中文 BM25+向量混合檢索）、網頁搜尋（Jina/Tavily）、遠端 MCP 工具（呼叫需逐次確認）、技能注入與使用者確認後寫入的長期記憶；API Key 以 AES-256-GCM 加密存伺服器。部署需 Neon 資料庫與環境變數設定，檔案功能另需 S3 相容物件儲存。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 接入任意 OpenAI 相容供應商，無內建供應商，允許空 API Key 自架模型
- 知識庫支援 PDF/DOCX 抽文字、中文斷詞 BM25+語意向量 RRF 混合檢索
- 遠端 MCP 工具與文件工具呼叫前需使用者按「允許」確認
- API Key 伺服器端 AES-256-GCM 加密，支援輪替與重新加密

## 适用场景

- 部署一個只有自己能登入的個人 AI 聊天工作區
- 把自架或第三方 OpenAI 相容模型接入帶知識庫的聊天介面
- 上傳 PDF/DOCX 建立可跨裝置同步的個人知識庫
- 給聊天模型接入遠端 MCP 工具並逐次確認執行

## 场景标签

`聊天机器人` `文档问答` · 领域:对话与助手

## 证据(README 行号)

> L3: 個人 AI 聊天工作台：接任何 OpenAI 相容模型，搭配知識庫、技能、長期記憶、網頁搜尋與 MCP 工具，資料存在自己的 Neon Postgres。
> L29: |供應商與模型|**沒有內建供應商**。來源只有兩種：設定面板新增（Key 加密存資料庫）與 `PROVIDER_N_*` 環境變數（唯讀，Key 不進資料庫也不到瀏覽器）。任何 OpenAI 相容服務皆可，**允許空 API K

## 星数曲线

```mermaid
xychart-beta
    title "ozuijoy/personal-ai-netlify 星数(近 3 点)"
    x-axis ["2026-11-16", "2026-11-19", "2026-11-24"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-11-16 3 → 2026-11-24 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `e44577981f69` · [字段定义](../../DATASET.md)*
