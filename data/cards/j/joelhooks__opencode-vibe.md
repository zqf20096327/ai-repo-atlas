# joelhooks/opencode-vibe

⭐ 179 · TypeScript · 推送 2026-07-27 · [GitHub](https://github.com/joelhooks/opencode-vibe) · [官网](https://opencode.ai) · 个人维护

**OpenCode 的 Next.js 16 Web 聊天界面，流式显示与多进程发现**

基于 Next.js 16（canary）重写的 OpenCode Web 应用，提供实时聊天 UI：消息流式显示、SSE 同步、React Server Components。自动发现本机所有运行中的 OpenCode 进程（经 lsof），支持跨进程消息（Web UI 发送、TUI 显示）、斜杠命令（/fix、/test 等）与 @ 文件引用。Monorepo 结构含 web 应用、swarm-cli 可视化 CLI、core 与 react 包。运行需 Bun v1.3+ 与本地 OpenCode CLI。README 声明使用 canary 版本，提示可能存在不稳定。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 自动发现所有运行中的 OpenCode 进程，无需配置
- 消息流式显示与 SSE 全量同步
- 跨进程消息：Web UI 发送内容出现在 TUI 中
- 斜杠命令与 @ 模糊搜索引用文件作为上下文

## 适用场景

- 在浏览器中以聊天界面使用本机 OpenCode CLI
- 同时查看和管理多个 OpenCode 进程的世界状态
- 用 @ 文件引用和斜杠命令快捷操作 AI 编码任务

## 场景标签

`聊天机器人` `编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L12: Next.js 16 rebuild of the OpenCode web application. Real-time chat UI with streaming message display, SSE sync, and
> L18: **Prerequisites:** Bun v1.3+ and OpenCode CLI running locally.

## 星数曲线

```mermaid
xychart-beta
    title "joelhooks/opencode-vibe 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-27"]
    y-axis "stars" 178 --> 181
    line [180, 179, 179]
```

2026-10-18 180 → 2026-10-27 179（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `b90d3d667416` · [字段定义](../../DATASET.md)*
