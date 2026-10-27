# convex/dryad

⭐ 40 · TypeScript · MIT · 推送 2026-02-06 · [GitHub](https://github.com/convex/dryad) · [官网](https://dryad.gg) · 组织维护

**面向任意 GitHub 仓库的语义代码搜索示例应用**

约 1000 行代码的语义代码搜索 Web 应用与起始模板：轮询目标仓库新提交，经 OpenAI 模型为源文件生成目标摘要并计算向量嵌入，存入 Convex 向量索引；用户查询时用同一嵌入 API 生成查询向量，检索语义相似的源文件并保持索引与 HEAD 同步。给想在 Convex + OpenAI + Vite/React 技术栈上搭建语义搜索应用的开发者使用。需配置 OpenAI 付费 API key 与 GitHub 访问令牌，作者自述功能相当基础、定位为演示项目。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 自动跟踪目标仓库变更，索引与 HEAD 保持同步
- ChatGPT 生成文件目标摘要 + OpenAI 向量嵌入 + Convex 向量索引的检索链路
- 配置项存于 Convex 数据库 settings 表，可在 dashboard 中在线修改
- 约 1000 SLOC，README 定位为可读、可 fork 的起始模板

## 适用场景

- 在任意 GitHub 仓库上做语义代码搜索
- 作为搭建更复杂语义搜索 Web 应用的起始模板
- 学习 Convex 向量索引与 OpenAI 嵌入的集成方式

## 场景标签

`语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L148: 1. Ask ChatGPT to summarize the "primary goals" of the source file in JSON format.
> L155: When someone submits a query in the web app, dryad uses the same OpenAI embeddings API to generate

## 星数曲线

```mermaid
xychart-beta
    title "convex/dryad 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 39 --> 41
    line [40, 40]
```

2026-10-18 40 → 2026-10-27 40（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `1d953cd8db6c` · [字段定义](../../DATASET.md)*
