# spencermarx/open-code-review

⭐ 380 · TypeScript · Apache-2.0 · 推送 2026-07-28 · [GitHub](https://github.com/spencermarx/open-code-review) · 个人维护

**面向 AI 辅助开发的多 agent 代码审查 CLI 与仪表盘**

通过 npm 全局安装的 CLI 工具，编排由 Tech Lead 领导的多 agent 审查团队：多个 reviewer 实例并行独立审查代码变更，经 AGREE/CHALLENGE/CONNECT/SURFACE 结构化辩论后合成去重的最终审查结果。内置 28 个 reviewer 人设，可为不同 reviewer 分配不同模型，支持按 spec/proposal 等需求文档做需求感知审查、大变更集的 Code Review Map、多轮迭代审查与 GitHub PR 发帖（需 GitHub CLI）。运行依赖 Node.js >= 22.5 与已安装的 AI 编码助手（如 Claude Code、Cursor、OpenCode），提供浏览器仪表盘与斜杠命令两种工作流。自身不替代人工代码审查。

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

- 8 阶段工作流：Tech Lead 编排并行审查、聚合、辩论与合成
- 28 个内置 reviewer 人设，支持自定义与临时 reviewer
- 按 reviewer 分配不同模型，仪表盘自动发现已装 vendor 的模型
- Code Review Map 用 Mermaid 依赖图导航 20+ 文件的大变更集
- 审查结果可直接以团队或人声改写模式发帖到 GitHub PR

## 适用场景

- 在大变更提交 PR 前跑多视角 AI 代码审查
- 对照 spec 或验收标准核验代码是否满足需求
- 在大规模重构中用 Code Review Map 定位阅读起点
- 把多 reviewer 审查结果整理后发到 GitHub PR

## 场景标签

`代码审查` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L25: `ocr init` detects your installed AI tools (Claude Code, Cursor, Windsurf, and 11 more) and configures each one aut
> L173: OCR follows an 8-phase workflow orchestrated by a Tech Lead agent:
> L103: Different reviewers, different models. Pair a fast model on a generalist with a deeper model on a specialist, mix 

## 星数曲线

```mermaid
xychart-beta
    title "spencermarx/open-code-review 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-27"]
    y-axis "stars" 378 --> 381
    line [379, 380, 380]
```

2026-10-18 379 → 2026-10-27 380（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `ff78109ac25e` · [字段定义](../../DATASET.md)*
