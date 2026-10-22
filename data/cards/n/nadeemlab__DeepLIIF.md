# nadeemlab/DeepLIIF

⭐ 264 · Python · NOASSERTION · 推送 2026-08-31 · [GitHub](https://github.com/nadeemlab/DeepLIIF) · [官网](https://deepliif.org) · 组织维护

**将 IHC 病理图像转为 mpIF 并做细胞分割与定量评分**

面向数字病理的多任务深度学习框架：单步完成染色分离、细胞分割与单细胞 IHC 定量评分，将低成本的 IHC 切片翻译为 mpIF 图像（Hematoxylin、DAPI、蛋白通道），同时输出阳性/阴性细胞分割掩码。训练于 Ki67 IHC 数据，README 称可泛化到 CD3、CD8、BCL2 等标志物及 H&E 图像核分割。以 pip 包与 CLI 提供，支持单/多 GPU 训练（DP/DDP）与 Torchscript 序列化推理；本地运行需 GPU，也可通过免费云平台/API/ImageJ 插件远程使用（无需 GPU）。仅限非商业学术用途。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单步完成染色分离、细胞分割与单细胞 IHC 评分
- IHC→mpIF 图像翻译并输出阳性/阴性细胞分割掩码
- 单/多 GPU 训练（DP/DDP）与 Torchscript 序列化推理
- 免费云平台（deepliif.org）+ 云 API + ImageJ/Fiji 插件远程使用，支持 150+ 输入格式

## 适用场景

- 病理图像 IHC 标志物的定量单细胞评分
- 生成 mpIF 多通道图像与细胞分割掩码
- 在 H&E 图像上做开箱即用的核分割

## 场景标签

 · 领域:数字病理/医学影像

## 证据(README 行号)

> L23: By creating a multitask deep learning framework referred to as DeepLIIF, we present a single-step solution to stain
> L24: deconvolution/separation, cell segmentation, and quantitative single-cell IHC scoring. Leveraging a unique de novo
> L36: **DeepLIIF** is deployed as a free publicly available cloud-native platform (https://deepliif.org) with Bioformats 

## 星数曲线

```mermaid
xychart-beta
    title "nadeemlab/DeepLIIF 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 263 --> 265
    line [264, 264]
```

2026-10-18 264 → 2026-10-22 264（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `5d41decef593` · [字段定义](../../DATASET.md)*
