# openai/openai-python

⭐ 32,215 · Python · Apache-2.0 · 推送 2026-11-20 · [GitHub](https://github.com/openai/openai-python) · [官网](https://pypi.org/project/openai/) · 组织维护

**OpenAI 官方 Python SDK：从 Python 访问 OpenAI REST API**

OpenAI 官方维护的 Python 库，为 OpenAI REST API 提供访问通道，要求 Python 3.10+。由 OpenAPI 规范自动生成，包含全部请求参数与响应字段的类型定义，提供基于 HTTPX2 的同步与异步客户端。支持 Responses API 与 Chat Completions API 生成文本、视觉输入、SSE 流式响应、Realtime WebSocket 连接、自动分页、文件上传与 webhook 签名验证。另支持 API key 之外的工作负载身份认证（Kubernetes/Azure/GCP/X.509 mTLS）。通过 PyPI 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 动量与使用信号

- 维护:`active` — 距上次 push 1.0 天,年发版 100,199 位贡献者
- 涨星:近 1 天 **+7**(自 20261016 起算)
- 安装:pypi 包 `openai` 月下载 295,856,631
- 平台:— · 协议:OPENAI-API

## 能力要点

- 同步与异步双客户端，含全量请求/响应类型定义
- 支持 SSE 流式响应与 Realtime WebSocket API
- 支持 Kubernetes/Azure/GCP/X.509 工作负载身份认证
- 内置 webhook 签名验证与分页迭代器

## 适用场景

- 在 Python 应用中调用 OpenAI 模型生成文本或处理图像
- 构建低延迟多模态实时对话应用
- 在云端托管环境中以短期令牌替代长期 API key 认证

## 场景标签

 · 领域:LLM 基础设施/SDK

## 证据(README 行号)

> L5: The OpenAI Python library provides convenient access to the OpenAI REST API from any Python 3.10+
> L7: and offers both synchronous and asynchronous clients powered by HTTPX2.
> L9: It is generated from our OpenAPI specification.

## 星数曲线

```mermaid
xychart-beta
    title "openai/openai-python 星数(近 28 点)"
    x-axis ["2026-10-21", "2026-10-22", "2026-10-23", "2026-10-24", "2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23"]
    y-axis "stars" 31856 --> 32247
    line [31888, 31899, 31910, 31919, 31930, 31946, 31958, 31970, 31982, 31976, 31987, 31993, 32001, 31930, 32080, 32109, 32119, 32135, 32147, 32159, 32168, 32180, 32183, 32189, 32202, 32206, 32210, 32215]
```

2026-10-21 31,888 → 2026-11-23 32,215（+327）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `4dfd943b04c7` · [字段定义](../../DATASET.md)*
