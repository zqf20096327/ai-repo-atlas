# silicondawn/memory-viewer

⭐ 20 · TypeScript · MIT · 推送 2026-03-13 · [GitHub](https://github.com/silicondawn/memory-viewer) · 个人维护

**浏览与编辑 OpenClaw agent 记忆文件的 Web 界面**

面向 OpenClaw AI agent 的深色主题 Web UI，用于浏览、搜索和编辑 agent 以 Markdown 文件（MEMORY.md、memory/*.md）存储的记忆。功能包括可折叠文件树、GitHub 风格 Markdown 渲染、浏览器内编辑（Ctrl+S、乐观锁冲突检测）、全文搜索、系统仪表盘（运行时间/内存用量）、WebSocket 实时刷新、PWA 离线缓存、多 agent 工作区连接及大屏/车载触控优化。支持源码运行、npm 构建生产版与 Docker 预构建镜像部署，默认端口 8901。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Markdown 记忆文件的可折叠树浏览与全文即时搜索（Ctrl+K）
- 浏览器内直接编辑，Ctrl+S 保存并带乐观锁冲突检测
- 系统仪表盘：运行时间、内存用量、负载与当日记忆摘要
- 支持多 OpenClaw agent 工作区连接与 Docker 预构建镜像部署

## 适用场景

- 查看和修改我的 OpenClaw agent 的记忆文件
- 实时监控 agent 的系统状态与记忆变化
- 通过一个大屏界面同时管理多个 agent 工作区

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L8: A beautiful, dark-themed web UI for browsing and editing OpenClaw AI agent memory files. Built specifically for Open
> L21: OpenClaw agents store their memory in Markdown files (`MEMORY.md`, `memory/*.md`). Memory Viewer provides a dedicat

## 星数曲线

```mermaid
xychart-beta
    title "silicondawn/memory-viewer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-29 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `8fac02ef1467` · [字段定义](../../DATASET.md)*
