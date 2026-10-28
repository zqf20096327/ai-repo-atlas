# ciglenecki/eeg-driver-fatigue-detection

⭐ 26 · Python · 推送 2026-02-21 · [GitHub](https://github.com/ciglenecki/eeg-driver-fatigue-detection) · 个人维护

**复现论文的 EEG 司机疲劳检测系统：多熵融合特征+SVM 等分类**

面向科研与课程作业的 EEG 司机疲劳检测实现：复现 PLOS ONE 论文的方法，对 12 名司机、30 电极、正常/疲劳两种状态的 5 分钟脑电信号做滤波（50Hz 陷波、0.15–40Hz 带通）后按 1 秒分 epoch，提取 4 种熵（谱熵/近似熵/样本熵/模糊熵）及均值、标准差、功率谱密度等特征，经防泄漏的 min-max 归一化后训练 SVM、神经网络、KNN、随机森林分类器，并按论文公式计算电极权重、筛选显著电极。数据为 BCIT 数据集的 .cnt 文件；README 给出虚拟环境与 pip 安装步骤。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 4 种熵与其他特征的多熵融合特征提取流水线
- SVM/BP 神经网络/KNN/随机森林 4 种分类器训练与对比
- LOO 交叉验证调参（C、gamma）与熵组合 powerset 搜索
- 按论文公式计算电极权重并筛选 10 个显著电极

## 适用场景

- 复现多熵融合 EEG 疲劳检测论文的实验流程
- 比较不同熵组合与电极区域对疲劳分类准确率的影响
- 作为 EEG 信号预处理与特征工程的参考代码

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L7: Implement steps described in the research paper and produce similar results.
> L176: analyze the multiple entropy fusion method and evaluate several channel regions to effectively detect a driver’s f

## 星数曲线

```mermaid
xychart-beta
    title "ciglenecki/eeg-driver-fatigue-detection 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-28 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `aa26037bb770` · [字段定义](../../DATASET.md)*
