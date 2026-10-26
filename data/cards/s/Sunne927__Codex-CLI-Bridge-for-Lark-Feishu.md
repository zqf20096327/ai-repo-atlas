# Sunne927/Codex-CLI-Bridge-for-Lark-Feishu

⭐ 31 · TypeScript · MIT · 推送 2026-07-31 · [GitHub](https://github.com/Sunne927/Codex-CLI-Bridge-for-Lark-Feishu) · 个人维护 · 中文 README

**在飞书（Lark）中远程操控 Codex CLI 任务的桥接器**

部署在云服务器或 VPS 上的桥接服务，把 Codex CLI/app-server 的任务流程接入 Lark：在聊天中发起并继续任务、通过 turn/steer 语义向运行中任务追加约束、用原生卡片处理状态查看、审批与中断，并通过 SQLite 持久化会话绑定、待处理交互与送达凭据以支持重启恢复。面向常驻服务器开发场景的开发者，明确界定为远程控制层而非终端替代。使用 Lark 长连接而非公网 webhook，回调按会话、任务版本与授权操作者校验。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 新消息通过 Codex turn/steer 语义附加到运行中任务，而非新建任务
- 状态、审批、中断、任务偏好通过原生 Lark 卡片与回调交互
- SQLite 持久化会话映射、待处理交互与送达凭据，支持重启后恢复
- 回调按会话、任务版本、卡片实例与授权操作者校验，过期控制失效即拒绝

## 适用场景

- 出差途中在飞书里向服务器上的 Codex 任务追加约束或处理审批
- 远程启动编码任务并在原对话中接收最终结果
- 移动端通过卡片查看任务状态并按需中断

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L15: Codex CLI Bridge for Lark (Feishu) is neither a terminal copied into Lark nor a replacement for Codex. It is a ligh
> L38: User client -> Lark services -> Bridge -> Codex app-server

## 星数曲线

```mermaid
xychart-beta
    title "Sunne927/Codex-CLI-Bridge-for-Lark-Feishu 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-26 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `b09ada8fa734` · [字段定义](../../DATASET.md)*
