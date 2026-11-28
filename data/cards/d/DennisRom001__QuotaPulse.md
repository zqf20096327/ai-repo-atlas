# DennisRom001/QuotaPulse

⭐ 4 · Rust · MIT · 推送 2026-11-25 · [GitHub](https://github.com/DennisRom001/QuotaPulse) · [官网](https://github.com/DennisRom001/QuotaPulse/releases/latest) · 个人维护

**Windows/macOS/Linux 桌面端 AI 配额监控器：汇总多工具余量与重置时间**

基于 Tauri 2 + Rust + React 的桌面应用，读取本机 Claude Code、Codex CLI、Gemini、Cursor 及 LiteLLM Proxy 的既有会话凭据，并直接调用各服务商官方 API，实时显示各套餐剩余用量与重置时间。提供悬浮胶囊、阈值告警与耗尽预测、基于本地日志的 90 天预算/历史统计、CSV/JSON/HTML 导出。宣称 100% 本地运行、无遥测、只读凭据、HTTPS 白名单受限网络访问；UI 当前为西班牙语；LiteLLM 自动启动仅 Windows 支持，需 Python 3.10–3.14。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一个窗口/悬浮胶囊聚合 Claude Code、ChatGPT/Codex、Gemini、Cursor、LiteLLM 的配额状态
- 只读本机既有登录凭据，直连服务商官方 API，无遥测与中间服务器
- 阈值桌面通知与配额耗尽时间预估，真实数字缺失时明确标注而非显示 0%
- 从本地 CLI 日志估算 token 与成本，保留最多 90 天，支持 CSV/JSON/HTML 导出

## 适用场景

- 同时使用多个 AI 编码工具时避免任务中途因配额耗尽被中断
- 替代逐个打开多个仪表盘查看各套餐余量
- 按项目、会话与服务商对比查看本地日志估算的成本

## 场景标签

 · 领域:开发者工具/AI 配额监控

## 证据(README 行号)

> L5: **Real-time AI quota monitor for Windows, macOS and Linux — every plan's remaining usage and reset time, at a glance
> L22: - **Native and light.** Tauri 2 + Rust + React. The Rust core uses about 30 MB of memory; the UI runs on the system
> L23: - **100% local, no telemetry.** It reuses the sessions your CLIs already have on this machine and talks **directly*

## 星数曲线

```mermaid
xychart-beta
    title "DennisRom001/QuotaPulse 星数(近 3 点)"
    x-axis ["2026-11-26", "2026-11-27", "2026-11-28"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-11-26 3 → 2026-11-28 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `299dc28cb7a4` · [字段定义](../../DATASET.md)*
