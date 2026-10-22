# BOTCAHX/RTXZY-MD

⭐ 462 · JavaScript · MIT · 推送 2026-10-11 · [GitHub](https://github.com/BOTCAHX/RTXZY-MD) · [官网](https://api.botcahx.eu.org) · 组织维护

**WhatsApp 多设备机器人：消息应答、媒体处理与 MCP 开发接口**

基于 zapo-js 的 WhatsApp 多设备机器人（ESM、Node.js 22+），支持 Pairing Code 与 QR 双认证方式，会话与数据库使用 SQLite（WAL，可选 MongoDB/JSON 后端）。功能通过 BOTCAHX Rest API 提供（需 API key，免费档每日 15 次请求），依赖 ffmpeg/ImageMagick/webp 处理媒体。内置 @zapo-js/mcp-server，可将 WhatsApp 连接、发消息、群组查询等暴露为 MCP tools 供 Claude Code、Cursor 等 LLM agent 在开发/测试场景调用。支持 Pterodactyl、Render、Heroku 部署，不支持 Termux。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Pairing Code 默认认证，--qr 可切 QR 模式
- SQLite 会话与数据库（WAL），可选 MongoDB/JSON/cloud 后端
- 内置 MCP server 将 zapo-js 会话暴露为 LLM agent tools（stdio/http）
- 提供 13 个启动参数（--self/--gconly/--autoread 等）

## 适用场景

- 搭建自己的 WhatsApp 群组/私聊应答机器人
- 通过 MCP 让 Claude Code 等 agent 在开发测试中收发 WhatsApp 消息
- 部署到 Pterodactyl/Render/Heroku 等托管平台运行

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L107: Bot ini menggunakan **97% fitur dari Rest API**, jadi kamu **wajib mengisi Apikey**.
> L153: Bot ini sudah menyertakan `@zapo-js/mcp-server` — server Model Context Protocol yang mengekspos sesi `zapo-js` (ko

## 星数曲线

```mermaid
xychart-beta
    title "BOTCAHX/RTXZY-MD 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22"]
    y-axis "stars" 461 --> 464
    line [463, 462, 462]
```

2026-10-18 463 → 2026-10-22 462（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `9e493841b65a` · [字段定义](../../DATASET.md)*
