# christinevall/ds-base-ui

⭐ 18 · TypeScript · MIT · 推送 2026-10-22 · [GitHub](https://github.com/christinevall/ds-base-ui) · [官网](https://christinevall.github.io/ds-base-ui/) · 个人维护

**供设计师学习 AI 设计系统工作流的教学型设计系统仓库**

基于 Base UI 与 React 的小型真实设计系统（42 个组件），用 Storybook 文档化并镜像到 Figma。token 以 DTCG JSON 为单一来源，经 Style Dictionary 生成 CSS 变量；代码为源，通过 figma-library-from-code 技能（Claude + Figma Console MCP）生成 Figma 库，validate/sync-status 检查两边命名一致。明确声明为教学仓库而非生产系统，提供在线 Storybook、ZIP 下载与 npm 本地运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 42 个 React 组件，Base UI 原语包装，Storybook 展示
- DTCG JSON token 经 Style Dictionary 生成 CSS 变量并同步为 Figma 变量
- validate/sync-status/audit/contrast 检查代码与 Figma 命名一致性
- Storybook MCP 与 Figma Console MCP 供 Claude/Cursor 读取与构建

## 适用场景

- 学习设计 token 从代码到 Figma 的完整链路
- 用 AI 助手（Claude/Cursor）在设计系统上实践 design-to-code 工作流
- 对照 Storybook 与 Figma 库理解组件变体映射

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L3: A playground for designers learning AI design system workflows. It is a small, real design system built on Base UI p
> L5: It is a teaching repo, not a production system. 42 components, 4 foundations pages, 4 full-screen patterns.
> L66: |**Storybook MCP** and **a11y** addons|A plug for AI assistants, and an accessibility checker|Claude or Cursor ask 

## 星数曲线

```mermaid
xychart-beta
    title "christinevall/ds-base-ui 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `b3a990177485` · [字段定义](../../DATASET.md)*
