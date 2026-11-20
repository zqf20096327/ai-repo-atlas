# waytosea-oss/suanli-dashboard

⭐ 10 · Swift · MIT · 推送 2026-09-20 · [GitHub](https://github.com/waytosea-oss/suanli-dashboard) · 个人维护 · 中文 README

**macOS 悬浮仪表盘：监控 Codex/Claude Code 订阅额度与 Token 消耗**

面向重度使用 Codex 与 Claude Code 的 macOS 用户的悬浮仪表盘：读取本机登录凭据与本地会话日志，显示 5 小时/7 天滚动窗口余额、今日与本月 Token 消耗、项目分布及多设备趋势（经 iCloud 同步）。支持 Codex、Claude Code 读本机状态，DeepSeek/Kimi/SiliconFlow/OpenRouter/GLM/SuperGrok 填 API Key 读余额，Key 以 0600 权限存本机明文 JSON。仅支持 macOS 14+（Apple Silicon 官方包，Intel 需源码构建），依赖 Keychain、iCloud Drive、Touch Bar 等 macOS 专属 API。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 监控 5 小时/7 天订阅窗口余额与刷新倒计时
- Token 消耗看板：今日/近 7 天/本月、用途分布、项目 Top 3
- 多设备 iCloud 同步趋势对比，Touch Bar 常驻面板与最近会话直达
- 接入 DeepSeek/Kimi/SiliconFlow/OpenRouter/GLM/SuperGrok API Key 读余额

## 适用场景

- 重度使用 Codex/Claude Code 时随时查看剩余额度与刷新时间
- 多台 Mac 上汇总对比各设备的 Token 消耗趋势
- 同时管理多个平台 API Key 的账户余额显示

## 场景标签

 · 领域:开发者工具/AI 用量监控

## 证据(README 行号)

> L3: > macOS 悬浮仪表盘：同时监控 **OpenAI Codex** 与 **Claude Code** 的订阅额度余额、Token 消耗与趋势。支持 Touch Bar 常驻显示、最近会话直达、多设备 iCloud 同步。
> L42: 重度使用 Codex / Claude Code 的人都遇到过：干着干着突然「额度用完了」。算力码表把两个工具的 **5 小时滚动窗口**和 **7 天窗口**余额变成一个始终可见的小仪表，让你随时知道还剩多少、什么时候刷新。
> L44: - **多平台监控（v1.2 起）**：在设置里的「添加平台」下拉菜单里选，选几个显示几个——Codex、Claude Code 读本机登录状态；**智谱 GLM Coding Plan** 填 API Key 读订阅窗口；**D

## 星数曲线

```mermaid
xychart-beta
    title "waytosea-oss/suanli-dashboard 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-11-20"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-18 10 → 2026-11-20 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 high · 依据 README sha `3d511067491c` · [字段定义](../../DATASET.md)*
