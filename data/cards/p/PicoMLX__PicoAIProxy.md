# PicoMLX/PicoAIProxy

⭐ — · [GitHub]() · 个人维护

**面向 Apple 开发者的 OpenAI/Anthropic 反向代理服务器**

用 server-side Swift（HummingBird HTTP 服务器）编写的反向代理，面向 iOS/macOS/iPadOS/VisionOS 应用开发者。它把 API key 保留在服务端以防泄露，通过 Apple App Store Server Library 验证 StoreKit 2 的 JWS 交易并签发 JWT 会话令牌，确保只有有效订阅用户可调用；接受标准 OpenAI Chat API 并自动转换转发到 OpenAI 或 Anthropic（Anthropic 仅支持 chat streaming）。内置速率限制与黑名单，不持久化数据。可在 Xcode 运行或一键部署到 Railway。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 用 App Store Server Library 验证收据，向客户端签发 JWT 会话令牌
- 代理自动将 OpenAI Chat API 调用转换为 Anthropic 等多家 LLM 供应商格式
- 按分钟/小时/永久封禁三级速率限制与黑名单（默认关闭）
- 兼容现有 OpenAI Swift 库（CleverBird、OpenAI-Kit 等），客户端无需改动

## 适用场景

- Apple 平台付费订阅应用保护 LLM API key 不被客户端泄露
- 只让完成 App Store 订阅验证的用户调用 AI 接口
- Swift 聊天应用不改客户端代码即可切换 OpenAI/Anthropic 后端

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L5: Pico AI Proxy is a reverse proxy created specifically for iOS, macOS, iPadOS, and VisionOS developers.
> L14: - Supports multiple LLM providers such as OpenAI and Anthropic (more to come, stay tuned). PicoProxy automatically 

## 星数曲线

```mermaid
xychart-beta
    title "PicoMLX/PicoAIProxy 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 152 --> 154
    line [153, 153]
```

2026-10-18 153 → 2026-10-22 153（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `30a1bf8a6e8e` · [字段定义](../../DATASET.md)*
