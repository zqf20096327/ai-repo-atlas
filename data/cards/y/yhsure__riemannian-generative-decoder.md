# yhsure/riemannian-generative-decoder

⭐ 23 · Jupyter Notebook · MIT · 推送 2026-04-28 · [GitHub](https://github.com/yhsure/riemannian-generative-decoder) · [官网](https://openreview.net/forum?id=vuPMXg1FDT) · 组织维护

**流形上表示学习研究代码：仅用解码器学习流形值隐变量**

TMLR 2026 论文 Riemannian Generative Decoder 的官方代码库。方法：去除编码器，仅训练解码器网络，用 Riemannian 优化器求取流形值最大似然隐变量，避免近似流形密度的困难目标。提供三个案例的 Jupyter notebook（合成分支扩散过程、人类线粒体 DNA 推断迁移、细胞分裂周期），notebook 自动拉取数据，数据也可从 HuggingFace 直接下载。依赖 Python 3.11、requirements.txt 与 geoopt 0.5.1 子模块。

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

- 仅解码器架构，以 Riemannian 优化器求流形值最大似然隐变量
- 三个案例 notebook：分支扩散、线粒体 DNA、细胞周期
- notebook 自动获取数据，数据另发布于 HuggingFace
- 提供更新线粒体序列的抓取与 haplogrep3 注释流程

## 适用场景

- 复现论文结果与图表
- 在自定义流形数据上做几何感知的表示学习
- 获取细胞周期与人类线粒体 DNA 的分析流程

## 场景标签

 · 领域:机器学习研究/几何深度学习

## 证据(README 行号)

> L12: > Riemannian representation learning typically relies on approximating densities on chosen manifolds. This involves
> L23: 2. **Cell cycle in human fibroblasts [1]**

## 星数曲线

```mermaid
xychart-beta
    title "yhsure/riemannian-generative-decoder 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-31 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `f34eefeb2f7f` · [字段定义](../../DATASET.md)*
