# Jamessdevops/micracode

⭐ 297 · TypeScript · MIT · 推送 2026-09-06 · [GitHub](https://github.com/Jamessdevops/micracode) · [官网](https://www.micracode.com/) · 个人维护

**本地运行的 AI 网页应用生成器：自然语言描述生成代码**

面向终端用户的桌面端 AI 编码工作区：输入自然语言描述即可流式生成完整项目代码，通过聊天迭代或在 Monaco 编辑器中直接编辑并实时预览。核心后端（TypeScript + pi coding agent SDK + Hono）以进程内方式运行于 Electron 33 内，无需单独后端与数据库；API key 本地存储。支持 OpenAI、Google Gemini、Anthropic 三类 provider。macOS 提供 Releases 构建包，源码开发需 Node.js 22 与 Bun。部分端点（VCS/checkpoints 等）为 stub 返回 501。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自然语言描述生成项目，聊天迭代 + Monaco 编辑器直接编辑
- 核心后端进程内运行于 Electron，无独立后端/数据库，项目存为普通文件夹
- 支持 OpenAI / Google Gemini / Anthropic API key，模型选择器按已配置 key 显示
- 可发布/更新/撤销 temp.md 静态公开预览链接

## 适用场景

- 用一句话描述让 AI 生成可运行的网页应用
- 在本地无后端环境下迭代改代码并实时预览
- 分享生成的应用的临时公开预览链接

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L6:  Describe an app in natural language and Micracode streams code into an in-browser workspace.
> L32: - Type a description on the home screen → Micracode generates a working project

## 星数曲线

```mermaid
xychart-beta
    title "Jamessdevops/micracode 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-24"]
    y-axis "stars" 295 --> 298
    line [296, 297, 297]
```

2026-10-18 296 → 2026-10-24 297（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `82aac005db5c` · [字段定义](../../DATASET.md)*
