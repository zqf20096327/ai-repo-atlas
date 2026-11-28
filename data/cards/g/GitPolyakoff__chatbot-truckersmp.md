# GitPolyakoff/chatbot-truckersmp

⭐ 10 · C# · MIT · 推送 2026-06-26 · [GitHub](https://github.com/GitPolyakoff/chatbot-truckersmp) · 个人维护

**TruckersMP 游戏内聊天机器人：提供服务器查询与 AI 问答**

面向欧洲卡车模拟 2 / 美洲卡车模拟联机平台 TruckersMP 玩家的聊天机器人，通过读取游戏聊天日志文件监听消息，支持 !gpt、!serverinfo、!players、!events 等命令，分别提供 AI 问答、服务器状态、在线人数、活动查询。AI 问答经 OpenRouter API 完成，用户可在配置时选择模型与最大 token 数；内置多语言违禁词过滤以阻止不当输出。以 Windows 可执行文件分发，首次运行需输入 API key、过滤词表路径与模型名，配置自动保存。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 读取 TruckersMP 聊天日志并在游戏内回复命令
- !gpt 命令经 OpenRouter API 获取 AI 回答，自动跟随提问语言
- 多语言违禁词过滤（含混淆变体检测）
- 以 tmp-bot.exe 单文件分发，首次配置后自动保存

## 适用场景

- 在 TruckersMP 联机聊天中直接向 AI 提问
- 查询当前服务器状态与全服在线人数
- 查看即将开始的联机活动（convoy 等）

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L3: A simple chat bot for **TruckersMP** (ETS2 / ATS).
> L5: It also connects to **OpenRouter API** for AI answers, allowing you to choose from various powerful models.
> L8: - `!gpt <text>` → ask AI (via OpenRouter API). The bot will answer in the same language as the question.

## 星数曲线

```mermaid
xychart-beta
    title "GitPolyakoff/chatbot-truckersmp 星数(近 2 点)"
    x-axis ["2026-10-26", "2026-11-28"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-26 10 → 2026-11-28 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `27974e784d2a` · [字段定义](../../DATASET.md)*
