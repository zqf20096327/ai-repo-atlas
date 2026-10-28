# trustabl/trustabl-docs

⭐ 22 · Python · 推送 2026-10-01 · [GitHub](https://github.com/trustabl/trustabl-docs) · 组织维护

**Trustabl 文档站源码：聚合 Agent 可靠性分析器文档**

基于 MkDocs Material 构建、发布到 GitHub Pages 的文档站源仓库。手写页面（概览、安装、快速上手、CLI 参考）存于 docs/，架构、覆盖范围与规则索引等页面在构建时由 scripts/gather.py 从 trustabl/agent-reliability-analyzer 与 trustabl/trustabl-rulebook 两个源仓库拉取，源仓库保持权威地位。本地预览需同级目录检出源仓库，GitHub Actions 推送 main 时自动构建部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 构建时从两个源仓库聚合拉取文档内容
- 手写页与拉取页分离，拉取文件不入库
- GitHub Actions 自动构建并部署到 GitHub Pages

## 适用场景

- 为 Trustabl Agent 可靠性分析器维护文档站
- 本地预览并调试文档内容

## 场景标签

 · 领域:开发工具/文档

## 证据(README 行号)

> L3: Source for the Trustabl documentation site, published with
> L6: The site **aggregates** content from the project's repos — it is not the source
> L11: - **Pulled pages** (architecture, coverage, the rule index and per-rule

## 星数曲线

```mermaid
xychart-beta
    title "trustabl/trustabl-docs 星数(近 2 点)"
    x-axis ["2026-10-23", "2026-10-28"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-23 22 → 2026-10-28 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `9339feb8f318` · [字段定义](../../DATASET.md)*
