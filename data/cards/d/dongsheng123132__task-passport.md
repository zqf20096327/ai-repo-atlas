# dongsheng123132/task-passport

⭐ 10 · JavaScript · MIT · 推送 2026-11-06 · [GitHub](https://github.com/dongsheng123132/task-passport) · [官网](https://taskpack.org) · 个人维护 · 中文 README

**让任务在多个 AI Harness 之间携带已验证状态接力交接**

以协议加工具形式提供的任务交接方案：每个任务对应一本带版本号与短号的"护照"，记录目标、已验证事实、决策与下一步；通过 pack/land 将状态封装为单文件 TaskPack 在人机之间搬运，打包时把机器级事实降级为未证并拒绝无验收标准的请求。同一 npm 包提供通用 CLI（stdout 输出 JSON）、DeepSeek Harness 插件、MCP 服务（Claude Code/Codex 接入）与 WorkBuddy 插件市场。状态可由 U-King、本地目录或第三方 Provider 托管；协议不搬运聊天记录、不搬运项目文件。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- pack/land 单文件交接，打包时封存机器级事实（verified_on）
- expected_version 冲突检测，过期写入不静默覆盖
- 同一 npm 包提供 CLI、MCP 服务与 DSH/WorkBuddy 插件
- 本地目录 Provider 支持跨进程锁与原子替换

## 适用场景

- 把进行中的任务从 Claude Code 交接给 Codex 继续
- 跨机器、跨同事传递任务状态而不搬运聊天记录
- 多个 AI Harness 读写同一台机器上的同一本护照

## 场景标签

`Agent 记忆` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L10: 让一个任务带着“当前世界状态”在 DeepSeek Harness、Claude Code、Codex 等 AI Harness 之间接力，不搬运聊天记录。
> L27: - 同一个包既是通用 CLI，也是 DeepSeek Harness 原生 bundle。

## 星数曲线

```mermaid
xychart-beta
    title "dongsheng123132/task-passport 星数(近 2 点)"
    x-axis ["2026-10-23", "2026-11-25"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-23 10 → 2026-11-25 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 high · 依据 README sha `587cbb988005` · [字段定义](../../DATASET.md)*
