# robert80203/EgoPER_official

⭐ 44 · Python · 推送 2026-10-07 · [GitHub](https://github.com/robert80203/EgoPER_official) · 组织维护

**自我中心程序性任务视频的错误检测官方实现（CVPR）**

CVPR 论文 Error Detection in Egocentric Procedural Task Videos 的官方代码实现，附带 EgoPER 与 EgoPED 数据集：提供任务图标注、I3D 与 VideoCLIP 特征、LLM 生成的错误描述等资源。流程包括 conda 环境搭建、数据集邮件申请获取（OneDrive 链接两周有效）、抽帧与特征提取预处理、基于 ActionFormer 分割骨干的训练与推理脚本，输出动作分割与错误检测的评估结果。给计算机视觉科研人员复现与扩展使用。

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

- 动作分割骨干为 ActionFormer，每步骤原型数为 2
- 支持 I3D 或 VideoCLIP 两类特征
- 提供预提取特征下载，也可用预训练权重自行生成
- EgoPED 支持遗漏错误（omission error）检测

## 适用场景

- 复现 CVPR 论文的错误检测实验
- 在 EgoPER/EgoPED 数据集上训练新模型
- 开展第一人称视频的程序性步骤理解研究

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L5: This is the official implementation of Error Detection on Egocentric Procedural Task Videos
> L105: - The code will evaluation the performance of action segmentation and error detection.

## 星数曲线

```mermaid
xychart-beta
    title "robert80203/EgoPER_official 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 43 --> 45
    line [44, 44]
```

2026-10-18 44 → 2026-10-30 44（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `c6773e2aa6b7` · [字段定义](../../DATASET.md)*
