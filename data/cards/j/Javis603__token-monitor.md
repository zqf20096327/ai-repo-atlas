# Javis603/token-monitor

⭐ 3,275 · JavaScript · MIT · 推送 2026-10-22 · [GitHub](https://github.com/Javis603/token-monitor) · [官网](http://javis-ai.com/token-monitor/) · 个人维护

**桌面小组件：追踪 46+ AI 编码工具的 token 用量与额度**

本地优先的桌面挂件，读取 46+ AI 编码工具（Claude Code、Codex、Cursor、OpenCode 等）的本地会话文件与数据库，展示实时 token 用量、成本、缓存命中率、按工具/模型/会话/项目的明细，以及账号额度检测与重置预测；多设备通过 hub 汇总同步，会话原文不参与同步。另支持多账号管理、一年期趋势热图、USD/TWD/HKD/CNY 计价与 WSL 用量合并。提供 Windows/macOS/Linux 构建。

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

- 读取 46+ AI 编码工具本地数据，实时展示 token 用量与成本
- 多设备 hub 汇总同步，各设备只上报摘要
- 按工具/模型/会话/设备的分解视图与缓存命中率统计
- 账号额度窗口检测、多账号管理与 Codex 重置预测

## 适用场景

- 同时在多台机器上使用 AI 编码工具，想在单一面板看总用量
- 跟踪各 AI 订阅的额度消耗与重置时间
- 按模型和项目分析 token 成本与缓存命中情况

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L20: A desktop widget that shows live token usage and AI Tool Limits across 46+ AI coding tools — Claude Code, Codex, Cu
> L107: Most usage monitors are useful on the machine they run on. Token Monitor is built for multi-device work: each devi
> L123: - **AI Tool Limits detection** — provider-specific session, daily, weekly, billing, and credits windows for Claude

## 星数曲线

```mermaid
xychart-beta
    title "Javis603/token-monitor 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22"]
    y-axis "stars" 3154 --> 3246
    line [3161, 3202, 3239]
```

2026-10-18 3,161 → 2026-10-22 3,239（+78）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-20 · 置信度 mid · 依据 README sha `1602a3a7ca1f` · [字段定义](../../DATASET.md)*
