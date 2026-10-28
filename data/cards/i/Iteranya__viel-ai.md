# Iteranya/viel-ai

⭐ 24 · Python · AGPL-3.0 · 推送 2026-08-02 · [GitHub](https://github.com/Iteranya/viel-ai) · 个人维护

**自托管的多角色 Discord AI 角色扮演机器人**

用 Python/FastAPI/SQLAlchemy 编写的自托管 Discord 机器人，面向沉浸式多角色扮演场景：可创建任意数量角色、按频道并行运行场景、角色间对话，并支持导入 SillyTavern 角色文件。提供 Web 控制面板（localhost:5666）管理角色、频道白名单与世界观设定，内置基于 Jinja2 的提示词模板工作室。AI 后端可自选：接入 OpenAI/Claude 等服务，或用 LM Studio/Ollama 跑本地模型；支持网页阅读与 search> 联网查询。安装提供 Windows installer.bat 或 Docker（含 Watchtower 自动更新），处于 Beta 阶段。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 多角色按频道并行扮演，角色间可互相对话
- Jinja2 提示词模板工作室，可编程角色动态行为
- AI 后端自由切换：OpenAI/Claude 或 LM Studio/Ollama 本地模型
- 支持导入 SillyTavern 角色文件

## 适用场景

- 在 Discord 服务器里搭建多角色并行剧情扮演
- 用本地模型实现零成本的 AI 角色扮演
- 自托管掌控角色、对话与社区数据的所有权

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L27: I am a **universal Discord bot designed for immersive, multi-character roleplay**. I'm here to be your ultimate sto
> L84: * **Run a Free, Private AI:** If you're more tech-savvy, you can run a free AI model on your own computer using too

## 星数曲线

```mermaid
xychart-beta
    title "Iteranya/viel-ai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-28 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `9caaf74a8b9b` · [字段定义](../../DATASET.md)*
