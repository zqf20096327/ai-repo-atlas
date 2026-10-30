# holistic-ai/surface

⭐ 31 · Rust · Apache-2.0 · 推送 2026-09-10 · [GitHub](https://github.com/holistic-ai/surface) · [官网](https://holistic-ai.github.io/surface/) · 组织维护

**本地扫描 AI 工具、站点、token 消耗与花费的终端仪表盘**

单个 Rust 静态二进制（约 2.06 MB），扫描本机磁盘上的既有文件，报告四类信息：安装了哪些 AI 工具（19 种，含是否可执行代码的判定）、浏览过哪些 AI 站点（10 种浏览器的 30 个 AI 域名）、Claude Code/Codex/OpenCode 转录中的 token 消耗，以及按 LiteLLM 公开价格表折算的花费。无账号、无守护进程、无遥测，浏览器历史在 SQLite 内过滤且只输出域名计数。支持 --json/--offline 输出，TUI 交互浏览。版本低于 1.0，可能含破坏性变更。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 识别 19 种 AI 工具、10 种浏览器中的 30 个 AI 域名、3 种 token 来源
- 无账号/无守护进程/无遥测，仅一次可选的价格表网络请求（--offline 可跳过）
- 增量读取转录：冷扫描约 19 秒后，后续运行读取追加字节（约 50 ms）
- 未定价模型显示为 ▲ unpriced 而非 $0.00，本地模型标记为 local

## 适用场景

- 盘点本机装了哪些 AI 工具、哪些能在机器上执行代码
- 统计各工具/模型/仓库的 token 消耗与折算花费
- 对比 API 列价与订阅计划的实际成本

## 场景标签

 · 领域:AI 可观测性/成本追踪

## 证据(README 行号)

> L29: A single binary that scans your own machine and tells you four things: which AI tools are installed, which AI sites
> L86: |**Usage**|Transcripts Claude Code, Codex and OpenCode already write|Tokens per day, tool and model, attributed to 

## 星数曲线

```mermaid
xychart-beta
    title "holistic-ai/surface 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-30 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `39316012391b` · [字段定义](../../DATASET.md)*
