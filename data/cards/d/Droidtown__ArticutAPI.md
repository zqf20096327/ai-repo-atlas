# Droidtown/ArticutAPI

⭐ 414 · Python · MIT · 推送 2026-06-04 · [GitHub](https://github.com/Droidtown/ArticutAPI) · [官网](https://api.droidtown.co) · 组织维护 · 中文 README

**中文斷詞與詞性標記 API 客戶端，規則式處理無需模型**

卓騰文化提供的中文斷詞暨詞性標記服務的 Python 客戶端：基於現代白話中文語法規則而非機器學習，不需資料模型，透過 HTTP Request 呼叫線上 API 或 Docker 版服務，支援 lv1（細粒度，適合 NLU/機器翻譯）與 lv2（詞組級，適合文本分析/關鍵詞擷取）兩種深度。附帶使用者自定義詞典、TF-IDF/TextRank 關鍵詞抽取、GraphQL 查詢斷詞結果等功能。空帳號可使用每小時 2000 字的公用額度。另有 MP_ArticutAPI（多程序批次）與 WS_ArticutAPI（WebSocket 即時）兩種 Docker 版本。

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

- 規則式斷詞，不使用機器學習與資料模型
- 兩種斷詞深度：lv1 細粒度、lv2 詞組級
- 使用者自定義詞典與 TF-IDF/TextRank 關鍵詞抽取
- 三種部署形態：線上 API、Multiprocessing、WebSocket（均為 Docker）

## 适用场景

- 對中文文本做斷詞與詞性標記供後續 NLU 處理
- 文本分析與關鍵詞擷取前的前處理
- 聊天機器人即時分詞（WS_ArticutAPI）

## 场景标签

 · 领域:NLP/中文資訊處理

## 证据(README 行号)

> L1: # Articut 中文斷詞暨詞性標記服務
> L2: ## [依語法結構計算，而非統計方法的中文斷詞。]
> L47: from ArticutAPI import Articut

## 星数曲线

```mermaid
xychart-beta
    title "Droidtown/ArticutAPI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 413 --> 415
    line [414, 414]
```

2026-10-18 414 → 2026-10-25 414（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `8932f3046469` · [字段定义](../../DATASET.md)*
