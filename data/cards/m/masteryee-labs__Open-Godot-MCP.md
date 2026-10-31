# masteryee-labs/Open-Godot-MCP

⭐ 14 · GDScript · MIT · 推送 2026-07-23 · [GitHub](https://github.com/masteryee-labs/Open-Godot-MCP) · 组织维护 · 中文 README

**連接 AI 助手與 Godot 引擎的 MCP server，支援自主開發測試除錯**

開源 Model Context Protocol server，將 Claude、Cursor、Windsurf 等 AI 客戶端連接到 Godot 4.5+ 編輯器，提供約 35 個 MCP 工具與約 130 個 actions：確定性 playtesting（凍結時鐘、step 時間、觀察 JSON 狀態）、連線遊戲測試（多實例、peer 模擬、延遲注入）、DAP 斷點除錯與 LSP 整合。具 Token 效率設計（diff 回傳、截圖壓縮）與 Windows 孤兒行程防護。另含 5 個預設關閉、需 API key 動態註冊的 Agnes/NVIDIA AI 工具。執行環境為 Python 3.11+ server 加 GDScript addon，MIT 授權。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 確定性 playtesting：凍結時鐘、step_until 條件、JSON 狀態 digest
- 連線遊戲測試：多實例 host/client、peer 模擬、網路條件注入
- DAP 斷點/變數除錯與 LSP 靜態診斷整合
- Token 效率設計：diff 回傳、截圖壓縮與自動清理、read/write 分離

## 适用场景

- 讓 AI 在 Godot 專案上寫程式、運行遊戲並自主修 bug
- 連線遊戲開發者驗證多實例同步與注入延遲測試
- 獨立遊戲工作室做自動化 playtesting 與回歸測試

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L14: **Open Godot MCP** 是一個開源的 Model Context Protocol server，將 AI 程式助手（Claude、GPT、Cursor、Windsurf 等）連接到 Godot Engine 編輯器
> L20: |**專案類型**|MCP server（Model Context Protocol）for Godot Engine|

## 星数曲线

```mermaid
xychart-beta
    title "masteryee-labs/Open-Godot-MCP 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `7d0634c82b62` · [字段定义](../../DATASET.md)*
