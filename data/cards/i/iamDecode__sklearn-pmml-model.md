# iamDecode/sklearn-pmml-model

⭐ 78 · Python · BSD-2-Clause · 推送 2026-04-14 · [GitHub](https://github.com/iamDecode/sklearn-pmml-model) · 个人维护

**将 PMML 模型文件解析为 scikit-learn 估计器的 Python 库**

读取按 PMML 格式导出的模型文件，转换为可在 Python 中直接调用的 scikit-learn 估计器类，使用方式与原生 sklearn 估计器一致。支持决策树、随机森林、梯度提升、线性模型、SVM、最近邻、神经网络等约 11 类模型的分类与回归加载，部分模型通过修改内部实现或自动 one-hot 编码支持类别特征。以 pip 包形式发布，开发构建依赖 Cython 扩展。面向需要在 Python 中复用其他平台/语言训练模型的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | BSD-2-Clause |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 将 PMML 文件转换为 scikit-learn 估计器，加载后按原生 sklearn 接口使用
- 支持决策树、随机森林、GBM、线性模型、SVM、最近邻、神经网络等模型加载
- 部分模型支持类别特征（修改内部实现或自动 one-hot 编码）
- README 附带与 PyPMML 的加载+预测运行时间基准数据

## 适用场景

- 在其他平台或语言训练模型后，导出 PMML 到 Python 环境中推理
- 复用既有 PMML 模型资产并保持 scikit-learn 工作流
- 希望以 sklearn 估计器接口统一管理导入模型

## 场景标签

 · 领域:机器学习/模型互操作

## 证据(README 行号)

> L8: A library to effortlessly import models trained on different platforms and with programming languages into scikit-le
> L19: The library currently supports the following models:

## 星数曲线

```mermaid
xychart-beta
    title "iamDecode/sklearn-pmml-model 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 77 --> 79
    line [78, 78]
```

2026-10-18 78 → 2026-10-25 78（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `6584f4422978` · [字段定义](../../DATASET.md)*
