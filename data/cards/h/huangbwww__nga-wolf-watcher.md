# huangbwww/nga-wolf-watcher

⭐ 63 · Python · MIT · 推送 2026-09-16 · [GitHub](https://github.com/huangbwww/nga-wolf-watcher) · [官网](https://github.com/huangbwww/nga-wolf-watcher/releases/latest) · 个人维护 · 中文 README

**NGA 回复监听推送工具，附股票看板与可选本地 AI Agent**

监听指定 NGA 用户或主题的新回复，推送到飞书、微信、钉钉、邮件或 WxPusher；通过浏览器 Cookie 读取账号可见页面。Windows 提供安装包与便携版，macOS 提供未签名实验版 dmg，Linux 一条命令安装并生成 ngawolf 命令（含 TUI 配置与后台服务）。v1.5.0 起桌面端包含股票看板与个股工作台（自选股、K 线、斐波那契回撤、牛市策略信号）。本地 AI Agent 默认关闭，开启后可将消息传给本地 Codex、Claude Code、CodeWhale 或自定义命令；声明不构成投资建议、不做自动交易。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 5 个推送渠道（飞书/微信/钉钉/邮件/WxPusher）
- Windows/macOS/Linux 三平台分发，Linux 一键安装含后台服务
- 股票看板：自选股、分时/K线、斐波那契回撤与牛市策略信号
- 可选本地 AI Agent，接入 Codex/Claude Code/CodeWhale/自定义命令

## 适用场景

- 监听 NGA 特定作者或主题的新回复并及时推送到群
- 在飞书/微信/钉钉里查询历史回复或打包导出
- 管理自选股与持仓，查看个股技术指标与策略信号
- 通过 /ai 命令调用本地 AI Agent 分析回复或行情

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L114: AI is disabled by default and is not required for normal NGA watching or pushing. When enabled, the app can pass F

## 星数曲线

```mermaid
xychart-beta
    title "huangbwww/nga-wolf-watcher 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 62 --> 64
    line [63, 63]
```

2026-10-18 63 → 2026-10-24 63（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `1013e9b00d43` · [字段定义](../../DATASET.md)*
