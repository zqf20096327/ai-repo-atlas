# Portkey-AI/portkey-node-sdk

⭐ 56 · TypeScript · 推送 2026-04-20 · [GitHub](https://github.com/Portkey-AI/portkey-node-sdk) · [官网](https://portkey.ai/docs) · 组织维护

**Node.js SDK：通过 Portkey AI 网关统一接入与管理 LLM API**

Portkey 官方 Node.js SDK，构建在 OpenAI SDK 之上，保持 OpenAI 方法兼容，替换 import 即可切换。提供 AI 网关功能：统一 API 签名、跨模型/提供商互操作、自动降级与重试、负载均衡、语义缓存、虚拟密钥、请求超时；以及可观测性功能：日志、请求追踪、自定义元数据、反馈收集与 40+ 指标分析。面向构建生产级 AI 应用的开发者，需注册 Portkey 账号获取 API Key 使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 兼容 OpenAI SDK 签名，切换仅需替换 import
- 自动降级重试、负载均衡与语义缓存
- 虚拟密钥托管 LLM API key
- 请求日志、追踪与 40+ 生产指标分析

## 适用场景

- 在 Node.js 应用中统一接入多个 LLM 提供商
- 为 LLM 调用添加重试、降级与负载均衡
- 收集 LLM 请求日志与性能指标做监控

## 场景标签

`模型网关` `LLM 可观测性` · 领域:Agent 开发

## 证据(README 行号)

> L10: ### AI Gateway
> L12:  Unified API Signature If you've used OpenAI, you already know how to use Portkey with any other provider.

## 星数曲线

```mermaid
xychart-beta
    title "Portkey-AI/portkey-node-sdk 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-25"]
    y-axis "stars" 55 --> 58
    line [57, 56, 56]
```

2026-10-18 57 → 2026-10-25 56（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `193a2d227f4c` · [字段定义](../../DATASET.md)*
