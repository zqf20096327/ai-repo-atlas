# aadorian/ProtegeDesk

⭐ 14 · TypeScript · MIT · 推送 2026-06-28 · [GitHub](https://github.com/aadorian/ProtegeDesk) · 个人维护

**带 AI 辅助的网页版本体编辑器，面向本体工程**

基于 Next.js/React/TypeScript 构建的网页端 OWL 本体编辑平台：提供 Manchester 语法公理编辑、层级可视化、多格式导入导出（Turtle/RDF/XML/OWL/XML/N-Triples）、实时校验，内置 WebAssembly 客户端推理器做一致性检测与不一致修复。AI 部分为自然语言生成本体结构、属性推荐与公理生成。项目自述处于 0.2.0 MVP 阶段，Sprint 1 进行中，需从源码构建运行。

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

- 自然语言描述生成本体结构与公理
- WebAssembly 客户端推理：一致性检测与不一致修复向导
- CodeMirror 驱动的 Manchester 语法公理编辑与智能补全
- 支持 Turtle/RDF/XML/OWL/XML/N-Triples 多格式导入导出

## 适用场景

- 在浏览器中创建和编辑 OWL 本体
- 通过自然语言描述快速生成本体初稿
- 对已有本体做一致性检测与修复

## 场景标签

`知识图谱` · 领域:知识与检索

## 证据(README 行号)

> L24: - 🤖 **Ontology Generation** from natural language descriptions
> L31: - 🧠 **Client-Side Reasoning** (WebAssembly) for instant feedback
> L330: - Protege - Inspiration for ontology editing

## 星数曲线

```mermaid
xychart-beta
    title "aadorian/ProtegeDesk 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `7b221e2d83ff` · [字段定义](../../DATASET.md)*
