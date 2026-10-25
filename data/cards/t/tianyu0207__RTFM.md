# tianyu0207/RTFM

⭐ — · [GitHub]() · 个人维护

**ICCV 2021 论文官方代码：弱监督视频异常检测方法 RTFM**

论文《Weakly-supervised Video Anomaly Detection with Robust Temporal Feature Magnitude Learning》（ICCV 2021）的 PyTorch 官方实现。面向视频异常检测方向的研究者，提供在 ShanghaiTech 与 UCF-Crime 两个数据集上的训练与测试流程：需先下载作者提供的 I3D（resnet50）预提取特征与 checkpoint，修改列表文件中的数据路径与 option.py 中的超参数后，通过运行 visdom.server 与 main.py 完成训练测试。README 未给出依赖安装清单与硬件要求。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- RTFM 弱监督视频异常检测的 PyTorch 实现
- 提供 ShanghaiTech 与 UCF-Crime 的 I3D 特征及 checkpoint 下载链接
- 采用 10-crop 数据增强，与此前工作流程一致

## 适用场景

- 复现 ICCV 2021 RTFM 论文实验结果
- 在 ShanghaiTech / UCF-Crime 上训练视频异常检测模型
- 作为弱监督视频异常检测研究的基线代码

## 场景标签

 · 领域:计算机视觉/视频异常检测

## 证据(README 行号)

> L2: This repo contains the Pytorch implementation of our paper:
> L3: > **Weakly-supervised Video Anomaly Detection with Robust Temporal Feature Magnitude Learning**

## 星数曲线

```mermaid
xychart-beta
    title "tianyu0207/RTFM 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 350 --> 352
    line [351, 351]
```

2026-10-18 351 → 2026-10-25 351（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `a5d00599929e` · [字段定义](../../DATASET.md)*
