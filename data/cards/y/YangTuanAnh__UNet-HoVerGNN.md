# YangTuanAnh/UNet-HoVerGNN

⭐ 18 · Jupyter Notebook · 推送 2026-03-04 · [GitHub](https://github.com/YangTuanAnh/UNet-HoVerGNN) · 个人维护

**病理图像细胞核实例分割与分类框架**

面向计算病理学的研究框架，将 CNN 分割与图神经网络推理结合：以细胞核质心构建 k 近邻图，从预训练 U-Net 编码器提取节点与边特征，由 GNN 结合空间与上下文依赖修正分类。在 MoNuSAC、PanNuke、CoNSeP 三个数据集上训练与评估，README 报告 AJI/F1/PQ 指标并与 HoVerNet、Mask2Former 等方法列表对比。以源码与 Jupyter notebook 形式提供，依赖 PyTorch 与 PyTorch Geometric，数据集需从 Kaggle 下载。

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

- CNN 分割与 GNN 图推理结合的混合框架
- 细胞核质心构建 kNN 图，U-Net 编码器提取节点/边特征
- 支持 MoNuSAC/PanNuke/CoNSeP 三个数据集
- 通过 main.py 命令行参数指定数据集与类别数训练评估

## 适用场景

- 病理切片图像中的细胞核实例分割与分类
- 复现论文实验或在新数据集上训练评估
- 图神经网络与分割模型结合的研究参考

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L9: We propose **UNet-HoVerGNN**, a hybrid framework for nuclei instance segmentation and classification that combines C
> L24: * **MoNuSAC**: Multi-organ nuclei segmentation and classification.
> L30: To train and evaluate the UNet-HoVerGNN model, navigate to the src directory and run the main.py script with the de

## 星数曲线

```mermaid
xychart-beta
    title "YangTuanAnh/UNet-HoVerGNN 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `d25d2f929dea` · [字段定义](../../DATASET.md)*
