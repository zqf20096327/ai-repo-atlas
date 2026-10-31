# abrahao-dev/podium-app

⭐ 14 · TypeScript · MIT · 推送 2026-07-12 · [GitHub](https://github.com/abrahao-dev/podium-app) · 个人维护

**在无限画布上编排多个 AI 编码 agent 终端的桌面应用**

基于 Tauri 2 + React 18 的桌面应用：把 Claude Code、Codex、OpenCode 等 CLI agent（或普通 shell）作为终端节点放到可缩放的 2D 画布上，支持拖拽、重命名与节点间连线。连线后可将源 agent 的输出包装为 handoff 模板写入目标 agent 的 stdin，实现 agent 间交接；也可连接 markdown 便签捕获带时间戳的输出；底部输入框可向所有相连终端广播 prompt。应用自身不含 AI 模型，需用户自行安装 agent CLI。工作区以 JSON 自动保存。作者声明这是早期 MVP，Windows 平台（ConPTY）仍在调整阶段。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 真 PTY 终端节点（portable-pty，支持 ConPTY/openpty）置于 React Flow 无限画布
- 终端→终端连线：源 agent 输出包装为 handoff 写入目标 agent 的 stdin
- 终端→便签：捕获最近 20 行输出为带时间戳的 markdown
- 底部输入框向所有相连终端广播同一 prompt

## 适用场景

- 并行运行多个 AI 编码 agent 并总览全局
- 把一个 agent 的输出直接交接给下一个 agent 处理
- 用便签记录 agent 输出供后续查阅

## 场景标签

`多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L7: Drop Claude Code, Codex, OpenCode — or plain shells — onto a zoomable canvas, wire them together, and let agents pip
> L35: |🖥️ **Real terminals**|Full PTY round-trip via `portable-pty` — typing, colors, resize, Ctrl+C, arrows. Launch `cla

## 星数曲线

```mermaid
xychart-beta
    title "abrahao-dev/podium-app 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-31"]
    y-axis "stars" 12 --> 15
    line [13, 14, 14]
```

2026-10-18 13 → 2026-10-31 14（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `65cf664fc9ad` · [字段定义](../../DATASET.md)*
