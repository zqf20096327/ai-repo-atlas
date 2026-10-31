# andyvandaric/opencode-ag-auth

⭐ 67 · TypeScript · MIT · 推送 2026-02-21 · [GitHub](https://github.com/andyvandaric/opencode-ag-auth) · [官网](https://www.npmjs.com/package/opencode-ag-auth) · 个人维护

**让 OpenCode 经 Google OAuth 接入 Antigravity 模型的认证插件**

opencode-antigravity-auth 的安全导向分支，作为 OpenCode 插件通过 Google OAuth 认证 Antigravity（Google 的 IDE）配额，接入 Claude Opus/Sonnet 4.6 与 Gemini 3.1 Pro/Flash 等模型。机制包括：70% 用量安全缓冲的严格配额协议、多账户自动轮换、Antigravity 与 Gemini CLI 双配额池路由、undici 代理支持及会话恢复集成。README 明确警告使用可能违反 Google 服务条款、存在账号被封风险，属非官方工具。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 严格配额协议在触达 Google 滥用限制前锁定账户（70% 安全缓冲）
- 多 Google 账户自动轮换与双配额池（Antigravity/Gemini CLI）智能路由
- Claude Opus/Sonnet 4.6 与 Gemini 3.1 Pro/Flash 模型变体与思考预算配置
- Oh-My-OpenCode 会话恢复集成与 undici 代理支持

## 适用场景

- 在 OpenCode 中使用 Antigravity 配额调用 Claude 与 Gemini 模型
- 多账户轮换延长 agent 长时间运行的可用配额
- 通过代理在受限网络环境完成 OAuth 认证

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L11: Enable OpenCode to authenticate against **Antigravity** (Google's IDE) with enterprise-grade **account protection**
> L15: This is a specialized fork of `opencode-antigravity-auth` focused on **Safety** and **Reliability** for power users

## 星数曲线

```mermaid
xychart-beta
    title "andyvandaric/opencode-ag-auth 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 66 --> 68
    line [67, 67]
```

2026-10-18 67 → 2026-10-31 67（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `94a7e0f95dce` · [字段定义](../../DATASET.md)*
