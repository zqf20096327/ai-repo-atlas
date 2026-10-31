# iamhenryhuang/AI-Study-Abroad-Consultant

⭐ 13 · Python · Apache-2.0 · 推送 2026-09-16 · [GitHub](https://github.com/iamhenryhuang/AI-Study-Abroad-Consultant) · 个人维护 · 中文 README

**北美 CS 留學申請問答系統：三校官方條件與社群經驗 RAG 檢索**

以 FastAPI、LangGraph 與 PostgreSQL 建構的留學申請問答系統，正式收錄 Georgia Tech、Purdue、Stanford 三校。透過爬蟲抽取官方申請條件，結合 GradCafe／一畝三分地錄取經驗與教授名單，由 Agent 按意圖路由至 SQL、全文檢索、向量混合檢索或 SerpAPI 查詢，以 SSE 串流回答。OpenAI 不可用時降級為本機規則與全文檢索。需自行啟動 PostgreSQL、配置 API key 並執行爬蟲初始化。

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

- LangGraph StateGraph 依意圖路由至結構化查詢／全文／向量／SerpAPI
- 收錄三校官方申請條件、GradCafe 與一畝三分地錄取經驗、教授名單
- OpenAI 不可用時降級為本機規則與全文檢索，不中斷 API
- 提供 FastAPI SSE 端點與 CLI 兩種使用方式

## 适用场景

- 查詢三校 CS 程式的官方申請條件（TOEFL/GRE/申請費）
- 參考 GradCafe 與一畝三分地的錄取經驗做選校
- 查詢三校教授名單與指定教授的研究資訊

## 场景标签

`RAG` · 领域:知识与检索

## 证据(README 行号)

> L3: 以 FastAPI、LangGraph 與 PostgreSQL 建構的留學申請問答系統。目前正式收錄 Georgia Tech、Purdue、Stanford 三校，支援官方申請條件、社群錄取經驗、選校推薦與教授查詢。
> L10:     API --> Agent[LangGraph Agent]
> L16: - Agent：依問題查結構化資料、全文、社群案例、推薦結果或教授資訊。

## 星数曲线

```mermaid
xychart-beta
    title "iamhenryhuang/AI-Study-Abroad-Consultant 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `7b08a83af727` · [字段定义](../../DATASET.md)*
