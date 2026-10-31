# dwave-examples/feature-selection

⭐ 18 · Python · Apache-2.0 · 推送 2026-04-24 · [GitHub](https://github.com/dwave-examples/feature-selection) · 组织维护

**D-Wave 混合量子求解器做机器学习特征选择的演示应用**

D-Wave 官方示例仓库：基于 Stride 混合求解器或 CQM 求解器，通过 D-Wave 的 scikit-learn 插件完成特征选择。目标是最小化特征间冗余（相关性）并最大化特征与目标变量的相关性，约束为选出指定数量的特征。提供 Titanic（14 特征）与 Scene（299 特征）两个数据集，以 Dash Web 应用呈现：可视化特征冗余、提交求解（典型 1-3 秒）、用随机森林分类器计算所选特征准确率。需配置 Leap 量子云服务访问权限，本地安装用 pip 安装 requirements.txt 后运行 app.py。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 以 CQM/非线性模型在 Leap 量子-经典混合求解器上求解特征选择
- 目标：最小化特征间相关性并最大化与目标变量的相关性
- Dash 界面可视化特征冗余并展示随机森林分类准确率
- 支持 Titanic 与 Scene（OpenML）两个数据集

## 适用场景

- 学习如何把特征选择建模为约束二次模型并用混合求解器求解
- 交互式观察特征冗余对所选特征子集与分类准确率的影响
- 了解 D-Wave scikit-learn 插件的调用方式

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L7: This demo showcases feature selection using D-Wave's Stride&trade; hybrid solver
> L8: or a constrained quadratic model (CQM) solver via
> L9: D-Wave's scikit-learn plug-in.

## 星数曲线

```mermaid
xychart-beta
    title "dwave-examples/feature-selection 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-31 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `11800deb8fe9` · [字段定义](../../DATASET.md)*
