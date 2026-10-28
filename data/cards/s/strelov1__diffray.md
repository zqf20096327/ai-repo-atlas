# strelov1/diffray

⭐ 25 · TypeScript · 推送 2026-01-25 · [GitHub](https://github.com/strelov1/diffray) · [官网](https://diffray.ai/cli) · 个人维护

**多 agent AI 代码审查 CLI：审查 git 变更中的问题**

面向开发者的命令行工具，读取 git 变更 diff，按匹配规则分派给多个专门化 AI agent（通用质量、bug、安全、性能、一致性）独立分析，再对结果去重并由 AI 验证过滤误报后输出报告。执行器需依赖外部 AI CLI 工具：默认 Claude Code，可切换 Cursor Agent、OpenCode、Codex CLI，并支持按 agent 覆盖模型。Agent 与规则以 Markdown 文件自定义，可从 git 仓库 extends 共享。本地运行，规则需手动配置；调用成本取决于所选 AI 提供方计费。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 5 个专门化 agent 独立分析后去重并 AI 验证过滤误报
- 支持 Claude Code / Cursor Agent / OpenCode / Codex CLI 四种执行器
- Agent 与规则均为 Markdown 文件，可按 agent/阶段覆盖模型、并发与超时
- extends 机制从任意 git 仓库加载共享 agents/rules

## 适用场景

- 提交前让多个 AI agent 审查未提交变更或最近一次提交
- 针对特定文件类型（如 *.ts 安全扫描）定制审查规则
- 团队通过 git 仓库共享统一的 agents 与 rules 配置

## 场景标签

`代码审查` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L6: > **What is this?** A CLI tool that runs multiple AI agents to review your code changes. Each agent specializes in d
> L46: - **AI CLI Tool** - diffray uses external AI tools to analyze code. You need to install and authorize one of them:
> L139: │  Git Diffs  │───▶│ Match Rules │───▶│ Run Agents  │───▶│  Deduplicate│

## 星数曲线

```mermaid
xychart-beta
    title "strelov1/diffray 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-28"]
    y-axis "stars" 23 --> 26
    line [24, 25, 25]
```

2026-10-18 24 → 2026-10-28 25（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `29b4cf140cf7` · [字段定义](../../DATASET.md)*
