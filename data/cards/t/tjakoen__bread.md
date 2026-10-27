# tjakoen/bread

⭐ 181 · Shell · Apache-2.0 · 推送 2026-09-15 · [GitHub](https://github.com/tjakoen/bread) · [官网](https://tjakoen.github.io/bread/) · 个人维护

**无构建、AI 可操作的 Web 技术栈总览仓库（五层+控制面）**

BREAD 是一个伞形仓库：它本身不含框架代码，而是五层技术栈（batch 基座、grain 设计系统、mill Markdown CMS、proof 计划看板、crumb 引导导览）的地图与控制面。核心理念：人类点击与 AI 决策统一为同一 Intent、经同一通道返回 SSE 渲染操作，AI 无特权 DOM 通道。层包以 @tjakoen/* 发布于 npm；本仓库提供 bun run cockpit/doctor/deps 等全栈操作脚本。运行需 Bun 1.3.x。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 人类与 AI 共用同一 Intent 与同一操作通道，AI 操作过程可视
- 五层各自独立成包发布于公共 npm（@tjakoen/*）
- grain-mcp：基于导出构建的 MCP 服务器（workspace 内，不参与层链）
- bun run doctor/deps 检查层版本 pin 漂移

## 适用场景

- 搭建无构建、服务端渲染超媒体且 AI 可操作的 Web 应用
- 把编码 agent 指向 kickstart 链接让其自行提议所需层
- 用 PANTRY 将五层组装为单一服务器做开发文档与 AI 驾驶舱

## 场景标签

`精选清单` · 领域:学习与行业

## 证据(README 行号)

> L26: The defining idea: a human click and an AI decision become the **same `Intent`**, flow through
> L41: `.npmrc` and no token. That monorepo carries a fifth package, `grain-mcp`, an MCP server over a

## 星数曲线

```mermaid
xychart-beta
    title "tjakoen/bread 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 180 --> 182
    line [181, 181]
```

2026-10-18 181 → 2026-10-27 181（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `a6d54842f713` · [字段定义](../../DATASET.md)*
