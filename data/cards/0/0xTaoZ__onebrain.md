# 0xTaoZ/onebrain

⭐ 29 · Rust · Apache-2.0 · 推送 2026-11-27 · [GitHub](https://github.com/0xTaoZ/onebrain) · 个人维护 · 中文 README

**在 Mac 群聊里协同运行多个编码 agent 并共享一份团队记忆**

OneBrain 是一款 macOS（Apple Silicon）桌面应用（Rust + Tauri 构建），把用户已安装的编码 CLI（Claude Code、Codex、Gemini CLI 等）拉进同一个群聊：@ 指定谁运行，@all 全员，或由其挑选。核心机制是按 agent 维护读取游标的增量提示，每个 agent 只读未读消息（基准测量 100 轮减少约 80.9% 输入 token，可复现）；另维护一个 git 跟踪、按 AGENTS.md 约定的 Markdown 团队记忆目录，每次变更以 agent 签名提交，支持文件级 undo 与审批卡片。不托管 API key，使用用户自己的订阅。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多 vendor 编码 agent 同一群聊互派任务与互相评审（@提及调度）
- 按读取游标的增量提示，基准测量长对话减少 31-81% 输入 token
- git 跟踪的共享团队记忆（AGENTS.md 约定），每次变更以 agent 为作者提交
- 每次 agent 运行可撤销，写盘外/改历史的命令强制审批

## 适用场景

- 让 Claude Code 构建、Codex 评审、Gemini 记录决策在同一任务上协作
- 多个编码 agent 共享项目决策，避免各自重读全部历史
- 新成员 agent 以少量 token 加入长对话接手工作

## 场景标签

`多智能体` `编码 Agent` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L6:  A Mac group chat for people who run Claude Code, Codex and Gemini on the same work.
> L39:  It finds the coding CLIs you already use. No API keys, your own subscriptions.
> L51: OneBrain runs the CLIs you already have, with your own subscriptions. It never sees your keys. The app shows up as 


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 mid · 依据 README sha `bce7ebf6fe10` · [字段定义](../../DATASET.md)*
