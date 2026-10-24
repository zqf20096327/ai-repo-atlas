# mag123c/toktrack

⭐ 196 · Rust · MIT · 推送 2026-10-21 · [GitHub](https://github.com/mag123c/toktrack) · [官网](https://www.npmjs.com/package/toktrack) · 个人维护

**多款 AI 编程 CLI 的 token 用量与费用追踪工具**

Rust 编写的 CLI/TUI 工具，读取 Claude Code、GitHub Copilot CLI、Codex CLI、Gemini CLI、Qwen Code、OpenCode、PI Agent、Antigravity、Grok CLI 等 9 种 AI 编程 CLI 的本地会话文件，汇总 token 与费用到统一仪表盘（5 个标签页）。关键机制是持久化缓存：各来源的历史日期摘要写入 ~/.toktrack 缓存且不可变，即使 CLI 自身（如 Claude Code 默认 30 天）删除原始会话文件，成本历史仍保留；无自带价格的来源按 LiteLLM 价格表估算并以 ~ 标注。支持 npx、Homebrew、cargo 及预编译二进制安装，可经 SSH/rsync 同步远程 Codex 会话。

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

- 9 种 AI 编程 CLI 的统一用量/费用仪表盘（TUI + CLI 命令）
- 持久化缓存保留被 CLI 删除的历史数据，含 audit 视图核对 live/cache-only/missing
- simd-json + rayon 并行解析，冷启动 ~1.0s、缓存查询 ~0.04s
- 支持远程 Codex 会话经 SSH/rsync 同步解析

## 适用场景

- 查看我在各 AI 编程 CLI 上每天/每月的 token 花费
- Claude Code 删除旧会话后仍保留完整成本历史
- 在终端提示符中实时显示当日 AI 支出
- 生成可分享的用量报告（文本/SVG）

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L13: Track usage across **all your AI coding CLIs** — Claude Code, GitHub Copilot CLI, Codex CLI, Gemini CLI, Qwen Code,
> L29: - **TUI Dashboard** — 5 tabs (Overview, Stats, Models, Projects, Audit) with daily/weekly/monthly views

## 星数曲线

```mermaid
xychart-beta
    title "mag123c/toktrack 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-24"]
    y-axis "stars" 194 --> 197
    line [195, 196, 196]
```

2026-10-18 195 → 2026-10-24 196（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `c54a68608e58` · [字段定义](../../DATASET.md)*
