# Guling-Pro/guling-trader

⭐ 22 · Python · AGPL-3.0 · 推送 2026-10-15 · [GitHub](https://github.com/Guling-Pro/guling-trader) · [官网](https://guling.pro) · 组织维护 · 中文 README

**把同花顺接入 AI 助手的 Windows 开源 MCP 交易客户端**

运行在 Windows 上的交易执行客户端：通过 MCP 协议把已登录的同花顺独立委托客户端（xiadan.exe）接入 Claude、Cursor 等 AI 助手，暴露买卖、撤单、查持仓/资金/委托/交割单/自选股等工具。账号密码不离开同花顺，客户端模拟键鼠操作并配合 Tesseract OCR 识别界面；配对经 mcp.guling.pro 中转隧道完成。限制：交易端仅支持 Windows、要求 DPI 缩放 100% 且界面不可最小化，订单 ID 需 UUID v7 幂等语义。提供 GitHub Releases 单文件 exe。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 通过 MCP 向 AI 暴露买卖/撤单/持仓/资金/交割单等交易工具
- 账号密码不离开同花顺，客户端仅模拟键鼠并自动装 Tesseract OCR
- 订单/撤单采用 client_order_id（UUID v7）幂等与两步撤单确认机制
- GitHub Releases 提供单文件免安装 exe，配对码经 mcp.guling.pro 换取永久凭证

## 适用场景

- 让 Claude/Cursor 等 AI 助手帮我盯盘、查询持仓并用自然语言下单 A 股
- 用 7×24 开机的 Windows 机器（物理机/云 VPS/虚拟机）常驻运行交易端
- 通过 MCP 工具接口把交易能力接入自定义 agent 工作流

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L14: guling-trader 是一个跑在 Windows 上的开源交易执行客户端。它把你登录的同花顺独立委托客户端（xiadan.exe）接入任意 AI 助手（Claude / Cursor / openclaw 等），通过 MCP
> L63: ## 路径 B · 任意 AI 客户端通过 mcp.guling.pro 自助接入
> L74: **原理一句话**：向 `https://mcp.guling.pro/pair` 用 6 位码换一个永久 `agent_token`，再用 `Authorization: Bearer <token>` 请求头把 MCP 服务器

## 星数曲线

```mermaid
xychart-beta
    title "Guling-Pro/guling-trader 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-28", "2026-10-29"]
    y-axis "stars" 20 --> 23
    line [21, 22, 22]
```

2026-10-18 21 → 2026-10-29 22（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `02a9a5cd8e41` · [字段定义](../../DATASET.md)*
