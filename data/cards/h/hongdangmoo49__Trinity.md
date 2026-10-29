# hongdangmoo49/Trinity

⭐ 20 · Python · MIT · 推送 2026-08-31 · [GitHub](https://github.com/hongdangmoo49/Trinity) · [官网](https://pypi.org/project/trinity-agent/) · 个人维护

**编排 Claude Code/Codex/Antigravity 三 CLI 的多智能体协作工具**

面向开发者的本地多智能体编排器：在同一终端环境中调用 Claude Code（claude）、Codex（codex）、Antigravity（agy）三个 CLI，以共享上下文文件、多轮讨论（deliberation）与中央合成组织三个代理分别担任设计者/实现者/检阅者角色，达成共识后生成 work package 并按文件所有权并行执行、交叉评审。以 Python 包（pipx/pip）安装，提供 Textual TUI、CLI 命令与 Rich 回退界面；要求至少一个 provider CLI 已安装并登录，workflow 状态持久化于 .trinity/ 目录。

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

- 共享上下文 + 多轮讨论 + 中央合成的三代理共识流程
- work package 自动分派、并行执行与非属主代理交叉评审
- Textual Workbench TUI，含模型 override、preflight、resume/retry
- workflow 状态持久化（session.json/events.jsonl），支持 NEEDS_USER_DECISION 问答续跑

## 适用场景

- 让多个 AI 编码 CLI 对同一需求讨论后分工实现
- 对现有代码库做多代理设计与代码评审
- 在 TUI 中跟踪共识过程、执行包与重试失败任务

## 场景标签

`多智能体` `编码 Agent` `代码审查` · 领域:Agent 开发

## 证据(README 行号)

> L7: **Claude Code** · **Codex** · **Antigravity CLI** 세 AI 에이전트를
> L38: Trinity는 로컬 터미널에서 provider CLI를 직접 호출하는 프로그램입니다.
> L42: - Claude Code CLI (`claude`)

## 星数曲线

```mermaid
xychart-beta
    title "hongdangmoo49/Trinity 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-29 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `8968a079db5a` · [字段定义](../../DATASET.md)*
