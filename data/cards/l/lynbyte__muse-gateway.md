# lynbyte/muse-gateway

⭐ 7 · TypeScript · MIT · 推送 2026-11-21 · [GitHub](https://github.com/lynbyte/muse-gateway) · [官网](https://www.npmjs.com/package/muse-gateway) · 个人维护

**把 muse.ai 账号转成 OpenAI 兼容 API 的本地网关**

基于 Node.js 的网关服务，通过浏览器驱动用户自有的 muse.ai 账号，将其能力以 OpenAI 兼容 API 暴露，覆盖 chat completions、responses、图像生成、语音合成与模型列表端点；视频通过任务 API 以轮询或 webhook 获取。核心机制包括多账号池（round-robin/failover/parallel）、按账号并发控制、MCP server 接入 Claude/Cursor 等代理，以及带账号管理、API key、用量统计和日志的仪表盘。支持 Windows 托盘常驻，可通过 Cloudflare tunnel、Tailscale 或 Telegram bot 远程访问。README 提醒用户自行确认符合 muse.ai 服务条款。

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

- OpenAI 兼容端点：chat/responses/images/audio/models（L15）
- MCP server 供 Claude、Cursor 等代理接入（L17）
- 多账号池与按账号自动并发、故障转移（L18）
- 仪表盘管理账号、API key、用量与日志（L19）

## 适用场景

- 让只支持 OpenAI API 的工具直接调用 muse.ai 的图像和视频生成
- 在多个 muse.ai 账号间做负载与故障转移
- 通过 Telegram bot 用 /vid /img /voice 命令远程生成内容

## 场景标签

`图像生成` `视频生成` `语音合成` · 领域:内容生成

## 证据(README 行号)

> L7: Turn your own muse.ai accounts into an **OpenAI-compatible API** that runs on your machine or VPS. Chat, images and 
> L15: - **OpenAI-compatible:** `/v1/chat/completions`, `/v1/responses`, `/v1/images/generations`, `/v1/audio/speech`, `/v
> L18: - **Account pool:** round-robin, failover or parallel across several Muse accounts, with automatic concurrency per 


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `b4130a9e0a76` · [字段定义](../../DATASET.md)*
