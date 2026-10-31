# saturncloud/examples

⭐ 18 · Python · BSD-3-Clause · 推送 2026-06-23 · [GitHub](https://github.com/saturncloud/examples) · [官网](https://saturncloud.io/docs/examples/) · 组织维护

**Saturn Cloud 平台的示例项目与默认模板资源合集**

Saturn Cloud 官方维护的示例项目仓库，其中多数示例被用作每次 Saturn Cloud 安装时的默认模板资源（管理员可开关）。每个示例包含一个 `.saturn/saturn.json` 资源配方（定义镜像、磁盘等）以及 notebook、markdown、Python 脚本等内容文件；`.saturn/templates.json` 指定哪些示例成为模板。文档站直接从这些 notebook 拉取生成。仓库还约定了缩略图、公共 S3 数据文件路径与 Dask 集群 worker 数同步等规范。面向 Saturn Cloud 用户与贡献示例的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 每个示例含 `.saturn/saturn.json` 资源配方与 notebook/脚本内容
- `.saturn/templates.json` 指定哪些示例成为平台默认模板
- 文档站通过 `make_md.py` 脚本直接从这些 notebook 生成
- 约定公共 S3 数据文件以 HTTP 路径引用、Dask worker 数需在配方与 notebook 中同步

## 适用场景

- 在 Saturn Cloud 上从模板快速创建数据科学/机器学习资源
- 查阅官方示例 notebook 学习平台用法
- 为本仓库贡献符合规范的新示例模板

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L9: These are the Saturn Cloud Examples most of which are used to create default template resources on every Saturn Clou
> L11: Each example has a recipe that describes how the resource should be setup as well as files (notebooks, markdown, py

## 星数曲线

```mermaid
xychart-beta
    title "saturncloud/examples 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-31 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `33964fd6e93e` · [字段定义](../../DATASET.md)*
