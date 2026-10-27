# chongzixuan-ai/openai-go-language

⭐ 22 · Go · Apache-2.0 · 推送 2025-11-01 · [GitHub](https://github.com/chongzixuan-ai/openai-go-language) · 个人维护

**Go 语言的 OpenAI API 非官方客户端库**

非官方的 OpenAI API Go 客户端库，覆盖 ChatGPT、GPT-3/GPT-4、DALL·E、GPT Image 1 图像生成、Whisper 语音转文字、Embedding、微调与结构化输出等接口，通过 go get 安装，要求 Go 1.18 及以上。提供代理配置、Azure OpenAI 接入、JSON Schema 函数调用辅助包与 APIError 错误处理示例；README 说明 temperature=0 因 omitempty 与 token 数量因素不保证确定性输出，且不提供 token 计数功能。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 覆盖聊天补全、图像生成、语音转文字、Embedding、微调等 OpenAI 接口
- 支持 Azure OpenAI 与代理配置
- 内置 jsonschema 包辅助函数调用定义
- 提供流式补全与结构化输出示例

## 适用场景

- 在 Go 项目中调用 OpenAI 的对话、图像与语音接口
- 通过 Azure OpenAI 使用同一套 Go 客户端
- 实现带函数调用与结构化输出的 LLM 应用

## 场景标签

 · 领域:LLM 基础设施/API 客户端

## 证据(README 行号)

> L6: This library provides unofficial Go clients for OpenAI API. We support:
> L16: go get github.com/sashabaranov/go-openai

## 星数曲线

```mermaid
xychart-beta
    title "chongzixuan-ai/openai-go-language 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-27 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `34d768081b02` · [字段定义](../../DATASET.md)*
