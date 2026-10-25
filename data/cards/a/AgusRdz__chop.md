# AgusRdz/chop

⭐ 46 · Go · MIT · 推送 2026-10-23 · [GitHub](https://github.com/AgusRdz/chop) · [官网](https://getchop.run/) · 个人维护

**AI coding agent 的 CLI 输出压缩器，减少 token 消耗**

面向使用 Claude Code、Gemini CLI、Codex CLI、Antigravity IDE 与 Pi 的开发者：chop 在命令输出进入上下文窗口前将其压缩，宣称节省 50-90% token。机制是通过 PreToolUse hook 拦截 Bash 命令的 tool_result，按命令内置过滤规则（覆盖 git、docker、kubectl、npm、terraform 等 60+ 命令），未识别命令走 JSON/CSV/表格/日志行自动检测；日志按结构指纹分组合并，错误行始终完整保留并置顶。提供自定义过滤规则、全局与项目级配置、本地 token 节省统计。Go 编写，二进制本地运行，不收集用户数据。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- PreToolUse hook 透明拦截并压缩 60+ 常用命令输出
- 未识别命令经自动检测（JSON/CSV/表格/日志行）仍可压缩
- 日志指纹分组：相似行合并为代表性行加重复计数，错误完整置顶
- 自定义过滤规则（keep/drop 正则、截断、外部脚本）与本地 token 统计

## 适用场景

- 我在 Claude Code 里跑大量构建和测试命令，想压住上下文膨胀
- 我在多个 AI coding agent（Gemini/Codex 等）间切换，希望统一压缩 CLI 输出
- 我想查看每条命令实际节省了多少 token

## 场景标签

 · 领域:开发者工具/LLM 上下文优化

## 证据(README 行号)

> L5: **CLI output compressor for Claude Code, Gemini CLI, Codex CLI, Antigravity IDE, and Pi.**
> L16: When Claude Code runs a Bash command, the raw output is fed back into the
> L18: `chop` intercepts that result and compresses it before it enters the context.

## 星数曲线

```mermaid
xychart-beta
    title "AgusRdz/chop 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-25"]
    y-axis "stars" 45 --> 48
    line [46, 47, 46]
```

2026-10-18 46 → 2026-10-25 46（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `3165dd61015f` · [字段定义](../../DATASET.md)*
