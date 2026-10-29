# smc2315/harness-memory

⭐ 21 · TypeScript · MIT · 推送 2026-04-09 · [GitHub](https://github.com/smc2315/harness-memory) · 个人维护

**给 AI 编码助手的本地项目记忆层插件**

OpenCode 插件，为 AI 编码助手提供持久、可审查的项目记忆：自动捕获工具交互证据，经信号标签分类、空闲时的 Dream 后台整合、LLM 抽取候选记忆，再由人工审查（CLI 逐条或批量 promote/reject）转为激活记忆，通过 4 层激活引擎选择性注入系统提示。存储用 SQLite WASM，检索为向量+BM25 混合。自述 v0.5.0 早期阶段，基准使用 mock embeddings，适合不超过 20 个会话的中小型项目。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 证据→信号标签→Dream 整合→人工审查→激活记忆的记忆生命周期
- 4 层激活引擎（Baseline/Startup/Scoped/Diversity）选择性注入记忆
- SQLite WASM 零原生依赖 + 向量(e5-small)与 BM25 混合检索
- 单命令 npx install 完成建库、注册插件并导入 CLAUDE.md/.cursorrules

## 适用场景

- 让 AI 编码助手跨会话记住项目规则、坑点与决策
- 替代手动维护 CLAUDE.md 的全量提示注入
- 审查并管理 AI 自动抽取的项目记忆候选

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L8: harness-memory is an OpenCode plugin that gives AI coding assistants persistent, reviewable project memory. It captu
> L39: - LLM extraction proposes structured knowledge via OpenCode SDK

## 星数曲线

```mermaid
xychart-beta
    title "smc2315/harness-memory 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-29"]
    y-axis "stars" 20 --> 23
    line [22, 21, 21]
```

2026-10-18 22 → 2026-10-29 21（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `c959d09faaa5` · [字段定义](../../DATASET.md)*
