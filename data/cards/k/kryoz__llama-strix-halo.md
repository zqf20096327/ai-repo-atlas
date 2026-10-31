# kryoz/llama-strix-halo

⭐ 14 · Shell · 推送 2026-07-26 · [GitHub](https://github.com/kryoz/llama-strix-halo) · 个人维护

**AMD Strix Halo 128Gb 迷你主机上部署 llama.cpp 服务器的配置指南**

一份面向 AMD Strix Halo（Ryzen AI Max）128Gb 迷你主机的运维笔记：覆盖 Ubuntu Server 24.04 LTS 全新安装后的 BIOS UMA 显存划分、新内核安装、GRUB/udev/sysctl 内核参数调整、tuned 加速性能配置，随后以 Lemonade ROCm 后端便携包（gfx1151 构建）方式安装 llama.cpp，并用 systemd 用户服务实现模型动态加载与开机自启；附带 ryzenadj 功耗调校、GMKtec Evo X2 BIOS 降级方法与 USB4/Thunderbolt RDMA 低延迟驱动（OdinLink-Five）的搭建步骤。面向自行搭建本地 LLM 推理主机的用户，仅为文档仓库，不含代码产品。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- BIOS/GRUB/sysctl 层面的共享内存与 GPU 显存分配调优步骤
- 以 Lemonade ROCm 便携包安装 llama.cpp 并配置 systemd 自启服务
- ryzenadj 功耗/TDP 调校与电压偏移对照表
- USB4/Thunderbolt RDMA 低延迟驱动 OdinLink-Five 双机互连配置

## 适用场景

- 在 Strix Halo 迷你主机上搭建本地 llama.cpp 推理服务器
- 调优 AMD APU 的显存分配与功耗平衡
- 用 USB4/TB5 线缆做双机低延迟互连

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L1: # Setup llama.cpp server on AMD Strix Halo 128Gb version
> L5: This note describes how to configure step by step local high-performance LLM setup with fresh install of Ubuntu Serv

## 星数曲线

```mermaid
xychart-beta
    title "kryoz/llama-strix-halo 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `4db33bbc5940` · [字段定义](../../DATASET.md)*
