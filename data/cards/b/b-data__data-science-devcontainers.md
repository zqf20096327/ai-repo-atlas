# b-data/data-science-devcontainers

⭐ 41 · Dockerfile · NOASSERTION · 推送 2026-10-23 · [GitHub](https://github.com/b-data/data-science-devcontainers) · 组织维护

**多架构数据科学/AI 开发容器镜像集，覆盖 R/Python/Julia/MAX/Mojo**

b-data GmbH 维护的 dev container 镜像集合，提供 linux/amd64 与 linux/arm64/v8 双架构的 R、Python、Julia、MAX/Mojo 数据科学开发容器，含 CUDA GPU 加速版本。镜像内置 JupyterLab、Git、Quarto、TinyTeX、GIS 工具链与一批 VS Code 扩展；CUDA 版本要求宿主机具备 NVIDIA GPU、驱动与 Container Toolkit（无需安装 CUDA toolkit）。可通过 GitHub Codespaces 或本地 Docker/Podman 配合 VS Code Dev Containers 使用，数据在 home 目录与 workspace 持久化。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- linux/amd64 与 linux/arm64/v8 双架构（可在 Apple M 系列上运行）
- CUDA 版镜像基于 NVIDIA CUDA runtime 镜像，宿主机仅需驱动
- 内置 JupyterLab、Git/Git LFS、Quarto、TinyTeX 与 GIS 工具链
- 预装 VS Code 扩展集并定义容器生命周期脚本

## 适用场景

- 在标准化容器中搭建 R/Python/Julia/MAX 数据科学开发环境
- 在 GPU 环境下运行 CUDA 加速的数据科学开发容器
- 通过 GitHub Codespaces 免安装获得开箱即用的开发环境

## 场景标签

 · 领域:开发环境/数据科学基础设施

## 证据(README 行号)

> L5: (GPU accelerated) Multi-arch (`linux/amd64`, `linux/arm64/v8`) Data Science
> L58: * **MAX**[^1]: A high-performance generative AI framework.
> L125: Dev containers require either Docker or Podman[^2] to be installed. CUDA-based

## 星数曲线

```mermaid
xychart-beta
    title "b-data/data-science-devcontainers 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 40 --> 42
    line [41, 41]
```

2026-10-18 41 → 2026-10-26 41（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `2abeedf4e45a` · [字段定义](../../DATASET.md)*
