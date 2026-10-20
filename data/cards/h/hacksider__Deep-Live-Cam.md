# hacksider/Deep-Live-Cam

⭐ 97,115 · Python · AGPL-3.0 · 推送 2026-10-10 · [GitHub](https://github.com/hacksider/Deep-Live-Cam) · [官网](https://deeplivecam.net/) · 组织维护

**给创作者提供单张图片实时换脸与一键视频 deepfake**

开源的实时换脸工具：选择一张源人脸图像后，可对图片/视频进行换脸输出，或在摄像头模式下实时替换面部并配合 OBS 推流。功能包括 Mouth Mask 保留原始嘴部动作、多人 Face Mapping、以及基于 execution provider 的多硬件加速路径（CUDA/CoreML/DirectML/OpenVINO/CPU）。安装分预构建版（官网付费 Ultimate 版）与手动源码安装，手动安装需自行下载两个模型文件并配置 Python 环境，需 ffmpeg 等系统依赖。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 动量与使用信号

- 维护:`active` — 距上次 push 8.1 天,年发版 9,82 位贡献者
- 涨星:近 1 天 **+13**(自 20261016 起算)
- 安装:pypi 包 `torch` 月下载 58,964,343
- 平台:WINDOWS · 协议:—

## 能力要点

- 单张图片驱动的实时摄像头换脸与图片/视频换脸
- Mouth Mask 保留原始嘴部、Face Mapping 多人多脸同时替换
- 支持 CUDA、CoreML、DirectML、OpenVINO 等 GPU 加速执行提供者
- 内置内容检查，阻止处理裸露等不当媒体

## 适用场景

- 视频通话/直播中实时替换面部
- 为动画角色制作提供面部驱动
- 制作换脸梗图与娱乐内容

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L3:  Real-time face swap and video deepfake with a single click and only a single image.
> L173: **Run:** If you don't have a GPU, you can run Deep-Live-Cam using `python run.py`. Note that initial execution wil
> L175: ### GPU Acceleration

---
*卡片 v1 · prompt 1.4 · 生成 2026-10-18 · 置信度 high · 依据 README sha `842864138f76` · [字段定义](../../DATASET.md)*
