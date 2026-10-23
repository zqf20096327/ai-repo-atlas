# xuiltul/animaworks

⭐ 268 · Python · Apache-2.0 · 推送 2026-10-22 · [GitHub](https://github.com/xuiltul/animaworks) · 组织维护

**把持久 AI 代理组成自治软件组织的编排框架**

AnimaWorks 是一个将持久化 AI 代理组织为『运行中组织』的框架：代理用 git/CI 分解任务、在并行 worktree 中实现、多模型互相评审、开 PR、修 CI、做部署与运行时观测，仅在例外时呼叫人类（call_human）。核心机制包括 GitHub 事件网关自动转任务、按 PR 串行化执行、心跳/Cron 驱动的 24/7 自治循环、神经科学启发的记忆（向量+BM25+事实/实体检索、巩固与主动遗忘），支持 7 种引擎（Claude SDK/Codex/Cursor Agent/Gemini CLI/Grok Build/LiteLLM/Assisted）及逐引擎回退链。提供 Web 设置向导、Workspace 仪表盘与像素办公室实时视图。安装支持 uv/Docker/pip，需 Python 3.12+；Claude Agent SDK 模式不支持 Windows。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- GitHub 事件（CI 失败/评审评论/合并冲突）自动转为代理任务，带去重与重试限制
- 每个 PR 多模型各出一份评审再整合为最终结论
- 神经科学启发的记忆：向量+BM25+事实/实体检索、巩固、主动遗忘
- 7 种模型引擎与逐引擎回退链，每个代理独立 OS 进程并有监督进程自动重启

## 适用场景

- 让一组 AI 代理承担软件产品的日常开发、评审与运维
- 把 GitHub 上的 CI 失败和评审评论自动变成代理的修复任务
- 以组织而非脚本的方式处理邮件回复、会议纪要、Slack 发帖等事务

## 场景标签

 · 领域:AI 代理框架/软件开发自动化

## 证据(README 行号)

> L5: AnimaWorks is a framework that turns persistent AI agents into a "living organization." Give it a goal, and the agen
> L12: AnimaWorks doesn't hardcode this pipeline. What the framework handles is turning GitHub events into tasks, serializ
> L163: 1. **A task arrives** — from a human, from another agent, from a schedule (heartbeat / cron), or from a GitHub eve

## 星数曲线

```mermaid
xychart-beta
    title "xuiltul/animaworks 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-23"]
    y-axis "stars" 266 --> 269
    line [267, 268, 268]
```

2026-10-18 267 → 2026-10-23 268（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `159d87315c0b` · [字段定义](../../DATASET.md)*
