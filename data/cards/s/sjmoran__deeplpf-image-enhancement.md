# sjmoran/deeplpf-image-enhancement

⭐ 260 · Python · MIT · 推送 2026-10-23 · [GitHub](https://github.com/sjmoran/deeplpf-image-enhancement) · 组织维护

**CVPR 2020 可解释图像增强模型：学习三次/渐变/椭圆三类滤镜**

华为诺亚方舟实验室的 DeepLPF 官方实现（CVPR 2020）：U-Net 骨干网络预测摄影师熟悉的三类局部参数化滤镜参数——色调曲线（Cubic）、渐变滤镜（Graduated）、椭圆径向滤镜（Elliptical）——并依序应用到图像。模型仅 1.7M 参数（6.9MB），在 Apple GPU 上单张 46ms。以 pip 包与 CLI（deeplpf enhance）提供，内置 MIT-Adobe FiveK 预训练权重，附训练、数据集复现与协议对照文档。设备自动在 CUDA/MPS/CPU 间选择。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 预测三次/渐变/椭圆三类滤镜参数并可视化叠加，增强结果可读可解释
- 1.7M 参数、6.9MB，M 系列 GPU 单张 46ms
- deeplpf enhance CLI 支持单文件或整目录，读取 PNG/JPEG/TIFF/BMP/WebP
- 附 Two 项可选能力：学习滤镜实例数（--learn_filter_count）与全局色彩混合（--colour_head）

## 适用场景

- 摄影师或普通用户一键自动修图增强照片
- 研究者复现 DeepLPF 训练或在 FiveK 上做基准对比
- 需要可解释滤镜参数而非纯像素输出的图像增强应用

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L30: Most enhancement networks paint the output pixel by pixel. DeepLPF instead
> L79: A U-Net backbone reads the image and produces per-pixel features. Three heads

## 星数曲线

```mermaid
xychart-beta
    title "sjmoran/deeplpf-image-enhancement 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 259 --> 261
    line [260, 260]
```

2026-10-18 260 → 2026-10-26 260（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `6630ebe8cc80` · [字段定义](../../DATASET.md)*
