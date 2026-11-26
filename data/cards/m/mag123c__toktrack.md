# mag123c/toktrack

⭐ 196 · Rust · MIT · 推送 2026-11-24 · [GitHub](https://github.com/mag123c/toktrack) · [官网](https://www.npmjs.com/package/toktrack) · 个人维护

**追踪多种 AI 编码 CLI 的 token 用量与成本的工具**

用 Rust 编写的 CLI/TUI 工具，读取 Claude Code、Codex CLI、Gemini CLI 等 9 种 AI 编码 CLI 的本地会话文件，聚合展示 token 与成本数据。通过持久化缓存保存每日用量摘要，原始会话文件被 CLI 按保留策略（如 Claude Code 默认 30 天）删除后历史仍可查询；提供 daily/weekly/monthly/stats/report/audit/remote 等命令与 JSON 输出，支持 SSH 远程 Codex 日志同步、shell 提示符集成与自定义定价。安装提供 npx、Homebrew、cargo 与预编译二进制四种途径。

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

- 支持 9 种 AI 编码 CLI 的统一用量仪表盘（TUI 5 个标签页）
- 持久化缓存保留成本历史，缓存查询约 0.04 秒
- toktrack audit 逐源逐日标记 live/cache-only/missing 数据状态
- 成本无记录的来源按 LiteLLM 列表价估算并带 ~ 标记，支持离线定价快照

## 适用场景

- 查看我在多个 AI 编码 CLI 上的总 token 花费
- 防止 Claude Code 30 天清理后丢失历史成本数据
- 按项目拆分统计各仓库的 AI 用量
- 在 shell 提示符里显示当天 AI 支出

## 场景标签

 · 领域:开发者工具/用量与成本监控

## 证据(README 行号)

> L11: **The token & cost tracker that never loses your history.** Most tools re-read your CLI's session files on every ru
> L13: Track usage across **all your AI coding CLIs** — Claude Code, GitHub Copilot CLI, Codex CLI, Gemini CLI, Qwen Code,
> L171: |CLI|Status|Data Location|

## 星数曲线

```mermaid
xychart-beta
    title "mag123c/toktrack 星数(近 2 点)"
    x-axis ["2026-10-24", "2026-11-26"]
    y-axis "stars" 195 --> 197
    line [196, 196]
```

2026-10-24 196 → 2026-11-26 196（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-25 · 置信度 high · 依据 README sha `be7db3ac8274` · [字段定义](../../DATASET.md)*
