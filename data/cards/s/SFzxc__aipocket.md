# SFzxc/aipocket

⭐ 15 · TypeScript · Apache-2.0 · 推送 2026-06-14 · [GitHub](https://github.com/SFzxc/aipocket) · 个人维护

**Chrome 扩展 AI 密钥钱包：网站经授权访问模型而不获取 API key**

Chrome MV3 扩展，将 OpenAI 兼容、Anthropic 兼容、OpenRouter、Gemini 等提供商的 API key 存储在扩展内；网站通过 aiWallet 协议与 @aipocket/connect-modal 集成包请求作用域权限（按来源、提供商、模型列表、会话、有效期、请求上限），由扩展校验后将模型流式输出回传网站，全程不暴露 key。面向需要安全接入 AI 提供商的网站开发者与用户；当前为 MVP，准备发布 Chrome Web Store v0.1.0。仓库为 monorepo，含扩展、React 演示站、集成包与协议包。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- API key 保存在扩展内，网站仅获得可撤销的作用域访问
- 支持 OpenAI 兼容、Anthropic 兼容、OpenRouter、Gemini 提供商
- 按 origin/会话/模型/有效期/请求上限校验并代理上游请求
- 提供 @aipocket/connect-modal 集成包与连接审批流程

## 适用场景

- 在第三方 AI 网站使用自己的模型额度而不粘贴 API key
- 网站开发者接入用户自有提供商密钥进行模型调用
- 对网站的模型访问做会话级限流与撤销

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L3: AIPocket is a Chrome MV3 AI access wallet that lets websites request user-approved model access without receiving yo
> L5: It keeps provider credentials in the extension, lets websites request scoped permission, and streams approved model 
> L62: AIPocket uses the `aiWallet` provider protocol internally for website integrations.

## 星数曲线

```mermaid
xychart-beta
    title "SFzxc/aipocket 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `abbc415259d2` · [字段定义](../../DATASET.md)*
