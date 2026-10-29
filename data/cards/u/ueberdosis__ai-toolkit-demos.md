# ueberdosis/ai-toolkit-demos

⭐ 25 · TypeScript · 推送 2026-10-23 · [GitHub](https://github.com/ueberdosis/ai-toolkit-demos) · [官网](https://tiptap.dev/docs/content-ai/capabilities/ai-toolkit/overview) · 组织维护

**Tiptap AI Toolkit 功能演示集：AI 读写文档的示例工程**

由 Tiptap 团队（ueberdosis）维护的 Next.js 演示项目，展示 Tiptap AI Toolkit 的能力：AI Agent 可读写与编辑 Tiptap 文档、管理评论与线程、感知 schema 与选区；Workflow 模式提供内置提示词执行插入、校对、编辑等单一任务；另有在服务端运行 AI 操作的 Server AI Toolkit 演示。技术栈为 React + Next.js、Vercel AI SDK、OpenAI 模型。运行需配置 .npmrc（Tiptap Pro 扩展）、OPENAI/ANTHROPIC API key，服务端演示还需 Tiptap Cloud 密钥。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- AI Agent 读取/编辑 Tiptap 文档，含多文档、schema 感知与选区感知
- Review Changes 演示以建议形式预览并逐条/批量接受或拒绝 AI 修改
- 服务端 AI Toolkit 在服务器执行编辑，支持流式与 tracked-changes 模式
- Workflow 模式提供内置提示词的插入、校对、编辑任务

## 适用场景

- 评估 Tiptap AI Toolkit 各项能力再决定是否接入
- 参考示例代码实现编辑器内的 AI 助手或校对功能
- 了解服务端运行 AI 编辑操作的实现方式

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L3: This is a Next.js project demonstrating the Tiptap AI Toolkit capabilities.
> L45: - Tiptap AI Toolkit

## 星数曲线

```mermaid
xychart-beta
    title "ueberdosis/ai-toolkit-demos 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-29 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `b7704397f2ab` · [字段定义](../../DATASET.md)*
