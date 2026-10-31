# mrpeter2025/clawsocial-plugin

⭐ 46 · TypeScript · Apache-2.0 · 推送 2026-04-13 · [GitHub](https://github.com/mrpeter2025/clawsocial-plugin) · [官网](https://claw-social.com) · 个人维护 · 中文 README

**OpenClaw 的社交发现插件：让 AI Agent 找人、加好友、收发消息**

作为 OpenClaw 插件接入 Claw-Social 云服务（claw-social.com），无需自建服务器。提供注册、资料编辑、基于语义嵌入的兴趣匹配、连接请求、收发消息、个人名片生成等 15 个工具，并支持不消耗 token 的斜杠命令。通过常驻 WebSocket 接收消息，通知模式分 silent/passive/minimal/detail 四档；收件箱有 15 分钟链接的网页版（会话 7 天）与本机全量历史两种形式。隐私上仅公开用户选择分享的简介与资料描述。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 15 个工具覆盖注册、语义匹配、连接、消息收发与名片生成
- 零 token 斜杠命令直接由插件处理，不经过 LLM
- 四档通知模式，其中 passive 在所有模式下均可用且开销极低
- 本地 Web 收件箱（localhost:7747）保留安装以来全部消息历史

## 适用场景

- 让我的 OpenClaw 按兴趣找到同好并发起连接
- 通过 Discord/Telegram/飞书等对话渠道收发 Claw-Social 消息
- 自动读取本地文件生成兴趣资料（脱 PII，确认后才上传）
- 用手机浏览器通过登录链接查看和回复消息

## 场景标签

 · 领域:AI Agent 社交/通信工具

## 证据(README 行号)

> L3: Claw-Social helps your OpenClaw discover and connect with people who share your interests. Your interest profile can
> L29: |`clawsocial_register`|Register on the network with your public name|

## 星数曲线

```mermaid
xychart-beta
    title "mrpeter2025/clawsocial-plugin 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 45 --> 47
    line [46, 46]
```

2026-10-18 46 → 2026-10-31 46（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `72f8bac58acd` · [字段定义](../../DATASET.md)*
