# plune-ai/cairn

⭐ 34 · TypeScript · Apache-2.0 · 推送 2026-10-24 · [GitHub](https://github.com/plune-ai/cairn) · [官网](https://plune.ai/cairn) · 组织维护

**自主 QA 代理：探索 Web 应用并生成可运行的 Playwright 测试**

基于 Node.js/TypeScript 的自主 QA agent：用保存的登录会话进入 Web 应用，通过 ARIA 快照与截图观察页面，按 ISO/IEC/IEEE 29119-4 方法设计测试用例，生成可运行的 @playwright/test 代码，并带定位符校验、自修复（keep-best）与基于 LLM 评审的自我改进（Langfuse 追踪）。另可从 OpenAPI 3.x 规格生成 API 测试（含负向与对抗用例）。UI+API 已交付，unit/docs 为规划项；需 Node.js 20+ 与 API key，浏览器需单独下载。以 npm CLI 与 TypeScript 库两种形式提供，旧名 Lex-Bot 已改名 Cairn（旧命令保留弃用别名）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- ARIA+截图观察、定位符逐一校验后再生成测试代码
- 按 ISO/IEC/IEEE 29119-4 设计 EP/BVA/决策表/状态迁移等用例
- 自修复采用 keep-best 策略：修复不会让套件变差
- OpenAPI 规格生成 API 测试，含对抗风格与安全限流（只读默认、300 请求上限）

## 适用场景

- 给我的 Web 应用自动生成可维护的 Playwright UI 测试
- 从 OpenAPI 规格批量生成含负向/对抗场景的 API 测试
- 记录登录会话后让 agent 探索页面并产出用例文档供人工评审

## 场景标签

`浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L14: Autonomous QA agent (Node.js / TypeScript) that logs into a web app with a saved session, explores
> L16: generates runnable `@playwright/test` code, self-validates, self-repairs, and **self-improves** via
> L19: **Cairn is the generation layer** — it produces tests across surfaces (UI + API shipped; unit / docs

## 星数曲线

```mermaid
xychart-beta
    title "plune-ai/cairn 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 33 --> 35
    line [34, 34]
```

2026-10-18 34 → 2026-10-26 34（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `7daa4b13af92` · [字段定义](../../DATASET.md)*
