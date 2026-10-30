# monas-team/zaloclaw

⭐ 24 · TypeScript · MIT · 推送 2026-10-26 · [GitHub](https://github.com/monas-team/zaloclaw) · [官网](https://openclaw.monas.us/zalo) · 组织维护

**把个人 Zalo 账号接入 OpenClaw AI agent 的非官方插件**

基于逆向工程库 zca-js 构建的 OpenClaw 插件，将 Zalo 个人账号（非 OA）作为消息通道连接到 AI agent，提供 153 个 actions，覆盖发消息、群管理、好友操作、自动回复、权限控制（allow/deny、DM/group policy、injection guard）等；支持文件/图片自动下载后转发给 agent 处理，可把群聊历史存为本地 JSONL 供 recall。限制：Zalo 不提供个人账号 API，插件可能违反 ToS 并导致封号；多个 Zalo endpoint 已失效（404），session 过期需重新扫码。

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

- 153 个 actions：消息、群管理、好友、自动回复、频道控制、self-update
- 文件/图片（含 quoted 图片）自动下载并转发给 agent，上限 50 MB
- Passive Collector 将群聊历史写入本地 JSONL，通过 recall-group-history 检索
- Bridge Service 允许其他 OpenClaw 插件零 AI turn 直接调用 actions

## 适用场景

- 把自己的 Zalo 个人号接入 OpenClaw agent 实现自动回复
- 让 agent 在 Zalo 群里按 @mention 响应并处理群管理
- 本地留存并检索 Zalo 群聊历史记录

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L3: **Unofficial OpenClaw plugin — Zalo Personal Account Channel**
> L5: Connect your personal Zalo account to an AI agent with **153 actions**.
> L141: Sibling OpenClaw plugins có thể gọi ZaloClaw actions trực tiếp mà không cần AI model turn:

## 星数曲线

```mermaid
xychart-beta
    title "monas-team/zaloclaw 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-30 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `686491846579` · [字段定义](../../DATASET.md)*
