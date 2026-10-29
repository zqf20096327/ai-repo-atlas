# enieuwy/showy-quota

⭐ 26 · Rust · MIT · 推送 2026-10-08 · [GitHub](https://github.com/enieuwy/showy-quota) · 个人维护

**在 SketchyBar/Zellij/tmux 常驻显示 AI 套餐配额的工具**

由 CodexBar 驱动的配额显示工具：本身不与提供商通信，凭据与用量解析全部依赖 CodexBar，为每个提供商渲染图标、进度条或环形图，按剩余配额与时间阈值着色，并显示提供商故障状态。提供 guard/prompt/run/pick 等子命令，可在配额低于阈值时拦截 CI 或 agent 钩子、生成 shell 提示符片段、在模型间路由任务。SketchyBar 集成需 macOS；Zellij/tmux 栏也可在 Linux 运行。发布包含预编译二进制，无需 Rust；shell 集成需 bash 4+ 与 jq 1.6+。

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

- 零自身鉴权：凭据与解析完全依赖 CodexBar，自动拉起 codexbar serve
- guard 子命令按剩余配额阈值拦截 CI/cron/agent 钩子（稳定退出码）
- 多 UI 集成：SketchyBar 行/环形、tmux TPM、Zellij WASM 插件、Agent CLI 状态栏
- 多套终端渲染模式（dual/mono3/mono4/dual2）与多套内置主题

## 适用场景

- 在 macOS 菜单栏或终端状态栏随时查看各 AI 套餐剩余配额
- 配额不足时自动拦截 CI 任务或 agent 钩子
- 在多个模型间挑选剩余配额最多的提供商来路由工作

## 场景标签

 · 领域:开发工具/AI 用量监控

## 证据(README 行号)

> L24: - **Zero auth/config:** Relies entirely on CodexBar for credentials and parsing.
> L218: - **`showy-quota guard`** gates CI, cron, and agent hooks on quota thresholds

## 星数曲线

```mermaid
xychart-beta
    title "enieuwy/showy-quota 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-29"]
    y-axis "stars" 24 --> 27
    line [25, 26, 26]
```

2026-10-18 25 → 2026-10-29 26（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `2e9b51fbdbbb` · [字段定义](../../DATASET.md)*
