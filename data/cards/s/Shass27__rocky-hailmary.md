# Shass27/rocky-hailmary

⭐ 10 · Python · MIT · 推送 2026-04-08 · [GitHub](https://github.com/Shass27/rocky-hailmary) · 个人维护

**本地 Ollama 角色扮演 Rocky 的粉丝 AI 聊天项目**

基于 Ollama 和自定义 Modelfile 的本地 AI 聊天项目，角色扮演《挽救计划》中的 Eridian 工程师 Rocky。使用 Meta Llama 3 作为基座模型，通过 ollama create 从 Modelfile（含系统提示词）构建本地模型 rocky。提供两种使用方式：Ollama 应用/CLI 直接聊天，或基于 Rich 库的 Python 终端 UI（经 Ollama 本地 API 连接，TUI 模式需 Python 3.10+）。首次拉取 llama3 需联网，运行本身在本地设备完成。项目为非商业粉丝作品。

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

- 自定义 Modelfile 定义 Rocky 角色与系统提示词
- 两种聊天方式：Ollama CLI 与 Python 终端 UI
- 完全本地运行，仅首次拉模型需联网

## 适用场景

- 与 Project Hail Mary 中的 Rocky 角色本地对话
- 体验基于 Llama 3 的离线角色扮演聊天

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L3: Local AI chat experience that roleplays Rocky (the Eridian engineer from
> L18: - `model/ModelFile` - Rocky model definition and system prompt
> L56: ollama create rocky -f model/ModelFile


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 mid · 依据 README sha `afd85cf11a27` · [字段定义](../../DATASET.md)*
