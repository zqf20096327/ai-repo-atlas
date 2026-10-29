# arikusi/nakkas

⭐ 30 · TypeScript · MIT · 推送 2026-07-14 · [GitHub](https://github.com/arikusi/nakkas) · [官网](https://www.npmjs.com/package/nakkas) · 个人维护

**让 AI 助手通过 JSON 配置生成动画 SVG 的 MCP 服务器**

面向 Claude Desktop、Claude Code、Cursor 等 MCP 客户端的渲染服务器：AI 构造声明式 SVGConfig JSON，服务器渲染为 CSS @keyframes 与 SMIL 动画的 SVG（无 JavaScript，可在 GitHub README 中显示）。提供 render_svg、preview、save 三个工具；渲染结果以 PNG 预览与 artifact id 返回，SVG 文本保留在服务端（上限 32 个，最旧淘汰），降低迭代 token 成本。含设计分析警告（溢出、对比度、文本重叠）与帧采样验证动画。零外部依赖，本地运行，无需 API key。

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

- 声明式 JSON 渲染纯 SVG 动画（CSS @keyframes + SMIL，无 JavaScript）
- 每次渲染返回 PNG 预览与 artifact id，SVG 文本不进入模型上下文窗口
- 设计审计：视口溢出、WCAG 对比度、文本重叠、动画数量等警告
- filmstrip 帧采样（2-10 帧）自行求值 @keyframes 以验证运动效果

## 适用场景

- 让 AI 助手生成 GitHub README 横幅、徽章、加载动画和 logo
- 通过预览-修改循环迭代生成矢量生成艺术
- 在本地无 API key 环境下让 AI 客户端输出可嵌入网页的动画 SVG

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L26: Nakkas is an MCP (Model Context Protocol) server that lets AI assistants like Claude create animated SVG graphics f
> L40: * **One tool, infinite designs.** `render_svg` takes a JSON config. AI fills in everything.

## 星数曲线

```mermaid
xychart-beta
    title "arikusi/nakkas 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-29"]
    y-axis "stars" 28 --> 31
    line [29, 30, 30]
```

2026-10-18 29 → 2026-10-29 30（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `6d70ef7a094f` · [字段定义](../../DATASET.md)*
