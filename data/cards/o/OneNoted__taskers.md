# OneNoted/taskers

⭐ 19 · Rust · MIT · 推送 2026-06-21 · [GitHub](https://github.com/OneNoted/taskers) · 个人维护

**面向大量 agent 终端作业的 Linux 工作区应用**

Linux 桌面终端工作区应用：以顶层工作区窗口、窗口内窗格、窗格内标签三级结构组织终端作业，通过 attention rail 呈现未读、等待、错误与完成四类状态；本地 taskersctl CLI 提供通知、agent 状态检查、浏览器自动化与调试工具，并内置 shell 辅助函数供脚本上报状态。安装走 cargo install 或 AUR 包，需 GTK4/libadwaita 与 WebKitGTK 6.0 依赖；macOS 版本未在本仓库发布。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 工作区窗口/窗格/标签三级终端组织模型
- attention rail 聚合未读、等待、错误、完成状态供运维分诊
- taskersctl 本地控制 CLI：通知、浏览器快照、shell 集成、运行时调试
- 内部 terminal sidecar 维持终端会话持久化，缺失时回退新 shell 并警告

## 适用场景

- 同时跑多个编码 agent 时分窗管理与分诊各任务状态
- 通过脚本通知与状态上报让长任务结果可被关注栏追踪
- 在终端工作区内打开浏览器窗格并用 CLI 做自动化检查

## 场景标签

`浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L3:  A Linux-first terminal workspace for agent-heavy work. Top-level workspace windows, panes, tabs, an attention rail,
> L25: work. The local `taskersctl` CLI ties those surfaces together with

## 星数曲线

```mermaid
xychart-beta
    title "OneNoted/taskers 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-30 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `bfe313939fb3` · [字段定义](../../DATASET.md)*
