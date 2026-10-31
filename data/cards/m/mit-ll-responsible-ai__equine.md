# mit-ll-responsible-ai/equine

⭐ 20 · Python · MIT · 推送 2026-10-30 · [GitHub](https://github.com/mit-ll-responsible-ai/equine) · [官网](https://mit-ll-responsible-ai.github.io/equine/) · 组织维护

**为监督分类模型提供校准概率与分布外评分的 PyTorch 库**

MIT Lincoln Laboratory 开发的 PyTorch 扩展库，面向监督标注问题的神经网络：对每个预测标签输出校准后的概率，并给出 in-distribution 分数以判断测试样本是否属于已知标签（OOD 检测）。机制上扩展 pytorch 的 nn.Module 接口，通过 predict 方法同时返回类别预测与 OOD 分数；依赖少，除 torch 外依赖有限。以 pip 安装的 Python 库形式提供，附文档示例与配套 Web 应用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 对预测标签输出校准概率
- in-distribution 分数指示预测是否可信（OOD 检测）
- 扩展 pytorch nn.Module，predict 同时返回预测与 OOD 分数

## 适用场景

- 给分类模型补充不确定性量化，缓解过度自信预测
- 检测不属于已知标签的分布外样本
- 在 PyTorch 训练流程中集成校准与 OOD 评分

## 场景标签

 · 领域:机器学习/不确定性量化

## 证据(README 行号)

> L18: EQUINE was created to simplify two kinds of uncertainty quantification for supervised labeling problems:
> L35: EQUINE extends pytorch's `nn.Module` interface using a `predict` method that returns both

## 星数曲线

```mermaid
xychart-beta
    title "mit-ll-responsible-ai/equine 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-31 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `136a4d45acf5` · [字段定义](../../DATASET.md)*
