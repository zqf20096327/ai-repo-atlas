# engasnm111/lnwdeck

⭐ 13 · Rust · MIT · 推送 2026-09-17 · [GitHub](https://github.com/engasnm111/lnwdeck) · 个人维护

**Windows 本地 AI 用量与配额追踪桌面应用**

Windows 桌面应用（Rust/React/SQLite 栈），读取本地 AI 工具已生成的产物文件，记录请求、输入/输出 token、模型与时间戳，基于内置本地价格目录计算成本，并展示各 provider 上报的配额余量。完全本地运行：无账号、无服务器、无云端同步。提供仪表盘、浮动配额挂件、桌面宠物三种界面，支持预算、告警、诊断与脱敏 JSON 导出。仅支持 Windows 平台，需逐机配置 OpenCode (Go) 等配额凭据。

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

- 读取本地 AI 工具产物记录 token 用量与成本，只读且有界扫描
- 区分 provider 上报配额与本地用量历史，缺失时显示 usage-only 而非编造百分比
- 本地价格目录计价，无精确匹配的模型给出显式估算
- 仪表盘/挂件/桌面宠物三界面，九种语言本地化

## 适用场景

- 在 Windows 上追踪多个 AI 工具的 token 消耗与花费
- 查看各 provider 上报的配额余量与重置窗口
- 设置预算与告警，导出脱敏用量数据

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L3: Universal AI usage and quota tracker for Windows. lnwdeck reads the local
> L14: - Records local usage history: requests, input/output tokens, models and
> L20: - Provides budgets, alerts, diagnostics and sanitized JSON export.

## 星数曲线

```mermaid
xychart-beta
    title "engasnm111/lnwdeck 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `e3bf8ac569f0` · [字段定义](../../DATASET.md)*
