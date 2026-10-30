# sony/sampleid

⭐ 34 · Python · MIT · 推送 2026-05-22 · [GitHub](https://github.com/sony/sampleid) · 组织维护

**论文代码：检测音乐采样片段并检索其原始来源**

Sony 研究团队发布的 ICASSP 2025 论文官方实现，任务为自动音乐采样识别：检测新曲目中复用的已有音频片段并检索其原始素材。方法采用自监督多轨对比学习，用多轨数据构造人工混音正样本对训练嵌入模型，推理时计算音频嵌入进行检索；提供 Zenodo 预训练 checkpoint，可仅装 PyTorch/Hydra 等依赖后 pip install -e . 直接在 Python 项目中调用，也支持用自己的多轨数据训练（基于 PyTorch Lightning + Hydra + Dora 模板）。模型对时间维取平均嵌入，需手动切分音频块。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多轨对比学习训练音频嵌入用于采样识别与来源检索
- 提供预训练 checkpoint，Python API 一行加载推理
- 支持自有数据集训练，基于 PyTorch Lightning/Hydra/Dora 实验管理
- README 列出与既有方法的 mAP/HR@1/HR@10 指标表

## 适用场景

- 检测新歌中是否采样了已有曲目并找到原始素材
- 用自有音乐数据集训练自己的采样识别模型
- 在自己的 Python 项目中嵌入音频做相似检索

## 场景标签

`语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L5: Sampling, the technique of reusing pieces of existing audio tracks to create new music content, is a very common pra
> L19: For inference, the only required dependencies are PyTorch, Hydra, numpy, scipy and tqdm. First, install them follow

## 星数曲线

```mermaid
xychart-beta
    title "sony/sampleid 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 33 --> 35
    line [34, 34]
```

2026-10-18 34 → 2026-10-30 34（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `468bf299aa53` · [字段定义](../../DATASET.md)*
