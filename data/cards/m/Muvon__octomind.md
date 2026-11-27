# Muvon/octomind

⭐ 657 · Rust · Apache-2.0 · 推送 2026-11-26 · [GitHub](https://github.com/Muvon/octomind) · [官网](https://octomind.run) · 个人维护

**给开发者的开源编码 agent 运行时：单一 Rust 二进制、任意模型、MCP 原生**

Octomind 是一个开源 coding agent harness，通过 MCP 给任意 LLM 提供读写文件、运行 shell、搜索代码、委派子 agent 等仓库操作工具，并以交互 CLI、stdin 管道、daemon、WebSocket 服务器、ACP 编辑器内 agent 五种形态运行同一二进制。将审批策略写为 TOML guardrails（guards/hooks/validators 三层），以支持无人值守的 CI、daemon 与定时运行；可选 Besydr 插件负责任务规划、完成度检查与从会话中沉淀经验教训。支持按角色选模型、按请求/会话设支出上限；沙箱通过 Landlock/Seatbelt 限制写入范围。发布于 Crates.io，提供安装脚本与 Homebrew 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 五种运行形态共用一个 Rust 二进制与一份 TOML 配置
- Policy as code：TOML guardrails 中的 guards/hooks/validators 确定性执行
- 任意模型：支持 OpenRouter/OpenAI/Anthropic/DeepSeek/Ollama 等，按角色选模型并设预算上限
- Specialists & taps：从 tap registry 拉取打包好的 agent（模型、提示词、MCP 服务器、权限）

## 适用场景

- 在 CI、定时任务或 daemon 中无人值守运行代码修改 agent
- 在终端、SSH/tmux 或编辑器（Zed/JetBrains/VS Code/Neovim）中使用编码 agent
- 用 TOML guardrails 替代逐条审批弹窗来约束 agent 风险操作
- 从 tap 发布和分发团队自定义的专用 agent

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L16: Octomind is an open-source coding agent harness. It gives any LLM the tools to work in a repository — read and edit
> L40: - **Any model, any budget.** Use Octomind Cloud or your own key (OpenRouter, Anthropic, OpenAI, DeepSeek, Ollama, a

## 星数曲线

```mermaid
xychart-beta
    title "Muvon/octomind 星数(近 22 点)"
    x-axis ["2026-10-25", "2026-10-26", "2026-10-28", "2026-10-29", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26", "2026-11-27"]
    y-axis "stars" 130 --> 712
    line [178, 179, 182, 181, 199, 230, 178, 619, 644, 651, 657, 661, 663, 662, 664, 637, 644, 645, 647, 654, 656, 657]
```

2026-10-25 178 → 2026-11-27 657（+479）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 mid · 依据 README sha `55b9be77ef14` · [字段定义](../../DATASET.md)*
