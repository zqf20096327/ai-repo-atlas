# bo-516/ide-byebye

⭐ 30 · TypeScript · MIT · 推送 2026-10-20 · [GitHub](https://github.com/bo-516/ide-byebye) · [官网](https://www.npmjs.com/package/ide-byebye) · 个人维护 · 中文 README

**前端开发者工具：⌘-点击页面元素即定位源码并唤起 AI 代理编辑**

以构建工具插件形式（Vite/webpack/rspack/rsbuild/Next.js/Angular CLI 等）接入前端项目。开发者按住 ⌘/Ctrl 点击运行中的应用元素并输入修改描述，工具生成含精确文件与行号的 `@file #lines` 提示词，交给 Claude App、Codex、Cursor、Grok Build、Claude Code CLI 等代理执行编辑。仅运行于开发环境，不含模型或 AI SDK，本地 127.0.0.1 通信，不直接改文件。README 附有 Grok Build 上的 token/耗时测量数据。

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

- ⌘-点击元素生成 `@file #lines` 精确定位提示词
- 支持 10 余种 AI 代理与 IDE，含注入已开启会话
- 兼容 Vite/webpack/rspack/rsbuild/esbuild/Farm/Next.js/Angular CLI 等构建工具
- 仅 dev 环境运行、本地通信、项目根目录限定

## 适用场景

- 给 AI 代理精确指出前端组件位置，减少其查找与误改
- 从运行中的页面直接发起 UI 修改并切换不同代理
- 降低代理编辑前端时的 token 消耗与上下文占用

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L68: It runs only in dev, ships no model or AI SDK, and never edits your files. It
> L31: **It works seamlessly with the agent you already use.** Claude, Codex, Cursor,

## 星数曲线

```mermaid
xychart-beta
    title "bo-516/ide-byebye 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-30 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `0a1bfdd86aeb` · [字段定义](../../DATASET.md)*
