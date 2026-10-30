# vitorsreis/sift

⭐ 15 · PHP · MIT · 推送 2026-10-19 · [GitHub](https://github.com/vitorsreis/sift) · 个人维护

**面向 PHP 项目的 Composer 原生 agent 技能管理工具**

以 Composer 插件形式为 PHP 团队提供两条工作流：`composer skills` 安装和管理可复用的 agent 技能，支持安装到 Cursor、Claude Code、GitHub Copilot、Gemini CLI 等 agent 目标目录；`composer sift <tool>` 以紧凑、规范化输出运行 20 余种 PHP 测试/静态分析/格式化工具，并注入机器可读报告以减少 agent 上下文消耗。安全机制含只读 Composer 报告、dry-run 重构、屏蔽参数、超时与历史脱敏。支持全局或项目安装，也提供 PHAR 与 vendor/bin 入口。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- `composer skills` 将 agent 技能安装到 standard 等多 agent 目标目录（Cursor/Copilot/Gemini CLI 等）
- `composer sift <tool>` 以紧凑规范化输出运行 20+ 种 PHP 工具
- 安全机制：只读报告、dry-run 重构、屏蔽参数、超时、历史脱敏
- 分页历史与摘要输出，减少 agent 会话中的 token 消耗

## 适用场景

- PHP 团队统一管理项目内 agent 技能并分发到多个编码 agent
- 用一条命令层运行测试、静态分析、格式化工具并获取 agent 友好输出
- 让编码 agent 按需查看分页的工具历史而非原始长日志

## 场景标签

 · 领域:PHP 开发工具/agent 工具链

## 证据(README 行号)

> L16: - `composer skills`: install and manage reusable agent skills inside the project.
> L17: - `composer sift <tool>`: run PHP tools with compact, normalized, agent-friendly output.
> L25: - **Manage skills through Composer** for the open agent target set, including a standard shared target, Cursor, Cla

## 星数曲线

```mermaid
xychart-beta
    title "vitorsreis/sift 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `9c96ae238807` · [字段定义](../../DATASET.md)*
