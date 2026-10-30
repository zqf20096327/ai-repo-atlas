# Merit-Systems/echo

⭐ 547 · TypeScript · NOASSERTION · 推送 2026-06-26 · [GitHub](https://github.com/Merit-Systems/echo) · [官网](https://echo.merit.systems) · 组织维护

**让终端用户为 AI 用量付费的 SDK 基础设施，开发者抽取加成**

面向构建 AI 应用的 TypeScript/React 开发者的 user-pays 计费基础设施：替换现有 AI SDK 导入为 Echo SDK，用户经一次 OAuth 登录获得通用余额并直接为自身用量付费，开发者设定加成比例自动获得收入，无需自建代理、计量、支付与密钥校验。架构含 Echo Control（Next.js 托管站点）、Echo Server（请求路由与计量的 Express 代理）及 TS/Next.js/React 三层 SDK；提供 pnpx echo-start 脚手架与 6 类模板（next/react/next-chat/assistant-ui/echo-cli）。依赖托管服务 echo.merit.systems 运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 用户 OAuth 一次登录即获跨应用通用余额，自行承担用量费用
- 开发者设置 markup 比例，按 token 自动产生收入
- TS 核心 SDK + Next.js / React 框架 SDK 分层提供
- echo-start 提供 6 种项目模板（含 CLI 与 chatbot 模板）

## 适用场景

- AI 应用开发者不想垫付 API 成本也不想自建计费系统
- 在现有 Vercel AI SDK 应用中切换为用户付费模式
- 通过加成比例从用户 AI 用量中获得持续收入

## 场景标签

 · 领域:LLM 基础设施/计费

## 证据(README 行号)

> L10: **User-pays AI infrastructure. Drop in Echo, users pay for their own usage—you never front costs.**
> L30: Replace your AI SDK imports with Echo. Users authenticate once, get a balance, and pay for their own usage. You set
> L70: - Echo Control: Next.js app for echo.merit.systems. Hosted site and api routes.
> L71: - Echo Server: Express server for router.echo.merit.systems. Proxy for routing and metering LLM requests from clien

## 星数曲线

```mermaid
xychart-beta
    title "Merit-Systems/echo 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 546 --> 548
    line [547, 547]
```

2026-10-18 547 → 2026-10-30 547（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `02feea93eabd` · [字段定义](../../DATASET.md)*
