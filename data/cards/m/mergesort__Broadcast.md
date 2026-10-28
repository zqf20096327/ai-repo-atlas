# mergesort/Broadcast

⭐ 50 · Swift · MIT · 推送 2026-10-17 · [GitHub](https://github.com/mergesort/Broadcast) · [官网](https://build.ms/broadcast/docs) · 个人维护

**面向 Swift 应用与编码代理的结构化日志库**

Swift 结构化日志库，提供 Log 类型与可组合的日志目的地（ConsoleLogger 写入 Apple 统一日志、SessionLogger 内存缓冲、MultiSessionLogger 跨启动持久化）。日志由 Level/Signal/Category/Payload 原语构成结构，支持 default/json/canonicalLogLine/tokenOptimized 四种内置格式，其中 tokenOptimized 为压缩 AI 上下文窗口设计；可转发至 swift-log 后端。另附 Claude Code 与 Codex 插件，帮助编码代理按推荐模式集成日志。要求 iOS 18+/macOS 15+/Swift 6.1+（Linux），作者称其已在 Plinky 生产环境使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 可组合的日志目的地架构（控制台/内存缓冲/跨启动持久化/自定义）
- Level/Signal/Category/Payload 四原语构成的结构化日志
- tokenOptimized 紧凑格式面向 AI 上下文窗口优化
- 内置 Claude Code 与 Codex 编码代理插件

## 适用场景

- Swift 应用中用接近 print 的 API 记录结构化生产日志
- 导出支持日志供人工或编码代理排查问题
- 服务器端通过 swift-log 后端统一收集日志

## 场景标签

 · 领域:软件开发/日志

## 证据(README 行号)

> L5: Broadcast is a structured logging library for Swift apps and servers that feels as lightweight as `print`, but gives
> L151: `.tokenOptimized`: A compact log format designed to optimize AI context windows.
> L188: Broadcast includes Claude Code and Codex plugins. These skills will help your coding agents integrate Broadcast in

## 星数曲线

```mermaid
xychart-beta
    title "mergesort/Broadcast 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 49 --> 51
    line [50, 50]
```

2026-10-18 50 → 2026-10-28 50（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `e7585f85af7d` · [字段定义](../../DATASET.md)*
