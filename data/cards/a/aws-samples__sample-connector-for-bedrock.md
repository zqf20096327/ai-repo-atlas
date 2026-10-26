# aws-samples/sample-connector-for-bedrock

⭐ 104 · TypeScript · MIT-0 · 推送 2026-10-24 · [GitHub](https://github.com/aws-samples/sample-connector-for-bedrock) · [官网](https://aws-samples.github.io/sample-connector-for-bedrock/) · 组织维护

**面向开发者的 Amazon Bedrock API 转发与虚拟密钥/成本管理工具**

Bedrock 及其他 AWS 生成式 AI 服务的 API 转发工具（BRConnector）：兼容任意可自定义 Host 与 API Key 的 OpenAI/Anthropic 客户端，支持 bedrock-converse 接入全部 Bedrock 模型、SageMaker LLM 部署模型与 Ollama 等自定义模型。提供虚拟 API key 发放（普通用户/管理员两类）、逐次调用成本记录、按 key 的月度配额与余额控制，以及后台模型与参数管理。以 Docker 镜像（DockerHub/ECR）与 CloudFormation 部署（含 Lambda Web Functions）提供。MIT-0 许可，声明仅供个人学习与研究用途。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT-0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 兼容任意 OpenAI/Anthropic 客户端，含 /v1/messages 透传路由
- 虚拟 API key 发放与逐次调用成本记录、月度配额/余额控制
- 支持 Bedrock（bedrock-converse）、SageMaker LMI 与 Ollama 等自定义模型
- 提供 Docker 镜像与 CloudFormation/Lambda Web Functions 部署方式

## 适用场景

- 团队内为多个用户分发 Bedrock 访问密钥并控制用量成本
- 让 Claude Code 或 Anthropic SDK 客户端经代理接入 Bedrock
- 统一管理多个后端模型（Bedrock/SageMaker/Ollama）并绑定到分组或密钥

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L3: This is a Bedrock (and other generative AI tools from AWS) API forwarding tool that can issue virtual keys, log chat
> L5: It is compatible with any OPENAI client or Anthropic client that can define Host and API Key.

## 星数曲线

```mermaid
xychart-beta
    title "aws-samples/sample-connector-for-bedrock 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 103 --> 105
    line [104, 104]
```

2026-10-18 104 → 2026-10-26 104（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `9d05694096be` · [字段定义](../../DATASET.md)*
