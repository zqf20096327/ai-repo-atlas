# Unstructured-IO/unstructured-python-client

⭐ 120 · Python · MIT · 推送 2026-10-21 · [GitHub](https://github.com/Unstructured-IO/unstructured-python-client) · 组织维护

**面向开发者的 Unstructured 文档处理平台 Python SDK**

Unstructured Platform API 的 HTTP 客户端 SDK，以 Python 库形式提供，覆盖 Workflow Endpoint 与 Partition Endpoint，用于将 PDF 等文档的解析接入 Python 代码。支持 uv/pip/poetry 安装，提供同步与异步调用、可配置重试策略、结构化错误类、自定义 httpx 客户端注入、PDF 按页切分并发上传（默认 5 并发、上限 15）、NDJSON 流式落盘以降低内存峰值，以及上下文管理器资源释放。SDK 自述处于 beta，版本间可能出现破坏性变更。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- Partition/Workflow Endpoint 的同步与异步调用
- PDF 按页切分并发上传并重组结果，可指定页范围与容错模式
- NDJSON 流式落盘降低大文档内存峰值
- 可覆盖的重试策略与自定义 httpx 客户端注入

## 适用场景

- 在 Python 管道中调用 Unstructured API 做文档解析
- 大体积 PDF 的并发切分处理与流式结果落盘
- 长驻服务中复用单一 SDK 客户端并控制连接资源

## 场景标签

`文档解析` · 领域:知识与检索

## 证据(README 行号)

> L6:  Python SDK for the Unstructured API
> L10: Please refer to the our documentation for a full guide on integrating the Workflow Endpoint and Partition Endpoint 

## 星数曲线

```mermaid
xychart-beta
    title "Unstructured-IO/unstructured-python-client 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 119 --> 121
    line [120, 120]
```

2026-10-18 120 → 2026-10-28 120（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `4a3cd33905fc` · [字段定义](../../DATASET.md)*
