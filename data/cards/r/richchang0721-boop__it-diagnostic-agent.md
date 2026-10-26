# richchang0721-boop/it-diagnostic-agent

⭐ 28 · HTML · MIT · 推送 2026-08-01 · [GitHub](https://github.com/richchang0721-boop/it-diagnostic-agent) · 个人维护 · 中文 README

**给 IT 支持团队的互动式故障排除 Runbook，可接入 AI 診斷**

純靜態 HTML 的 IT 故障排除工具，涵蓋網路（CCTV/NAS/DNS）、硬體與軟體（AD/Exchange/Outlook/SQL Server）三類決策樹，逐步 YES/NO 引導排障。提供瀏覽器內表單式編輯模式與 JSON 匯入匯出，無需寫程式即可擴充診斷內容。AI 部分為可選對話面板，支援 Claude、Gemini、OpenAI 相容介面與 Ollama 本地模型，可切換純 Runbook 模式隱藏 AI。零後端依賴，GitHub Pages 部署，繁中/英文雙語。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 網路/硬體/軟體三模組互動式決策樹與逐步 YES/NO 引導
- 瀏覽器內表單編輯診斷內容，匯出帶版本號 JSON 備份
- 多模型 AI 面板：Claude、Gemini、OpenAI 相容介面、Ollama 本地
- 純靜態 HTML 零後端依賴，可 Runbook 模式隱藏 AI

## 适用场景

- IT 一線支持人員按決策樹逐步排除主機、網路、印表機故障
- 企業以純 Runbook 模式做內部 SOP 展示與新人培訓
- 資安要求高的環境用 Ollama 本地模型做 AI 診斷，資料不出公司
- IT 團隊自行擴充與客製化診斷流程並在團隊間分享

## 场景标签

 · 领域:企業 IT 運維/技術支持

## 证据(README 行号)

> L16: - **Runbook 模式** — 隱藏 AI 面板，純決策樹介面，適合企業內部 SOP 展示
> L127: 點擊右上角 📋 按鈕開啟 Runbook 模式，隱藏 AI 面板。
> L136: 使用 Ollama 在本機或內網跑模型，資料完全不離開公司。

## 星数曲线

```mermaid
xychart-beta
    title "richchang0721-boop/it-diagnostic-agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-26 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `745abbef9913` · [字段定义](../../DATASET.md)*
