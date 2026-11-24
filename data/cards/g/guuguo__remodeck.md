# guuguo/remodeck

⭐ 11 · JavaScript · MIT · 推送 2026-11-23 · [GitHub](https://github.com/guuguo/remodeck) · [官网](https://hub.guuguo.top/agent-control) · 个人维护 · 中文 README

**给 AI 编程 Agent 的手机远程控制与 3D 桌面控制台**

自托管的多 AI 编程 Agent 控制台：只读解析 ~/.codex、~/.claude、~/.gemini 等本机记录，将 Codex、Claude Code、Antigravity、Grok、Qoder 会话聚合到统一界面，支持续发消息、批权限、打断、排队派活与多账号额度标注。通过扫码生成手机远程链接（Cloudflare/Tailscale 隧道或自托管 Docker 中继），并提供免提语音总控（本地 mlx-whisper 离线识别）。不改上游工具配置与数据库，不读取 Token/API Key。需 Node.js 22+ 与 Git。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一个界面聚合 Codex、Claude Code、Antigravity、Grok、Qoder 会话
- 5 秒扫码手机远程：看输出、批权限、打断与排队派活
- 免提语音总控，本地 mlx-whisper 离线识别，可切换后端模型
- 多账号自动发现与额度归属标注，只读不改动上游数据库

## 适用场景

- 出门在外用手机查看和推进电脑上的编程 Agent 任务
- 同时管理多个 Codex/Claude 账号并区分额度
- 开车等免提场景下用语音审批或打断 Agent

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L5:  把 Codex、Claude Code、Antigravity、Grok 和 Qoder 收进一个桌面 + 手机遥控台 （原 Agent Control）
> L21: > - **严格只读解析上游记录**：只读解析 `~/.codex`、`~/.claude`、`~/.gemini`，自定义标题、置顶与归档保存在 RemoDeck（Agent Control）独立数据目录，**绝不修改**上游工
> L95: 2. **电脑端统一管理**：左侧按项目查看所有运行中或历史会话，点进去即可续发消息、切换模型、设置 `/goal` 自动推进或批量归档；多账号（如多个 Codex 账号）自动标注归属与额度。


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `dccdb434ae27` · [字段定义](../../DATASET.md)*
