# fxerkan/concealer

⭐ 15 · Python · MIT · 推送 2026-09-28 · [GitHub](https://github.com/fxerkan/concealer) · [官网](https://fxerkan.github.io/concealer/) · 个人维护

**本地优先的密钥管理器，让 AI agent 用密钥而不见明文**

基于 SOPS + age 的本地密钥管理工具：加密全部委托给 SOPS/age，自身不实现密码学，提供类型化密钥（API key、数据库、SSH 等 16 类）、tenant/project/environment/repo 维度作用域、篡改可见的 HMAC 链式审计日志与泄露风险扫描。面向 AI 编程场景：内置 MCP 服务器让 Claude Code、Cursor 等 agent 以注入环境变量方式使用密钥，明文值从输出中脱敏。提供 CLI、Web UI、TUI、Chrome 扩展与移动端界面，仅本地运行、无云无遥测。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 加密 100% 委托给 SOPS（AES-256-GCM）与 age（X25519）
- MCP 服务器让 agent 注入并使用密钥而不见明文值
- HMAC 链式审计日志，可校验篡改/删除/截断并导出 CSV/JSON
- 16 种类型化密钥表单 + tenant/project/env/repo 多维作用域继承

## 适用场景

- 在 Claude Code / Cursor 等 AI 编程助手中安全使用 API 密钥而不泄露到上下文
- 本地集中管理多个项目的数据库、SSH、网站等各类凭据
- 审计与撤销 agent 的密钥访问令牌，扫描目录中的泄露密钥

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L17: `concealer` is a thin, auditable wrapper around two battle‑tested tools — it does **not** implement its own cryptog
> L37: 4. **AI‑safe by design.** Agents get an MCP server that can **list** names and **inject** secrets into a command's 

## 星数曲线

```mermaid
xychart-beta
    title "fxerkan/concealer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `7cb109ce45f8` · [字段定义](../../DATASET.md)*
