# whobot-ai/claude-code-feishu-channel

⭐ 26 · TypeScript · 推送 2026-03-22 · [GitHub](https://github.com/whobot-ai/claude-code-feishu-channel) · 组织维护 · 中文 README

**连接飞书与 Claude Code 的 Channel 插件：飞书消息直达本地会话**

Claude Code 的社区飞书（Feishu/Lark）Channel 插件，以本地 MCP 服务器形式运行，通过飞书 WebSocket 长连接接收消息并经 stdio 转发给本机 Claude Code 会话，Claude 完成工作后将结果回复到飞书，无需公网 IP。支持图片/文件双向传输、6 位配对码认证、pairing/allowlist/disabled 三种访问策略、群组聊天（@提及触发）与 Lark 国际版域名配置。提供 5 个 MCP 工具（reply/react/edit_message/download_attachment/fetch_messages）。需 Claude Code v2.1.80+ 与 Bun 运行时，当前自定义 Channel 需以 --dangerously-load-development-channels 标志启动。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 飞书消息经 WebSocket 长连接推送至本地 Claude Code 会话，无需公网 IP
- 6 位配对码认证与 pairing/allowlist/disabled 访问策略
- 图片与文件附件双向传输、群组 @提及触发
- 提供 reply/react/edit_message/download_attachment/fetch_messages 五个 MCP 工具

## 适用场景

- 在飞书中远程指挥本机 Claude Code 写代码、查问题
- 出差时通过飞书群组与 Claude 沟通并接收任务结果
- 仅授权白名单同事使用自己的 Claude Code 会话

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L29: Claude 的回复 ◀─────────│   (本地 MCP 服务)  │◀─── stdio ────  (你的终端)
> L33: - 插件作为 MCP 服务器运行在你的本地机器上

## 星数曲线

```mermaid
xychart-beta
    title "whobot-ai/claude-code-feishu-channel 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-26 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `987f8072ae5d` · [字段定义](../../DATASET.md)*
