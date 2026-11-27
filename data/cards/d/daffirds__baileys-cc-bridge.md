# daffirds/baileys-cc-bridge

⭐ 3 · Go · MIT · 推送 2026-11-21 · [GitHub](https://github.com/daffirds/baileys-cc-bridge) · [官网](https://www.npmjs.com/package/baileys-cc-bridge) · 个人维护

**把 Claude Code/Codex 接入 WhatsApp 群聊的 Mac 桥接守护进程**

用 Go 编写的 macOS 守护进程，通过 Baileys 以 WhatsApp Web 链接设备方式将 WhatsApp 号码连接到 Mac，为选定的聊天各自启动一个 `claude -p` 或 `codex app-server` CLI 会话并持续续传消息。代理通过 MCP 工具在 WhatsApp 上发送消息、文件、贴纸、表情与定时任务，自身不主动发言；CLI 使用用户自己的登录，用量计入其 Claude 或 ChatGPT 套餐。提供浏览器面板扫码配对与配置（引擎、模型、自主级别、工作目录、系统提示词），支持 npm 安装或 Go 源码构建。限制：仅 macOS，需 Node 22.18+，离线期间消息丢失。

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

- 每个选定聊天独立 CLI 会话，重启后续传
- MCP 工具集：发消息/文件/贴纸/表情/定时任务
- 浏览器面板扫码配对并编辑配置
- 自主级别可设 full/auto/readonly

## 适用场景

- 让 Claude Code 在 WhatsApp 群里帮成员跑测试、改代码并回传结果
- 在家庭群部署代理做账单支付或提醒
- 在常开的 Mac mini 上托管个人 WhatsApp 代理

## 场景标签

`编码 Agent` `AI 助手` · 领域:编码与开发

## 证据(README 行号)

> L9: A small daemon for your Mac, written in Go. It links a WhatsApp number to the Mac the way WhatsApp Web
> L11: Claude Code or Codex session.
> L19: - Each chat you pick gets its own CLI session (`claude -p` or `codex app-server`), started by its


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `ab873b304b72` · [字段定义](../../DATASET.md)*
