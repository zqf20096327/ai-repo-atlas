# cern-sis/react-formule

⭐ 17 · JavaScript · MIT · 推送 2026-02-06 · [GitHub](https://github.com/cern-sis/react-formule) · [官网](https://cern-sis.github.io/react-formule/) · 组织维护

**React 表单构建库：JSON Schema/RJSF 上零代码建表单，AI 生成改表**

基于 JSON Schema 和 RJSF 的 React 表单构建库，提供可视化编辑器（字段选择、Schema 树、实时预览）、20 余种预定义字段类型、自定义字段/组件扩展、错误处理与文件字段（仅存 UID，存储由用户实现）。FormuleAI 部分集成 OpenAI/Gemini，用户可用自然语言生成或修改表单 Schema，以 diff 方式确认或自动应用（Vibe Mode）。源自 CERN Analysis Preservation 的需求，面向技术与非技术用户。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 基于 JSON Schema 与 RJSF 的可视化表单编辑器（含实时预览与编辑/发布版本切换）
- FormuleAI 支持自然语言生成/修改表单 Schema，默认接入 OpenAI 与 Gemini，可添加自定义 provider（含自托管）
- 简单字段、集合、高级字段等三类预定义字段类型，可扩展自定义字段与组件
- Files 字段只存 UID，文件获取与存储由用户通过回调实现

## 适用场景

- 在我的应用里嵌入零代码表单构建器让非技术人员建表
- 用自然语言描述需求生成或调整表单结构
- 编辑既有 JSON Schema 并以 diff 对比变更

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L14: Formule is a **powerful, user-friendly, extensible and mobile-friendly form building library** based on JSON Schema
> L181: FormuleAI brings Artificial Intelligence capabilities to Formule, allowing users to **generate and modify form sch
> L185: FormuleAI integrates AI providers (like OpenAI or Gemini) to process natural language requests and generate corres

## 星数曲线

```mermaid
xychart-beta
    title "cern-sis/react-formule 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-30 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `a18878004bb4` · [字段定义](../../DATASET.md)*
