# soonsoon2/lun

⭐ 15 · JavaScript · MIT · 推送 2026-06-02 · [GitHub](https://github.com/soonsoon2/lun) · 个人维护

**多 AI 编程 agent 共答与共识 CLI：一个问题问多个 agent**

Lun（論）是 Node.js CLI 工具，驱动用户已安装并登录的 AI 编程 agent CLI（Claude Code、GitHub Copilot、Kiro、Antigravity、Codex，Cline 为可选），就同一问题并行作答并对比。提供三种模式：并行比较（可选共识综合）、接力讨论（agent 相互质疑、主持人综合）、PM 对话（PM agent 调用专家 agent）。无守护进程也可运行，可选 daemon 保持 worker 常驻；另有本地 Web UI（localhost:3456）、VS Code 扩展（VSIX）与 NDJSON 输出（-j）供其他 agent 调用。限制：需至少一个 agent CLI 已安装并认证；自身不调用 API key。

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

- 驱动已安装的 agent CLI（Claude Code/Copilot/Kiro/Antigravity/Codex），无需额外 API key
- 三种模式：并行比较、接力讨论（含主持人综合）、PM 对话
- 终端/REPL/本地 Web UI/VS Code 扩展/NDJSON 多界面
- 会话自动保存为 .md+.json，daemon 常驻 worker 减少 CLI 冷启动

## 适用场景

- 向多个 AI agent 同时提问同一架构/选型问题并对比答案
- 让多个 agent 接力讨论相互质疑以暴露盲点
- 在 VS Code 或终端里养成 10 秒多agent 咨询习惯
- 让其他 AI agent 通过 lun -j 咨询意见面板

## 场景标签

`多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L26: **Lun (論)** runs the AI coding agent CLIs you **already use** — Kiro, Claude Code, GitHub Copilot, Antigravity, Cod
> L28: Most multi-model tools want your API keys and bill you per token. Lun doesn't: it drives the CLIs you've already in

## 星数曲线

```mermaid
xychart-beta
    title "soonsoon2/lun 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `d8d071d1fb4f` · [字段定义](../../DATASET.md)*
