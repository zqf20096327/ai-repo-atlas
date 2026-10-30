# Onweekendd/ScreenWright

⭐ 30 · TypeScript · MIT · 推送 2026-10-29 · [GitHub](https://github.com/Onweekendd/ScreenWright) · 组织维护 · 中文 README

**对话式 AI 生成数据大屏/BI 可视化的编辑器**

B/S 架构的大屏编辑器：Vue 3 编辑器负责画布渲染与手动编辑，Hono + Mastra 后端提供多角色 Agent 服务。用户通过对话或 Figma 链接描述需求，Agent 做语义分区、选组件、生成 Schema 与排版，结果经 SSE 流实时同步到画布，改动可审批、可回溯；也支持在沙箱中写 Vue 代码并实时预览。内置 76+ 物料组件，可导出静态包脱离编辑器运行。需要 Node ≥22.13、pnpm 10 与带 pgvector 的 PostgreSQL，模型按 OpenAI 兼容端点配置，支持 docker compose 七服务部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 对话/Figma 链接驱动 Agent 生成大屏，SSE 实时同步画布，改动可审批与回溯
- 76+ 物料组件（图表/指标/媒体/地图下钻等），可导出脱离编辑器的静态包
- 编辑器核心框架无关（packages/core），可迁移其他 UI 框架或做 headless 场景
- 按 ROLE 环境变量拆分 api/ai/worker 进程，docker compose 七服务编排

## 适用场景

- 用自然语言描述需求直接产出数据大屏
- 从 Figma 设计稿转换生成可编辑的大屏组件树
- 在编辑器中手动微调 Agent 生成的大屏并保存为模板复用

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L5: AI 原生的数据大屏 / BI 可视化编辑器。跟 Agent 描述需求，或者给一个 Figma 链接，它会直接在画布上创建组件、接上数据、配好联动，产出一个可以继续在编辑器里改的大屏。
> L13: 把需求描述清楚，Agent 会自己做语义分区、挑组件、生成 Schema、排版，实时同步到画布，改动前可以审批，也可以回溯。也可以给一个 Figma 链接：设计稿数据来自我们自己的 `packages/figma-helper` 
> L15: 组件能力覆盖不到的效果，内置的 Artifact App 子系统可以在沙箱里直接写 Vue 代码并实时预览。数据接好之后 Agent 会自己跑一遍数据流做校验。做好的大屏可以存成模板，之后复用。

## 星数曲线

```mermaid
xychart-beta
    title "Onweekendd/ScreenWright 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-30 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `ae4fa31f666b` · [字段定义](../../DATASET.md)*
