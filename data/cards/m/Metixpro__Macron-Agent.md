# Metixpro/Macron-Agent

⭐ 13 · Go · MIT · 推送 2026-11-18 · [GitHub](https://github.com/Metixpro/Macron-Agent) · 个人维护 · 中文 README

**自托管的个人 AI 代理，桌面/终端/Telegram 三端执行真实任务**

以 Go 编写、运行在用户自己机器上的个人 AI 代理，跨 Windows/Linux/macOS，提供桌面应用、交互式终端 UI 与 Telegram 机器人三种界面。通过真实工具执行任务：读写项目代码、执行命令与测试、Git 操作、生成 Word/PowerPoint、网络搜索、服务器管理等。用户自选模型服务（OpenAI/Anthropic/Gemini/OpenRouter/DeepSeek/Ollama 等），支持本地 endpoint 使推理留在本机。具备持久记忆文件（SOUL.md/USER.md/MEMORY.md）、可编辑技能、MCP 服务器与插件扩展、危险命令确认、SSH 远程服务器控制。Windows 安装包未经数字签名会触发 SmartScreen 提示。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 桌面应用、终端 UI、Telegram 机器人三种界面
- 持久记忆与可编辑技能，配置保存在用户自己的 profile
- MCP 服务器与插件可从设置中添加启停，工具跨三端可用
- SSH 远程控制已安装 macron 的服务器，不开放互联网端口

## 适用场景

- 在项目文件夹里让代理读代码、跑测试、写文档
- 通过 Telegram 远程指挥家中或服务器上的代理做事
- 用本地模型 endpoint 让推理留在自己的机器上
- 让代理定时跑长任务、管理服务器与进程

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L8: A personal AI agent for Windows, Linux and macOS — desktop, terminal and messaging.
> L35: مکرون یک عامل شخصی با Go است که روی ماشین خودت اجرا می‌شود و کار را با ابزارهای واقعی پیش می‌برد: از بررسی پروژه و 
> L125: |مدل و افزونه|پروایدر دلخواه، مسیریابی، اجرای چندمدلی، پلاگین و MCP|

## 星数曲线

```mermaid
xychart-beta
    title "Metixpro/Macron-Agent 星数(近 3 点)"
    x-axis ["2026-11-14", "2026-11-18", "2026-11-20"]
    y-axis "stars" 11 --> 14
    line [12, 13, 13]
```

2026-11-14 12 → 2026-11-20 13（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-18 · 置信度 mid · 依据 README sha `e93d04397474` · [字段定义](../../DATASET.md)*
