# xcanwin/manyoyo

⭐ 13 · JavaScript · Apache-2.0 · 推送 2026-10-29 · [GitHub](https://github.com/xcanwin/manyoyo) · [官网](https://xcanwin.github.io/manyoyo/) · 个人维护 · 中文 README

**AI 编程智能体的 Docker/Podman 容器安全沙箱**

面向使用 Claude Code、Codex、Gemini CLI、OpenCode 等编程智能体的开发者，提供单一入口在 Docker/Podman 容器内以 YOLO 模式运行这些 Agent，实现容器隔离（Agent 仅可见指定工作目录）。提供浏览器网页界面（对话、看文件、开终端，手机可用），配置集中于 ~/.manyoyo/manyoyo.json。安装支持 curl 脚本或 npm 全局安装，默认镜像首次使用自动拉取，支持自定义构建。README 明确声明：主要隔离手段是容器而非虚拟机，不是绝对安全，YOLO/SOLO 模式仍可能执行危险命令。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一个入口管理 claude/codex/gemini/opencode 四种 Agent
- 基于 Docker/Podman 的容器隔离，Agent 仅可见指定工作目录
- 浏览器网页界面：对话、文件浏览、终端，手机可用
- 一条命令完成安装、升级、卸载，配置统一集中管理

## 适用场景

- 让 AI 编程智能体以 YOLO 全自动模式跑在隔离沙箱里，保护宿主机
- 在浏览器或手机上远程使用和监控多个 AI 编程 Agent
- 把本机已有的多个 Agent 配置统一搬进一个沙箱环境管理

## 场景标签

 · 领域:开发者工具/Agent 基础设施

## 证据(README 行号)

> L4:  Open-source sandbox for AI coding agents: run Claude Code, Codex, Gemini CLI and OpenCode in YOLO mode safely insid
> L52: - **多 Agent**：`claude`、`codex`、`gemini`、`opencode` 一个入口
> L53: - **容器隔离**：基于 Docker / Podman，Agent 只能看到你给它的工作目录

## 星数曲线

```mermaid
xychart-beta
    title "xcanwin/manyoyo 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-31"]
    y-axis "stars" 11 --> 14
    line [12, 13, 13]
```

2026-10-18 12 → 2026-10-31 13（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `ec068c3555dc` · [字段定义](../../DATASET.md)*
