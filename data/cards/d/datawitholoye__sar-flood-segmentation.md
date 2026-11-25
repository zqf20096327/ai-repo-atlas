# datawitholoye/sar-flood-segmentation

⭐ 3 · Jupyter Notebook · MIT · 推送 2026-10-10 · [GitHub](https://github.com/datawitholoye/sar-flood-segmentation) · 个人维护

**研究者复现 SAR 洪水分割基准实验的 PyTorch 代码库**

Hull 大学 MSc 论文的配套仓库：在 Sen1Floods11 数据集上以相同条件训练 Random Forest、U-Net、Attention U-Net、DeepLabV3+、SegFormer-B2 五种分割模型，并在模型未见过的地理区域（西班牙、美国）上测试跨区域泛化，附带阈值优化、随机划分对照与 Otsu 弱标签扩展实验。全部流程打包为 12 节 Jupyter notebook，采用跳过式 checkpoint 机制避免重复训练；MIT 许可，需自备 CUDA GPU 并从 Google Cloud Storage 下载数据。

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

- 五种分割模型在相同超参数下训练并按洪水事件划分地理外推测试集
- 完整流程封装为 12 节 notebook，带跳过式 checkpoint 可分段重跑
- 实验结论：跨区域泛化瓶颈是训练数据覆盖而非模型结构；弱标签扩展反而降低测试 IoU
- 预处理含 Lee 斑纹滤波，类别不均衡用加权采样与 BCE+Dice 组合损失处理

## 适用场景

- 复现或扩展 Sen1Floods11 上的洪水分割基准实验
- 研究分割模型跨地理区域泛化失败的机制
- 作为遥感语义分割（PyTorch + SegFormer/U-Net）的端到端教学流程

## 场景标签

`目标检测` `科研工具` · 领域:学习与行业

## 证据(README 行号)

> L3: **Benchmarking CNN and Transformer architectures for cross-geographic flood mapping on Sen1Floods11**
> L21: Automated SAR flood segmentation models often **fail to generalise beyond the regions they were trained on**. This 
> L36: 1. Implement and train five segmentation models (**Random Forest, U-Net, Attention U-Net, DeepLabV3+, SegFormer-B2*


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-25 · 置信度 high · 依据 README sha `01738d87ad9c` · [字段定义](../../DATASET.md)*
