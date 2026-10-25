# aa0101181514/tw-legal-rag

⭐ 334 · Python · NOASSERTION · 推送 2026-10-21 · [GitHub](https://github.com/aa0101181514/tw-legal-rag) · [官网](https://dr-legal.com.tw) · 个人维护 · 中文 README

**台灣法律語義檢索 MCP 伺服器與 CLI，供 AI 助理調用判決資料**

由律師個人開發的台灣法律檢索工具：公開原始碼 CLI（twlegalrag）連接 2,273 萬筆裁判書的 hosted 語義檢索端點，並提供同一後端的 Remote MCP 伺服器，可接入 Claude、ChatGPT、Gemini、Copilot 等工具。功能含自然語言檢索、案號精確調卷、審級關聯 case_history、現行法條查詢、allowed_citations 引用白名單與 bundle 層級 citation check。本工具不呼叫任何 LLM、不生成法律意見，答案由使用者自己的 AI 生成；檢索與向量索引留在伺服器端，僅 CLI 公開。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 2,273 萬筆台灣裁判書語義檢索，每日增量同步司法院公開資料
- Remote MCP 端點一個網址接入 Claude/ChatGPT/Gemini/Copilot，OAuth 動態註冊免金鑰
- allowed_citations 引用白名單＋verification_instructions＋bundle 層級 citation check
- 審級關聯 case_history 附廢棄／駁回旗標，函釋效力狀態追蹤

## 适用场景

- 用自然語言搜尋台灣判決並打包成 bundle 餵給自己的 AI 工具
- 透過 MCP 讓 Claude/ChatGPT 等 AI 助理直接檢索台灣法律資料
- 對 AI 產生的法律答案做引用字號是否存在於 bundle 的檢查
- 引用法條或判決前核驗條號存在、效力狀態與是否被上級審廢棄

## 场景标签

`语义搜索` `科研工具` · 领域:知识与检索

## 证据(README 行号)

> L16: does **not** generate legal advice, does **not** call any LLM, and does **not**
> L195: **不做**：本工具**不呼叫任何 LLM、不生成法律意見、不背書**任何模型輸出。答案要由
> L368: 不論走 CLI、MCP 還是 Claude Code skill,答案都由**你自己的 AI** 生成,本服務只提供

## 星数曲线

```mermaid
xychart-beta
    title "aa0101181514/tw-legal-rag 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22", "2026-10-25"]
    y-axis "stars" 327 --> 334
    line [328, 330, 332, 333]
```

2026-10-18 328 → 2026-10-25 333（+5）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `b604328d1281` · [字段定义](../../DATASET.md)*
