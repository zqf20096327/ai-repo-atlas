# johndotpub/DiscordianAI

⭐ 26 · Python · Unlicense · 推送 2026-10-29 · [GitHub](https://github.com/johndotpub/DiscordianAI) · [官网](https://github.com/johndotpub/DiscordianAI) · 个人维护

**Discord AI 聊天机器人：OpenAI GPT-5 与 Perplexity 双后端混合路由**

用 Python 编写的开源 Discord 机器人，在频道与私信中提供 AI 对话：Smart Hybrid 模式按语义分析将消息路由到 GPT-5（推理/创作）或 Perplexity Sonar-Pro（时事与引用），并含仅用单一后端的模式。机制包括追问一致性检测、引用感知 embed、消息自动分段、HTTP/2 连接池与熔断、健康检查。需自备 Discord/OpenAI/Perplexity token，通过 config.ini 配置，支持 pip 源码安装、launcher 脚本、systemd 与 Docker 部署。Python 3.12+，Unlicense 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Unlicense |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Smart Hybrid 模式按消息语义在 GPT-5 与 Sonar-Pro 间路由，追问保持同一服务
- 引用感知 embed 与按 Discord 字数限制的消息自动分段
- HTTP/2 连接池、熔断器与启动时健康检查
- 提供 launcher 脚本与 --install-systemd 一键生成 systemd 用户单元

## 适用场景

- 在 Discord 服务器里让成员通过 @ 提及或 DM 与 AI 对话
- 研究/新闻型服务器使用 Perplexity 模式获得带引用的回答
- 创作/编程型服务器固定使用 GPT-5 后端

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L23: DiscordianAI is a production-ready Discord bot that blends OpenAI GPT-5 frontier models with Perplexity Sonar-Pro w
> L37: | 🧠 **Smart Hybrid** | Analyze each message, then route to GPT-5 or Sonar-Pro with follow-up consistency.

## 星数曲线

```mermaid
xychart-beta
    title "johndotpub/DiscordianAI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-30 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `7fe7ca88cc50` · [字段定义](../../DATASET.md)*
