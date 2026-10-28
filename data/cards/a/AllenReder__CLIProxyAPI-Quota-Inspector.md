# AllenReder/CLIProxyAPI-Quota-Inspector

⭐ 33 · Go · MIT · 推送 2026-04-17 · [GitHub](https://github.com/AllenReder/CLIProxyAPI-Quota-Inspector) · 个人维护 · 中文 README

**CLIProxyAPI 用户查看各提供商配额用量的终端工具**

用 Go 编写的跨平台命令行工具，连接运行中的 CLIProxyAPI/CPA 服务，读取实时数据并在终端按提供商（Codex、Gemini CLI、Antigravity）分区展示配额状态、进度条与汇总统计，支持按 plan/status/剩余额度归并账户。可通过 go build 从源码构建，需提供 CPA 管理 key 与已配置的认证文件，支持批量检查、JSON/纯文本输出、并发与过滤参数。注意 README 声明不显示 Code review 配额。

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

- 按提供商分区展示 Codex 5h/7d、Gemini CLI、Antigravity 配额
- 按 plan/status/剩余额度汇总账户统计
- 支持多认证文件批量检查与 JSON/纯文本输出
- 提供并发数、过滤、重试等命令行参数

## 适用场景

- 运维多个 CLI 代理账户时快速查看各提供商配额余量
- 按套餐或状态筛选并汇总账户配额情况
- 以 JSON 输出接入其他监控或脚本流程

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L7: A cross-platform quota inspector for CLIProxyAPI / CPA.
> L9: It reads live data from a running CPA service and shows provider-based quota sections, statuses, progress bars, and 

## 星数曲线

```mermaid
xychart-beta
    title "AllenReder/CLIProxyAPI-Quota-Inspector 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-28 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `ca191f1b4c3f` · [字段定义](../../DATASET.md)*
