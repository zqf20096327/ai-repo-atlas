# tinovyatkin/amazon-bedrock-copilot-chat

⭐ 33 · TypeScript · MIT · 推送 2026-10-24 · [GitHub](https://github.com/tinovyatkin/amazon-bedrock-copilot-chat) · 个人维护

**把 Amazon Bedrock 模型接入 GitHub Copilot Chat 的 VSCode 扩展**

基于 VSCode 官方 Language Model Chat Provider API 与 AWS SDK for JavaScript 构建的 VSCode 扩展，使 GitHub Copilot Chat 可调用 Amazon Bedrock 上的 Claude、DeepSeek、OpenAI OSS 等模型。支持 AWS Profile/API Key/Access Keys 三种认证方式、流式输出、函数调用、跨区域推理、Claude 扩展思考与 1M 上下文窗口、提示缓存与图像输入。自动过滤仅显示支持工具调用的文本生成模型，排除嵌入、图像生成与 LEGACY 生命周期模型。限制：仅支持 Copilot 个人计划，组织计划暂不可用；需 VSCode 1.104.0+ 与 AWS Bedrock 访问权限。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 通过官方 Language Model Chat Provider API 接入 Bedrock 模型
- 三种 AWS 认证方式，凭据存于 VSCode SecretStorage
- 支持流式输出、函数调用、跨区域推理、提示缓存与 Vision
- 自动过滤仅显示支持工具调用的文本模型，排除已弃用模型

## 适用场景

- 在 Copilot Chat 中使用自有 AWS 账号下的 Bedrock 模型
- 为 Copilot Chat 配置 Claude 扩展思考与 1M 上下文窗口
- 通过 AWS Profile 或 API Key 管理模型访问凭据

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L3: A VSCode extension that brings Amazon Bedrock models into GitHub Copilot Chat using VSCode's official Language Model
> L7: - VSCode's **Language Model Chat Provider API** for integrating custom models into Copilot Chat

## 星数曲线

```mermaid
xychart-beta
    title "tinovyatkin/amazon-bedrock-copilot-chat 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-26 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `df832107f722` · [字段定义](../../DATASET.md)*
