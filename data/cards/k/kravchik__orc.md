# kravchik/orc

⭐ 15 · Python · 推送 2026-10-16 · [GitHub](https://github.com/kravchik/orc) · 个人维护

**通过 Telegram/Slack 操控本地编码 agent 的控制平面与会话路由器**

自托管的聊天控制平面：把本地运行的编码 agent（Codex、Claude Code、OpenCode、通用 ACP 协议）接入 Telegram 或 Slack，在聊天中发送任务、查看推理过程与最终回答、处理命令与文件修改审批、上传文件（单文件 50 MiB 上限）。提供 Steward 会话用于自然语言管理。支持给会话分配地址组成 agent 网络（Shaman/Grunt 两种路由角色），实现多 agent 任务传递与审批委托。使用 Telegram 轮询或 Slack Socket Mode，不开放公网监听端口；README 中安装细节指向各 Setup 文档，本页未给出具体安装命令。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 在 Telegram/Slack 中直接对话本地编码 agent 并处理审批
- 会话地址路由：Shaman/Grunt 角色组成多 agent 网络
- 审批可由正则规则、委托其他 agent 或默认策略处理
- 文件上传以编号列表随消息传递给 agent

## 适用场景

- 在手机 Telegram/Slack 上远程操控本地 Codex/Claude Code 会话写代码
- 搭建多 agent 协作网络，让一个 agent 分派任务、另一个审查方案
- 通过聊天处理 agent 的命令与文件修改审批请求

## 场景标签

`多智能体` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L5: Orc Master is a chat control plane and a network router for local agent sessions.
> L35: Orc Master supports Codex, Claude, OpenCode, and general ACP protocol for any agent that supports it.

## 星数曲线

```mermaid
xychart-beta
    title "kravchik/orc 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `5c02d73f3406` · [字段定义](../../DATASET.md)*
