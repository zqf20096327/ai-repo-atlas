# xai-org/xai-proto

⭐ 152 · Apache-2.0 · 推送 2026-10-23 · [GitHub](https://github.com/xai-org/xai-proto) · 组织维护

**xAI gRPC API 的公开 protobuf 定义，用于生成客户端 SDK**

xAI 官方发布的 gRPC API Protocol Buffer 定义文件，描述服务接口与消息结构，开发者可据此在 protobuf/gRPC 生态支持的任意语言中生成客户端 SDK。提供 buf.gen.yaml 配置（默认生成 Python 代码至 gen/python，xAI 官方 Python SDK 基于此构建），也可改用 protoc 或 grpcio-tools 等工具；文件按主版本目录组织（如 proto/xai/api/v1），遵循语义化版本，破坏性变更放入新主版本目录。采用 Apache-2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 定义 xAI gRPC 服务接口与消息结构，支持生成任意语言客户端
- 提供 buf.gen.yaml 配置，默认生成 Python 代码
- 按主版本目录组织，遵循语义化版本
- xAI 官方 Python SDK 基于这些定义构建

## 适用场景

- 为 xAI gRPC API 生成所需语言的客户端 SDK
- 了解 xAI gRPC API 的接口与消息结构
- 跟踪 xAI API 版本变更与兼容性

## 场景标签

 · 领域:LLM 基础设施/API 定义

## 证据(README 行号)

> L3: This repository hosts the public Protocol Buffer (protobuf) definitions for xAI's gRPC-based APIs. These protobuf fi
> L7: You have multiple options for generating code from these `.proto` files, depending on your preferences and tech stac

## 星数曲线

```mermaid
xychart-beta
    title "xai-org/xai-proto 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-25"]
    y-axis "stars" 150 --> 153
    line [151, 152, 152]
```

2026-10-18 151 → 2026-10-25 152（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `be46d203116c` · [字段定义](../../DATASET.md)*
