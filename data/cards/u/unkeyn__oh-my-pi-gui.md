# unkeyn/oh-my-pi-gui

⭐ 20 · TypeScript · NOASSERTION · 推送 2026-08-16 · [GitHub](https://github.com/unkeyn/oh-my-pi-gui) · 个人维护

**Oh My Pi 编码 agent 的原生 Windows 桌面图形界面**

基于 Tauri 的 Windows 桌面端，为 Oh My Pi (OMP) agent 运行时提供图形工作区：多工作区与会话管理、流式响应与工具调用展示、上下文预算检查、模型角色分配、API key 池管理（轮换/隔离/健康检查）、MCP 与插件浏览、浏览器工具侧边栏。面向不想在终端中全天使用 OMP 的用户；自身不替代 OMP 核心，复用上游运行时与 provider 注册表。首次启动经 Desktop.cmd 引导脚本自动下载依赖（Bun、原生组件等），支持 FreeLLMAPI 可选本地安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多工作区/会话管理与流式响应、工具调用、浏览器操作的时序展示
- API key 池管理：健康检查、轮换、冷却、隔离与无效键清理
- 上下文预算检查：系统上下文、工具、MCP、技能、消息历史的占用
- 模型角色（Primary/Fast/Heavy/Vision 等）与思考级别分配

## 适用场景

- 在桌面图形界面中运行 Oh My Pi 编码 agent 而非终端
- 集中管理多个项目的会话、上下文与 token 用量
- 管理 provider 凭据、API key 池与模型路由

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L12: Oh My Pi GUI is for people who want Pi's agent runtime without spending the whole day in a terminal. It is a Deskto
> L119: Oh My Pi GUI does not replace the OMP core. It provides a native Desktop surface for the upstream runtime and keep

## 星数曲线

```mermaid
xychart-beta
    title "unkeyn/oh-my-pi-gui 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-30 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `8c942d18f21c` · [字段定义](../../DATASET.md)*
