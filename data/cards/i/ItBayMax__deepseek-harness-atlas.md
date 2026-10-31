# ItBayMax/deepseek-harness-atlas

⭐ 15 · JavaScript · MIT · 推送 2026-10-24 · [GitHub](https://github.com/ItBayMax/deepseek-harness-atlas) · 个人维护 · 中文 README

**deepseek-harness 仓库的交互式架构学习地图与文档库站点**

针对 deepseek-harness 仓库的第三方源码分析与学习工具，以 React+TypeScript+Vite 静态站点形式提供架构分层、依赖脉络、核心流程、模块深读（含关键源码片段）与双源文档库（官方文档中文优先 + Claude 解读文档）。分析数据与文档已提交进仓库，npm install 后即可完整使用，无需旁边有上游仓库；仅『源码浏览』页需要真实的 deepseek-harness checkout。知识库先落 SQLite 再导出 JSON，模块数据在 scripts/modules-data.mjs 中维护。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 架构分层/依赖脉络/核心流程/模块深读的交互式可视化
- 双源文档库：官方文档（.zh.md 优先）+ Claude 解读文档
- 分析数据与文档已提交仓库，clone 后零配置使用
- 数据管线按上游源码可用性逐步守卫，缺源自动跳过

## 适用场景

- 系统学习 deepseek-harness 的架构分层与模块依赖
- 对照关键源码片段深读核心流程
- 查阅官方中文文档与解读文档的双源对照

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L1: # DeepSeek Harness 架构学习知识库（可视化站点）
> L3: 针对 `deepseek-harness` 仓库的交互式学习地图：架构分层、依赖脉络、核心流程、模块深读（含**关键源码片段**）、**双源文档库**（官方文档中文优先 + Claude 解读文档）、活体源码浏览。
> L20: 技术栈：React + TypeScript + Tailwind + Vite；知识库先落 SQLite 再导出 JSON（构建期）。

## 星数曲线

```mermaid
xychart-beta
    title "ItBayMax/deepseek-harness-atlas 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `4d45b1817173` · [字段定义](../../DATASET.md)*
