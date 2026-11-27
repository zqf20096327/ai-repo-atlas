# cheapbutsimilar/Agent-Meter

⭐ 5 · Rust · MIT · 推送 2026-11-26 · [GitHub](https://github.com/cheapbutsimilar/Agent-Meter) · 个人维护

**为多 AI 编码 CLI 用户聚合显示配额、燃速与 API 成本的桌面小组件**

Rust + Tauri 2 编写的 Windows 任务栏/macOS 菜单栏小组件，读取本机各 CLI 的日志文件与官方用量接口，集中显示 Claude Code、Codex、Gemini CLI、Antigravity、Grok、MiniMax、Z.AI、Qwen 的限额百分比、按当前速率的耗尽预测与按公开 API 价格折算的等效成本；提供 14/30 天用量图表、CSV 导出、阈值提醒与主题设置。100% 本地运行，无遥测；版本以 2.3 MB 安装包分发，Windows 未签名、macOS 未公证，Linux 仅可源码构建，任务栏停靠仅 Windows 支持。

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

- 读取本机日志与官方用量接口，聚合多 agent 限额百分比
- 按近期速率计算限额耗尽预测与 API 等效成本（USD/KRW）
- 每日 token/成本图表、时段热力图、按项目与模型统计、CSV 导出
- 100% 本地无遥测，发行版由公开 GitHub Actions 工作流构建

## 适用场景

- 同时使用多个 AI 编码 CLI 时查看哪个限额最先耗尽
- 估算订阅用量折算成 API 价格的成本
- 在限额临期时收到提醒以安排重置前的工作节奏

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L5: Live usage limits for **Claude Code · Codex · Gemini CLI · Antigravity · Grok · MiniMax · Z.AI · Qwen**,
> L141: There's no AgentMeter server. Everything is read from **log files on your machine** and the **logins each CLI has


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `b188cf9a5e33` · [字段定义](../../DATASET.md)*
