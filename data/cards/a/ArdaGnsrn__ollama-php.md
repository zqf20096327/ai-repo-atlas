# ArdaGnsrn/ollama-php

⭐ 210 · PHP · MIT · 推送 2026-09-14 · [GitHub](https://github.com/ArdaGnsrn/ollama-php) · [官网](https://packagist.org/packages/ardagnsrn/ollama-php) · 个人维护

**Ollama 的 PHP 客户端库，供 PHP 应用调用本地 LLM 服务**

封装 Ollama HTTP API 的 PHP 8.1+ 库，通过 Composer 安装，支持自定义 base URL 创建客户端。资源覆盖 Completions（含流式）、Chat（含流式与 tools 参数，tools 不可与流式同用）、Models（列表/详情/创建/复制/删除/pull/push 及流式、运行中模型列表）、Blobs（存在检查/创建）与 Embed 生成。要求本机或指定地址运行 Ollama 服务，面向在 PHP 项目中接入本地 LLM 的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Completions/Chat 的流式生成接口
- Chat 支持 tools 参数调用自定义函数（不支持与流式同用）
- Models 全生命周期操作：创建/复制/删除/pull/push 及运行中模型列表
- 文本嵌入（Embed）与 Blobs 存在检查/创建

## 适用场景

- PHP 应用中调用 Ollama 本地模型生成对话或补全
- 在 PHP 服务端拉取、管理 Ollama 模型
- 为 PHP 项目生成文本嵌入向量

## 场景标签

 · 领域:LLM 基础设施/PHP 客户端

## 证据(README 行号)

> L1: Ollama PHP Library
> L30: composer require ardagnsrn/ollama-php
> L40: $client = \ArdaGnsrn\Ollama\Ollama::client('http://localhost:11434');

## 星数曲线

```mermaid
xychart-beta
    title "ArdaGnsrn/ollama-php 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-26"]
    y-axis "stars" 208 --> 211
    line [209, 210, 210]
```

2026-10-18 209 → 2026-10-26 210（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `924561a1ed1a` · [字段定义](../../DATASET.md)*
