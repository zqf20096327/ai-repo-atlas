# milistu/cuda-cudnn-installation

⭐ 21 · Python · 推送 2026-05-14 · [GitHub](https://github.com/milistu/cuda-cudnn-installation) · [官网](https://medium.com/@milistu/how-to-install-cuda-cudnn-7e4a00ae4f44) · 个人维护

**在 Ubuntu 上安装 CUDA 与 cuDNN 以配置深度学习环境的教程**

面向深度学习开发者的安装指南文档：以 Ubuntu 22.04、GeForce RTX 3090、PyTorch 为例，覆盖 NVIDIA 驱动卸载与安装（ubuntu-drivers 自动推荐、nvidia-driver-595-open）、CUDA Toolkit 13.2 deb 本地安装与 PATH 配置、cuDNN 9.22.0 下载安装（需 NVIDIA 账号），最后用 pip 安装 PyTorch cu132 版并以 Python 脚本验证 GPU 可用。内容为教程 README，无可安装代码包。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从旧驱动清理到 nvidia-smi/nvcc 验证的完整 NVIDIA 驱动与 CUDA 安装流程
- cuDNN 与 CUDA/驱动版本匹配说明及 deb 安装步骤
- PyTorch cu132 轮子安装与 Python 验证脚本
- bashrc PATH 配置与 /usr/local/cuda 符号链接设置

## 适用场景

- 我在 Ubuntu 上为深度学习配置 NVIDIA GPU 环境
- 我需要按步骤安装 CUDA Toolkit 与 cuDNN 并验证 PyTorch GPU 可用
- 我清理旧的 NVIDIA/CUDA 安装后重装

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L1: # How to install CUDA & cuDNN
> L3: Setting up CUDA & cuDNN for Machine Learning can be overwhelming. In this guide, I will walk you through the steps t

## 星数曲线

```mermaid
xychart-beta
    title "milistu/cuda-cudnn-installation 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-29 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `552af4e64325` · [字段定义](../../DATASET.md)*
