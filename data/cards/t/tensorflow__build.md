# tensorflow/build

⭐ 313 · Shell · Apache-2.0 · 推送 2026-09-04 · [GitHub](https://github.com/tensorflow/build) · 组织维护

**TensorFlow 构建资源策展：Dockerfile、指南与社区多平台构建**

TensorFlow SIG Build 社区组的成果展示仓库：汇集与 TensorFlow 构建/运行/打包相关的 Dockerfile（SIG Build 内部用、Runtime、manylinux2014、Distroless）、语言绑定安装指南（Golang）、平台构建文档（ppc64le、树莓派、WSL2 GPU），并维护一张社区支持的构建清单——AMD ROCm、IBM ppc64le/s390x、Intel oneDNN 等平台的 nightly/stable 构建与容器产物。供需要在非官方平台构建或运行 TensorFlow 的开发者查阅与取用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多类 TensorFlow 构建/运行 Dockerfile（manylinux2014、Distroless、Jupyter 变体等）
- 社区构建清单覆盖 AMD ROCm、IBM ppc64le/s390x、Intel oneDNN 平台
- 平台指南：ppc64le 构建、树莓派、WSL2 GPU 配置

## 适用场景

- 在非官方支持平台（如 ppc64le、s390x、ROCm）上获取 TensorFlow 构建
- 查找 TensorFlow 构建与运行用的 Docker 镜像
- 配置 WSL2 GPU 环境运行 TensorFlow

## 场景标签

`精选清单` · 领域:学习与行业

## 证据(README 行号)

> L5: **TensorFlow SIG Build** is a community group dedicated to the TensorFlow build
> L6: process. This repository is a showcase of resources, guides, tools, and builds
> L60: Amazing members of the TensorFlow community build, test, and package TensorFlow

## 星数曲线

```mermaid
xychart-beta
    title "tensorflow/build 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-30"]
    y-axis "stars" 311 --> 314
    line [312, 313, 313]
```

2026-10-18 312 → 2026-10-30 313（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `45b65e9e87c6` · [字段定义](../../DATASET.md)*
