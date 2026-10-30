# bhklab/med-imagetools

⭐ 61 · Python · MIT · 推送 2026-09-03 · [GitHub](https://github.com/bhklab/med-imagetools) · [官网](https://bhklab.github.io/med-imagetools) · 组织维护

**医学影像处理流水线：将 DICOM 数据集转为深度学习就绪格式**

Python 包 med-imagetools，面向医学影像深度学习预处理：爬取数据集并按模态（CT/PET/RTDOSE/RTSTRUCT）构建模态依赖网络图，按用户定义的模态查询图并处理原始 DICOM，保存为 NRRD，再转为 TorchIO subject 数据集与 torch dataloader，供 ML 流水线使用。以 subject 为单位组织数据，处理同一患者研究中不同模态间的依赖。提供 CLI（imgtools），通过 pip 安装，文档另行托管。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 爬取数据集并构建模态间依赖网络图
- 处理 CT/PET/RTDOSE/RTSTRUCT 等多种 DICOM 模态
- 输出 NRRD 并转为 TorchIO subject 与 torch dataloader

## 适用场景

- 将杂乱的医学影像文件夹整理为深度学习可用的按患者组织的数据集
- 构建保留模态依赖关系的医学影像 ML 训练数据
- 通过命令行批量处理 DICOM 数据

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L26: medical dataset folders to deep learning ready format in few lines of code.
> L52: which med-imagetools converts to torchio subject dataset and

## 星数曲线

```mermaid
xychart-beta
    title "bhklab/med-imagetools 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 60 --> 62
    line [61, 61]
```

2026-10-18 61 → 2026-10-30 61（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `83ec4d68707f` · [字段定义](../../DATASET.md)*
