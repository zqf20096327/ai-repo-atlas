# adursun/wsddn.pytorch

⭐ 51 · Python · Apache-2.0 · 推送 2026-07-22 · [GitHub](https://github.com/adursun/wsddn.pytorch) · 个人维护

**弱监督深度检测网络 WSDDN 的 PyTorch 复现，供科研使用**

用较新版本 PyTorch 实现 CVPR 2016 论文《Weakly Supervised Deep Detection Networks》（Bilen & Vedaldi），面向计算机视觉研究者。在图像级弱标注下训练目标检测模型，支持 VGG16 与 AlexNet 两种骨干网络；实现差异为使用 Adam 优化器（替代 SGD）且未加空间正则项。README 给出在 PASCAL VOC 上的复现结果（VGG16 均值 32.3 mAP、AlexNet 30.9 mAP）及预训练权重下载方式。运行依赖 Docker 与 nvidia-container-toolkit，在容器内执行训练与评估脚本。

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

## 能力要点

- WSDDN 论文的 PyTorch 复现，弱监督目标检测
- 支持 VGG16 与 AlexNet 两种骨干网络
- 提供 VOC 上分类别 mAP 结果与预训练权重下载
- Docker + GPU 容器化运行环境

## 适用场景

- 复现或验证 WSDDN 弱监督检测论文结果
- 在仅有图像级标注的数据上训练目标检测器
- 作为弱监督检测研究的代码基础进行修改

## 场景标签

`科研工具` `目标检测` `模型训练` · 领域:学习与行业

## 证据(README 行号)

> L3: Implementation of `Weakly Supervised Deep Detection Networks` using the latest version of PyTorch.
> L5: _`Bilen, H., & Vedaldi, A. (2016). Weakly supervised deep detection networks. In Proceedings of the IEEE Conference 

## 星数曲线

```mermaid
xychart-beta
    title "adursun/wsddn.pytorch 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 50 --> 52
    line [51, 51]
```

2026-10-18 51 → 2026-10-26 51（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `90d936812616` · [字段定义](../../DATASET.md)*
