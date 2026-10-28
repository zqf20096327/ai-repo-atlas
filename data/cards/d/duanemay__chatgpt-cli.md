# duanemay/chatgpt-cli

⭐ 38 · Go · Apache-2.0 · 推送 2026-10-18 · [GitHub](https://github.com/duanemay/chatgpt-cli) · 个人维护

**命令行调用 ChatGPT 的 CLI 工具：聊天/图像/语音/转录/嵌入**

用 Go 编写的命令行客户端，通过 OpenAI/ChatGPT API 提供交互式与非交互式（管道/stdin）两类用法：chat 对话、image 文生图、vision 图像理解、speech 文本转语音、transcribe 音频转写、embedding 生成向量，另有 list-models 与 replay-session 命令。支持会话文件保存与回放，配置按命令行参数 > 环境变量 > 配置文件 > 默认值排序。需要用户提供 ChatGPT API key 并充值账户；通过 Homebrew cask 或 GitHub releases 预编译二进制安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- chat/image/vision/speech/transcribe/embedding 六类模型调用命令
- 支持管道与重定向的非交互式模式，可批量处理文件
- 会话文件保存与 replay-session 回放
- 配置四级优先级：命令行 > 环境变量 > 配置文件 > 默认值

## 适用场景

- 在终端直接与 ChatGPT 对话或提问
- 用管道批量改写文档、生成笔记封面图
- 在脚本中调用文本转语音、音频转写或生成嵌入向量

## 场景标签

`AI 助手` `图像生成` `语音合成` `语音识别` · 领域:对话与助手

## 证据(README 行号)

> L3: The ChatGPT CLI allows you to interact with ChatGPT directly from your command line, offering an efficient platform 
> L16: { echo "What is the largest file in this directory?"; ls -l } | chatgpt-cli chat
> L46: echo "Monkey in a banana costume, on a high wire above a circus" | chatgpt-cli image -o monkey
> L277: 1. `chat`: Start a chat session with ChatGPT.

## 星数曲线

```mermaid
xychart-beta
    title "duanemay/chatgpt-cli 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 37 --> 39
    line [38, 38]
```

2026-10-18 38 → 2026-10-28 38（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `03bf3e5dbbfb` · [字段定义](../../DATASET.md)*
