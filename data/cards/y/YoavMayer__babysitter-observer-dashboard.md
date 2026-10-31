# YoavMayer/babysitter-observer-dashboard

⭐ 25 · TypeScript · MIT · 推送 2026-08-10 · [GitHub](https://github.com/YoavMayer/babysitter-observer-dashboard) · 个人维护

**AI agent 运行的实时只读看板：任务进展与编排状态监控**

面向使用 babysitter 编排多步 AI agent 工作流的开发者，提供浏览器端的实时监控看板：自动发现磁盘上 .a5c/runs/ 目录，按项目分组展示运行状态，通过 SSE 在 journal 文件变化时即时推送更新。提供看板视图、流水线可视化、运行详情、全局搜索等只读功能，唯一写路径为断点批准（写 result.json）。零配置启动，支持 npx 直接运行、全局安装或作为 dev 依赖，默认监听 4800 端口。限制：依赖 Node.js >= 20 与 babysitter 产生的运行目录。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自动发现多项目 .a5c/runs/ 目录并按项目分组
- SSE 实时推送 + 可调轮询的事件流更新
- 看板/列表双视图与全键盘导航（WCAG AA 无障碍）
- CLI/环境变量/设置面板三种配置途径（持久化到 ~/.a5c/observer.json）

## 适用场景

- 多项目并行的 agent 编排运行需要集中监控是否需要人工介入
- 在浏览器中查看运行流水线、耗时与错误详情
- 不切回终端即可批准或忽略等待中的断点

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L13: Real-time observability dashboard for babysitter orchestration runs.
> L17: Babysitter Observer Dashboard is a real-time browser-based monitoring UI for babysitter orchestration runs. If you 

## 星数曲线

```mermaid
xychart-beta
    title "YoavMayer/babysitter-observer-dashboard 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-31 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `f280fc7ff872` · [字段定义](../../DATASET.md)*
