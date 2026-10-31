# Alessandro-Pang/harnessmith

⭐ 15 · TypeScript · MIT · 推送 2026-09-17 · [GitHub](https://github.com/Alessandro-Pang/harnessmith) · [官网](http://alexpang.cn/harnessmith/) · 个人维护 · 中文 README

**面向多 Coding Agent 的个人 Harness 分发与工作状态管理工具**

本地优先的跨 Host Personal Harness 控制层：把个人规则、渐进式文档检索（BM25 全文索引带回退扫描）、非权威 Memory 与 Task 工具安装到 Codex、Cursor、Claude Code、OpenCode、Kimi Code CLI、DeepSeek Harness、Pi 等宿主，并提供备份、锁、回滚、dry-run 预检与 audit record 等安全生命周期。明确不实现通用 Agent Runtime，不接管模型循环、权限与 sandbox。面向同时使用多个 Coding Agent 的开发者，通过 npx 运行，需 Node.js 24.12.0+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 支持 7 种 Coding Agent 宿主的规则与状态分发（含 dry-run 预检）
- 内嵌 BM25 全文检索，索引为可重建缓存、不可用时回退扫描
- 备份/锁/回滚等安全生命周期与拒绝敏感数据的审计记录
- 明确的责任边界表：已实现/宿主负责/不支持三档声明

## 适用场景

- 我在多个项目和 Coding Agent 之间切换，希望个人规则保持一致
- 需要安全升级、备份、恢复和卸载个人 Harness
- 希望长任务跨会话可继续且文档可按需检索而非全量塞入上下文

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L16: Harnessmith 是一个本地优先、跨 Host 的 Personal Harness 分发与工作状态控制层。它把实践中已经有效的个人规则、
> L29: Harnessmith 不实现通用 Agent Runtime，也不接管模型循环、工具权限或远端服务。

## 星数曲线

```mermaid
xychart-beta
    title "Alessandro-Pang/harnessmith 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `6d0c3194b6d4` · [字段定义](../../DATASET.md)*
