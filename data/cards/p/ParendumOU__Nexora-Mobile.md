# ParendumOU/Nexora-Mobile

⭐ 14 · TypeScript · MIT · 推送 2026-09-01 · [GitHub](https://github.com/ParendumOU/Nexora-Mobile) · [官网](https://nexora.parendum.com) · 组织维护

**自托管 Nexora 工作区的原生 iOS/Android 聊天客户端**

基于 Expo（React Native + TypeScript）构建的原生移动客户端，连接用户自托管的 Nexora（AI-agent 编排平台）实例，通过 Web 端展示的配对二维码完成设备绑定后，以流式方式与自有 agent 对话。每台设备持有独立可撤销的 nxd_ 密钥并存于系统钥匙串，设备端不输入密码；令牌为标准 Nexora JWT，可访问全部 REST/WebSocket 端点。需服务端完成 051_device_tokens 迁移并部署 /api/auth/device/* 端点。开发与构建使用 pnpm 和 EAS，明确禁止在宿主机使用 npm。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- QR 扫码一次性配对，设备持有独立可撤销令牌（存于 OS 钥匙串）
- 流式对话自家服务器上的 agent，数据不经第三方后端
- 令牌为标准 Nexora JWT，适用于全部 REST/WebSocket 端点
- 服务端需 core migration 051_device_tokens 与 /api/auth/device/* 端点

## 适用场景

- 在手机上随时与自托管 Nexora agent 对话
- LAN/VPN 环境下安全访问私有部署的 AI 工作区
- 为团队成员分发可单独撤销的移动设备访问凭证

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L5: **Native iOS + Android client for self-hosted Nexora
> L24: The app connects to **your own** Nexora instance (LAN or VPN). It is linked to a workspace
> L30: - **📱 Your agents in your pocket.** Chat with self-hosted Nexora agents, with live streaming replies.

## 星数曲线

```mermaid
xychart-beta
    title "ParendumOU/Nexora-Mobile 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `514f6413bd3d` · [字段定义](../../DATASET.md)*
