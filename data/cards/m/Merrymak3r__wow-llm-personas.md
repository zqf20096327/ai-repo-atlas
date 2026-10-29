# Merrymak3r/wow-llm-personas

⭐ 24 · Python · MIT · 推送 2026-07-19 · [GitHub](https://github.com/Merrymak3r/wow-llm-personas) · 个人维护

**给 CMaNGOS/playerbots 机器人注入本地 LLM 人格的游戏服务垫片**

约 230 行、仅用标准库的 Python 垫片，把 playerbots 的 LLM 聊天钩子（KoboldCpp 形状的 API）转发到本地 Ollama，为每个机器人注入人格（文本文件人格或按名字确定性生成的程序化人格）、按 (bot, speaker) 维护对话记忆、触发机器人间斗嘴并做输出清洗（去标签、剧透、注入回显等）。需先自建 CMaNGOS 1.12 + playerbots 服务器与 Ollama 运行时；默认模型为 3B 未审查微调版，约占 2.6 GB VRAM，全部离线运行。零依赖，直接 python shim.py 启动。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- personas/<name>.txt 文本文件注入人格，无文件机器人按 md5(名字) 确定性生成程序化人格
- 按 (bot, speaker) 键的环形缓冲对话记忆，无全局串线
- 机器人间斗嘴模式带亚临界概率控制（推荐 20% 防反馈风暴）
- 输出清洗：剥离标签、旁白、注入回显、非 BMP 字符与复读脚手架

## 适用场景

- 给自己的魔兽世界私服队友机器人加性格与记忆
- 搭建全部离线、数据不出局域网的 AI NPC 聊天服务器
- 给数百个环境机器人生成稳定且互不重复的程序化人格

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L3: A tiny (~230-line, **stdlib-only**) Python shim that gives CMaNGOS +
> L39: So instead of running KoboldCpp, you point it at **this shim**, which speaks that shape on the front
> L40: and talks to **Ollama** on the back. In between, it does the three things that turn "an LLM answered"

## 星数曲线

```mermaid
xychart-beta
    title "Merrymak3r/wow-llm-personas 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-29 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `672ff20e0604` · [字段定义](../../DATASET.md)*
