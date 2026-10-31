# tensorflow/tfjs-website

⭐ 75 · CSS · Apache-2.0 · 推送 2026-06-16 · [GitHub](https://github.com/tensorflow/tfjs-website) · [官网](https://js.tensorflow.org) · 组织维护

**TensorFlow.js 官方文档网站的源码仓库与构建工具**

TensorFlow.js 官网（js.tensorflow.org / tensorflow.org/js）的源码仓库。网站内容以 markdown/yaml 形式存放于 docs 目录，API 文档由 Hexo 静态站点生成器构建，从 tfjs-core、tfjs-layers、tfjs-node、tfjs-vis 等库的源码生成。面向需要修改网站内容或 API 文档的贡献者：通过 yarn prep 拉取 tfjs 源码子仓库，yarn build 构建并在 localhost:8080 预览，yarn build-prod 用于生产部署（部署流程在 Google 内部）。部分站点构建依赖内部工具，站外无法完整预览设计。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Hexo 静态生成器构建站点，API 文档从 tfjs 各库源码自动生成
- yarn prep 拉取 tfjs 源码子仓库并同步文档
- 本地开发可构建 local 版 API 文档并在 localhost:8080 预览
- 生成 tfjs / tfjs-vis / tfjs-node / tfjs-react-native 等多套 API 页面

## 适用场景

- 修改 TensorFlow.js 官网的教程与内容并提交 PR
- 为 tfjs-core 等库的 API 文档做修改并本地预览
- 了解 TensorFlow.js 文档站的构建与部署流程

## 场景标签

 · 领域:AI 框架文档/开发者资源

## 证据(README 行号)

> L3: This repo is for the website for TensorFlow.js. The API docs are built using Hexo (a static site generator) that put
> L54: Updating the API docs is a bit more involved as they are built from the sources of tfjs-core, tfjs-layers, tfjs-nod

## 星数曲线

```mermaid
xychart-beta
    title "tensorflow/tfjs-website 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 74 --> 76
    line [75, 75]
```

2026-10-18 75 → 2026-10-31 75（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `aea87dd3d035` · [字段定义](../../DATASET.md)*
