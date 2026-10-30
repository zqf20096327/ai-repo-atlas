# alloevil/AgentXRay

⭐ 16 · JavaScript · MIT · 推送 2026-10-18 · [GitHub](https://github.com/alloevil/AgentXRay) · [官网](https://alloevil.github.io/AgentXRay/) · 个人维护 · 中文 README

**本地查看 AI Agent 会话日志、追溯执行证据的 Web 面板**

读取本地已有会话日志的 Web 面板与 CLI 工具：把工具调用、后台进程退出、编辑后的检查等记录并排关联到原始记录，无需插桩、模型调用或人工标注；明确声明不做根因推断、修复或完成度判定。兼容 OpenClaw、Codex、Claude Code、DeepSeek Harness 等七种平台日志格式；离线 inspect 命令不联网、不执行日志中的命令。以 npm 包形式提供，需 Node.js ≥ 22.13，另有在线演示（合成数据）。

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

- 将测试/编辑/检查记录并排关联到原始调用记录，无需插桩
- 支持 7 种 agent 平台日志（OpenClaw/Codex/Claude Code/DeepSeek Harness 等）
- 离线 inspect CLI 生成 JSON 报告，不做网络或模型调用
- 默认本地运行，可选的提示词功能需自配端点并可能外联

## 适用场景

- 调试编码 agent 的会话日志，查看工具调用与检查记录的关联
- 在 CI 中对单个日志文件生成 JSON 检查报告
- 审查编辑后是否缺失后续检查等未完成证据

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L5: Read existing session logs locally. Connect tool calls, background exits and checks after edits to their original re
> L105: **Dashboard:** OpenClaw, Codex, Claude Code, Hermes, OMP, DeepSeek Harness and Gemini CLI. Hermes uses SQLite; the

## 星数曲线

```mermaid
xychart-beta
    title "alloevil/AgentXRay 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `86698b66e6b2` · [字段定义](../../DATASET.md)*
