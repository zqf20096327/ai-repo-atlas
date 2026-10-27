# kocort/kocort

⭐ 25 · Go · MIT · 推送 2026-04-12 · [GitHub](https://github.com/kocort/kocort) · [官网](https://kocort.com) · 个人维护 · 中文 README

**免命令行的桌面 AI Agent 助手，云端推理+本地安全审查**

面向不熟悉命令行的个人用户的桌面级 AI Agent 应用。核心是双脑架构：云端/远端 LLM（OpenAI、Anthropic 等兼容接口）负责推理，本地 1.7B 量化小脑模型离线对每次 tool_call 做语义安全审查（意图一致性、注入攻击、数据外泄），本地模型也可完全替代云端后端。内置 30+ 工具、技能系统、子代理编排、cron 调度，并适配飞书/Telegram/Discord/Slack 等消息渠道。采用 7 层安全模型，Go 单二进制编译、内嵌 Next.js 前端，支持 Windows/macOS/Linux 桌面打包。构建需 Go 1.23+ 与 Node.js 20+，本地推理可选 llama.cpp 共享库（自动下载）。

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

- 云端 Brain 推理 + 本地 Cerebellum 离线语义安全审查的双脑架构
- 30+ 内置工具与 7 层安全模型（策略/分级拦截/沙箱/审批/环路检测等）
- 飞书/Telegram/Discord/Slack/WhatsApp 等多消息渠道适配
- Go 单二进制部署，内嵌 Web 前端，支持本地 llama.cpp 推理替代云端

## 适用场景

- 不熟悉命令行的用户开箱即用获得带工具执行能力的个人 AI 助手
- 通过飞书/Telegram 等消息渠道远程使用 Agent 并接收主动推送
- 对敏感数据要求不出本机、需要本地模型离线运行的 Agent 场景

## 场景标签

`AI 助手` `聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L21: Kocort is a **desktop-grade AI Agent application**, similar to OpenClaw, designed to give everyone—even those unfam
> L50: - **Brain**: Cloud/remote LLM handles reasoning and decision-making (supports OpenAI, Anthropic, etc.)
> L51: - **Cerebellum**: Local 1.7B quantized model, runs fully offline

## 星数曲线

```mermaid
xychart-beta
    title "kocort/kocort 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-27 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `33894047d933` · [字段定义](../../DATASET.md)*
