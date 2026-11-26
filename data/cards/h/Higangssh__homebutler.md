# Higangssh/homebutler

⭐ 403 · Go · MIT · 推送 2026-11-25 · [GitHub](https://github.com/Higangssh/homebutler) · [官网](https://homebutler.dev) · 个人维护

**给 homelab 用户的差异化巡检工具：只报告值得说的变更**

单个 Go 二进制的家用服务器运维工具：对上次快照与当前状态做对比，按八类变更（gone/new/replaced/port/disk 等）输出人读摘要与 JSON，专门识别同名容器被替换这类计数不变的变更；附带 doctor 体检（磁盘、证书、备份、Proxmox 等）、backup drill 恢复验证（隔离容器启动 + HTTP 健康检查）与一键应用部署。无守护进程、无数据库，通过 SSH 按需运行；判定规则为书面规则而非模型，支持 cron 与终端彩色输出。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 快照对比报告：八类变更分类，JSON 与终端输出字段一致
- backup drill 在隔离容器中启动备份并通过 HTTP 健康检查
- doctor 只读体检，逐项给出下一条命令，支持 --strict 供 cron/CI
- 内置 MCP server，AI 代理可在不持有 SSH shell 的情况下检查服务器

## 适用场景

- 想知道两次巡检之间服务器上到底变了什么
- 验证备份是否真的可以恢复
- 让 AI 助手查看服务器状态而不开放完整 SSH 权限
- 一键部署 Uptime Kuma、Jellyfin 等自托管应用

## 场景标签

 · 领域:服务器运维/homelab 工具

## 证据(README 行号)

> L91: The design goal is simple: give humans and agents a narrow, structured interface to the server. HomeButler returns 
> L103: - **The judgement is a written rule, not a model.** What earns a line is in docs/report.md, and the same input giv
> L152: - **Use it anywhere** — CLI, JSON, web dashboard, or MCP for AI agents without giving them SSH

## 星数曲线

```mermaid
xychart-beta
    title "Higangssh/homebutler 星数(近 24 点)"
    x-axis ["2026-10-24", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-30", "2026-10-31", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26"]
    y-axis "stars" 296 --> 412
    line [305, 306, 308, 309, 313, 314, 315, 305, 315, 343, 353, 356, 358, 360, 365, 371, 377, 380, 381, 383, 387, 391, 397, 403]
```

2026-10-24 305 → 2026-11-26 403（+98）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 mid · 依据 README sha `ba8c0801a43f` · [字段定义](../../DATASET.md)*
