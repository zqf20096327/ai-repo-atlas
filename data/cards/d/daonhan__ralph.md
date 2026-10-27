# daonhan/ralph

⭐ 24 · TypeScript · MIT · 推送 2026-10-06 · [GitHub](https://github.com/daonhan/ralph) · [官网](https://www.npmjs.com/package/@daonhan/ralph) · 个人维护

**自主编码代理循环：在 Docker 沙箱中迭代驱动 Claude Code/Codex 完成计划或 GitHub issue**

面向开发者的 CLI 编排工具，由 @daonhan/ralph（CLI）与 @daonhan/ralph-core（库）组成。它驱动 Claude Code（默认）或 Codex（--agent codex）在自定义 Docker 镜像内按 implementer → reviewer 两阶段循环迭代，直到计划完成或代理输出哨兵标记；支持计划/PRD 驱动（ralph-afk）与 GitHub issue 驱动（ralph-ghafk）两个入口，可分离运行、重试与通知。需注意：默认绑定挂载宿主 Docker socket，代理在沙箱内无交互审批运行，存在安全风险文档（SECURITY.md）。前置依赖包括 Docker、Node.js 20+、gh CLI 与对应代理认证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- implementer → reviewer 两阶段迭代循环，代理输出哨兵标记时退出
- ralph-afk（计划/PRD 驱动）与 ralph-ghafk（GitHub issue 驱动）两个 AFK 入口
- Claude Code 默认、Codex 可选，模型与 effort 按优先级独立解析
- 支持分离运行、重试、stderr 配置打印与凭据跨 Windows/WSL 挂载

## 适用场景

- 无人值守地让编码代理按计划文档或 PRD 完成整批任务
- 从 GitHub 开放 issue 中自动领取并完成开发任务
- 以 implementer/reviewer 双角色循环迭代代码实现与审查

## 场景标签

`编码 Agent` `代码审查` · 领域:编码与开发

## 证据(README 行号)

> L8: Ralph drives Claude Code by default, or Codex when selected with
> L16: - **`@daonhan/ralph-core`** — library: iteration loop, docker runner, template renderer, stage registry. Importable
> L19: Two AFK entry points (both installed globally after `npm i -g @daonhan/ralph`):

## 星数曲线

```mermaid
xychart-beta
    title "daonhan/ralph 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-27 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `2dcc843a81bf` · [字段定义](../../DATASET.md)*
