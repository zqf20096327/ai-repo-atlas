# keezwus/sketch2naiwa

⭐ 4 · Python · 推送 2026-10-21 · [GitHub](https://github.com/keezwus/sketch2naiwa) · 个人维护 · 中文 README

**简笔画/照片/视频转奶娃角色生成的课程项目，一键脚本本地运行**

课程项目交付仓库，将简笔画、照片、视频或手机直播画面转换为奶娃角色图像。包含两条自训模型产品线：pix2pix（U-Net+PatchGAN，256px，约14ms/张）用于实时场景；SD1.5+LoRA+ControlNet+LCM（512px）用于单图精修。提供 Windows 一键启动脚本（演示版/完整版/实时直播三个 Gradio 服务）与下载脚本自动补齐权重，全部推理在单台 8GB 显存笔记本本地完成。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自训 pix2pix（2358 训练对）与 SD1.5 LoRA/ControlNet/LCM 双产品线
- Windows 一键启动脚本，含画板、图片、视频、手机直播输入
- download_all.py 自动下载自训权重与 SD1.5 基础栈（hf-mirror 镜像）
- 全部推理本地运行于 8GB 显存笔记本，无需联网（首次除外）

## 适用场景

- 课堂演示中现场画简笔画生成角色
- 视频逐帧转换或手机直播实时变装效果
- 单张图片的精细风格化生成

## 场景标签

`图像生成` `教程课程` · 领域:内容生成

## 证据(README 行号)

> L3: **简笔画 / 照片 / 视频 / 手机直播 → 奶娃角色生成** · 课程项目最终提交仓库
> L54: |模型|自训 pix2pix（U-Net + PatchGAN）|SD1.5 + 自训 LoRA + ControlNet + LCM|

## 星数曲线

```mermaid
xychart-beta
    title "keezwus/sketch2naiwa 星数(近 3 点)"
    x-axis ["2026-10-26", "2026-10-29", "2026-11-27"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-10-26 3 → 2026-11-27 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `16eb0f77827d` · [字段定义](../../DATASET.md)*
