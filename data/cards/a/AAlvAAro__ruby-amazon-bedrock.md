# AAlvAAro/ruby-amazon-bedrock

⭐ 17 · Ruby · MIT · 推送 2026-02-26 · [GitHub](https://github.com/AAlvAAro/ruby-amazon-bedrock) · 个人维护

**Ruby 封装 Amazon Bedrock API 的文本与图像生成客户端库**

面向 Ruby 开发者的 AWS Amazon Bedrock 客户端 gem：通过传入 AWS IAM 凭据或 Named Profile 实例化 Client，用 invoke_model 调用 Bedrock 上的模型，覆盖 AI21 Labs、Amazon Titan、Anthropic、Cohere、Meta、Stability AI 等提供商的文本生成、摘要、嵌入等能力，支持各模型特定参数配置。需要用户自行申请模型访问权限并承担 Bedrock 使用费用；Cohere embed 模型调用标注为 WIP。README 顶部声明该 gem 已停止维护，建议改用 RubyLLM。

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

- invoke_model 统一调用 Bedrock 上多家提供商模型
- 支持 AWS IAM 凭据与 Named Profiles 两种认证方式
- 各模型可选参数配置（temperature/top_p/max_tokens 等）
- README 声明项目已废弃，推荐迁移到 RubyLLM

## 适用场景

- 在 Ruby/Rails 应用中调用 Bedrock 模型做文本生成或摘要
- 通过同一客户端切换 Anthropic/Meta/Cohere 等不同模型
- 用 Cohere embed 模型构建语义检索（功能标注 WIP）

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L8: Seamless Integration with Amazon Bedrock API for AI-Powered Text and Image Generation in Ruby 🤖 + 💎. Amazon Bedrock 
> L59: client = RubyAmazonBedrock::Client.new(
> L92: Amazon Bedrock is a fully managed service that makes FMs from leading AI startups and Amazon available via an API, 

## 星数曲线

```mermaid
xychart-beta
    title "AAlvAAro/ruby-amazon-bedrock 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-30 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `94e9f07afebd` · [字段定义](../../DATASET.md)*
