# LucaAngioloni/ProteinSecondaryStructure-CNN

⭐ 113 · Python · MIT · 推送 2026-04-14 · [GitHub](https://github.com/LucaAngioloni/ProteinSecondaryStructure-CNN) · 个人维护

**用 CNN 从氨基酸序列预测蛋白质二级结构的科研项目**

基于 Keras/TensorFlow 实现的蛋白质二级结构 8 态预测器：输入 CullPDB 数据集（6133 条蛋白质，使用 Protein Profiles 特征而非氨基酸残基指示），探索两种 CNN 方法——整序列预测（700×9 输出，因 padding 影响损失被放弃）和滑动窗口 CNN（窗口宽度 17）。窗口模型测试集 Q8 准确率 0.7215，CB513 基准上 0.6833。面向生物信息学与机器学习研究者，README 未给出安装运行命令。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 滑动窗口 CNN（cnn_width=17）实现 8 态二级结构预测
- 使用 Protein Profiles（PSSM）而非氨基酸残基指示作为输入特征
- 测试集 Q8 准确率 0.7215，CB513 基准 0.6833
- 探索了整序列预测与滑动窗口两种方法并对比结果

## 适用场景

- 研究 CNN 方法在蛋白质二级结构预测任务上的表现
- 复现并与 DeepCNF 等方法的 Q8 准确率结果对比
- 作为生物信息学深度学习项目的学习参考

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L5: Protein secondary structure predictor using CNN
> L28: I focused on the primary and secondary structure (SS), more specifically on using Convolutional Neural Networks (CN

## 星数曲线

```mermaid
xychart-beta
    title "LucaAngioloni/ProteinSecondaryStructure-CNN 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 112 --> 114
    line [113, 113]
```

2026-10-18 113 → 2026-10-28 113（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `e21188fcdce8` · [字段定义](../../DATASET.md)*
