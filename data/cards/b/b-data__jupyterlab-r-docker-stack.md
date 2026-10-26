# b-data/jupyterlab-r-docker-stack

⭐ 36 · Dockerfile · NOASSERTION · 推送 2026-10-24 · [GitHub](https://github.com/b-data/jupyterlab-r-docker-stack) · [官网](https://gitlab.com/b-data/jupyterlab/r-project/docker-stack) · 组织维护

**多架构 JupyterLab R 语言 Docker 镜像栈，面向数据科学开发**

提供 base→tidyverse→verse→geospatial→qgisprocess 五层构建链的 JupyterLab R Docker 镜像，支持 linux/amd64 与 linux/arm64/v8，可在 Apple M 系列 Docker Desktop 上运行。镜像内置 R、code-server（Code - OSS）、Git、RStudio（4.4.0+）、Pandoc、Quarto、TinyTeX 等工具；另提供 devtools/docker 等子标签组合。镜像从 GitLab Container Registry 拉取或本地 docker build，需预装 Docker；CUDA 加速版本在另一仓库。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 五层镜像构建链：base→tidyverse→verse→geospatial→qgisprocess
- 多架构支持 linux/amd64 与 linux/arm64/v8（含 Apple M 系列）
- 内置 code-server、RStudio、Git、Quarto、TinyTeX 等工具
- 提供 devtools/docker/root 等子标签组合与 Podman rootless 用法

## 适用场景

- 用容器快速搭建 R 数据科学开发环境
- 在 ARM 设备（含 Apple M 系列）上运行 JupyterLab R 环境
- 需要 code-server 或 RStudio 的浏览器端 IDE 环境

## 场景标签

 · 领域:数据科学/开发环境

## 证据(README 行号)

> L33: * **JupyterLab**: A web-based interactive development environment for Jupyter
> L34:  notebooks, code, and data. The images include
> L54:  * **R**: A language and environment for statistical computing and graphics.

## 星数曲线

```mermaid
xychart-beta
    title "b-data/jupyterlab-r-docker-stack 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 35 --> 37
    line [36, 36]
```

2026-10-18 36 → 2026-10-26 36（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 low · 依据 README sha `75c23b5a93df` · [字段定义](../../DATASET.md)*
