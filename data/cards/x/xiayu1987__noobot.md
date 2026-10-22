# xiayu1987/noobot

⭐ 191 · JavaScript · MIT · 推送 2026-10-13 · [GitHub](https://github.com/xiayu1987/noobot) · 个人维护 · 中文 README

**自托管 AI agent 工作台：多模型路由、工具调用与 3D 角色动画**

基于 Node.js、Vue 3 与 Electron 的开源 Web/桌面 AI agent 应用，可自托管部署。提供多用户隔离工作区、持久会话、文件/脚本执行/浏览器自动化等可扩展工具、OpenAI 兼容接口的多模型族路由、MCP 与连接器、多 agent 任务委派与语义工作流；另支持导入 3D 角色用自然语言生成与迭代动画（Three.js 渲染）。安装含 Windows/macOS 桌面包与 start.sh 一键部署，沙箱模式依赖 Docker 执行命令，libreoffice/ffmpeg 为可选系统依赖。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- OpenAI 兼容多模型路由、工具调用与 MCP 连接器
- 多 agent 编排：任务委派、语义工作流、规划/审查机制
- 自然语言创建并迭代 3D 单/多角色动画，无需动画代码
- start.sh 一键 PM2 + Caddy 部署，桌面端提供 Windows/macOS 安装包

## 适用场景

- 自托管一个多用户隔离的 AI agent 工作区
- 在对话中编排多 agent 工作流并调用文件、浏览器等工具
- 用自然语言驱动 3D 角色生成和修改动画

## 场景标签

 · 领域:AI Agent 应用/生产力工具

## 证据(README 行号)

> L18: Noobot is an open-source Web and desktop AI agent application built with Node.js, Vue 3, and Electron. It provides 
> L5: **Cheap Money-Saving Self-hosted AI agent workspace for tool calling, multi-model routing, MCP, and multi-agent work
> L59: - **Model interoperability:** OpenAI-compatible provider interfaces, provider/model-family routing, tool calling, s

## 星数曲线

```mermaid
xychart-beta
    title "xiayu1987/noobot 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22"]
    y-axis "stars" 187 --> 192
    line [188, 191, 191]
```

2026-10-18 188 → 2026-10-22 191（+3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `50826b55e0eb` · [字段定义](../../DATASET.md)*
