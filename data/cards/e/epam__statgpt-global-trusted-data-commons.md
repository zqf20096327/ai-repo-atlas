# epam/statgpt-global-trusted-data-commons

⭐ 19 · TypeScript · MIT · 推送 2026-10-30 · [GitHub](https://github.com/epam/statgpt-global-trusted-data-commons) · [官网](https://statgpt.dialx.ai) · 组织维护

**面向用户的统计数据问答门户：LLM 对话探索 SDMX 数据**

EPAM 维护的 Global Trusted Data Commons 门户，基于 React、Next.js 与 Nx 单仓构建。前端通过 AI DIAL API 接入 LLM 后端，提供聊天界面与会话历史、SSE 流式响应、SDMX 数据集探索与跨数据集过滤、图表展示、会话链接/二维码分享，以及基于 NextAuth.js 的可选认证（支持 Auth0、Azure AD/B2C、GitLab、Google、Keycloak 等 IdP）。安装需 Node.js >= 24.14.0 与 npm，通过 npm 脚本启动和构建，LLM 能力依赖外部 DIAL API 地址配置。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 DIAL API 的聊天界面与会话历史，SSE 流式响应
- SDMX 数据集探索、跨数据集过滤与图表展示
- 会话可通过链接或二维码分享
- NextAuth.js 可选认证，支持 Auth0/Azure AD/B2C/GitLab/Google/Keycloak

## 适用场景

- 通过自然语言对话查询和探索 SDMX 统计数据
- 在图表视图中查看和过滤统计数据集
- 将统计问答会话分享给他人

## 场景标签

`聊天机器人` `数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L15: - **Chat interface & history**: based on DIAL Api
> L17: - **Effortless SDMX data exploration**: powered by the SDMX API

## 星数曲线

```mermaid
xychart-beta
    title "epam/statgpt-global-trusted-data-commons 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-31 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `631ff080642a` · [字段定义](../../DATASET.md)*
