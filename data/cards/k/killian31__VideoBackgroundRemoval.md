# killian31/VideoBackgroundRemoval

⭐ 41 · Python · Apache-2.0 · 推送 2026-10-23 · [GitHub](https://github.com/killian31/VideoBackgroundRemoval) · [官网](https://nelikcode-video-background-removal.hf.space) · 个人维护

**视频抠背景工具：框选主体后自动跟踪抠像并换底色**

输入视频后在首帧框选主体（或由 RT-DETRv2 自动检测主要对象），EdgeTAM 模型逐帧跟踪并分割该主体，输出替换为绿幕或任意底色的视频，同时保留原音频。分割采用流水线并行：读下一帧的同时分割当前帧。支持 CPU 运行，命令行可选 cpu/mps/cuda 设备；首次运行从 Hugging Face 下载模型。提供本地网页界面（app.py，localhost:7860）与命令行两种使用方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 首帧框选主体或 RT-DETRv2 自动检测主体
- EdgeTAM 逐帧跟踪分割，输出绿幕或任意底色
- 支持 cpu/mps/cuda 设备，可在 CPU 上运行
- 本地网页界面与命令行两种使用方式，保留原音频

## 适用场景

- 为视频更换或移除背景以叠加到其他画面
- 不想用付费/在线服务、本地 CPU 生成绿幕素材
- 批量处理已有视频的主体抠像

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L7: The Video Background Removal Tool is designed to enable users to effortlessly remove backgrounds from videos by sele
> L56: EdgeTAM tracks the subject from its box on the
> L58: it moves or crosses other people. Without a box, RT-DETRv2

## 星数曲线

```mermaid
xychart-beta
    title "killian31/VideoBackgroundRemoval 星数(近 2 点)"
    x-axis ["2026-10-24", "2026-10-25"]
    y-axis "stars" 40 --> 42
    line [41, 41]
```

2026-10-24 41 → 2026-10-25 41（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `6b2c3bb1e7fd` · [字段定义](../../DATASET.md)*
