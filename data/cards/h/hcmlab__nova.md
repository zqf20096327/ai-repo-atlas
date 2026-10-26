# hcmlab/nova

⭐ 195 · C# · GPL-3.0 · 推送 2026-03-18 · [GitHub](https://github.com/hcmlab/nova) · [官网](http://openssi.net/) · 组织维护

**社交互动行为标注与分析工具：标注过程中提供机器学习辅助**

面向社会交互行为研究的标注与分析桌面工具：支持逐帧离散标注与连续值标注（如情绪、社会态度），可可视化 SSI 框架及外部来源录制的多被试数据流，并支持多人协作分工的标注数据库。其机器学习部分：在界面内训练/评估 SVM、神经网络等模型，含会话补全（用前几分钟标注预测剩余会话）与会话迁移（用多会话预测未知数据）两步，借助人工输入迭代精化模型。标注格式可与 ELAN、Excel 互导。为 Windows WPF 应用，Mac/Linux 需虚拟机；可选搭配 DISCOVER 分析服务器。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 逐帧离散标注与连续值标注，支持多被试数据加载
- 界面内训练 SVM/神经网络，含会话补全与会话迁移预测流程
- 人机协作标注数据库，标注工作可在多端与人机间分工
- 标注格式支持 ELAN/ANVIL/Excel 导入导出

## 适用场景

- 对社交互动视频/多模态数据做行为编码标注
- 用机器学习模型预测补全剩余会话的标注以减少人工量
- 多人协作分工完成大型标注数据库

## 场景标签

 · 领域:行为科学/多模态标注工具

## 证据(README 行号)

> L4: A main feature of NOVA is that it allows to employ a collaborative annotation database where annotation work can be 
> L12: The Cooperative Machine Learning capabilities allow to train and evaluate machine learning models, such as Support 

## 星数曲线

```mermaid
xychart-beta
    title "hcmlab/nova 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 194 --> 196
    line [195, 195]
```

2026-10-18 195 → 2026-10-26 195（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `3a140064d64a` · [字段定义](../../DATASET.md)*
