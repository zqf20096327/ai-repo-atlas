# Relomoney/relo

⭐ 240 · JavaScript · NOASSERTION · 推送 2026-10-21 · [GitHub](https://github.com/Relomoney/relo) · [官网](https://relo.money) · 组织维护

**开发者变现平台：AI 编码等待期展示赞助信息并付费**

开源的开发者变现平台：通过 CLI（npx relo-money init 将 relo.js 安装到 ~/.relo 并自动配置检测到的 AI 编码工具）在 Claude Code、Cursor、Codex 的推理等待期展示赞助信息，开发者经 10 秒验证观看后获得报酬，并通过 relo.money/dashboard 面板跟踪观看数与收入。仓库含 CLI 与 Cursor 状态栏扩展（仅读取本地状态文件，不联网）。声明不读取代码、提示词与对话；hook 传入 stdin 的提示文本会被丢弃不上传。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 在 AI 推理等待期展示赞助信息，验证 10 秒观看后付酬
- CLI 自动配置检测到的 AI 编码工具
- Cursor 状态栏扩展仅读取本地 state-cursor.json，不联网
- 声明不读取代码/提示词/对话，stdin 输入被丢弃

## 适用场景

- 抵消每月 AI 工具订阅开销
- 在不打断编码流程的情况下通过观看赞助信息获得收入
- 在仪表盘跟踪验证观看与提现

## 场景标签

 · 领域:开发者工具/变现

## 证据(README 行号)

> L5: Relo is an open-source developer monetization platform that pays developers for their attention while using AI codin
> L35: - `cli/` — the `relo-money` command. `init` copies it to `~/.relo/relo.js` and configures the tools it finds.


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `e45819319323` · [字段定义](../../DATASET.md)*
