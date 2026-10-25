# majiayu000/vibeguard

⭐ 44 · Rust · MIT · 推送 2026-10-21 · [GitHub](https://github.com/majiayu000/vibeguard) · [官网](https://majiayu000.github.io/vibeguard/) · 个人维护 · 中文 README

**Rust CLI：为编码 agent 提供规则库与 Bash/Git 防护钩子**

面向 Claude Code、Codex CLI 与 Grok 等编码 agent 的 Rust 运行时工具：内嵌 75 个按范围组织的评审规则（common/rust/python/golang/typescript），安装不向宿主 prompt 注入指令；通过原生 Bash 钩子拦截部分破坏性命令拼写并记录最近一次观测结果，可选 Git pre-push 钩子检查提交祖先关系拒绝远端删引用/改标签。提供安装诊断、status/uninstall 管理与只读 v1 遗留清单。DeepSeek Harness 可经适配器调用。macOS/Linux/WSL 支持，Windows 为实验性（仅 Claude Code+Git Bash）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 内嵌 75 个范围化评审规则，支持搜索与 JSON 导出，安装不注入 prompt
- Bash PreToolUse 钩子识别批量 checkout/restore、强制 clean 与递归强删
- Git pre-push 拒绝远端 ref 删除与 tag 替换，要求 fast-forward/祖先关系
- 一条 curl 命令安装预编译产物并校验 SHA256，无需 Rust 工具链

## 适用场景

- 给 Claude Code/Codex/Grok 加装破坏性命令拦截钩子
- 防止 git push 误删远端分支或覆盖标签
- 以 CLI 按需查阅语言相关的编码评审规则

## 场景标签

 · 领域:开发者工具/编码 agent 基础设施

## 证据(README 行号)

> L3: A Rust CLI for coding-agent rules, native hooks, and installation diagnostics.
> L9: Native Bash hooks reject a small set of destructive command spellings and record the latest observed outcome. An opt

## 星数曲线

```mermaid
xychart-beta
    title "majiayu000/vibeguard 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 42 --> 44
    line [43, 43]
```

2026-10-18 43 → 2026-10-25 43（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `013a999af2ff` · [字段定义](../../DATASET.md)*
