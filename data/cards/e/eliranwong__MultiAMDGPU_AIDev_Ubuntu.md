# eliranwong/MultiAMDGPU_AIDev_Ubuntu

⭐ 55 · 推送 2026-02-14 · [GitHub](https://github.com/eliranwong/MultiAMDGPU_AIDev_Ubuntu) · [官网](https://letmedoit.ai) · 个人维护

**Ubuntu 多张 AMD GPU 搭配 ROCm 的 AI 开发环境搭建笔记**

个人经验整理的配置指南仓库：面向在 Ubuntu 上用多张 AMD GPU（作者实测 2 张 RX 7900 XTX、Ubuntu 24.04、内核 6.11、ROCm 7.1.1）做 AI 开发的用户，覆盖 PCIe 插槽要求、用户组配置、ROCm 安装命令、GRUB 修改（iommu=pt 解决多卡挂起、禁用核显）、环境变量（ROCR_VISIBLE_DEVICES 等）与故障排查。README 顶部还附有 llama.cpp 与 Ollama 的速度对比、在 48GB 双卡上运行 GPT OSS 120B 的测试记录。仓库声明内容基于个人经验，不保证适用所有配置。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多卡 PCIe 电气要求（相同 lane 宽度、PCIe 3.0 Atomics、避免走芯片组插槽）
- ROCm 7.1.1 完整安装与卸载步骤
- GRUB 修改解决多 GPU 挂起问题（iommu=pt）与禁用核显方法（pci-stub.ids）
- 含 llama.cpp vs Ollama 速度对比与双 RX 7900 XTX 跑 GPT OSS 120B 的测试链接

## 适用场景

- 我在 Ubuntu 上配多张 AMD GPU 跑本地大模型，需要完整踩坑记录
- 我遇到 ROCm 多卡系统挂起或核显冲突问题，需要排查方案
- 我想了解 AMD 平台上 llama.cpp 与 Ollama 的运行表现

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L21: Welcome to this repository, where I share my notes and insights on
> L25: This repository aims to bridge that gap, providing an overview and step-by-step guide based on my personal experien
> L31: This repository contains notes, guides, and scripts that I've compiled during my

## 星数曲线

```mermaid
xychart-beta
    title "eliranwong/MultiAMDGPU_AIDev_Ubuntu 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 54 --> 56
    line [55, 55]
```

2026-10-18 55 → 2026-10-31 55（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `95e5d069ad8a` · [字段定义](../../DATASET.md)*
