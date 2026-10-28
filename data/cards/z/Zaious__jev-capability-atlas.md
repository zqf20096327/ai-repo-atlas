# Zaious/jev-capability-atlas

⭐ 28 · Python · MIT · 推送 2026-09-24 · [GitHub](https://github.com/Zaious/jev-capability-atlas) · 个人维护 · 中文 README

**Jev 模型能力边界的实证地图：判断任务适不适合交给它**

独立、非官方的社群專案，基於真實 API 呼叫收據與第三方跑分，整理 TypeSafe Jev（System One 模型）適用與失效的邊界：核心結論為一條「訊號是否自足於 state」的軸。內容包含能力地圖、與 BERT/Laya 的技術對照表、瀏覽器自動化案例分析、變體整理、給人與給 agent 的使用指引，並接受附原始 log 的實驗結果貢獻。雙語（繁中/英文）README，程式碼 MIT 授權，部分內容打包為 Claude Skill 可安裝。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 以真實 API 呼叫收據與第三方跑分交叉驗證能力邊界
- 核心「一條軸」：正確答案能否從 state 讀出 vs 需要外部知識
- 與 BERT、Laya 的技術面/應用面對照表
- 含給 agent 的掃描判準（AGENTS.md）與可安裝的 Claude Skill

## 适用场景

- 評估手上的分類/判斷任務適不適合接 Jev
- 了解 Jev 在校準、延遲、多語言上的實測邊界
- 在 BERT／Laya／Jev 之間按訓練資料與任務變動性做選型
- 把第三方實驗結果貢獻進知識庫

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L5: **獨立、非官方、非 TypeSafe 贊助的社群專案**（除了一般的早鳥候補名單，我們沒有收到 TypeSafe 任何報酬或提前使用權）。這個 repo 幫你、我，還有任何想用 Jev（TypeSafe 的 System One 
> L7: 不是排行榜（市面上已經有 jev-benchmarks、thaiexam-jev-charts 在做這件事，做得很紮實，我們引用它們、不重做）。這裡回答的是另一個問題：**什麼情況下它強，什麼情況下它弱，為什麼**。
> L140: 歡迎四種貢獻：①新的測試組 ②整理並查證外部來源（跑分、文章、貼文、repo）③純分析/心得 ④修正或補充既有頁面（變體清單、實作指南、能力地圖）。**收據優先，不收手打數字**。①要附真實 API 回應的原始 log，其他要附

## 星数曲线

```mermaid
xychart-beta
    title "Zaious/jev-capability-atlas 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-28"]
    y-axis "stars" 26 --> 29
    line [27, 28, 28]
```

2026-10-18 27 → 2026-10-28 28（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `03c4e6e5f8ca` · [字段定义](../../DATASET.md)*
