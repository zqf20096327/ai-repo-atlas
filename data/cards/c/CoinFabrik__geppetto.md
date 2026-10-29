# CoinFabrik/geppetto

⭐ 21 · Python · AGPL-3.0 · 推送 2026-05-04 · [GitHub](https://github.com/CoinFabrik/geppetto) · [官网](https://deeptechia.io/) · 组织维护

**接入多种 AI 模型的 Slack 对话机器人，支持图片生成**

由 DeepTechia 开发的 Slack 机器人：团队成员通过私信或 @ 提及与机器人对话，可按消息内命令（llm_openai / llm_gemini / llm_claude）切换 ChatGPT、Gemini、Claude 模型，默认 gpt4-turbo；支持 DALL-E-3 在 Slack 会话中生成图片。配置基于 Slack App manifest 与环境变量（各模型 API key），部署方式包括 Poetry 源码运行与 Docker Compose，镜像发布于 Docker Hub。访问权限通过 allowed users 配置文件限制。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 消息内命令切换 ChatGPT / Gemini / Claude 多模型
- DALL-E-3 在 Slack 对话内直接生成图片
- Slack App manifest 配置流程与 .env 环境变量管理
- 提供 Docker Compose 部署与 Docker Hub 镜像

## 适用场景

- 在 Slack 工作区为团队成员提供 AI 对话入口
- 无需逐用户付费配置即可让全组使用多种 LLM
- 在频道讨论中 @ 机器人发起 AI 对话线程

## 场景标签

`聊天机器人` `图像生成` · 领域:对话与助手

## 证据(README 行号)

> L12: - 🔀 **Multi-Model Support:** Toggle effortlessly between AI models like ChatGPT, Claude and Gemini to suit your spe
> L17: - 🎨 **Creative Image Generation:** Unleash the power of DALL-E-3 to generate innovative images directly within your

## 星数曲线

```mermaid
xychart-beta
    title "CoinFabrik/geppetto 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-29 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `2bf328d7335c` · [字段定义](../../DATASET.md)*
