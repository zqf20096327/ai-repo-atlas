# roadhero/claude-code-setup

⭐ 37 · Markdown · MIT · 推送 2026-09-14 · [GitHub](https://github.com/roadhero/claude-code-setup) · [官网](https://eltexsoft.com) · 组织维护

**面向 Claude Code 的工程化配置集：全局规则包、42 个子代理与安全钩子**

一套可克隆安装的 Claude Code 实际工作配置：约 220 行的全局 CLAUDE.md 主干、按路径 glob 触发加载的 web/Android/iOS/compute 规则包、42 个分栈子代理（架构→开发→评审→QA 链及专家角色）、阻止 agent 强推/跳过 git hook/提交密钥的 commit 守卫钩子、自动格式化与仓库脚手架技能。两级结构（全局+项目），主干预设 prompt-cache 不变，每仓库仅编辑项目文件。需要 jq 与 git 2.28+，自带钩子行为测试并在 CI 运行。作者是 EltexSoft 团队，配置来自其书籍《42: The AI Builder's Stack》。README 自述观点化、面向 PR 流程与受保护分支。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 42 个子代理跨 web/Android/iOS/compute 四栈，含四帽链与专家角色
- rules 包按 paths glob 路径触发加载，未触碰的栈不入上下文
- guard-commit.sh 阻止 agent 强推/--no-verify/提交密钥，无法分类的形态拒绝而非猜测
- 钩子带行为测试（bash+jq），CI 在每个 PR 上运行

## 适用场景

- 为 Claude Code 搭建一套跨栈的工程规范与子代理体系
- 防止 AI agent 在提交时跳过钩子、强推或泄漏密钥
- 新仓库快速生成 CLAUDE.md 模板与质量门禁脚手架

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L3: This is the actual Claude Code configuration I run day to day at EltexSoft: a stack-agnostic engineering "spine," pl
> L27: Two tiers. The **global** tier (`~/.claude/CLAUDE.md` + `rules/` + `agents/` + `hooks/`) is everything that's true 

## 星数曲线

```mermaid
xychart-beta
    title "roadhero/claude-code-setup 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-28 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `f96d429bdb30` · [字段定义](../../DATASET.md)*
