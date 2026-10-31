# OpenChara/OpenCharaAgent

⭐ 14 · Python · Apache-2.0 · 推送 2026-10-19 · [GitHub](https://github.com/OpenChara/OpenCharaAgent) · 组织维护 · 中文 README

**开源 AI 角色扮演 agent 运行框架，一键创建可持续协作的角色**

以持久进程方式运行 AI 角色卡（chara）：每个角色拥有独立工作区、记忆与日程，可在消息间隔自主工作并产出网站、代码、音乐等文件。兼容 SillyTavern V1/V2/V3 卡片格式并内置卡片市场；通过终端工具（python3/node/git/ffmpeg）与浏览器进行创作，工具调用运行在 OS 级沙箱（sandbox-exec/bubblewrap/Landlock）并记录审计日志。模型接入支持 OpenRouter、OpenAI、火山方舟、混元、DashScope 及任何 OpenAI 兼容端点（含本地 Ollama），未配置时提供离线 mock 引擎。支持 WeChat/QQ/Telegram/Discord/Slack 消息网关。一条命令安装预编译 wheel，面向 macOS/Linux，自称 Beta。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 持久角色进程：独立工作区、持久记忆与日程
- SillyTavern V1/V2/V3 卡片导入与内置卡片市场
- OS 级沙箱（sandbox-exec/bubblewrap/Landlock）与逐次工具调用审计日志
- WeChat/QQ/Telegram/Discord/Slack 消息网关，仅投递 speak 输出

## 适用场景

- 导入 SillyTavern 角色卡并让角色持续陪伴创作
- 通过微信/QQ/Telegram 等聊天工具与自托管角色对话
- 自建服务器多角色托管并用手机浏览器访问

## 场景标签

`聊天机器人` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L5:  An open source AI roleplay agent harness. One click builds an autonomous character agent
> L25: OpenCharaAgent runs AI characters as persistent agents. Each character (a **chara**) keeps its own workspace, memor
> L30: 2. 🎨 **Co-creation.** With tools enabled, a chara builds websites, writes code, makes music and video, draws, and w

## 星数曲线

```mermaid
xychart-beta
    title "OpenChara/OpenCharaAgent 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-31"]
    y-axis "stars" 12 --> 15
    line [13, 14, 14]
```

2026-10-18 13 → 2026-10-31 14（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `1e6d5bdff51a` · [字段定义](../../DATASET.md)*
