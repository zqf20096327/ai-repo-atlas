# kendryte/k230_linux_sdk

⭐ 66 · C · BSD-2-Clause · 推送 2026-10-10 · [GitHub](https://github.com/kendryte/k230_linux_sdk) · [官网](https://www.kendryte.com/zh/sdkResource/230linux) · 组织维护 · 中文 README

**K230 RISC-V 芯片的 Linux SDK：构建系统镜像与运行 AI Demo**

Canaan Kendryte 官方维护的 K230/K230D Linux 开发套件。基于 Buildroot 组织构建流程：安装 GCC 工具链与依赖后，通过 make 选择 defconfig、下载源码并编译，产出 sysimage-sdcard.img.gz 镜像烧写 TF 卡启动；另支持生成 Debian/Ubuntu 发行版镜像。内核、U-Boot、SDK 配置均可通过 make 目标修改重建。内置 AI Demo 包（默认启用 face_detection，含 .kmodel 模型与 ISP/图像脚本，经 menuconfig 启用更多），AI 部分依赖 KPU/nncase。已在 Ubuntu 22.04/24.04 验证，也可跳过编译下载每日构建镜像。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | BSD-2-Clause |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Buildroot 构建流程产出 TF 卡系统镜像
- 支持生成 Debian/Ubuntu 发行版镜像
- 内置 AI Demo 包（face_detection 等，kmodel 模型）
- 提供 U-Boot/内核/SDK 配置的 make 修改与重建目标

## 适用场景

- 为 K230/K230D 开发板构建定制 Linux 系统镜像
- 在设备上运行人脸检测等 AI Demo
- 调整内核或 U-Boot 配置进行板级开发

## 场景标签

`人脸识别` · 领域:感知与多模态

## 证据(README 行号)

> L101: - **Source directory**: `buildroot-overlay/package/ai_demo/`
> L129:   # face_detect_image.sh       face_detection_320.kmodel

## 星数曲线

```mermaid
xychart-beta
    title "kendryte/k230_linux_sdk 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-24"]
    y-axis "stars" 64 --> 67
    line [65, 66, 66]
```

2026-10-18 65 → 2026-10-24 66（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `00c6547aed26` · [字段定义](../../DATASET.md)*
