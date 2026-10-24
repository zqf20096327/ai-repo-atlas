# FullStackWithLawrence/aws-openai

⭐ 68 · Python · AGPL-3.0 · 推送 2026-10-14 · [GitHub](https://github.com/FullStackWithLawrence/aws-openai) · [官网](https://openai.lawrencemcdaniel.com/) · 个人维护

**OpenAI 官方示例的全栈实现：React+AWS Serverless 聊天应用模板**

将 OpenAI API 官方文档中的 30 个示例应用以 ReactJS 前端 + AWS Serverless（Lambda、Terraform、API 网关）后端形式实现的教学项目，覆盖 ChatGPT、DALL·E、Whisper、TTS、Embeddings 等接口，并集成 LangChain 端点。用户通过 make 命令完成脚手架、Terraform 初始化、构建与本地运行。附带基于 YAML 的 Function Calling 插件模型，可作为 YouTube 频道与 UBC 课程的配套教材。运行需要 AWS 账号、Terraform、Python 3.11、NPM 与 Docker Compose。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 实现 OpenAI 官方文档 30 个示例应用（GPT-3.5/GPT-4、DALL·E、Whisper 等）
- Terraform 全自动化 AWS Serverless 部署，含 IAM 策略与代理式 API 隐藏密钥
- 提供 LangChain API 端点与 YAML 格式 Function Calling 插件模型
- ReactJS 聊天前端，支持文本与文件附件输入

## 适用场景

- 学习如何用 AWS Serverless 架构部署 OpenAI API 应用
- 参考 12-Factor 方法论的 AI 微服务工程实践
- 基于模板快速搭建可定制皮肤的聊天机器人应用

## 场景标签

`聊天机器人` `教程课程` · 领域:对话与助手

## 证据(README 行号)

> L18: A React + AWS Serverless full stack implementation of the example applications found in the official OpenAI API doc
> L42: - **Complete OpenAI API**: Deploys a production-ready API for integrating to OpenAI's complete suite of services, i

## 星数曲线

```mermaid
xychart-beta
    title "FullStackWithLawrence/aws-openai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 67 --> 69
    line [68, 68]
```

2026-10-18 68 → 2026-10-24 68（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `7dc8e94077e1` · [字段定义](../../DATASET.md)*
