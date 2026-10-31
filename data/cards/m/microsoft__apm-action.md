# microsoft/apm-action

⭐ 21 · TypeScript · MIT · 推送 2026-10-17 · [GitHub](https://github.com/microsoft/apm-action) · 组织维护

**GitHub Action：安装 APM 并把 agent 资产部署进 CI 流程**

微软维护的 GitHub Action，安装 APM（Agent Package Manager）CLI，读取 apm.yml 并执行 apm install，将 instructions/prompts/skills/agents 等 agent 原语部署到 CI 工作区。支持隔离模式、锁定文件驱动的可复现安装与 update 刷新、打包（apm/plugin 两种布局，含 Claude Code 市场格式）、带完整性校验的恢复与多包合并、一键 tag 发布流水线，以及隐藏 Unicode 字符安全扫描（SARIF 报告）。同组织私有仓库认证零配置。面向在 CI 中管理 AI agent 资产的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 读取 apm.yml 运行 apm install，按 apm.lock.yaml 锁定 commit 保证可复现
- pack 模式产出 .tar.gz 包，支持 Claude Code plugin 市场格式（claude/codex 多格式）
- 恢复模式经 apm unpack 校验完整性，支持多包按序合并覆盖
- 安装时自动阻断含严重隐藏字符风险的包，可输出 SARIF 报告

## 适用场景

- 在 CI 中一行接入 APM 安装与 agent 资产部署
- 定时刷新分支/标签引用的 agent 依赖并开 PR
- 打包并发布 agent 资产包到市场（如 Claude Code 插件市场）

## 场景标签

 · 领域:AI agent 工具链/CI-CD

## 证据(README 行号)

> L3: A GitHub Action that installs APM (Agent Package Manager) and deploys agent primitives (instructions, prompts, skill
> L13: This installs the APM CLI, reads your `apm.yml`, and runs `apm install`.

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/apm-action 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-31 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `ee60c6b5567b` · [字段定义](../../DATASET.md)*
