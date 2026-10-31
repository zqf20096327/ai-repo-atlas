# specpact/specpact

⭐ 14 · Shell · MIT · 推送 2026-07-06 · [GitHub](https://github.com/specpact/specpact) · [官网](https://github.com/specpact/specpact) · 组织维护

**零依赖的规格驱动开发（SDD）工具包，供 AI 编码助手使用**

Node.js CLI 工具，为 AI 辅助开发提供规格驱动开发（Spec-Driven Development）工作流：在仓库根目录生成 .sdd/ 目录，包含每次会话自动加载的 Memory Bank（AGENTS.md/architecture/decisions）、按功能组织的永久规格文档、以及 nano/feature/system 三级模式规则文件。提供 init/new/verify/update 等命令，附带 Claude Code 斜杠命令与 GitHub Copilot 的 agent/prompt 配置；要求 Node.js 18+，工作流文件为普通 Markdown，无锁定。规格生命周期为 draft→in-progress→stable→deprecated，规格弃用但不删除。

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

- Memory Bank 三文件每次 AI 会话自动加载
- nano/feature/system 三级规格工作流
- specpact verify 生成审计提示，人工判定实现是否符合规格
- 规格永久保留（deprecated 不删除），CLI 可选、无锁定

## 适用场景

- 让 AI 编码助手按规格而非提示语义实现功能
- 跨会话保留项目上下文与架构决策
- 对 bug 修复与架构变更采用不同仪式级别的工作流

## 场景标签

 · 领域:软件开发工具/AI 辅助开发

## 证据(README 行号)

> L5: SpecPact helps teams define software intent before coding and keeps specifications as living, trackable contracts th
> L25: AI coding assistants are powerful, but they forget everything between sessions. They implement what the prompt impl

## 星数曲线

```mermaid
xychart-beta
    title "specpact/specpact 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `d3a325c7369f` · [字段定义](../../DATASET.md)*
