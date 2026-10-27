# entropy-cloud/nop-chaos-flux

⭐ 41 · TypeScript · MIT · 推送 2026-10-12 · [GitHub](https://github.com/entropy-cloud/nop-chaos-flux) · 组织维护 · 中文 README

**Schema 驱动的低代码渲染与运行时框架，面向平台团队**

NOP Chaos Flux 是一个基于七原语（Template/ScopeRef/Value/Resource/Reaction/Capability/Host Projection）构建的 schema 驱动运行时与渲染框架：JSON schema 编译为可执行值后实例化运行时，由 React 作渲染层、vanilla Zustand 承载状态。Monorepo 内含 Flow Designer、Report/Spreadsheet Designer、Word Editor 与调试工具，主入口为 apps/playground。面向评估低代码运行时的工程师、贡献者与构建内部低代码基础设施的平台团队。运行时不依赖 AMIS，但参考 AMIS schema 约定，兼容层为规划项。工作区包当前为 private。

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

- 七原语为核心的编译一次执行模型，数据/行为/实例定位职责分离
- JSON schema 驱动页面、表单、表格、对话框与设计器表面
- Monorepo 含 Flow/Report/Spreadsheet 设计器、Word Editor 与 Debugger 工具
- 运行时不依赖 AMIS，状态基于框架无关的 Zustand stores

## 适用场景

- 平台团队构建 schema 驱动的低代码内部基础设施
- 评估与实验 schema 驱动 UI 运行时架构
- 在 playground 中探索 Flow Designer 等设计器表面

## 场景标签

 · 领域:低代码/前端工程

## 证据(README 行号)

> L25: NOP Chaos Flux is a schema-driven runtime and rendering framework for low-code systems, organized around a compact 
> L65: - JSON schema drives pages, forms, tables, dialogs, and richer design surfaces

## 星数曲线

```mermaid
xychart-beta
    title "entropy-cloud/nop-chaos-flux 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-27"]
    y-axis "stars" 39 --> 42
    line [40, 41, 41]
```

2026-10-18 40 → 2026-10-27 41（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 low · 依据 README sha `f2daad27e9b6` · [字段定义](../../DATASET.md)*
