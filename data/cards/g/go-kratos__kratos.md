# go-kratos/kratos

⭐ 25,977 · Go · MIT · 推送 2026-09-16 · [GitHub](https://github.com/go-kratos/kratos) · [官网](https://go-kratos.dev) · 组织维护 · 中文 README

**Go 微服务框架：云原生服务开发全流程支持**

Kratos 是用于构建云原生微服务的 Go 框架，提供传输层、中间件、注册发现、配置、日志、编码与代码生成等小型显式 API。以 Protobuf 为核心做 API-first 开发，自动生成 HTTP/gRPC 代码，并通过 contrib 生态提供注册中心、配置存储、可观测性等可选集成。通过 CLI 工具创建、生成和运行服务，要求 Go 1.25+ 与 protoc 工具链，采用 MIT 许可证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 动量与使用信号

- 维护:`active` — 距上次 push 32.0 天,年发版 2,289 位贡献者
- 涨星:近 1 天 **+1**(自 20261016 起算)

## 能力要点

- 基于 Protobuf 生成 HTTP/gRPC 代码的 API-first 开发
- 统一 HTTP 与 gRPC 的传输层及可组合中间件（恢复、日志、校验、追踪、指标、鉴权）
- 可插拔的注册、配置与编码组件，contrib 生态提供可选集成
- CLI 工具支持服务脚手架创建、proto 代码生成与运行

## 适用场景

- 用 Go 搭建 HTTP/gRPC 微服务
- 需要从 Protobuf 定义生成服务端与客户端代码
- 需要注册发现、配置、日志、追踪等微服务基础设施组件的项目

## 场景标签

 · 领域:云原生/微服务开发框架

## 证据(README 行号)

> L17: Kratos is a lightweight Go framework for building cloud-native microservices. It provides small, explicit APIs for 
> L21: - API-first development with Protobuf and generated HTTP/gRPC code.
> L33: - Go 1.25 or later

---
*卡片 v1 · prompt 1.4 · 生成 2026-10-18 · 置信度 high · 依据 README sha `a90bdcbca34f` · [字段定义](../../DATASET.md)*
