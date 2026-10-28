# imprsnst/Comfy-Spaces

⭐ 45 · TypeScript · MIT · 推送 2026-04-30 · [GitHub](https://github.com/imprsnst/Comfy-Spaces) · 个人维护

**隔离运行多个 ComfyUI 工作区的管理工具，含自定义节点依赖检查**

面向 ComfyUI 用户的 Web 端工作区管理工具：创建并隔离多个 ComfyUI 实例，从 GitHub 安装与更新自定义节点，自动解析依赖并处理冲突，记录并回滚 requirements 变更历史；支持跨工作区共享模型、应用内运行 ComfyUI 与输出文件管理。技术栈为 Node.js 18+/Python 3.8+/Git，通过 npm install 与 npm run dev 启动开发服务器，每个工作区位于 /spaces/space-id/ComfyUI 路径下。

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

- 创建和管理相互隔离的多个 ComfyUI 工作区
- 自定义节点 GitHub 安装/更新与依赖冲突处理
- requirements 变更历史追踪与回滚
- 跨工作区共享模型与应用内运行 ComfyUI

## 适用场景

- 为不同项目或工作流维护互不干扰的 ComfyUI 环境
- 安装自定义节点时自动处理依赖冲突，避免破坏主环境
- 回溯并恢复节点的依赖版本变更

## 场景标签

 · 领域:AI 工作流/开发工具

## 证据(README 行号)

> L3: Run your ComfyUI in clean, isolated workspaces with smart custom-node checks — so broken nodes don’t crash, conflict
> L16: - **Multiple Workspaces** — Create and manage isolated ComfyUI spaces

## 星数曲线

```mermaid
xychart-beta
    title "imprsnst/Comfy-Spaces 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 44 --> 46
    line [45, 45]
```

2026-10-18 45 → 2026-10-28 45（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `6e1b172c70b7` · [字段定义](../../DATASET.md)*
