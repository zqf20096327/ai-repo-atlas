# marcuspat/turbo-flow

⭐ 180 · Shell · MIT · 推送 2026-10-26 · [GitHub](https://github.com/marcuspat/turbo-flow) · [官网](https://www.turboflow.online) · 组织维护

**面向 AI 编写代码的治理套件：跨模型审查门禁与规则层**

rig-lite 是一个仅依赖 bash 的可移植治理工具包，不捆绑任何 agent 或编排器，可放入任意仓库。核心是 gate.sh 跨模型审查门禁：先跑确定性检查，再由与构建者不同模型家族的审查者（Claude Code / Codex CLI）返回 APPROVED/REVISE，fail-closed 且从不自动合并；配套 tf 命令行、protect.sh 分支保护、git 版本化记忆、密钥加密、token 用量仪表盘与 9 个定时任务。给在仓库中运行多个 AI 编码工具并需要合并前审查的团队使用。v5 已移除早期版本的编排栈。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- gate.sh 跨模型审查门禁：确定性检查 + 异家族审查者，fail-closed，从不合并
- protect.sh 将门禁判定设为 GitHub 必需状态检查
- 仅依赖 bash，无新依赖，init-repo.sh 十分钟接入任意仓库
- tf 统一命令：gate/test/status/wt/secrets/tokens/digest 等

## 适用场景

- 在 PR 合并前用不同模型家族交叉审查 AI 写的代码
- 多 agent 并行写作时用隔离 worktree 与 git 版本化记忆管理状态
- 通过分支保护把审查门禁变成强制规则

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L6: > One product lives here: `rig-lite/` — a portable governance kit. It ships no harness, installs nothing, and depend
> L47: |`gate.sh`|a cross-model review gate — deterministic checks first (they're free), then a reviewer from a **differen

## 星数曲线

```mermaid
xychart-beta
    title "marcuspat/turbo-flow 星数(近 2 点)"
    x-axis ["2026-10-19", "2026-10-28"]
    y-axis "stars" 175 --> 178
    line [176, 177]
```

2026-10-19 176 → 2026-10-28 177（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `2b8756cc04d7` · [字段定义](../../DATASET.md)*
