# upstash/box

⭐ 42 · TypeScript · MIT · 推送 2026-10-22 · [GitHub](https://github.com/upstash/box) · [官网](https://upstash.com/docs/box) · 组织维护

**Upstash Box 的 TypeScript/Python SDK 与 CLI：沙箱化 AI 编程 agent**

Upstash 官方为 Box 服务（沙箱化 AI 编程 agent，支持流式输出、结构化输出、文件 I/O、git 与快照）提供的客户端工具集：@upstash/box TypeScript SDK、upstash-box Python SDK（同步+异步客户端，发布于 PyPI）以及 REPL 优先的 @upstash/box-cli 终端 CLI。TS 部分位于 pnpm workspace，Python SDK 独立工具链；包含 Vitest/pytest 单元与集成测试、Changesets 版本管理与 OIDC 发布流程。

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

- TypeScript SDK、Python SDK（sync+async）与 REPL 优先 CLI 三个包
- 覆盖 Box API 的流式输出、结构化输出、文件 I/O、git、快照能力
- npm 与 PyPI 各自独立版本化，经 OIDC Trusted Publishing 发布
- 单元/集成测试分离，集成测试依赖 UPSTASH_BOX_API_KEY 环境变量

## 适用场景

- 在 TypeScript 或 Python 项目中编程调用 Upstash Box 沙箱化编程 agent
- 通过终端 CLI 以 REPL 方式使用 Box 服务
- 为基于 Box 构建的自动化编码流水线提供 SDK 接入

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L3: TypeScript SDK, Python SDK, and CLI for Upstash Box — sandboxed AI coding agents with streaming, structured output, 
> L9: |`@upstash/box`|TypeScript SDK — programmatic access to the Box API|

## 星数曲线

```mermaid
xychart-beta
    title "upstash/box 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 41 --> 43
    line [42, 42]
```

2026-10-18 42 → 2026-10-25 42（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `7be2e8ce9db4` · [字段定义](../../DATASET.md)*
