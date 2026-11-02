# NeuralNomadsAI/CodeNomad

⭐ 2,657 · TypeScript · MIT · 推送 2026-11-01 · [GitHub](https://github.com/NeuralNomadsAI/CodeNomad) · [官网](https://neuralnomadsai.github.io/CodeNomad/) · 组织维护

**面向开发者的 OpenCode V2 桌面与浏览器工作台**

CodeNomad 是连接 OpenCode V2 共享后台服务的桌面（Electron/Tauri）与浏览器客户端：提供多项目管理、嵌套会话与全历史导航、会话分叉、Git worktree 管理、附件与富对话渲染、MCP 连接管理、SideCar 网页工具嵌入、远程访问（密码认证、HTTPS、OpenTunnel 中继配对）以及语音输入输出。要求 OpenCode V2（2.2.3 起）与 Git；桌面版内置 Node.js，服务器模式需 Node.js 24 LTS。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 连接 OpenCode 共享后台服务，会话可跨客户端访问
- 嵌套会话、分叉、时间线导航与全历史搜索
- Git worktree 创建/迁移与工作区内变更审查
- 桌面/浏览器/手机远程访问（OpenTunnel 中继，无需开端口）

## 适用场景

- 在多个项目与长对话中管理 AI 编码会话
- 用 Git worktree 并行开展多分支 agent 任务
- 从手机或其他电脑远程接入本机编码会话

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L5: CodeNomad is a **desktop and browser workspace for OpenCode V2** — built for developers who work across projects, lo
> L25: - **🧩 Tools and previews** — Monitor native background shells, manage MCP connections and Global/Project plugin act
> L91: - **One shared OpenCode service** owns sessions and messages. Closing a CodeNomad tab, window, or backend leaves th


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-02 · 置信度 mid · 依据 README sha `759c0e2d787a` · [字段定义](../../DATASET.md)*
