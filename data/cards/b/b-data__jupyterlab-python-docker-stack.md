# b-data/jupyterlab-python-docker-stack

⭐ 41 · Dockerfile · NOASSERTION · 推送 2026-10-26 · [GitHub](https://github.com/b-data/jupyterlab-python-docker-stack) · [官网](https://gitlab.com/b-data/jupyterlab/python/docker-stack) · 组织维护

**面向 Python 数据科学的 JupyterLab 多架构 Docker 镜像栈**

提供 linux/amd64 与 linux/arm64/v8 双架构的 JupyterLab Python Docker 镜像（base 与 scipy 两级构建链），镜像内预装 code-server（浏览器中的 Code - OSS）、Git/Git LFS、Neovim、Pandoc、Quarto、TinyTeX 与 Zsh，并为 code-server 预装约 20 个扩展。提供 devtools/docker/root 等子标签组合，Python 版本 ≥ 3.10.5 视为稳定。运行需先安装 Docker，也给出 Podman rootless 与 Docker Desktop 用法；GPU 加速版本在另一 CUDA 镜像栈中提供。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多架构镜像（linux/amd64、linux/arm64/v8，可在 Apple M 系列 Docker Desktop 上运行）
- base → scipy 构建链，内含 code-server、Git、Pandoc、Quarto、TinyTeX 等工具
- devtools/docker/root 子标签组合可选
- 提供在线 demo 与自建/注册表两种运行方式

## 适用场景

- 在容器中快速获得带 IDE 的 Python 数据科学开发环境
- 在 ARM 机器（如 Apple M 系列）上运行统一的 JupyterLab 环境
- 通过 code-server 在浏览器中使用 Code - OSS 进行开发

## 场景标签

 · 领域:开发环境/容器化

## 证据(README 行号)

> L8: Multi-arch (`linux/amd64`, `linux/arm64/v8`) docker images:
> L26: * **JupyterLab**: A web-based interactive development environment for Jupyter
> L28:  * **code-server**: `Code - OSS` in the

## 星数曲线

```mermaid
xychart-beta
    title "b-data/jupyterlab-python-docker-stack 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 40 --> 42
    line [41, 41]
```

2026-10-18 41 → 2026-10-29 41（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `90f262e4d27d` · [字段定义](../../DATASET.md)*
