# nubidubi09/Bloub

⭐ 5 · HTML · MIT · 推送 2026-11-27 · [GitHub](https://github.com/nubidubi09/Bloub) · [官网](https://nubidubi09.github.io/Bloub/) · 个人维护

**驻留 Mac 刘海区的主动式 AI 助手，含浏览器与 agent 模式**

以 Swift/SwiftUI 编写的 macOS 应用，驻留刘海屏并提供完整窗口，包含聊天、编码模式与自带浏览器。默认通过用户自备的 Claude API key 调用 Anthropic 模型；主动模式按周期查看日历、准备会议笔记等，文件操作带 Undo 与审批门槛。接入 MCP 服务（Notion、Linear、Figma 等 88 项清单）、Mac 日历与本地记忆；亦可在设置中添加 OpenAI/Gemini/Kimi 等其他提供方（README 标注未经真实服务测试）。通过 Homebrew 构建安装，要求 macOS 27.2+ 与 Xcode。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 驻留刘海区：快捷键 ⌥⌘ 语音或文字提问，并附带屏幕截图作为上下文
- Code 模式：指定文件夹内读写文件、运行终端命令，支持 subagents 与 sub-sessions
- Connectors：88 项 MCP 服务清单，工具级 Allow/Ask/Block 权限控制
- 主动模式每 15 分钟检查日历与会话变化，带每日/每月消费上限

## 适用场景

- 在 Mac 上通过对话完成编码任务并审批文件改动
- 让助手根据日历主动准备会议材料与早晚简报
- 用 MCP 连接 Notion、Linear 等服务由助手调用工具

## 场景标签

`AI 助手` `编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L11: An AI assistant for the Mac. He lives in the notch and has a full app window with a chat and a coding mode.
> L12: Bloub is a small cloud with eyes, written in Swift, and runs on Claude with your own API key.
> L148: Opus 5.5, Sonnet 5.5 or Haiku 5.5.


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `863b4ebc34af` · [字段定义](../../DATASET.md)*
