# systemime/coding-plan-mask

⭐ 91 · Go · MIT · 推送 2026-07-05 · [GitHub](https://github.com/systemime/coding-plan-mask) · 个人维护 · 中文 README

**本地代理：将 Coding Plan API 伪装成官方 IDE 客户端供任意工具使用**

Go 编写的轻量本地代理，面向已订阅大模型厂商 Coding Plan（智谱 GLM、阿里云、MiniMax、DeepSeek、Moonshot 等）的开发者。它把请求头/User-Agent 伪装成 Claude Code、Kimi Code、OpenCode、OpenClaw 或自定义工具，透明转发 OpenAI/Anthropic 兼容请求，使任意 OpenAI 兼容客户端可使用套餐 API。另提供 SQLite 用量统计、本地 API Key 鉴权、限流、流式转发，以及默认关闭的本地隐私过滤（S1/S2/S3 分级脱敏/拦截/审计）。需注意其用途可能违反服务商条款，存在密钥吊销风险。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 伪装为 Claude Code / Kimi Code / OpenClaw 等官方支持客户端的 User-Agent
- 透传任意上游 API 路径，兼容任意 OpenAI 兼容客户端
- use_anthropic 模式下 Anthropic Messages 与 OpenAI 格式双向转换
- 可选本地隐私过滤：S1/S2/S3 分级、脱敏、拦截与审计

## 适用场景

- 让不在官方支持列表里的 AI 编码工具使用已订阅的 Coding Plan API
- Claude 风格客户端通过 Anthropic Messages 格式调用 OpenAI 兼容上游
- 提示词发出前在本地脱敏敏感信息
- 通过 /stats 与会话端点跟踪 token 消耗与请求记录

## 场景标签

 · 领域:LLM 基础设施/代理网关

## 证据(README 行号)

> L31: **Coding Plan Mask** is a lightweight local proxy for developers who want to use Coding Plan APIs from their prefer
> L35: │  Your Favorite AI  │────▶│   Coding Plan Mask   │────▶│   LLM Provider      │

## 星数曲线

```mermaid
xychart-beta
    title "systemime/coding-plan-mask 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 90 --> 92
    line [91, 91]
```

2026-10-18 91 → 2026-10-24 91（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `feb9106b88b7` · [字段定义](../../DATASET.md)*
