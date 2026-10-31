# abczsl520/weixin-bot

⭐ 13 · JavaScript · MIT · 推送 2026-03-22 · [GitHub](https://github.com/abczsl520/weixin-bot) · 个人维护 · 中文 README

**一条命令启动的微信 AI 聊天机器人，可选多种 AI 提供商**

基于 Node.js 的微信 AI 机器人 CLI 工具：通过 npx 一条命令启动，扫码登录后由另一个微信号向 Bot 发消息获得 AI 回复。内置 9 种提供商选择（OpenAI/Claude/Gemini/Ollama/Codex/Claude Code/OpenClaw/自定义 OpenAI 兼容 API/回声模式），支持 Codex 与 Claude Code 的 Agent 模式在本机写代码。使用微信 iLink Bot API 而非 hook，API 密钥 AES-256-CBC 加密存盘，含限流、自动重连与 Docker Alpine 镜像。限制：仅能收到用户主动发给 Bot 的消息，不能监听聊天或冒充个人号，需 Node.js 18+，目前支持 iOS 微信 8.0.70 与安卓（安卓可能有 Bug）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- npx 一条命令启动，零依赖，无需服务器与配置文件
- 9 种 AI 提供商可选，含本地 Ollama 与任意 OpenAI 兼容 API
- Codex/Claude Code Agent 模式可在本机执行编程任务
- API 密钥 AES-256-CBC 加密、机器指纹绑定、限流与日志脱敏

## 适用场景

- 给自己的微信号接入 AI 自动回复
- 通过微信对话让编程 Agent 在本机写代码
- 用 Ollama 本地模型跑免费微信 AI 机器人

## 场景标签

`聊天机器人` `编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L77: 现在用另一个微信号给你的 Bot 发消息试试！Bot 会自动回复。
> L109: |**Ollama**|`--provider ollama`|本地运行 AI，完全免费|

## 星数曲线

```mermaid
xychart-beta
    title "abczsl520/weixin-bot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `6671b74a7d37` · [字段定义](../../DATASET.md)*
