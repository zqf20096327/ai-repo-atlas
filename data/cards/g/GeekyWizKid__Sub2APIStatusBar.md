# GeekyWizKid/Sub2APIStatusBar

⭐ 15 · Swift · MIT · 推送 2026-05-21 · [GitHub](https://github.com/GeekyWizKid/Sub2APIStatusBar) · 个人维护 · 中文 README

**macOS 菜单栏应用：监控 Sub2API 用户的用量与花费**

面向 Sub2API 用户的 SwiftUI 菜单栏伴随应用：登录自建的 Sub2API 服务器（/api/v1 端点），在菜单栏常驻展示余额、日花费、Token 用量、配额压力、模型分布与订阅限额，无需保持网页仪表盘。提供 Usage Insights 信号分级、本地提醒（含静默期控制）、数据过期护栏、多账户切换、匿名分享卡与支持诊断复制。配置存本地文件，不用 Keychain，无遥测。需 macOS 13+、Swift 6.1+ 本地开发，提供 DMG 打包脚本与 GitHub Releases 更新检查。

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

- 菜单栏常驻展示余额/花费/Token/配额/模型分布
- Usage Insights 信号分级与可自定义阈值
- 本地通知提醒与静默期控制、数据过期护栏
- 多账户切换、本地配置存储、无遥测

## 适用场景

- 不开网页仪表盘随时查看我的 Sub2API 花费与配额
- 配额或余额接近阈值时收到本地提醒
- 多账户用户在菜单栏快速切换查看用量

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L5: Sub2API Status Bar is a macOS menu bar companion for Sub2API users. It keeps daily spend, token usage, quota pressur
> L49: The app expects a Sub2API server with `/api/v1` endpoints:
> L54: - `GET /api/v1/usage/dashboard/stats`

## 星数曲线

```mermaid
xychart-beta
    title "GeekyWizKid/Sub2APIStatusBar 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `01b5425c76bd` · [字段定义](../../DATASET.md)*
