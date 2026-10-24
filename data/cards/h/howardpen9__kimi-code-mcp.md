# howardpen9/kimi-code-mcp

⭐ 61 · TypeScript · MIT · 推送 2026-10-12 · [GitHub](https://github.com/howardpen9/kimi-code-mcp) · [官网](https://github.com/howardpen9/kimi-code-mcp#readme) · 个人维护 · 中文 README

**让 Claude Code 把大批代码库分析委托给 Kimi 的 MCP server**

TypeScript 实现的 MCP server，将 Claude Code 与 Kimi Code（k3/kimi-for-coding，256K 上下文）连接：Claude 编排任务，Kimi 通过 kimi_analyze/kimi_resume 等工具读取整个代码库并回传结构化报告，以减少 Claude 侧 token 消耗。提供 8 个工具，分两种后端：kimi_query/kimi_verify 直连 API（仅需 API key），kimi_analyze/kimi_resume 需本地 Kimi CLI 与登录。限制：需有效的 Kimi Code 订阅；节省比例为说明性估算，仅计 Claude 侧 token。

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

- 8 个 MCP 工具，覆盖代码库分析、会话续接、问答与第三方核验
- 双后端：API 直连（仅需 API key）与本地 CLI 子进程（可读磁盘代码库）
- Kimi Code 256K 上下文，一次读取整个代码库
- npm 全局安装或从源码构建

## 适用场景

- 让 Claude Code 委托 Kimi 分析大型/陌生代码库，降低 Claude 侧 token 开销
- 提交前让 Kimi 以第三方身份核验 diff 或代码声明
- 扫描安全漏洞或梳理依赖后由 Claude 综合处理
- 跨会话续接保留 256K 上下文的代码分析

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L57: │  Claude Code │ ◄──────────► │ kimi-code-mcp│ ────────────► │ Kimi CLI     │
> L96: MCP server that connects Kimi Code (model `kimi-for-coding`, 256K context, auto-upgraded) with Claude Code — lettin

## 星数曲线

```mermaid
xychart-beta
    title "howardpen9/kimi-code-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 60 --> 62
    line [61, 61]
```

2026-10-18 61 → 2026-10-24 61（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `9aa119c8817e` · [字段定义](../../DATASET.md)*
