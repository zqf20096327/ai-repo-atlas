# nkmc-ai/sdk

⭐ 15 · TypeScript · MIT · 推送 2026-03-25 · [GitHub](https://github.com/nkmc-ai/sdk) · [官网](https://nkmc.ai) · 组织维护 · 中文 README

**开放 agent API 网关 SDK：让 AI agent 以 6 条类 Unix 命令发现并调用互联网 API**

面向 agent 与开发者的两套工具：CLI 提供 ls/cat/grep/write/rm/pipe 六条类 Unix 命令，经网关以 HTTP 方式浏览和调用 40+ 已注册 API（GitHub、Stripe、OpenAI 等）；服务端 SDK @nkmc/core 提供 JWT 验证、中间件与 skill.md 生成。开发者可扫描自身路由生成 .well-known/skill.md，通过 DNS 挑战认领域名后将 API 注册到网关供 agent 发现。以 npm 包分发，MIT 许可。

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

## 能力要点

- 6 条类 Unix 命令（ls/cat/grep/write/rm/pipe）映射 HTTP 操作
- 网关已收录 40+ API，覆盖开发工具、云部署、AI/ML、数据库等类别
- @nkmc/core 提供 JWT 验证、中间件与 skill.md 程序化生成
- DNS 挑战式域名认领与 API 注册流程

## 适用场景

- 让 AI agent 用统一命令发现并调用第三方 API
- 开发者将自己的 API 注册到网关供 agent 调用
- 对网关转发到自身服务的请求做 JWT 验证

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L5: Open agent API gateway SDK. Let AI agents discover and call any API on the internet with 6 Unix-like commands, and l
> L10: |`@nkmc/core`|Server SDK — JWT verification, middleware, skill generation|npm|

## 星数曲线

```mermaid
xychart-beta
    title "nkmc-ai/sdk 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `6679c11ff4ac` · [字段定义](../../DATASET.md)*
