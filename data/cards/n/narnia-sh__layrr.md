# narnia-sh/layrr

⭐ 267 · TypeScript · MIT · 推送 2026-05-10 · [GitHub](https://github.com/narnia-sh/layrr) · [官网](https://layrr.dev) · 个人维护

**浏览器点击选元素并向编码 agent 下指令的中间层**

Layrr 运行在浏览器与本地开发服务器之间：通过代理注入 overlay，用户在运行中的 web 应用里点击元素，Layrr 将元素映射回源码位置，连同自然语言指令发送给所选编码 agent（Claude Code、Codex CLI 或经 Pi 的 Gemini）完成编辑。以 git 提交作为撤销路径，支持从 overlay 历史预览与回滚编辑。面向使用本地编码 agent 的前端/全栈开发者，通过 npm 全局安装。

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

- 点击元素映射回源码位置并附指令发给编码 agent
- 支持 Claude Code / Codex CLI / Gemini（经 Pi）三种 agent
- git 提交作为撤销路径，可预览与回滚编辑
- 以代理方式注入 overlay，无需改动应用本身

## 适用场景

- 在浏览器里指着元素直接描述样式或文案修改
- 免去手工定位文件与行号再转述给编码 agent
- 通过 overlay 历史回滚不满意的 AI 编辑

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L7:  Layrr lets you click an element in your running web app, describe the change in plain English, and send the exact s
> L16: Layrr sits between your browser and local dev server. It injects a small overlay, maps clicked elements back to sou

## 星数曲线

```mermaid
xychart-beta
    title "narnia-sh/layrr 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 266 --> 268
    line [267, 267]
```

2026-10-18 267 → 2026-10-24 267（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `764e137ad0d9` · [字段定义](../../DATASET.md)*
