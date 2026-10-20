# k4yt3x/video2x

⭐ 22,304 · C++ · AGPL-3.0 · 推送 2026-03-07 · [GitHub](https://github.com/k4yt3x/video2x) · [官网](https://docs.video2x.org) · 个人维护 · 中文 README

**基于机器学习的视频超分辨率与插帧框架**

用 C/C++ 重写的视频处理框架，支持超分辨率放大与帧插值两种模式，通过 ncnn 与 Vulkan 运行 Anime4K v4、Real-ESRGAN、Real-CUGAN、RIFE 模型及 MPV 兼容 GLSL 着色器。提供 Windows 安装包（含 GUI，支持多语言界面）、Linux 发行版包与 AppImage、Docker/Podman 容器镜像，以及 Google Colab 免费使用方式。预编译二进制要求 CPU 支持 AVX2，GPU 需支持 Vulkan。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 动量与使用信号

- 维护:`declining` — 距上次 push 224.7 天,年发版 0,24 位贡献者
- 涨星:近 1 天 **+17**(自 20261016 起算)
- 平台:WINDOWS / MACOS / LINUX · 协议:—

## 能力要点

- 支持超分辨率与帧插值两种模式
- 通过 ncnn 与 Vulkan 运行 Real-ESRGAN、Real-CUGAN、RIFE 模型
- 支持 Anime4K v4 及所有 MPV 兼容 GLSL 着色器
- 处理过程无需额外磁盘空间

## 适用场景

- 将低分辨率动漫视频放大到高分辨率
- 为低帧率视频补帧提升流畅度
- 无本地 GPU 时在 Google Colab 上处理视频

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L24: - supports Real-ESRGAN, Real-CUGAN, and RIFE (all models) via ncnn and Vulkan;
> L31: Your system must meet the minimum hardware requirements below to run Video2X.

---
*卡片 v1 · prompt 1.4 · 生成 2026-10-18 · 置信度 high · 依据 README sha `c327d1ef0f13` · [字段定义](../../DATASET.md)*
