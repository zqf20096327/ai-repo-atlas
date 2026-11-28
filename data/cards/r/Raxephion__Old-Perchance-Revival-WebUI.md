# Raxephion/Old-Perchance-Revival-WebUI

⭐ 14 · Python · MIT · 推送 2026-11-27 · [GitHub](https://github.com/Raxephion/Old-Perchance-Revival-WebUI) · 个人维护

**本地 WebUI：复刻旧 Perchance 体验的 SD 1.5 图像生成器**

基于 Gradio 的本地图像生成 WebUI，通过 diffusers 格式的旧 Perchance 配置、模型与预设复现旧 Perchance 图像生成器的使用体验。提供文生图与图生图两个模式，支持 Hires. fix 放大、单批最多 12 张、PNG 无损输出，可调提示词、步数、CFG、调度器与种子。Windows 提供批处理一键安装运行，其他平台可手动部署。默认优先使用 NVIDIA GPU，也支持 CPU 运行但生成速度受限；作者标注该项目为实验性、未测试，现已进入 legacy 状态。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 文生图与图生图两种模式，内置 Hires. fix 放大功能
- 单批最多生成 12 张图片，PNG 格式输出
- 支持 NVIDIA GPU 加速与 CPU 运行，可调步数/CFG/调度器/种子
- Windows 批处理一键安装，附 CPU 降速优化建议

## 适用场景

- 在本地 PC 免费生成 SD 1.5 图像
- 习惯旧 Perchance 站点的用户延续原有参数与模型使用
- 上传自己的图片做风格转换或改图（img2img）

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L7: Welcome to **Perchance Revival**! This is a user-friendly Gradio web application designed to bring back the experien
> L9: Generate images effortlessly and for free, directly on your own PC. This version is designed to **prioritize and uti


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `b1e714a9cfd7` · [字段定义](../../DATASET.md)*
