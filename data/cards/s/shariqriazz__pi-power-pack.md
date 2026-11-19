# shariqriazz/pi-power-pack

⭐ 15 · TypeScript · MIT · 推送 2026-11-10 · [GitHub](https://github.com/shariqriazz/pi-power-pack) · [官网](https://pi.dev/packages/pi-power-pack) · 个人维护

**Pi 编码代理的扩展合集：子代理、后台终端与上下文压缩等**

面向 Pi coding agent 1.0 的单一 npm 扩展包，包含子代理（带 profile、worktree 隔离与接管面板）、后台终端、智能上下文压缩、目标、任务列表、ask_user 结构化提问、图像/视频/音频理解、WebP 图片、Firecrawl 网络搜索等十余个扩展，每个扩展可经 pi config 独立开关。通过 pi install 安装，支持 npm 与 Git 两种来源；在 Linux 与 macOS 上开发测试。旧名 shariq-pi-extensions 已停更，需切换到本包且不可同时安装。

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

- 子代理支持 profiles、worktree 隔离、peer messaging 与接管面板
- 智能压缩：上下文填满时保留文件、worktree 状态与进行中工作
- 图像/视频/音频理解与 WebP 图片转换（默认关闭）
- 每个扩展可独立开关，跟随包配置

## 适用场景

- 给 Pi 编码代理加子代理与后台终端能力
- 长任务中压缩上下文而不丢失工作状态
- 让代理向用户提多选题而非猜测
- 通过 Firecrawl 为代理接入网络搜索与抓取

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L8: Subagents, background terminals, smart compaction, goals, a task list, structured questions, image, video, and audio
> L49: The suite is developed and tested against Pi 1.0 on Linux and macOS. See docs/EXTENSIONS.md for commands, tools, co

## 星数曲线

```mermaid
xychart-beta
    title "shariqriazz/pi-power-pack 星数(近 3 点)"
    x-axis ["2026-11-02", "2026-11-11", "2026-11-19"]
    y-axis "stars" 13 --> 16
    line [14, 15, 15]
```

2026-11-02 14 → 2026-11-19 15（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-18 · 置信度 high · 依据 README sha `71ae7899aeeb` · [字段定义](../../DATASET.md)*
