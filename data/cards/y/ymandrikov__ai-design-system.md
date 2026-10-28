# ymandrikov/ai-design-system

⭐ 21 · TypeScript · MIT · 推送 2026-09-22 · [GitHub](https://github.com/ymandrikov/ai-design-system) · 个人维护

**教编码 agent 何时及如何使用项目 UI 组件的技能**

面向 Claude Code、Codex 等编码 agent 的技能（skill）：以 Markdown 契约记录设计系统中各组件的公共 API、适用场景与组合规则，生成索引供 agent 查找，并附带 Node.js 脚本校验契约结构、链接与源文件新鲜度，防止文档与代码漂移。组件与业务逻辑保留在项目内，支持迁移已有 UI、接入 Figma 设计稿、通过 Lefthook 在 pre-commit 时校验暂存契约。需要 Node.js 与 Git，无法仅凭外观推断缺失的设计意图。

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

- Markdown 契约记录组件公共 API、适用场景与组合规则
- Node.js 脚本校验契约结构、链接、索引与源文件新鲜度
- migrate 工作流可为既有代码库补写契约并支持断点续跑
- Lefthook 集成在 pre-commit 检查受影响的契约

## 适用场景

- 让编码 agent 在我现有的设计系统内正确选用组件搭页面
- 为已有 UI 代码库补写组件契约并保持与代码同步
- 在提交时自动检查契约与源码是否漂移

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L3: A coding-agent skill that documents when and how to use your UI components.
> L31: npx skills add ymandrikov/ai-design-system --skill design-system
> L61: - Claude Code: `/design-system <task>`

## 星数曲线

```mermaid
xychart-beta
    title "ymandrikov/ai-design-system 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-28 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `5ddb7778373a` · [字段定义](../../DATASET.md)*
