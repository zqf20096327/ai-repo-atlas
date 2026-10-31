# gregorydickson/pickle-rick-claude

⭐ 32 · JavaScript · Apache-2.0 · 推送 2026-10-13 · [GitHub](https://github.com/gregorydickson/pickle-rick-claude) · 个人维护

**基于 Claude Code 的 PRD 驱动自主编码工作流工具集**

构建于 Claude Code 之上的 agentic 工程工具集：接收或起草 PRD 后，将需求分解为原子 ticket，在 tmux 中生成隔离的 worker 子进程，每个 ticket 自主走完 research → plan → implement → verify → review → simplify 生命周期。提供 PRD 访谈与三方分析师精炼、代码质量与数据流加固 ticket、指标驱动的迭代精炼（Microverse）等模块。worker/manager 可切换 codex、hermes、deepseek 后端，DeepSeek 需环境变量 DEEPSEEK_API_KEY。以 Claude Code 斜杠命令与脚本形式运行于 ~/.claude 目录。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- PRD → ticket 分解 → tmux 中自主实现的 Ralph Loop（每 ticket 8 阶段）
- 三个并行 AI 分析师多轮交叉精炼 PRD，产出原子 ticket 与加固 ticket
- 可选 codex/hermes/deepseek 后端，选择持久化于 state.json 并支持 resume
- Microverse 指标驱动精炼：单次变更-测量-保留/回退循环

## 适用场景

- 给出 PRD 或目标后让多 worker 自主完成研究、实现与代码审查
- 对已有 PRD 做需求缺口与集成点分析并生成可执行 ticket
- 以可量化指标（测试覆盖率、延迟）为目标做自动迭代优化

## 场景标签

`编码 Agent` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L7: Pickle Rick is a complete agentic engineering toolbelt built on the Ralph Wiggum loop and ideas from Andrej Karpathy
> L61: ### Step 3: Implement with tmux (the Ralph Loop)
> L76: Rick prints a `tmux attach` command — open a second terminal to watch the live 3-pane dashboard:

## 星数曲线

```mermaid
xychart-beta
    title "gregorydickson/pickle-rick-claude 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-31 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `7869ce361ce9` · [字段定义](../../DATASET.md)*
