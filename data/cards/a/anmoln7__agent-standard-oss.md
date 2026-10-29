# anmoln7/agent-standard-oss

⭐ 19 · Shell · MIT · 推送 2026-09-21 · [GitHub](https://github.com/anmoln7/agent-standard-oss) · [官网](https://anmoln7.github.io/agent-standard-oss/) · 个人维护

**AI 编码代理指令文件的单一来源规范与配套 bash 工具集**

一套面向 AI 编码代理（Claude Code、Codex、Cursor、Gemini 等 harness）的指令文件组织规范：以 AGENTS.md 为唯一事实源、CLAUDE.md 用一行 include 指向同一文件，配合子目录作用域规则、docs/solutions/ 修复日志、Keep in sync 同步块、SessionStart 自愈钩子等 11 节机制防止指令漂移。附带零依赖 bash 工具（adopt 向导、repo-audit、secrets-audit、crew 等）与 GitHub Action CI 检查，输出 L0–L3 成熟度评分。分为 docs-only、只读检查、本地钩子、可写自动化四个信任层级，按需采用。MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- AGENTS.md 单一事实源，CLAUDE.md 一行 include，跨 harness 无锁定
- adopt 向导与 adopt --check 评分（L0–L3，STD-01…STD-06 检查 ID，JSON 输出）
- 提供 curl 一键安装、Claude Code 插件、GitHub Action CI 三种采用途径
- 零依赖 bash 脚本：repo-audit、secrets-audit、crew 并行代理等

## 适用场景

- 让多个 AI 编码代理读取同一份准确的指令文件
- 在 CI 中检测仓库指令文件是否偏离规范
- 审计仓库历史与提交中的密钥泄漏并披露代理署名

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L25: agent-standard is a small, opinionated convention for structuring the instruction
> L67: agent-standard is **cross-harness** — a *harness* is whichever tool runs your agent
> L82: |**Read-only checks**|`adopt --check`, `repo-audit`, the `standard-compliance` CI action|Read-only — scans and repo

## 星数曲线

```mermaid
xychart-beta
    title "anmoln7/agent-standard-oss 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-29 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `10240bf646af` · [字段定义](../../DATASET.md)*
