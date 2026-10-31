# elon-choo/fablever

⭐ 33 · JavaScript · MIT · 推送 2026-07-28 · [GitHub](https://github.com/elon-choo/fablever) · 个人维护

**让 Claude Code 采用 Fable 工作风格的输出样式与 MCP 配置包**

面向 Claude Code（及 Codex CLI、任意 MCP 客户端）用户的工作风格移植工具：将 Anthropic 文档中的 Fable 提示指南提炼为 always-on 输出样式，可选附加 hooks、零依赖 MCP、按需 Agent Skills 与 stop-gate 交付门控。作者明确声明它不提升模型能力或原始质量，实测降低范围蔓延与不必要编辑，成本约 +14%/call。通过 git clone 后运行 install.mjs 安装，支持 macOS/Linux/原生 Windows，无需额外 API key。

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

- always-on 输出样式 + 零依赖 MCP + 子代理注入，零 npm 依赖
- stop-gate 将 fable_lint 规则编译为 Stop hook，不依赖模型自觉调用
- 提供分档安装选项（style-only / 默认 / stop-gate / xverify / Codex 版）
- README 附可离线复算的 A/B 实验数据与未主张内容的声明

## 适用场景

- 让 Claude Code 在编码任务中控制范围、避免不必要编辑
- 通过交付门控在提交前强制展示验证结果
- 在 Codex CLI 中获得同一套行为约束

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L10: Apply Anthropic's documented **Fable working-style guidance** as an always-on output style in
> L13: and disciplined about stopping. Every project, every subagent, installable by anyone. Also runs natively in
> L90: > and applied through documented Claude Code mechanisms (output styles, hooks, MCP). It works on Claude

## 星数曲线

```mermaid
xychart-beta
    title "elon-choo/fablever 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-31 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `d60f5751ee55` · [字段定义](../../DATASET.md)*
