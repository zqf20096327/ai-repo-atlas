# MIC-DKFZ/nnWorkbench

⭐ 4 · Python · Apache-2.0 · 推送 2026-11-06 · [GitHub](https://github.com/MIC-DKFZ/nnWorkbench) · 组织维护

**为医学影像标注者提供 nnU-Net/nnInteractive 一体化 GUI 与 CLI**

围绕 nnU-Net 与 nnInteractive 的工作台：对已有标注的图像提供预处理、训练、验证、预测的完整流程；对无标注图像提供 nnInteractive 交互式标注（Napari 中点击勾画 3D 目标）与涂鸦稀疏标注，可直接保存为 nnU-Net 训练数据，并支持

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 标注、预处理、训练、验证、预测在同一 GUI 内完成
- nnInteractive 稀疏标注直接保存为 nnU-Net 数据，无需转换
- 每一步可复制为精确的 nnU-Net 终端/集群命令
- 内置稀疏标注训练器 nnUNetTrainerBetterIgnoreSampling，自动选择

## 适用场景

- 从少量标注迭代训练自己的医学影像分割模型
- 用 nnInteractive 在 Napari 中快速勾画 3D 结构生成标签
- 在集群上远程运行 nnU-Net 命令并查看验证结果

## 场景标签

`目标检测` `科研工具` · 领域:学习与行业

## 证据(README 行号)

> L10: > A GUI for nnU-Net and nnInteractive-powered annotation that keeps the entire workflow in one place.
> L26: - **nnInteractive and nnU-Net, connected:** Create labels with nnInteractive in Napari, save them directly as nnU-N
> L49: - For training: an NVIDIA GPU, 24 GB of memory for the recommended setup, 8 GB at minimum with a smaller planner (s

## 星数曲线

```mermaid
xychart-beta
    title "MIC-DKFZ/nnWorkbench 星数(近 3 点)"
    x-axis ["2026-11-14", "2026-11-19", "2026-11-21"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-11-14 3 → 2026-11-21 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `04b677be33c0` · [字段定义](../../DATASET.md)*
