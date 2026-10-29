# elenavanengelenmaslova/mocknest-serverless

⭐ 18 · Kotlin · MIT · 推送 2026-10-26 · [GitHub](https://github.com/elenavanengelenmaslova/mocknest-serverless) · 个人维护

**部署在自己 AWS 账号的 WireMock 兼容 serverless mock 服务器**

运行在 AWS Lambda 上的持久化 mock 服务，供集成测试替代不稳定的外部 API：通过 REST/SOAP/GraphQL 端点返回 mock 响应，mock 定义与请求日志存于 S3 以跨冷启动与重部署保留。支持 CRUD 管理、WireMock 映射格式导入导出、SQS 异步 webhook、IAM SigV4/API Key 认证、最高 200MB 的 Lambda 流式响应。AI 功能为借助 Amazon Bedrock 从 OpenAPI/WSDL/GraphQL 规范生成 WireMock 映射并自动校验自纠（仅支持 SOAP 1.2 绑定）。经 SAR 一键部署或 SAM 源码构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- WireMock 映射格式兼容，可复用既有 stubs
- mock 定义经 S3 持久化，存活于 Lambda 冷启动与重部署
- Amazon Bedrock 从 OpenAPI/WSDL/GraphQL 规范生成并自纠 mock 映射
- Lambda 响应流式交付最高 200MB，支持 SSE

## 适用场景

- 集成测试中替代不可用或难配置的外部第三方 API
- CI/CD 流水线中提供稳定的 mock 端点
- 从 API 规范文档用 AI 批量生成 mock 定义

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L107: - **Serve Mock Responses**: Call mocked REST, SOAP, and GraphQL endpoints like real APIs — from tests, apps, or CI
> L114: - **AI-Assisted Mock Generation**: Generate realistic, consistent mocks from OpenAPI, WSDL/SOAP, or GraphQL specs 

## 星数曲线

```mermaid
xychart-beta
    title "elenavanengelenmaslova/mocknest-serverless 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `5ef339e0f0b6` · [字段定义](../../DATASET.md)*
