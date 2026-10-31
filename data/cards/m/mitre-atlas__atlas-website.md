# mitre-atlas/atlas-website

⭐ 20 · Vue · NOASSERTION · 推送 2026-10-28 · [GitHub](https://github.com/mitre-atlas/atlas-website) · [官网](https://atlas.mitre.org) · 组织维护

**MITRE ATLAS 网站源码：展示 AI 系统威胁知识库的静态站点**

MITRE ATLAS（Adversarial Threat Landscape for AI Systems）网站的源码仓库，帮助研究者浏览针对人工智能系统的威胁全景。网站基于 Vue 3 构建，通过 GitHub Pages 部署于 atlas.mitre.org。仓库包含网站静态代码，内容数据通过 atlas-data Git 子模块引入，需用 sparse checkout 只取 dist 目录；本地开发依赖 node v20 与 npm。仓库本身不含威胁数据内容，仅承载网站工程。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 Vue 3 构建并通过 GitHub Pages 提供服务
- ATLAS 数据以 atlas-data Git 子模块形式接入，支持 sparse checkout
- 提供子模块更新与本地开发流程说明

## 适用场景

- 本地搭建或二次开发 ATLAS 网站前端
- 了解 MITRE ATLAS 威胁知识库的站点工程结构

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L3: ATLAS enables researchers to navigate the landscape of threats to artificial intelligence systems. Visit https://atl
> L5: This repository contains the ATLAS website source code, which is built upon Vue 3 and served via GitHub Pages at htt

## 星数曲线

```mermaid
xychart-beta
    title "mitre-atlas/atlas-website 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-31 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `273453ab25ca` · [字段定义](../../DATASET.md)*
