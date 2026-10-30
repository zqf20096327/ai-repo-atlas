# openai/euphony

⭐ 424 · TypeScript · Apache-2.0 · 推送 2026-04-22 · [GitHub](https://github.com/openai/euphony) · [官网](https://openai.github.io/euphony/) · 组织维护

**在浏览器中可视化 Harmony 对话与 Codex 会话数据的查看器**

OpenAI 维护的浏览器端数据可视化工具：以可嵌入的 Web Components 渲染 Harmony 结构化对话数据与 Codex 会话 JSONL 日志，支持剪贴板、本地 .json/.jsonl 文件或公共 HTTP(S) URL 加载数据，并提供 Markdown 渲染、元数据检查、JMESPath 过滤、网格视图、JSONL 编辑与 Harmony token 渲染等功能。可选 FastAPI 后端用于本地开发加载大数据集，但 README 提示其远程 URL 抓取路径存在 SSRF 风险，仅限本地使用。面向需要检查训练、评测与 agent 工作流对话数据的开发者。

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

- 渲染 Harmony 对话与自动检测并转换 Codex 会话 JSONL 文件
- 可嵌入任意框架（React/Svelte/Vue）的 Web Components 库
- JMESPath 过滤、网格视图、编辑器模式与 Harmony token 渲染
- 前端独立与后端辅助两种运行模式

## 适用场景

- 在浏览器中检查 Harmony 训练/评测对话数据
- 查看 Codex CLI 会话日志的时间线
- 将对话查看器组件嵌入自己的 Web 应用

## 场景标签

 · 领域:AI 开发工具/数据可视化

## 证据(README 行号)

> L12: Harmony conversations and [Codex session
> L15: inspect. Euphony addresses that gap by providing **portable**, **customizable**,

## 星数曲线

```mermaid
xychart-beta
    title "openai/euphony 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-30"]
    y-axis "stars" 422 --> 425
    line [423, 424, 424]
```

2026-10-18 423 → 2026-10-30 424（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `7a77832774c0` · [字段定义](../../DATASET.md)*
