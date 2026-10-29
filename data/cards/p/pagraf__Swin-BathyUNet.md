# pagraf/Swin-BathyUNet

⭐ 21 · Jupyter Notebook · NOASSERTION · 推送 2026-03-02 · [GitHub](https://github.com/pagraf/Swin-BathyUNet) · [官网](https://www.magicbathy.eu) · 个人维护

**科研用：无需现场测深数据的浅水水深遥感反演深度学习模型**

ISPRS Journal 2025 论文的官方代码：Swin-BathyUNet 将 U-Net 与 Swin Transformer 自注意力层及交叉注意力机制结合，面向光谱推导测深（SDB）；以含数据空洞的折射校正 SfM-MVS DSM 作为训练先验，生成完整水深图，也可脱离 SfM-MVS 输出独立用于标准 SDB。提供 aerial（GSD=0.25m）与 Sentinel-2（GSD=10m）两类数据的示例结果。训练与测试通过一个 Jupyter notebook 完成，依赖经 conda 环境安装，数据集需从 MagicBathy 项目 Zenodo 仓库下载。由 NTUA 研究者个人维护，属欧盟 HORIZON Europe MagicBathy 项目成果。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- U-Net + Swin Transformer 自注意力 + 交叉注意力的测深网络
- 以含空洞的折射校正 SfM-MVS DSM 作训练先验生成完整水深图
- 可独立用于标准 SDB，支持不同训练深度数据
- 提供 aerial 与 Sentinel-2 两类示例推理结果

## 适用场景

- 我需要用航空/卫星影像反演浅水区水深，且没有现场测深数据
- 我想用 MagicBathyNet 数据集复现论文的水深预测结果
- 我需要在均匀纹理海域补全 SfM-MVS DSM 的深度空洞

## 场景标签

`科研工具` `图像视频处理` · 领域:学习与行业

## 证据(README 行号)

> L16: Accurate, detailed, and high-frequent bathymetry is crucial for shallow seabed areas facing intense climatological 
> L51: Swin-BathyUNet combines U-Net with Swin Transformer self-attention layers and a cross-attention mechanism, tailored

## 星数曲线

```mermaid
xychart-beta
    title "pagraf/Swin-BathyUNet 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-29 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `c2c194512c1c` · [字段定义](../../DATASET.md)*
