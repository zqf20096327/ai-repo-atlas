# montanarograziano/Multimodal-approach-for-AD

⭐ 19 · Jupyter Notebook · MIT · 推送 2026-08-25 · [GitHub](https://github.com/montanarograziano/Multimodal-approach-for-AD) · [官网](https://montanarograziano.github.io/Multimodal-approach-for-AD/) · 个人维护

**阿尔茨海默病多模态（MRI+PET）3D CNN 检测代码：论文配套**

Scientific Reports 2024 论文的代码仓库：在 OASIS-3 的 3D 结构 MRI 与淀粉样 PET 体积上训练 3D 卷积网络，按模态分别及晚融合分类痴呆/非痴呆受试者，并用 Grad-CAM 与 AAL2 图谱将模型注意力对应到已知 AD 脑区。代码正从 Colab 笔记本迁移为 src/ 布局的 Python 包，数据管线与模型管线已移植，但尚未在真实 OASIS-3 数据上验证、未复现论文指标；全部测试使用合成数据。安装需 Python 3.13 与 uv，真实数据须自行向 OASIS-3 申请且本仓库不分发。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 3D CNN 构建、训练、评估、Grad-CAM、AAL2 区域排序的完整模型管线
- 含合成数据生成器与 OASIS-3 本地数据适配器（校验布局、读取本地文件）
- CLI 快速冒烟测试可在 CPU 上无真实数据运行
- 明示未在真实 OASIS-3 数据验证、未复现论文指标

## 适用场景

- 复现或研读论文的 3D MRI+PET 多模态 AD 分类方法
- 在获得 OASIS-3 数据前用合成数据熟悉管线流程
- 基于 Grad-CAM 与 AAL2 图谱做模型可解释性分析

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L15: The paper trains 3D convolutional networks on structural MRI and amyloid
> L18: late-fusion, and uses Grad-CAM to relate model attention to known
> L32: > notebooks. **What has not happened: validation against real OASIS-3

## 星数曲线

```mermaid
xychart-beta
    title "montanarograziano/Multimodal-approach-for-AD 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-31 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `8a54767ce14e` · [字段定义](../../DATASET.md)*
