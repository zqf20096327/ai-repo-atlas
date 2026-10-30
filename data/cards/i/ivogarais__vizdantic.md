# ivogarais/vizdantic

⭐ 15 · Python · MIT · 推送 2026-01-30 · [GitHub](https://github.com/ivogarais/vizdantic) · 个人维护

**校验 LLM 可视化输出的 Python 库：数据层与渲染层分离**

面向构建 LLM 生图应用的 Python 库：用 Pydantic 强类型 schema 约束 LLM 输出的可视化描述（chart 类型、数据映射），LLM 不直接编写绘图代码；校验后的 spec 经插件渲染为图表。支持 14 类图表类别、Plotly 插件（Matplotlib/Altair 等在计划中），风格控制留给调用方。提供 prompt 嵌入 schema 与工具调用两种接入方式，附带可选的 Codex skill。版本 0.2.2，自述为实验性，Python 3.10+，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Pydantic schema 校验 LLM 输出的可视化 spec，避免幻觉 API
- 14 类图表类别，强类型约束不允许无效组合
- 插件化渲染，当前支持 Plotly，插件仅需实现 render(spec, data)
- 可选 Codex skill（vizdantic install-codex-skill）本地运行

## 适用场景

- 让 LLM 选择图表类型而不写绘图代码的应用开发
- 在 LLM 输出与渲染逻辑间建立稳定接口，可切换渲染库
- 对 LLM 生成图表强制类型校验与品牌样式规范

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L24: Vizdantic gives LLMs a stable contract: describe *what* to visualize, not *how* to plot it.
> L107: Vizdantic works with any LLM. Two common patterns:

## 星数曲线

```mermaid
xychart-beta
    title "ivogarais/vizdantic 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `b6496bb1ba56` · [字段定义](../../DATASET.md)*
