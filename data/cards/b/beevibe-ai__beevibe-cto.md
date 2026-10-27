# beevibe-ai/beevibe-cto

⭐ 104 · JavaScript · Apache-2.0 · 推送 2026-06-14 · [GitHub](https://github.com/beevibe-ai/beevibe-cto) · [官网](https://beevibe.ai/cto) · 组织维护

**面向编码代理的架构决策深研与守卫工具（CLI/MCP/插件）**

以 CLI、MCP 服务器和 Claude Code 插件三种形态提供的架构决策工具：`adr decide` 对指定决策运行深度研究（扫描仓库、发现同类产品、采集证据、生成含引用与 Mermaid 图的 HTML 报告，单次约 3-6 分钟、$0.10-$0.30 API 费用）；`adr principles` 从仓库中用 LLM 提取团队代码评审原则；`adr review`/`adr drift` 检查 PR 与全仓库偏移；`adr guard` 注入 Claude Code PreToolUse 钩子与 git pre-commit。需要至少一个搜索 API key 与 LLM key（默认 gpt-4.1-mini，可指向 OpenAI 兼容本地服务）。核心开源（Apache-2.0），商业版叠加托管语料与团队治理。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 深度研究流水线：仓库扫描→同类产品发现→证据采集→对抗性验证→带引用审计的报告
- LLM 提取团队代码评审原则，cite-or-die 过滤器仅保留有真实 file:line 引用的原则
- adr guard 接入 Claude Code PreToolUse 钩子与 git pre-commit（高危违规阻断提交）
- 支持 CLI、MCP 服务器（Cursor/Codex 等）、Claude Code 插件三种接入形态

## 适用场景

- 在选定向量库/框架等技术选型前生成带证据的对比研究报告
- 把团队代码评审惯例沉淀为可自动检查的原则文件
- 在 CI 或提交时自动拦截违反既定架构原则的代码

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L55: ### MCP server — Cursor, Codex, any MCP host
> L58: npm install -g github:beevibe-ai/beevibe-cto
> L134: - **Claude Code `PreToolUse`** — every Edit/Write/MultiEdit, the hook filters principles to ones relevant to the f

## 星数曲线

```mermaid
xychart-beta
    title "beevibe-ai/beevibe-cto 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-27"]
    y-axis "stars" 103 --> 107
    line [106, 104, 104]
```

2026-10-18 106 → 2026-10-27 104（-2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `3bff849e0c26` · [字段定义](../../DATASET.md)*
