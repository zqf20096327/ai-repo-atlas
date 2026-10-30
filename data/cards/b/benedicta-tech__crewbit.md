# benedicta-tech/crewbit

⭐ 17 · TypeScript · MIT · 推送 2026-09-13 · [GitHub](https://github.com/benedicta-tech/crewbit) · [官网](https://crewbit.sh/) · 组织维护

**用单个命令驱动 AI 代理处理 issue 的守护进程**

crewbit 是一个守护进程：按 YAML 工作流定义轮询 issue 跟踪器（如 Jira），按优先级取出待办 issue，在隔离的 git worktree 中调用 Claude Code 的 slash 命令（claude --print）执行任务，成功后取下一项，失败则退避重试。代理的全部行为（做什么、顺序、用哪些命令）集中在一个 YAML 文件中，并提供 dev-junior、releaser、qa-bot 等示例人设。需注意：它以 --dangerously-skip-permissions 启动 Claude Code，会跳过所有权限提示。安装提供二进制脚本（macOS/Linux/Windows）与源码构建（需 Bun）两种方式。

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

- 轮询 issue 跟踪器并按优先级自动派发 Claude Code slash 命令
- 单个 YAML 文件定义代理的全部行为（transitions、命令、顺序）
- 每个 issue 在隔离的 git worktree 中执行，失败自动退避重试
- 内置 dev-junior/releaser/copywriter/qa-bot/translator 示例工作流

## 适用场景

- 让 AI 代理自动实现工单并合并已接受的 PR
- 自动化执行发布流程与测试套件
- 翻译 i18n 工单、起草营销文案等重复性 issue 工作

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L11: crewbit is a daemon that watches an issue tracker, picks up work in priority order, and runs a Claude Code slash co
> L17: 3. When an issue is ready, it spawns `claude --print <command> <issue-key>` in an isolated git worktree.

## 星数曲线

```mermaid
xychart-beta
    title "benedicta-tech/crewbit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-30 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `579aa5fa9976` · [字段定义](../../DATASET.md)*
