# yagi-agent/yagi

⭐ 45 · Go · 推送 2026-09-01 · [GitHub](https://github.com/yagi-agent/yagi) · 个人维护

**多 LLM 供应商的 CLI 聊天客户端，支持运行时 Go 插件**

基于 Yaegi 解释器的命令行聊天客户端：支持 OpenAI、Google、Anthropic、DeepSeek、Groq、Qwen 等 16 家云服务商，也可通过自定义 providers.json 接入 llama-server、Ollama、LM Studio 等本地模型服务。工具以纯 Go 源文件形式放置在 ~/.config/yagi/tools/ 下，启动时解释加载，无需重新编译；内置记忆系统（remember/recall/list_memories）、技能与身份文件、按目录保存并恢复会话（保留最近 100 条消息）、自主模式与计划模式。安装方式为 go install，MIT 许可，作者为 mattn。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 16 家云 LLM 供应商 + 本地 llama-server/Ollama/LM Studio 接入
- Yaegi 运行时加载 Go 源码插件，无需重编译
- 持久记忆系统与 remember/recall/list_memories 内置工具
- 按目录保存会话并支持 -resume 恢复（保留工具调用历史）

## 适用场景

- 在终端中跨多家 LLM 供应商进行对话或一次性命令执行
- 用自然语言驱动的工具调用做代码审查等日常任务
- 以无编译方式编写和加载自定义 Go 工具扩展能力
- 接入本机或局域网内自部署模型进行对话

## 场景标签

`聊天机器人` `AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L3: A CLI chat client for multiple LLM providers with a plugin system powered by Yaegi.
> L98: Models are specified in `provider/model` format. The following providers are supported:

## 星数曲线

```mermaid
xychart-beta
    title "yagi-agent/yagi 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 44 --> 46
    line [45, 45]
```

2026-10-18 45 → 2026-10-28 45（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `e6e508fb583b` · [字段定义](../../DATASET.md)*
