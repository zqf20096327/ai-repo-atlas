# dronefreak/clearview

⭐ 13 · Python · Apache-2.0 · 推送 2026-09-17 · [GitHub](https://github.com/dronefreak/clearview) · [官网](https://huggingface.co/spaces/dronefreak/clearview-derain-demo) · 个人维护

**PyTorch 图像去雨工具：单图/目录/视频去雨，含训练与评测**

基于 PyTorch 的神经图像去雨项目：提供 clearview-inference 命令行工具处理单图、图像目录与视频（视频逐帧处理、无时序一致性项），clearview-train / clearview-evaluate 用于训练与评测。含 10 种架构（Restormer、UNet、NAFNet Small/Mid/Large、ResNet-UNet、Histoformer 仅推理），权重托管于 Hugging Face；采用合成+真实混合数据训练（5 个数据源、真实域 2x 过采样）与混合验证指标选点。提供 HuggingFace 在线 demo，本地运行需 git clone 源码并 pip 安装。限制：视频处理可能存在帧间闪烁，roadmap 中时序一致性、移动端部署、雪雾去除尚未完成。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- clearview-inference 支持单图/目录/视频三种输入自动匹配
- 10 种去雨架构，9 种按统一混合域配方训练，权重托管 Hugging Face
- 5 个数据源混合训练（34,264 对），真实域 2x 过采样
- 提供 clearview-train / clearview-evaluate 训练与评测命令及混合验证选点机制

## 适用场景

- 对雨景照片或视频批量做去雨处理
- 在自有雨数据集上训练或微调去雨模型
- 对比不同去雨架构在合成/真实测试集上的 PSNR/SSIM

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L58: clearview-inference --model unet --weights clearview-derain-unet.pth \
> L142: |Test Set|Domain|Restormer|NAFNet (Large)|NAFNet (Mid)|UNet (Vanilla)|ResNet50-UNet|

## 星数曲线

```mermaid
xychart-beta
    title "dronefreak/clearview 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `a6ab462649b5` · [字段定义](../../DATASET.md)*
