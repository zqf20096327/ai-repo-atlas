# Zeyi-Lin/HivisionIDPhotos

⭐ 21,645 · Python · Apache-2.0 · 推送 2026-07-03 · [GitHub](https://github.com/Zeyi-Lin/HivisionIDPhotos) · [官网](https://modelscope.cn/studios/SwanLab/HivisionIDPhotos) · 组织维护 · 中文 README

**AI 证件照制作工具：抠图、换底、排版一站式生成**

基于 AI 模型工作流的证件照制作工具：对人像照片进行离线抠图（仅需 CPU 推理），按尺寸规格生成标准证件照与六寸排版照，支持自定义底色、美颜与裁剪。提供 Gradio Demo、Python 推理脚本与 FastAPI 服务三种使用形态，支持纯离线或端云推理（Face++ 在线人脸检测为可选项）。Apache-2.0 许可，支持 Docker 部署，社区有 ComfyUI、微信小程序、Windows GUI 等扩展。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 动量与使用信号

- 维护:`maintenance` — 距上次 push 107.2 天,年发版 0,24 位贡献者
- 涨星:近 1 天 **+6**(自 20261016 起算)
- 安装:pypi 包 `requirements-app.txt` 月下载无数据
- 平台:WINDOWS / MACOS / LINUX · 协议:—

## 能力要点

- 轻量级人像抠图，纯离线且仅需 CPU 即可推理
- 多种抠图模型可选（MODNet、hivision_modnet、rmbg-1.4、birefnet-v1-lite）
- 生成标准证件照、六寸排版照，支持五种排版尺寸与 HEX 自定义底色
- 提供 Gradio Demo、Python CLI 与 API 服务，支持 Docker 部署

## 适用场景

- 离线批量制作标准证件照并排版打印
- 为应用集成证件照生成 API 服务
- 对人像照片做抠图与背景替换

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L47: HivisionIDPhoto 旨在开发一种实用、系统性的证件照智能制作算法。
> L49: 它利用一套完善的AI模型工作流程，实现对多种用户拍照场景的识别、抠图与证件照生成。
> L53: 1. 轻量级抠图（纯离线，仅需 **CPU** 即可快速推理）

## 星数曲线

```mermaid
xychart-beta
    title "Zeyi-Lin/HivisionIDPhotos 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-21"]
    y-axis "stars" 21638 --> 21646
    line [21639, 21645, 21645]
```

2026-10-18 21,639 → 2026-10-21 21,645（+6）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-18 · 置信度 high · 依据 README sha `20fa8c375ca0` · [字段定义](../../DATASET.md)*
