# brakit-ai/brakit

⭐ 14 · TypeScript · MIT · 推送 2026-06-20 · [GitHub](https://github.com/brakit-ai/brakit) · [官网](https://www.brakit.ai) · 组织维护

**本地优先的开发期 API 观测工具：自动发现性能与安全问题**

面向 Node.js（及 Python FastAPI/Flask）开发者的进程内观测工具：通过 patch http.Server 拦截全部请求，自动捕获 fetch 调用、数据库查询、控制台输出与错误，按用户动作分组展示在 /__brakit 实时仪表盘；内置 8 条安全规则扫描、N+1 查询检测、重复调用检测与 p95 回归检测。通过 MCP 服务器让 Claude Code、Cursor 等 AI 助手直接查询问题并验证修复。设 7 层保护确保不在生产环境运行，支持 Next.js/Express 等 7 种框架自动检测。

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

- patch http.Server 进程内拦截，零代码改动、无需代理或第二进程
- 8 条安全规则扫描实时流量（密钥泄露、PII、Token 入 URL 等）
- N+1 查询检测、重复调用检测与 p95 延迟回归检测
- 内置 MCP 服务器，AI 编码助手可直接查询问题与验证修复
- 7 层保护确保不会在生产环境激活

## 适用场景

- 开发期发现 AI 生成代码引入的性能与安全问题
- 不用加 console.log 就看清每个 API 动作执行了什么
- 让 Claude Code/Cursor 通过 MCP 读取问题报告并修复代码

## 场景标签

`LLM 可观测性` `网络安全` · 领域:评测与运维

## 证据(README 行号)

> L79: - **AI-native via MCP** — Claude Code and Cursor can query issues, inspect endpoints, and verify fixes directly
> L116:                           +-- MCP server      (AI assistant integration)
> L111: import 'brakit'  →  hooks into http.Server  →  captures everything

## 星数曲线

```mermaid
xychart-beta
    title "brakit-ai/brakit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `4db7bd098caf` · [字段定义](../../DATASET.md)*
